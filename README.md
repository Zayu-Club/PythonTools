PythonTools
====
Some Python3 scripts to improve productivity<br>

## Extract_IP_from_URL_in_Excel<br>
Extract the valid IP from the URL string of the xlsx file and put it in another column.<br>
Yes, you are right, the xls format is not supported. It is impossible to adapt to what should be thrown into the garbage in the future. If you need to use it in an xls file, please convert it to xlsx format first. You can subscribe to Office365 through the following link to get the latest Office suite:<br>
[https://www.microsoft.com/en-us/microsoft-365/](https://www.microsoft.com/en-us/microsoft-365/).<br>
### Operation premise<br>
python 3+<br>
pip openpyxl et-xmlfile jdcal<br>
Before running, you also need to modify some parameters in Extract_IP_from_URL_in_Excel.py:<br>
* `workPath`:Path to workbook.
* `sheetName`:The name of the worksheet.
* `urlCol`:The column number of URL.
* `dstCol`:The column number filled in with the extracted IP.<br>
#### Update - 09/30/2020
* Exception handling of getDomainFromURL() function.<br>
#### Update - 09/29/2020
* Support to convert domain name URL to IP address.<br>
* Support extracting multiple IP addresses corresponding to domain names.<br>
* Support the extraction of URLs containing multiple IP addresses in the same cell.<br>
#### Note
* that the index of row number and column number starts from 1, not 0.<br>
* Suggestion: Modify the cell format of the URL field to text.

## IP_Address_Change_Reminder<br>
In environments with dynamic IP addresses, monitor IP address changes and issue notifications.<br>
This tool currently supports ServerChan and email notifications.<br>
Serverchan is a third-party messaging platform that can push messages to your WeChat. You need to log in to ServerChan and obtain a token, and then associate it with your WeChat account. For specific usage, please refer to:<br>
[http://sc.ftqq.com/3.version](http://sc.ftqq.com/3.version).<br>
[http://pushbear.ftqq.com/admin/#/](http://pushbear.ftqq.com/admin/#/).<br>
### Operation premise<br>
python 3+<br>
requirements:certifi==2020.6.20 chardet==3.0.4 idna==2.10 pip==20.1.1 requests==2.24.0 setuptools==47.1.0 urllib3==1.25.10<br>
Before running, you also need to modify some parameters in conf.json:<br>
* `cycle_period`:Detection cycle, the unit is "minutes".
* `sckey`:The token value used by ServerChan. If ServerChan is not used for message push, the value of remindServerChan is set to false, and the remindServerChan node is ignored.
* `SendKey`:The token value used by PushBear. If PushBear is not used for message push, the value of remindPushBear is
set to false, and the remindPushBear node is ignored.
* `smtp_host`:SMTP Server
* `smtp_user`:Sender user name(Email address used by sender)
* `smtp_pass`:Email password used by sender
* `sender`:Email address used by sender
* `receivers`:The recipient��s email address, supports multiple recipients<br>
#### Update - 10/06/2020
* Fixed: Program crash caused by network connection interruption.<br>
#### Update - 19/02/2021
* Added PushBear push support.<br>
#### Note
* The `public_ip` field in the `conf.json` file can be left blank and does not need to be modified. When the latest address is obtained, it will be filled in automatically.
* You can use your own mail server or the SMTP service provided by a third-party mail service provider.
* This is a tool that requires a permanent process, and most of the time we don't want it to always run on the front-end console. If you are under Linux, you need other software to make it run in the background.For example using nohup or daemon.<br>