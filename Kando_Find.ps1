param([string]$Keyword)

$searchPath = "D:\KANDO-CORE\Projects"
Write-Host "Searching for $Keyword in $searchPath..." -ForegroundColor Cyan

Get-ChildItem -Path $searchPath -Recurse -Filter "*$Keyword*" | Select-Object FullName, Name
