[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

# === 設定 ===
$HOST_ALIAS = "raspberrypi"
$SSH_CONFIG = "$HOME\.ssh\config"

# === 解析 SSH config ===
$lines = Get-Content $SSH_CONFIG
$block = $lines -join "`n" | Select-String -Pattern "Host\s+$HOST_ALIAS[\s\S]*?(?=^Host\s|\z)" -AllMatches | ForEach-Object { $_.Matches[0].Value }

function Get-ConfigValue($block, $key) {
    ($block -split "`n" | Where-Object { $_ -match "^\s*$key\s+" }) `
        -replace "^\s*$key\s+", "" -replace "\s+$", ""
}

$PI_HOST = Get-ConfigValue $block "HostName"
$PI_USER = Get-ConfigValue $block "User"

# === 本地與遠端路徑 ===
$PI_PATH = "/home/$PI_USER/flask_app"
$LOCAL_PATH = Join-Path (Split-Path $PSScriptRoot -Parent) "flask_app"
$VENV_PATH = "$PI_PATH/venv"

# === 開始同步 ===
Write-Host "Starting sync with SCP..."
Write-Host "Local path: $LOCAL_PATH"
Write-Host "Remote path: $PI_PATH"

# 1. 使用 SCP 上傳檔案
scp -r "$LOCAL_PATH\*" ${PI_USER}@${PI_HOST}:$PI_PATH

if ($LASTEXITCODE -eq 0) {
    Write-Host "Sync completed successfully."
} else {
    Write-Host "Sync failed. Please check SSH connection."
    exit 1
}

# 2. 停止舊 Flask
Write-Host "Stopping old Flask process..."
ssh ${PI_USER}@${PI_HOST} "pkill -f 'flask run' || true"

# 3. 啟動 Flask（啟用 venv）
Write-Host "Starting Flask server in venv..."
$startCmd = "cd $PI_PATH && source $VENV_PATH/bin/activate && export FLASK_APP=app.py && nohup flask run --host=0.0.0.0 --reload > flask.log 2>&1 &"
ssh ${PI_USER}@${PI_HOST} "$startCmd"

Write-Host "Flask is running at: http://${PI_HOST}:5000"
