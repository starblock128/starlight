# tools/git_sync.ps1

Write-Host "Starting Git sync..."
git add .
git commit -m "auto commit"
git push
