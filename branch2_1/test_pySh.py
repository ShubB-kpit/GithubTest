from datetime import date, timedelta


b4today = (date.today()-timedelta(days=1)).strftime("%d/%m/%Y")

pdxName = "OOOOOOOO_123456F7.123_456_789"
hglght_shp = ["highlightColorGreen","highlightColorRed"]
hglght_html = ["lime","red"]
hglght_indx = 1

CH_red  = ["""(<span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130">UnChanged</span>)""", \
"""(<span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#E81123">Changed&nbsp;</span>)"""]
CH_red_h = ["UnChanged", "&lt;span class=\\\\\&quot;fontColorRed\\\\\&quot;&gt;Changed&lt;/span&gt;"]
CH_red_i = 1

htmlPlainTextPayload = """
<html><head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"><meta name="Generator" content="Microsoft Word 15 (filtered medium)"><style>
<!--
@font-face
	{font-family:Wingdings}
@font-face
	{font-family:"Cambria Math"}
@font-face
	{font-family:Calibri}
@font-face
	{font-family:"Segoe UI"}
p.MsoNormal, li.MsoNormal, div.MsoNormal
	{margin:0in;
	font-size:11.0pt;
	font-family:"Calibri",sans-serif}
span.EmailStyle17
	{font-family:"Calibri",sans-serif;
	color:windowtext}
.MsoChpDefault
	{}
@page WordSection1
	{margin:1.0in 1.0in 1.0in 1.0in}
div.WordSection1
	{}
ol
	{margin-bottom:0in}
ul
	{margin-bottom:0in}
-->
</style></head><body lang="EN-US" link="#0563C1" vlink="#954F72" style="word-wrap:break-word"><div class="WordSection1"><p class="MsoNormal" style="margin-bottom:16.8pt; line-height:16.8pt; background:white"><b><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130; background:""" + \
hglght_html[hglght_indx] + \
"""">""" + \
pdxName + \
"""</span></b><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130">&nbsp;(G123BF4 Engineering build,<b>Cmake build</b>)</span></p><ul type="disc"><li class="MsoNormal" style="color:#323130; line-height:16.8pt; background:white"><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif">Created on """ + \
b4today + \
"""</span></li></ul><p class="MsoNormal" style="margin-left:102.0pt; text-indent:-.25in; line-height:16.8pt; background:white"><span style="font-size:10.0pt; font-family:&quot;Courier New&quot;; color:#323130"><span style="mso-list:Ignore">o<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp; </span></span></span><b><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130">THIS IS A CM D2.0 - SAMPLE SOFTWARE</span></b><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130"></span></p><p class="MsoNormal" style="margin-left:102.0pt; text-indent:-.25in; line-height:16.8pt; background:white"><span style="font-size:10.0pt; font-family:&quot;Courier New&quot;; color:#323130"><span style="mso-list:Ignore">o<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp; </span></span></span><u><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130">PDXlocation</span></u><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130">:</span></p><p class="MsoNormal" style="margin-left:102.0pt; text-indent:-.25in; line-height:16.8pt; background:white"><span style="font-size:10.0pt; font-family:&quot;Courier New&quot;; color:#323130"><span style="mso-list:Ignore">o<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp; </span></span></span><u><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130">PDX Template</span></u><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130">:&nbsp;<b>PT01_template.123_456_789.pdx</b></span></p><p class="MsoNormal" style="margin-left:102.0pt; text-indent:-.25in; line-height:16.8pt; background:white"><span style="font-size:10.0pt; font-family:&quot;Courier New&quot;; color:#323130"><span style="mso-list:Ignore">o<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp; </span></span></span><u><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130">CuC/ PuC/ SMuC Git Hash</span></u><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130">: 12345vfv67a89aa0123adfvh4567890dc173</span></p><p class="MsoNormal" style="margin-left:102.0pt; text-indent:-.25in; line-height:16.8pt; background:white"><span style="font-size:10.0pt; font-family:&quot;Courier New&quot;; color:#323130"><span style="mso-list:Ignore">o<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp; </span></span></span><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130">CuC</span></p><p class="MsoNormal" style="margin-left:138.0pt; text-indent:-.25in; line-height:16.8pt; background:white"><span style="font-size:10.0pt; font-family:Wingdings; color:#323130"><span style="mso-list:Ignore">§<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130">1234: LIDAR :: Basae :: rfga :: 143123 - some comments</span></p><p class="MsoNormal" style="margin-left:138.0pt; text-indent:-.25in; line-height:16.8pt; background:white"><span style="font-size:10.0pt; font-family:Wingdings; color:#323130"><span style="mso-list:Ignore">§<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130">sda</span></p><p class="MsoNormal" style="margin-left:102.0pt; text-indent:-.25in; line-height:16.8pt; background:white"><span style="font-size:10.0pt; font-family:&quot;Courier New&quot;; color:#323130"><span style="mso-list:Ignore">o<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp; </span></span></span><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130">PuC</span></p><p class="MsoNormal" style="margin-left:168.0pt; text-indent:-.25in; line-height:16.8pt; background:white"><span style="font-size:10.0pt; font-family:Wingdings; color:#323130"><span style="mso-list:Ignore">§<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130">None</span></p><p class="MsoNormal" style="margin-left:3.25in; text-indent:-.25in; line-height:16.8pt; background:white"><span style="font-size:10.0pt; font-family:Wingdings; color:#323130"><span style="mso-list:Ignore">§<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><b><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130">CvApp Innoviz</span></b><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130">&nbsp;K123-v4<b>_RC3</b>&nbsp;</span>""" + \
CH_red[CH_red_i] + \
"""</p><p class="MsoNormal" style="margin-left:102.0pt; text-indent:-.25in; line-height:16.8pt; background:white"><span style="font-size:10.0pt; font-family:&quot;Courier New&quot;; color:#323130"><span style="mso-list:Ignore">o<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp; </span></span></span><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130">SMuC</span></p><p class="MsoNormal" style="margin-left:168.0pt; text-indent:-.25in; line-height:16.8pt; background:white"><span style="font-size:10.0pt; font-family:Wingdings; color:#323130"><span style="mso-list:Ignore">§<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130">None</span></p><p class="MsoNormal" style="margin-left:102.0pt; text-indent:-.25in; line-height:16.8pt; background:white"><span style="font-size:10.0pt; font-family:&quot;Courier New&quot;; color:#323130"><span style="mso-list:Ignore">o<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp; </span></span></span><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130">OM</span></p><p class="MsoNormal" style="margin-left:168.0pt; text-indent:-.25in; line-height:16.8pt; background:white"><span style="font-size:10.0pt; font-family:Wingdings; color:#323130"><span style="mso-list:Ignore">§<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130">&nbsp;</span></p><div style="border:none; border-bottom:double windowtext 2.25pt; padding:0in 0in 1.0pt 0in"><p class="MsoNormal" style="border:none; padding:0in"><span style="font-size:10.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130; background:white">&nbsp;</span></p></div><p class="MsoNormal"><span style="font-size:10.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130; background:white">&nbsp;</span></p><p class="MsoNormal">&lt;p&gt;&lt;span class=\\\\\&quot;""" + \
hglght_shp[hglght_indx] + \
"""\\\\\&quot;&gt;&lt;b&gt;""" + \
pdxName + \
"""&lt;/b&gt;&lt;/span&gt;&amp;nbsp;(G123BF4 Engineering build, &lt;strong&gt;Cmake build&lt;/strong&gt;)&lt;/p&gt;&lt;p&gt;&lt;/p&gt;&lt;ul&gt;&lt;li&gt;Created on """ + \
b4today + \
"""&lt;ul style=\\\\\&quot;margin-left:40px;\\\\\&quot;&gt;&lt;li&gt;&lt;b&gt;THIS IS A CM D2.0 - SAMPLE SOFTWARE&lt;/b&gt;&lt;/li&gt;&lt;li&gt;&lt;u&gt;PDXlocation&lt;/u&gt;: &lt;/li&gt;&lt;li&gt;&lt;u&gt;PDX Template&lt;/u&gt;:&amp;nbsp;&lt;strong&gt;PT01_template.123_456_789.pdx&lt;/strong&gt;&lt;/li&gt;&lt;li&gt;&lt;u&gt;CuC/ PuC/ SMuC Git Hash&lt;/u&gt;: 12345vfv67a89aa0123adfvh4567890dc173&lt;/li&gt;&lt;li&gt;CuC&lt;ul&gt;&lt;li&gt;1234: LIDAR :: Basae :: rfga :: 143123 - some comments&lt;/li&gt;&lt;li&gt;sda&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;&lt;li&gt;PuC&lt;ul style=\\\\\&quot;margin-left:40px;\\\\\&quot;&gt;&lt;li&gt;None&lt;ul style=\\\\\&quot;margin-left:40px;\\\\\&quot;&gt;&lt;li&gt;&lt;strong&gt;CvApp Innoviz&lt;/strong&gt; K123-v4&lt;strong&gt;_RC3&lt;/strong&gt;&amp;nbsp;(""" + \
CH_red_h[CH_red_i] + \
""")&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;&lt;li&gt;SMuC&lt;ul style=\\\\\&quot;margin-left:40px;\\\\\&quot;&gt;&lt;li&gt;None&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;&lt;li&gt;OM&lt;ul style=\\\\\&quot;margin-left:40px;\\\\\&quot;&gt;&lt;li&gt;&lt;br&gt;&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;&lt;/ul&gt;</p><div style="border:none; border-bottom:double windowtext 2.25pt; padding:0in 0in 1.0pt 0in"><p class="MsoNormal" style="border:none; padding:0in">&nbsp;</p></div><p class="MsoNormal">&nbsp;</p></div></body></html>
"""

print(htmlPlainTextPayload)