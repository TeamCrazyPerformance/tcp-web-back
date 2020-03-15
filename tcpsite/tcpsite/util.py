import os
import json


def get_secret_info(info: str):
    with open(os.path.join(os.getcwd(), 'tcpsite/settings/secret.json'), mode='rt', encoding='utf-8') as file:
        data = json.load(file)
        for key, val in data.items():
            if key == info:
                return val
        raise ValueError('서버정보를 확인할 수 없습니다.')
