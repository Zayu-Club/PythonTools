PythonTools
====
Some Python3 scripts to improve productivity<br>

## Extract_IP_from_URL_in_Excel<br>
Extract the valid IP from the URL string of the xlsx file and put it in another column<br>
Yes, you are right, the xls format is not supported. It is impossible to adapt to what should be thrown into the garbage in the future. If you need to use it in an xls file, please convert it to xlsx format first. You can subscribe to Office365 through the following link to get the latest Office suite:<br>
[https://www.microsoft.com/en-us/microsoft-365/](https://www.microsoft.com/en-us/microsoft-365/)<br>
### Operation premise<br>
python3+<br>
pip openpyxl<br>
Before running, you also need to modify some parameters in Extract_IP_from_URL_in_Excel.py:<br>
* `workPath`:Path to workbook.
* `sheetName`:The name of the worksheet.
* `urlCol`:The column number of URL.
* `dstCol`:The column number filled in with the extracted IP.<br>

Note that the index of row number and column number starts from 1, not 0
