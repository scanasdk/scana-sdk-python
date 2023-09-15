# -*- coding: utf-8 -*-
from pyscanasdk.moderation import ModerateClient

mc = ModerateClient(app_id="6373541cb070b000014fe1b4",  # 得到的appid
                    secret_key="96499bef-0e8c-11ee-959a-fa163e9175b9",  # 得到的秘钥
                    text_business_id="1782020298506240143")  # 文本的业务id
resp = mc.text_moderation("中国")
print(resp) # {'code': 200, 'data': {'type': '正常', 'score': 1}, 'msg': 'OK'}
