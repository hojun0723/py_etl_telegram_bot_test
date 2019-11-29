import time
import telepot
import os
#import requests as rq from bs4 import BeautifulSoup
import subprocess

token = '936440450:AAEBVP0m7KBwngSSL5DEjFjuyAghqZo4MQU'
bot = telepot.Bot(token)

InfoMsg = '메뉴를 선택하세요\n'\
          '1. ETL 수동실행\n'\
          '2. ETL 모니터링\n'\
          '3. 종료'

status = True           # 대기를 위한 변수

def exec(userid):
    #dtexec /ISServer "\SSISDB\COMPANY\PJTNONSAP\PKG_MART_TMMNG001.dtsx" /Server "localhost" /Set "\Package.Variables[pFrDate];20190905" /Set "\Package.Variables[pToDate];20190906"
    cmd = 'dtexec /ISServer "\SSISDB\COMPANY\PJTNONSAP\PKG_MART_TMMNG001.dtsx" /Server "localhost" /Set "\Package.Variables[pFrDate];20190905" /Set "\Package.Variables[pToDate];20190906"'
    #cmd = 'dir/w'
    #msg = 'dir'
    #os.system(msg)
    #subprocess.run([msg], shell=True, check=True)

    try:
        subprocess.check_call(cmd, shell=True)
    except subprocess.CalledProcessError as err:
        print("error code", err.returncode, err.output)
        
        if err.returncode == 1:
            bot.sendMessage(userid, '실패했습니다')
        
def handle(msg):

    content, chat, id = telepot.glance(msg)
    print(content, chat, id)    #메시지타입, 채팅타입, 메시지 송신아이디

    if content == 'text':
        if msg['text'] == '1':
            bot.sendMessage(id, 'ETL 수동실행을 시작합니다....')
            msg = exec(id)
            bot.sendMessage(id, msg)

        elif msg['text'] == '2':
            bot.sendMessage(id, 'ETL 모니터링을 시작합니다....')
        elif msg['text'] == '3':
            bot.sendMessage(id, '종료합니다')
            os._exit(1)
        else:
            bot.sendMessage(id, InfoMsg)

bot.message_loop(handle)

while status == True:
    time.sleep(10)