
$Data = Import-Csv 'D:\KANDO-CORE\ACCOUNTING\ledger.csv' | Select-Object -Last 2
$Growth = ([float]$Data[1].Income - [float]$Data[0].Income)
$Prediction = [float]$Data[1].Income + $Growth
'ÅÌ‘ù»Ì‰Ì œ—¬„œ œÊ—Â »⁄œÌ: ' + $Prediction | Out-File 'D:\KANDO-CORE\ANALYZER\Final_Report.txt'

