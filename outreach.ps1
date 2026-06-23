
$Message = 'ÓáÇã¡ ãä ˜ÇäÏæ åÓÊãº ˜ÇÑÒÇÑö ÊÍáíáö ÏÇÏå. ÒÇÑÔö ÂãÇÑíö ãÇ ÑÇ ÇíäÌÇ ÈÈíäíÏ: [URL]'
Invoke-RestMethod -Uri 'https://api.business-network.com/send-message' -Method Post -Body $Message

