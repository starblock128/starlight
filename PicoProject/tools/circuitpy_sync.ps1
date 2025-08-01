# ===========================================
# sync.ps1 - 專案同步腳本 (Pico CircuitPython)
# 功能：
#   1. 將專案的 .py 檔案同步到 CIRCUITPY (D:\)
#   2. main.py 自動改為 code.py
#   3. 排除不需要同步的資料夾
#   4. 只複製修改過的檔案，加快速度
# ===========================================

# === 設定來源與目標 ===
$source = "C:\Users\water\Desktop\StarLight\PicoProject"
$target = "D:\"  # 請依你實際的 CIRCUITPY 掛載盤調整

# === 排除資料夾（相對於專案根目錄）===
$excludeDirs = @(
    ".vscode",      # VS Code 設定檔
    "stubs",        # CircuitPython stubs
    "tools",        # 工具腳本資料夾
    "__pycache__",  # Python 編譯快取
    ".fseventsd",   # macOS 系統資料夾
    "sd"            # 占位資料夾 (如不需要同步)
)

# === 驗證 CIRCUITPY 是否存在 ===
if (-Not (Test-Path $target)) {
    Write-Host "ERROR: Pico drive not found at $target. Please check connection."
    exit
}

Write-Host ">>> Starting sync from $source to $target ..."
Write-Host ">>> Excluding folders: $($excludeDirs -join ', ')"

# === 搜尋所有 .py 檔案並同步 ===
Get-ChildItem -Path $source -Recurse -Include *.py | ForEach-Object {
    # 計算相對路徑
    $relativePath = $_.FullName.Substring($source.Length).TrimStart('\')
    $firstDir = $relativePath.Split('\')[0]

    # 如果第一層資料夾在排除清單，略過
    if ($excludeDirs -contains $firstDir) {
        return
    }

    # 設定目標路徑
    $dest = Join-Path $target $relativePath

    # main.py → code.py
    if ($_.Name -ieq "main.py") {
        $dest = Join-Path (Split-Path $dest) "code.py"
    }

    # 判斷是否需要複製（只複製新檔）
    $needsCopy = $true
    if (Test-Path $dest) {
        if ($_.LastWriteTime -le (Get-Item $dest).LastWriteTime) {
            $needsCopy = $false
        }
    }

    # 如果需要更新就執行複製
    if ($needsCopy) {
        $destDir = Split-Path $dest
        if (-Not (Test-Path $destDir)) {
            New-Item -ItemType Directory -Path $destDir | Out-Null
        }
        Copy-Item $_.FullName $dest -Force
        Write-Host ("Updated: {0} -> {1}" -f $_.Name, (Split-Path $dest -Leaf))
    }
}

Write-Host ">>> Sync complete!"
