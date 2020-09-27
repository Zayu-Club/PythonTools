import openpyxl
import re

#Only xlsx format is supported
workPath = 'D:\提取IP测试工作簿.xlsx'
sheetName = '咕咕咕'
urlCol = 2
dstCol = 3

#正则提取IP地址
def getUrl2ip(urlStr):
    resultIP = re.findall(r'(?:(?:25[0-5]|2[0-4]\d|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)', urlStr)
    if(resultIP):
        return resultIP
    else:
        return "-"

def main():
    #打开工作簿
    workBook = openpyxl.load_workbook(workPath,data_only=True)
    print("[INFO]工作簿打开成功：" + workPath + "," + str(workBook.sheetnames))
    #选择工作表
    workSheet = workBook[sheetName]
    print("[INFO]目标工作表选择：" + sheetName)
    #获取最大列&最大行
    maxCol = workSheet.max_column
    maxRow = workSheet.max_row
    print("[INFO]获取工作表最大列、行：" + str(maxCol) + "，" + str(maxRow))
    #遍历提取IP写入dstCol列中
    for i in range(2,maxRow+1):
        urlStr = workSheet.cell(row=i, column=urlCol).value
        if urlStr:
            print("[INFO]读取的URL：" + str(urlStr))
            res = getUrl2ip(str(urlStr))
            print("[INFO]提取结果：" + res[0])
            directionCell = workSheet.cell(row=i, column=dstCol)
            directionCell.value = res[0]
            print("[INFO]写入IP")
    workBook.save(workPath)

if __name__ == '__main__':
    args = 'n'
    while not args == 'y' and not args == 'Y':
        args = input("[WARNING]对工作簿的操作无法恢复，请在操作前备份工作簿，按Y键继续[N]：")
    main()
    print("[INFO]全部完成")