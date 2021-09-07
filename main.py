#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 20:14:04 2019

@author: Kshitij Gupta <kshitijgm@gmail.com>
"""

from bs4 import BeautifulSoup
from shutil import which
import requests
import time
import subprocess
import sys
import dotenv
import os

dotenv.load_dotenv('config.env')

def telegram_bot_sendtext(bot_message):
   bot_token = os.environ.get("BOT_TOKEN", 0)
   bot_chatID = os.environ.get("CHAT_ID", 0)
   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
   response = requests.get(send_text)
   return response.json()

def check_app(name):
    ret = which(name) is not None
    if not ret:
        print('[*] command not found: {}'.format(name))
    return ret


def main():
    url = 'https://android.googlesource.com/platform/manifest/+refs'
    matching = []

    while len(matching) == 0:
        print('\n[*] Checking!')
        tag_list = []
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for li in soup.findAll('li', {'class': 'RefList-item'}):
            tag = li.findChildren('a', recursive=False)[0]['href'].split('/')[-1]
            tag_list.append(tag)
        matching = [s for s in tag_list if 'android-12' in s or 'android12' in s]
        if len(matching) > 0:
            telegram_bot_sendtext("ANDROID 12 IS HERE!")
        else:
            telegram_bot_sendtext("No Android 12 (yet) 😕")
            time.sleep(60 * 60)  # Wait for 60 minutes
    try:
        from subprocess import DEVNULL
    except ImportError:
        import os
        DEVNULL = open(os.devnull, 'wb')
    subprocess.Popen([term, '-e', 'nyancat'], stdout=DEVNULL, stderr=subprocess.STDOUT)


if __name__ == '__main__':
    main()
