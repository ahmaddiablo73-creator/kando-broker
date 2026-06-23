# [ãÇæáö íÔÈíäíö äæÓÇä - äÓÎå 2.0 ÈÇ ÊÍáíáö ãŞÇíÓåÇí]
function Get-ComparativeVolatility {
    $CurrentRisk = 4.5 # ÔÈíåÓÇÒíö ÏÇÏåíö ÒäÏå
    $PreviousRisk = Get-Content 'D:\KANDO-CORE\WEB-SITE\last_risk.txt' -ErrorAction SilentlyContinue
    
    if ($PreviousRisk) {
        $Delta = $CurrentRisk - $PreviousRisk
        $Status = if ($Delta -gt 0) { "ÇİÒÇíÔ íÇİÊå" } else { "˜ÇåÔ íÇİÊå" }
        $Result = "äæÓÇäö ÈÇÒÇÑ: $CurrentRisk/10 (äÓÈÊ Èå ŞÈá $Status)"
    } else {
        $Result = "äæÓÇäö ÈÇÒÇÑ: $CurrentRisk/10"
    }
    
    $CurrentRisk | Out-File 'D:\KANDO-CORE\WEB-SITE\last_risk.txt'
    return $Result
}
Get-ComparativeVolatility | Out-File "D:\KANDO-CORE\WEB-SITE\volatility.txt"
