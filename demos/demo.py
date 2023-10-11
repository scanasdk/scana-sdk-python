# -*- coding: utf-8 -*-
from pyscanasdk.v3 import ModerateClient
import uuid

app_id = "xxxx"
secret_key = "xxxx"
text_business_id = 'xxxx'
img_business_id = 'xxxx'
audio_business_id = 'xxxx'
video_business_id = 'xxxx'
doc_business_id = 'xxxx'

def gen_sign_by_url(url):
    mc = ModerateClient(app_id=app_id,  # 得到的appid
                        secret_key=secret_key,  # 得到的秘钥
                        doc_business_id=doc_business_id)  # 文档的业务id

    result = mc.validate_signature_by_url(url)
    return result


def gen_sign(business_id, timestamp, nonce):
    mc = ModerateClient(app_id=app_id,  # 得到的appid
                        secret_key=secret_key,  # 得到的秘钥
                        doc_business_id=doc_business_id)  # 文档的业务id
    # 生成signature  business_id为当前业务类型的id     timestamp：时间戳  nonce 随机数
    sign = mc.gen_signature(business_id=business_id, timestamp=timestamp, nonce=nonce)
    return sign

def text_test():
    """
    文本检测 示例
    """
    mc = ModerateClient(app_id=app_id,  # 得到的appid
                        secret_key=secret_key,  # 得到的秘钥
                        text_business_id=text_business_id)  # 文本的业务id
    content = [
        {"contentId": uuid.uuid4().__str__(), "data": "待检测内容1"},
        {"contentId": uuid.uuid4().__str__(), "data": "待检测内容2"},
    ]
    resp = mc.text(content=content, ac=True)  # ac默认值为False 同步     为True时异步
    print(resp)
    # 生成signature  business_id为当前业务类型的id     timestamp：时间戳  nonce 随机数
    sign = mc.gen_signature(business_id=text_business_id, timestamp=1615646461100, nonce=1)
    print(sign)


def img_test():
    """
    图片检测 示例
    """
    mc = ModerateClient(app_id=app_id,  # 得到的appid
                        secret_key=secret_key,  # 得到的秘钥
                        img_business_id=img_business_id)  # 图片的业务id
    content = [
        {
            "contentId": "测试回调",
            "data": "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png",  # 图片链接
            "type": 1  # 调用类型，1图片url，2图片base64
        },
        {
            "contentId": "测试回调2",
            "data": "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png",  # 图片链接
            "type": 1  # 调用类型，1图片url，2图片base64
        },
    ]
    resp = mc.image(content=content, ac=True)  # ac默认值为False 同步     为True时异步
    print(resp)
    # 生成signature  business_id为当前业务类型的id     timestamp：时间戳  nonce 随机数
    sign = mc.gen_signature(business_id=img_business_id, timestamp=1615646461100, nonce=1)
    print(sign)


def video_test():
    """
    视频检测 示例
    """
    mc = ModerateClient(app_id=app_id,  # 得到的appid
                        secret_key=secret_key,  # 得到的秘钥
                        video_business_id=video_business_id)  # 视频的业务id
    content = 'http://example.mp4'  # 待检测视频链接
    resp = mc.video(content=content)
    print(resp)
    # 生成signature  business_id为当前业务类型的id     timestamp：时间戳  nonce 随机数
    sign = mc.gen_signature(business_id=video_business_id, timestamp=1615646461100, nonce=1)
    print(sign)


def audio_test():
    """
    音频检测 示例
    """
    mc = ModerateClient(app_id=app_id,  # 得到的appid
                        secret_key=secret_key,  # 得到的秘钥
                        audio_business_id=audio_business_id)  # 音频的业务id
    content = 'http://example.mp4'  # 待检测音频链接
    resp = mc.audio(content=content)
    print(resp)
    # 生成signature  business_id为当前业务类型的id     timestamp：时间戳  nonce 随机数
    sign = mc.gen_signature(business_id=audio_business_id, timestamp=1615646461100, nonce=1)
    print(sign)


def doc_test():
    """
    文档检测 示例
    """
    mc = ModerateClient(app_id=app_id,  # 得到的appid
                        secret_key=secret_key,  # 得到的秘钥
                        doc_business_id=doc_business_id)  # 文档的业务id
    content = 'http://example.docx'  # 待检测文档链接
    resp = mc.doc(content=content)
    print(resp)
    # 生成signature  business_id为当前业务类型的id     timestamp：时间戳  nonce 随机数
    sign = mc.gen_signature(business_id=doc_business_id, timestamp=1615646461100, nonce=1)
    print(sign)




if __name__ == "__main__":

    url = 'https://xxxx.xxx?businessId=111111111&nonce=1&timestamp=1611111111111&signature=xxxxxxx'
    print(gen_sign_by_url(url))
    # pass
    # mc = ModerateClient(img_business_id='1800097935845781514', secret_key='a2f175a8-5373-11ed-9949-0242ac12000e',
    #                     app_id='62ac786311b92177337a933b'
    #                     )
    # content = [
    #     {
    #         "contentId": "测试回调",
    #         "data": "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png",  # 图片链接
    #         "type": 1  # 调用类型，1图片url，2图片base64
    #     }
    #
    # ]
    # res = mc.image(content=content, extra='123')
    # print(res)