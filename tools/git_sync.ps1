# tools/git_sync.ps1

Write-Host "執行 git 同步任務..."
git add .
git commit -m "auto commit"
git push
