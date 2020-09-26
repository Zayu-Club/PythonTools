PythonTools
====
Some Python3 scripts to improve productivity<br>

## Extract_IP_from_URL_in_Excel<br>
Extract the valid IP from the URL string of the xlsx file and put it in another column
### Operation premise<br>
python3+<br>
pip openpyxl<br>
Before running, you also need to modify some parameters in Extract_IP_from_URL_in_Excel.py:<br>
* `workPath`:Path to workbook.
* `sheetName`:The name of the worksheet.
* `urlCol`:Column number of URL.
* `dstCol`:The line number filled in with the extracted IP.<br>

Note that the index of row number and column number starts from 1, not 0
