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
   bot_token = os.environ['BOT_TOKEN']
   bot_chatID = os.environ['CHAT_ID']
   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=MarkdownV2=' + bot_message
   response = requests.get(send_text)
   return response.json()

def check_app(name):
    ret = which(name) is not None
    if not ret:
        print('[*] command not found: {}'.format(name))
    return ret


def main():
    url = 'https://android.googlesource.com/platform/frameworks/base/+refs'
    matching = []

    while len(matching) == 0:
        print('\n[*] Checking!')
        tag_list = []
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for li in soup.findAll('li', {'class': 'RefList-item'}):
            tag = li.findChildren('a', recursive=False)[0]['href'].split('/')[-1]
            tag_list.append(tag)
        matching = [s for s in tag_list if 'android-12' in s or 'android12' in s or 'android-12.0.0_r1' in s or 'android-12.0.0_r2' in s]
        if len(matching) > 0:
            telegram_bot_sendtext("platform_frameworks_base is out! [frameworks/base](https://android.googlesource.com/platform/frameworks/base/+/refs/tags/android-12.0.0_r2)"
            exit()
        else:
            time.sleep(1 * 60)  # Wait for 1 minutes

if __name__ == '__main__':
    main()
