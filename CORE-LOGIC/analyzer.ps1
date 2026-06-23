
$Data = Import-Csv 'D:\KANDO-CORE\ACCOUNTING\ledger.csv'
$Profit = ($Data | Measure-Object -Property Income -Sum).Sum - ($Data | Measure-Object -Property Expense -Sum).Sum
Write-Output 'CURRENT_NET_PROFIT: ' + $Profit | Out-File 'D:\KANDO-CORE\ACCOUNTING\report.txt'

