from zs_eyes import logger, doctorCode, deptCode
import requests
import json


def check_registration_result(raw_resp: dict) -> (bool, list):
    l = raw_resp.get("list", [])
    has_leave = [{'regDate': reg.get('regDate'),
                  'regWeekDay': reg.get('regWeekDay'),
                  'doctorName': reg.get('doctorName'),
                  'treatFee': reg.get('treatFee')}
                 for reg in l
                 if float(reg.get('treatFee', 0)) <= 60
                 and
                 int(reg.get('regLeaveCount', 0)) > 0]
    logger.info("has leave: %s" % has_leave)
    print("has leave : %d" % len(has_leave))
    if len(has_leave) == 0:
        logger.info("----------> 没有号了!!!")
        print("-------------> 没有号了!!!")
        return False, []
    else:
        logger.info("============> 查到有号了!!!")
        print("============> 查到有号了!!!")
        return True, has_leave


def get_registration(g_host: str) -> dict:
    # global doctorCode
    # global deptCode
    path = "/smc/api/registration/v2/doctorSchedule"
    params = {
        'doctorCode': doctorCode,
        'orgCode': "2",
        'deptId': deptCode,
        'sourceDeptId': "",
        'majorId': "",
        'isTodayRegist': "false",
        'isTeam': ""
    }
    logger.info("[req]: %s, %s" % (path, json.dumps(params)))
    result = requests.post(url=g_host + path, params=params)
    if result.ok:
        logger.info("[resp]: %s" % result.json())
        print("[resp]: %s" % result.json())
        return result.json()
    else:
        logger.error("code:%s, content:%s" % (result.status_code, result.content))
        print(result.content)
        return dict()


def check_info_result(raw_result: dict) -> list:
    clear_info = []
    for data, value in raw_result.items():
        more_info_list = value.get('more_info', [])
        tmp = []
        for more_info in more_info_list:
            tmp = [{'startTime': json.loads(i.get('param', {})).get('startTime', '0'),
                    'endTime': json.loads(i.get('param', {})).get('endTime', '0'),
                    'data_range': i.get('title', '0-0'),
                    'regLeaveCount': i.get('regLeaveCount')}
                   for i in more_info.get('list', [])
                   if int(i.get('regLeaveCount')) > 0]
            tmp.sort(key=lambda t: t['startTime'])

        clear_info.append({'key': data, 'key_info': value.get('key_info', data), 'more_info': tmp})
    return clear_info


def get_reg_more_info(g_host: str, registration_result: list) -> dict:
    # global doctorCode
    # global deptCode
    path = "/smc/api/org/regMoreInfo"
    info_list = {}
    for reg in registration_result:
        params = {
            'doctorCode': doctorCode,
            'orgCode': "2",
            'deptCode': deptCode,
            'date': reg.get('regDate'),
            'time': "1",
            'patientId': ""
        }
        logger.info("[req]: %s, %s" % (path, json.dumps(params)))
        result = requests.post(url=g_host + path, params=params)
        key = "%s_%s_%s" % (reg.get('regDate'), reg.get('regWeekDay'), reg.get('doctorName'))
        key_info = "日期:%s, 星期:%s, 医生:%s" % (reg.get('regDate'), reg.get('regWeekDay'), reg.get('doctorName'))
        if key not in info_list:
            info_list[key] = {'key_info': key_info, 'more_info': []}
        if result.ok:
            logger.info("[resp]: %s" % result.json())
            print("[resp]: %s" % result.json())
            info_list[key]['more_info'].append(result.json())
        else:
            logger.error("code:%s, content:%s" % (result.status_code, result.content))
            print(result.content)
            continue
    return info_list