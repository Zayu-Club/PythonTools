import smtplib
import sys
import json
import os
import requests
import time
import datetime
from time import strftime
from email.mime.text import MIMEText
from email.header import Header

CONFPATH = 'conf.json'

def ReadConfig(configPath, rwopt):
    config = ''
    try:
        with open(configPath, rwopt, encoding='utf-8') as jsonFile:
            config = json.load(jsonFile)
        #print("[INFO]Load JSON file successfully: " + configPath)
        jsonFile.close()
        #print("[DEBUG]JSON file  " + str(config))
    except Exception as e:
        print("[INFO]Loading JSON file failed: " + configPath)   
        print(e)
    return config

def GetPublicIpAddress():
    requestIpUrl="http://ip.42.pl/raw"
    try:
        reponse = requests.get(requestIpUrl)   
        responseIpAddress = reponse.text
    except Exception as e:
        print("[WARN]Failed to obtain public network address, retrying...")
        return 'Failed'
    print("[INFO]Successfully obtained public network address: " + responseIpAddress)
    return responseIpAddress

def SendWechat(config,messageTitle,messageStr):
    if(config['remindServerChan']['enable'] == "true"):
        print("[INFO]Config['remindServerChan']['enable'] value is : true ,should send Wechat message")
        sckey = config['remindServerChan']['sckey']
        print("[INFO]Your ServerChan Token: " + sckey)
        reqStr = "https://sc.ftqq.com/" + sckey + ".send"
        try:
            reponse = requests.get(reqStr,params={'text': messageTitle, 'desp': messageStr})
            print("[DEBUG]HTTP GET Reponse :" + reponse.text.encode('utf-8').decode('unicode_escape'))
        except Exception as e:
            print("[ERROR]Failed to send WechatMessage")

def SendWechatPushBear(config,messageTitle,messageStr):
    if(config['remindPushBear']['enable'] == "true"):
        print("[INFO]Config['remindPushBear']['enable'] value is : true ,should send WechatPushBear message")
        SendKey = config['remindPushBear']['SendKey']
        print("[INFO]Your PushBearn Token: " + SendKey)
        reqStr = "https://pushbear.ftqq.com/sub"
        try:
            reponse = requests.get(reqStr,params={'sendkey': SendKey, 'text': messageTitle, 'desp': messageStr}) 
            print("[DEBUG]HTTP GET Reponse :" + reponse.text.encode('utf-8').decode('unicode_escape'))
        except Exception as e:
            print("[ERROR]Failed to send remindPushBearMessage")


def SendMessage(config,messageStr):
    if(config['remindMail']['enable'] == "true"):
        print("[INFO]Config['remindMail']['enable'] value is : true ,should send message")
        #print("[DEBUG]The Message is :" + messageStr)
        smtp_host = config['remindMail']['smtp_host']
        smtp_user = config['remindMail']['smtp_user']
        smtp_pass = config['remindMail']['smtp_pass']
        sender = config['remindMail']['sender']
        receivers = config['remindMail']['receivers']
        subject = 'IP address has been updated'
        message = MIMEText(messageStr, 'plain', 'utf-8')
        message['From'] = Header("Alert", 'utf-8')
        message['Subject'] = Header(subject, 'utf-8')
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(smtp_host, 25)
            smtpObj.login(smtp_user,smtp_pass)
            smtpObj.sendmail(sender, receivers, message.as_string())
            print("[INFO]Mail sent successfully")
        except smtplib.SMTPException:
            print("[ERROR]Failed to send mail")

def UpdateRecord(config):
    conf_ip = config['public_ip']
    try:
        new_ip = GetPublicIpAddress()
        if(not conf_ip == new_ip and not new_ip == 'Failed'):
            print("[INFO]IP address has been updated")      
            config['public_ip'] = new_ip
            with open(CONFPATH, 'w+') as new_conf:
                json.dump(config, new_conf, indent=4)
            new_conf.close()
            print("[INFO]Update record successfully")
            return True
    except Exception as e:
        print("[ERROR]Failed to Update record")
        return False
    else:
        return False

def main():
    while(True):
        CONFIG_FILE = ReadConfig(CONFPATH, 'r')     
        CYCLE_PERIOD = CONFIG_FILE['cycle_period']

        timeNow = datetime.datetime.now()
        timeNow.strftime("%Y/%m/%d %H:%M:%S")

        boolUpdated = UpdateRecord(CONFIG_FILE)
        if(boolUpdated):
            msgTitle = "公网IP地址变更提醒"
            msgText = "The public IP address of the node you are following has been updated. The new address is: " + CONFIG_FILE['public_ip']
            SendMessage(CONFIG_FILE, msgText)
            SendWechat(CONFIG_FILE, msgTitle, msgText)
            SendWechatPushBear(CONFIG_FILE, msgTitle, msgText)
    
        timeNext = timeNow + datetime.timedelta(seconds = 60*CYCLE_PERIOD)
        print("[INFO]Next Check Time: " + str(timeNext))

        time.sleep(60*CYCLE_PERIOD)

if __name__ == '__main__':
    main()