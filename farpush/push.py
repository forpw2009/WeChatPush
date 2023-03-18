from itchat.config import PHONE_TYPE
from itchat.config import PUSH_REGID
from itchat.config import BLOCK_NAME
from itchat.config import MES_THROUGH
import requests
import socket
import json

farpush_url = ""



class farpush:
    def __init__(self):
        self.regid = PUSH_REGID
        self.phone = PHONE_TYPE
        self.block = BLOCK_NAME
        self.through = MES_THROUGH

    def push(self, title, content):
        # block name
        try:
            response = requests.post(
                farpush_url,
                headers={
                    "Content-Type": "application/json; charset=utf-8",
                },
                data=json.dumps({
                    "body": content,
                    "device_key": "nysrshcqielvoxsa",
                    "title": title,
                    "category": "myNotificationCategory",
                    "sound": "minuet.caf",
                    "badge": 1,
                    "icon": "https://day.app/assets/images/avatar.jpg",
                    "group": "wechat",
                    "url": "mp://"
                })
            )
            print('Response HTTP Status Code: {status_code}'.format(
                status_code=response.status_code))
            print('Response HTTP Response Body: {content}'.format(
                content=response.content))
        except requests.exceptions.RequestException:
            print('HTTP Request failed')

        
        
    def mediapush(self, title, content, filename):
        # block name
        try:
            resource = {"filename": filename}
            data['resource'] = json.dumps(resource)
            response = requests.post(
                farpush_url,
                headers={
                    "Content-Type": "application/json; charset=utf-8",
                },
                data=json.dumps({
                    "body": content,
                    "device_key": "nysrshcqielvoxsa",
                    "title": title,
                    "category": "myNotificationCategory",
                    "sound": "minuet.caf",
                    "badge": 1,
                    "icon": "https://day.app/assets/images/avatar.jpg",
                    "group": "wechat",
                    "url": "mp://"
                })
            )
            print('Response HTTP Status Code: {status_code}'.format(
                status_code=response.status_code))
            print('Response HTTP Response Body: {content}'.format(
                content=response.content))
        except requests.exceptions.RequestException:
            print('HTTP Request failed')        
