
import subprocess
from zs_eyes import logger
import time
import json
import requests


def message(tel: str, msg: str) -> bool:

    adb_exec = 'adb shell am start -a android.intent.action.SENDTO -d smsto:%s --es sms_body "%s"'
    action = adb_exec % (tel, msg)
    logger.info(action)
    p1 = subprocess.Popen(action, shell=True, stdout=subprocess.PIPE)
    logger.info("code: " + str(p1.returncode))

    time.sleep(0.5)

    # 移动发送按钮的坐标
    action = 'adb "input keyevent 22 && input keyevent 22"'
    logger.info(action)
    p2 = subprocess.Popen(action, shell=True, stdout=subprocess.PIPE)
    logger.info("code: " + str(p2.returncode))

    return p1.returncode == 0 and p2.returncode == 0


def call(tel: str, wait: int) -> bool:

    adb_exec = 'adb shell am start -a android.intent.action.CALL -d tel:%s'
    action = adb_exec % tel
    logger.info(action)
    p1 = subprocess.Popen(action, shell=True, stdout=subprocess.PIPE)

    # 持续call
    time.sleep(wait)

    # 挂断
    action = 'adb shell input keyevent 6'
    logger.info(action)
    p2 = subprocess.Popen(action, shell=True, stdout=subprocess.PIPE)
    logger.info("code: " + str(p2.returncode))

    return p1.returncode == 0 and p2.returncode == 0


def pushpush(title, p_content, pushplus_token):
    """
    使用pushplus服务做微信消息推送
    http://www.pushplus.plus/
    :return:
    """
    token = pushplus_token
    content = p_content
    url = 'http://www.pushplus.plus/send'
    data = {
        "token": token,
        "title": title,
        "template": "txt",
        "content": content
    }
    body = json.dumps(data).encode(encoding='utf-8')
    headers = {'Content-Type': 'application/json'}

    requests.post(url=url, data=body, headers=headers)
