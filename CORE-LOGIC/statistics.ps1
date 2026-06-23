
$Data = Import-Csv 'D:\KANDO-CORE\ACCOUNTING\ledger.csv'
$Summary = $Data | Group-Object Category | Select-Object Name, @{Name='Total';Expression={($_.Group | Measure-Object Income -Sum).Sum}}
$Summary | Out-File 'D:\KANDO-CORE\ACCOUNTING\stats.txt'

