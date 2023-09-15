
import subprocess
from zs_eyes import logger
import time
import json
import requests


def message(tel: str, msg: str) -> bool:

    for retry in range(3):
        adb_exec = 'adb shell \'am start -a android.intent.action.SENDTO -d smsto:%s --es sms_body "%s"\''
        action = adb_exec % (tel, msg)
        logger.info(action)
        p1 = subprocess.Popen(action, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Popen是异步的, 要等待执行结果
        p1.wait()

        stdout, stderr = p1.communicate()
        logger.info("code: %d, out: %s, err:%s" % (p1.returncode, stdout, stderr))

        if p1.returncode != 0:
            time.sleep(0.5)
            continue

        time.sleep(0.5)

        # 移动发送按钮的坐标
        action = 'adb shell \'input keyevent 22 && input keyevent 22 && input keyevent 66\''
        logger.info(action)
        p2 = subprocess.Popen(action, shell=True, stdout=subprocess.PIPE)
        p2.wait()

        stdout, stderr = p2.communicate()
        logger.info("code: %d, out: %s, err:%s" % (p2.returncode, stdout, stderr))

        if p2.returncode != 0:
            time.sleep(0.5)
            continue

        return True

    return False


def call(tel: str, wait: int) -> bool:

    for retry in range(3):
        adb_exec = 'adb shell am start -a android.intent.action.CALL -d tel:%s'
        action = adb_exec % tel
        logger.info(action)
        p1 = subprocess.Popen(action, shell=True, stdout=subprocess.PIPE)
        p1.wait()

        stdout, stderr = p1.communicate()
        logger.info("code: %d, out: %s, err:%s" % (p1.returncode, stdout, stderr))

        if p1.returncode != 0:
            time.sleep(0.5)
            continue

        # 持续call
        time.sleep(wait)
        break

    # 挂断
    action = 'adb shell input keyevent 6'
    logger.info(action)
    p2 = subprocess.Popen(action, shell=True, stdout=subprocess.PIPE)
    p2.wait()

    stdout, stderr = p2.communicate()
    logger.info("code: %d, out: %s, err:%s" % (p2.returncode, stdout, stderr))
    return p2.returncode == 0


def pushpush(title, p_content, pushplus_token, topic=None):
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
        "content": content,
        "topic": topic
    }
    body = json.dumps(data).encode(encoding='utf-8')
    headers = {'Content-Type': 'application/json'}
    result = False
    for retry in range(3):
        result = requests.post(url=url, data=body, headers=headers)
        if result.ok:
            result = True
            break
    return result


if __name__ == "__main__":
    message('15018444971', '测试免打扰')