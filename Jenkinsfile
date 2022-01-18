pipeline {
    agent any
    stages {
        stage('Welcome Step') {
            steps { 
                echo 'Welcome to the LambdaTest'
            }
        }
        stage('check if py file exists'){
            steps {
                
                script {
                    if(fileExists("./branch2_1/test_pySh.py")) {
                        echo 'py file exists'
                        var1 = bat(script:'python ./branch2_1/test_pySh.py', returnStdout: true).trim()
                        var2 = var1[var1.indexOf('<html>')..(var1.indexOf('</html>')+7)]
                        writeFile file: 'smpl.txt', text: var2
                        mail to:'shubham.bawankar@kpit.com',
                        mimeType: 'text/html',
                        subject:'test email1',
                        body: var2
//                         body:"""<html><head>
// <meta http-equiv="Content-Type" content="text/html; charset=utf-8"><meta name="Generator" content="Microsoft Word 15 (filtered medium)"><style>
// <!--
// @font-face
// 	{font-family:Wingdings}
// @font-face
// 	{font-family:"Cambria Math"}
// @font-face
// 	{font-family:Calibri}
// @font-face
// 	{font-family:"Segoe UI"}
// p.MsoNormal, li.MsoNormal, div.MsoNormal
// 	{margin:0in;
// 	font-size:11.0pt;
// 	font-family:"Calibri",sans-serif}
// span.EmailStyle17
// 	{font-family:"Calibri",sans-serif;
// 	color:windowtext}
// .MsoChpDefault
// 	{font-family:"Calibri",sans-serif}
// @page WordSection1
// 	{margin:1.0in 1.0in 1.0in 1.0in}
// div.WordSection1
// 	{}
// ol
// 	{margin-bottom:0in}
// ul
// 	{margin-bottom:0in}
// -->
// </style></head><body lang="EN-US" link="#0563C1" vlink="#954F72" style="word-wrap:break-word"><div class="WordSection1"><p class="MsoNormal" style="margin-bottom:16.8pt; line-height:16.8pt; background:white"><b><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130; background:lime">JJJJJJJJJJJJJ_123456F7.123_456_789</span></b><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130">&nbsp;(G123BF4 Engineering build,<b>Cmake build</b>)</span><span style="color:black"></span></p><ul type="disc" style="margin-top:0in"><li class="MsoNormal" style="color:#323130; line-height:16.8pt; background:white"><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif">Created on 01/01/2020</span></li></ul><p class="MsoNormal" style="margin-left:102.0pt; text-indent:-.25in; line-height:16.8pt; background:white"><span style="font-size:10.0pt; font-family:&quot;Courier New&quot;; color:#323130">o</span><span style="font-size:7.0pt; font-family:&quot;Times New Roman&quot;,serif; color:#323130">&nbsp;&nbsp;&nbsp;&nbsp;</span><b><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130">THIS IS A CM D2.0 - SAMPLE SOFTWARE</span></b><span style="color:black"></span></p><p class="MsoNormal" style="margin-left:102.0pt; text-indent:-.25in; line-height:16.8pt; background:white"><span style="font-size:10.0pt; font-family:&quot;Courier New&quot;; color:#323130">o</span><span style="font-size:7.0pt; font-family:&quot;Times New Roman&quot;,serif; color:#323130">&nbsp;&nbsp;&nbsp;&nbsp;</span><u><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130">PDXlocation</span></u><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130">:</span><span style="color:black"></span></p><p class="MsoNormal" style="margin-left:102.0pt; text-indent:-.25in; line-height:16.8pt; background:white"><span style="font-size:10.0pt; font-family:&quot;Courier New&quot;; color:#323130">o</span><span style="font-size:7.0pt; font-family:&quot;Times New Roman&quot;,serif; color:#323130">&nbsp;&nbsp;&nbsp;&nbsp;</span><u><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130">PDX Template</span></u><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130">:&nbsp;<b>PT01_template.123_456_789.pdx</b></span><span style="color:black"></span></p><p class="MsoNormal" style="margin-left:102.0pt; text-indent:-.25in; line-height:16.8pt; background:white"><span style="font-size:10.0pt; font-family:&quot;Courier New&quot;; color:#323130">o</span><span style="font-size:7.0pt; font-family:&quot;Times New Roman&quot;,serif; color:#323130">&nbsp;&nbsp;&nbsp;&nbsp;</span><u><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130">CuC/ PuC/ SMuC Git Hash</span></u><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130">: 12345vfv67a89aa0123adfvh4567890dc173</span><span style="color:black"></span></p><p class="MsoNormal" style="margin-left:102.0pt; text-indent:-.25in; line-height:16.8pt; background:white"><span style="font-size:10.0pt; font-family:&quot;Courier New&quot;; color:#323130">o</span><span style="font-size:7.0pt; font-family:&quot;Times New Roman&quot;,serif; color:#323130">&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130">CuC</span><span style="color:black"></span></p><p class="MsoNormal" style="margin-left:138.0pt; text-indent:-.25in; line-height:16.8pt; background:white"><span style="font-size:10.0pt; font-family:Wingdings; color:#323130">§</span><span style="font-size:7.0pt; font-family:&quot;Times New Roman&quot;,serif; color:#323130">&nbsp;&nbsp;</span><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130">1234: LIDAR :: Basae :: rfga :: 143123 - some comments</span><span style="color:black"></span></p><p class="MsoNormal" style="margin-left:138.0pt; text-indent:-.25in; line-height:16.8pt; background:white"><span style="font-size:10.0pt; font-family:Wingdings; color:#323130">§</span><span style="font-size:7.0pt; font-family:&quot;Times New Roman&quot;,serif; color:#323130">&nbsp;&nbsp;</span><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130">sda</span><span style="color:black"></span></p><p class="MsoNormal" style="margin-left:102.0pt; text-indent:-.25in; line-height:16.8pt; background:white"><span style="font-size:10.0pt; font-family:&quot;Courier New&quot;; color:#323130">o</span><span style="font-size:7.0pt; font-family:&quot;Times New Roman&quot;,serif; color:#323130">&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130">PuC</span><span style="color:black"></span></p><p class="MsoNormal" style="margin-left:168.0pt; text-indent:-.25in; line-height:16.8pt; background:white"><span style="font-size:10.0pt; font-family:Wingdings; color:#323130">§</span><span style="font-size:7.0pt; font-family:&quot;Times New Roman&quot;,serif; color:#323130">&nbsp;&nbsp;</span><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130">None</span><span style="color:black"></span></p><p class="MsoNormal" style="margin-left:3.25in; text-indent:-.25in; line-height:16.8pt; background:white"><span style="font-size:10.0pt; font-family:Wingdings; color:#323130">§</span><span style="font-size:7.0pt; font-family:&quot;Times New Roman&quot;,serif; color:#323130">&nbsp;&nbsp;</span><b><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130">CvApp Innoviz</span></b><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130">&nbsp;K123-v4<b>_RC3</b>&nbsp;(</span><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#E81123">Changed&nbsp;</span><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130">UnChanged)</span><span style="color:black"></span></p><p class="MsoNormal" style="margin-left:102.0pt; text-indent:-.25in; line-height:16.8pt; background:white"><span style="font-size:10.0pt; font-family:&quot;Courier New&quot;; color:#323130">o</span><span style="font-size:7.0pt; font-family:&quot;Times New Roman&quot;,serif; color:#323130">&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130">SMuC</span><span style="color:black"></span></p><p class="MsoNormal" style="margin-left:168.0pt; text-indent:-.25in; line-height:16.8pt; background:white"><span style="font-size:10.0pt; font-family:Wingdings; color:#323130">§</span><span style="font-size:7.0pt; font-family:&quot;Times New Roman&quot;,serif; color:#323130">&nbsp;&nbsp;</span><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130">None</span><span style="color:black"></span></p><p class="MsoNormal" style="margin-left:102.0pt; text-indent:-.25in; line-height:16.8pt; background:white"><span style="font-size:10.0pt; font-family:&quot;Courier New&quot;; color:#323130">o</span><span style="font-size:7.0pt; font-family:&quot;Times New Roman&quot;,serif; color:#323130">&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130">OM</span><span style="color:black"></span></p><p class="MsoNormal" style="margin-left:168.0pt; text-indent:-.25in; line-height:16.8pt; background:white"><span style="font-size:10.0pt; font-family:Wingdings; color:#323130">§</span><span style="font-size:7.0pt; font-family:&quot;Times New Roman&quot;,serif; color:#323130">&nbsp;&nbsp;</span><span style="font-size:13.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130">&nbsp;</span><span style="color:black"></span></p><p class="MsoNormal"><span style="font-size:10.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130; background:white">&nbsp;</span><span style="color:black"></span></p><p class="MsoNormal"><span style="font-size:10.5pt; font-family:&quot;Segoe UI&quot;,sans-serif; color:#323130; background:white">&nbsp;</span><span style="color:black"></span></p><p class="MsoNormal"><span style="color:black">&lt;p&gt;&lt;span class=\\\\”highlightColorGreen\\\\”&gt;&lt;b&gt;JJJJJJJJJJ_123456F7.123_456_789&lt;/b&gt;&lt;/span&gt;&amp;nbsp;(G123BF4 Engineering build,&lt;strong&gt;Cmake build&lt;/strong&gt;)&lt;/p&gt;&lt;p&gt;​​​​​​​​​​​​​​&lt;/p&gt;&lt;ul&gt;&lt;li&gt;Created on 01/01/2020&lt;ul style=\\\\”margin-left:40px;\\\\”&gt;&lt;li&gt;&lt;b&gt;THIS IS A CM D2.0 - SAMPLE SOFTWARE&lt;/b&gt;&lt;/li&gt;&lt;li&gt;&lt;u&gt;PDXlocation&lt;/u&gt;: &lt;/li&gt;&lt;li&gt;&lt;u&gt;PDX Template&lt;/u&gt;:&amp;nbsp;&lt;strong&gt;PT01_template.123_456_789.pdx&lt;/strong&gt;&lt;/li&gt;&lt;li&gt;&lt;u&gt;CuC/ PuC/ SMuC Git Hash&lt;/u&gt;: 12345vfv67a89aa0123adfvh4567890dc173&lt;/li&gt;&lt;li&gt;CuC&lt;ul&gt;&lt;li&gt;1234: LIDAR :: Basae :: rfga :: 143123 - some comments&lt;/li&gt;&lt;li&gt;sda&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;&lt;li&gt;PuC&lt;ul style=\\\\”margin-left:40px;\\\\”&gt;&lt;li&gt;None&lt;ul style=\\\\”margin-left:40px;\\\\”&gt;&lt;li&gt;&lt;strong&gt;CvApp Innoviz&lt;/strong&gt; K123-v4&lt;strong&gt;_RC3&lt;/strong&gt;&amp;nbsp;(&lt;span class=\\\\”fontColorRed\\\\”&gt;Changed &lt;/span&gt;UnChanged)&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;&lt;li&gt;SMuC&lt;ul style=\\\\”margin-left:40px;\\\\”&gt;&lt;li&gt;None&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;&lt;li&gt;OM&lt;ul style=\\\\”margin-left:40px;\\\\”&gt;&lt;li&gt;&lt;br&gt;&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;&lt;/ul&gt;</span></p><p class="MsoNormal"><span style="color:black">&nbsp;</span></p><p class="MsoNormal"><span style="color:black">&nbsp;</span></p><p class="MsoNormal">&nbsp;</p></div></body></html>"""
                        
                        
                    }
                    else {
                        echo '404: file not exists'
                    }
                }
                
            }
            
        }
    }
}
