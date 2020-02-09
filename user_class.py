#https://github.com/bobrynya/py-23/blob/master/vkclient.py
import requests
from pprint import pprint
from urllib.parse import urlencode

class User:
    APP_ID = 7314323
    AUTH_URL = 'https://oauth.vk.com/authorize'
    TOKEN = '619d71b1619d71b1619d71b18561f2ea226619d619d71b13fdd44940bc438bdea8b5efc'

    params = {
        'client_id': APP_ID,
        'access_token': TOKEN,
        'v': '5.95'

    }

    pass