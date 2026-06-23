
$raw = Invoke-RestMethod -Uri 'https://api.target-system.com/data' -Method Get
$raw | Select-Object Value | Export-Csv 'D:\KANDO-CORE\ACCOUNTING\ledger.csv' -Append

