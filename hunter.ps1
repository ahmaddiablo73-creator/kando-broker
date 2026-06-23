
$Target = Invoke-RestMethod -Uri 'https://api.project-boards.com/find?q=data-analysis'
if ($Target) { Start-Process 'D:\KANDO-CORE\outreach.ps1' }

