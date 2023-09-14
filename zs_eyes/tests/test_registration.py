import pytest
import requests_mock
from zs_eyes.scanner import get_registration, check_registration_result


class TestRegistration(object):
    def test_check_registration_has(self, requests_mock):
        host = "http://mobile.pku-hit-test.com"

        requests_mock.post("/smc/api/registration/v2/doctorSchedule",
                           json={
                               "code": "0",
                               "msg": "成功",
                               "list": [
                                   {
                                       "deptName": "青光眼门诊",
                                       "regStatus": "7834",
                                       "deptParentId": "762",
                                       "regLeaveCount": "4",
                                       "majorId": "青光眼",
                                       "regDate": "2023-08-16",
                                       "title": "主治医师",
                                       "type": "专科",
                                       "regWeekDay": "星期三",
                                       "doctorName": "高凯",
                                       "timeName": "下午",
                                       "regTotalCount": "27",
                                       "doctortype": "0",
                                       "needMoreInfo": "1",
                                       "regFee": "0.00",
                                       "teamdoctorid": "-1",
                                       "treatFee": "10.00",
                                       "doctorCode": "7834",
                                       "time": "1",
                                       "isTimeReg": "1",
                                       "deptCode": "1131"
                                   }, {
                                       "deptName": "青光眼门诊",
                                       "regStatus": "7834",
                                       "deptParentId": "762",
                                       "regLeaveCount": "4",
                                       "majorId": "青光眼",
                                       "regDate": "2023-08-17",
                                       "title": "主治医师",
                                       "type": "专科",
                                       "regWeekDay": "星期四",
                                       "doctorName": "高凯",
                                       "timeName": "下午",
                                       "regTotalCount": "27",
                                       "doctortype": "0",
                                       "needMoreInfo": "1",
                                       "regFee": "0.00",
                                       "teamdoctorid": "-1",
                                       "treatFee": "10.00",
                                       "doctorCode": "7834",
                                       "time": "1",
                                       "isTimeReg": "1",
                                       "deptCode": "1131"
                                   }
                               ],
                               "teamList": [
                                   {
                                       "teamName": "",
                                       "teamId": "-1"
                                   }
                               ]
                           }
                           )

        raw_reg = get_registration(host)
        r, content = check_registration_result(raw_reg)
        print(content)
        assert r is True
        assert len(content) == 2

    def test_check_registration_has_no(self, requests_mock):
        host = "http://mobile.pku-hit-test.com"

        requests_mock.post("/smc/api/registration/v2/doctorSchedule",
                           json={
                               "code": "0",
                               "msg": "成功",
                               "list": [
                                   {
                                       "deptName": "青光眼门诊",
                                       "regStatus": "7834",
                                       "deptParentId": "762",
                                       "regLeaveCount": "0",
                                       "majorId": "青光眼",
                                       "regDate": "2023-08-16",
                                       "title": "主治医师",
                                       "type": "专科",
                                       "regWeekDay": "星期三",
                                       "doctorName": "高凯",
                                       "timeName": "下午",
                                       "regTotalCount": "27",
                                       "doctortype": "0",
                                       "needMoreInfo": "1",
                                       "regFee": "0.00",
                                       "teamdoctorid": "-1",
                                       "treatFee": "10.00",
                                       "doctorCode": "7834",
                                       "time": "1",
                                       "isTimeReg": "1",
                                       "deptCode": "1131"
                                   }, {
                                       "deptName": "青光眼门诊",
                                       "regStatus": "7834",
                                       "deptParentId": "762",
                                       "regLeaveCount": "4",
                                       "majorId": "青光眼",
                                       "regDate": "2023-08-17",
                                       "title": "主治医师",
                                       "type": "专科",
                                       "regWeekDay": "星期四",
                                       "doctorName": "高凯",
                                       "timeName": "下午",
                                       "regTotalCount": "27",
                                       "doctortype": "0",
                                       "needMoreInfo": "1",
                                       "regFee": "0.00",
                                       "teamdoctorid": "-1",
                                       "treatFee": "100.00",
                                       "doctorCode": "7834",
                                       "time": "1",
                                       "isTimeReg": "1",
                                       "deptCode": "1131"
                                   }
                               ],
                               "teamList": [
                                   {
                                       "teamName": "",
                                       "teamId": "-1"
                                   }
                               ]
                           }
                           )

        raw_reg = get_registration(host)
        r, content = check_registration_result(raw_reg)
        print(content)
        assert r is False
        assert len(content) == 0

    def test_check_registration_has_filter(self, requests_mock):
        host = "http://mobile.pku-hit-test.com"

        requests_mock.post("/smc/api/registration/v2/doctorSchedule",
                           json={
                               "code": "0",
                               "msg": "成功",
                               "list": [
                                   {
                                       "deptName": "青光眼门诊",
                                       "regStatus": "7834",
                                       "deptParentId": "762",
                                       "regLeaveCount": "4",
                                       "majorId": "青光眼",
                                       "regDate": "2023-08-16",
                                       "title": "主治医师",
                                       "type": "专科",
                                       "regWeekDay": "星期三",
                                       "doctorName": "高凯",
                                       "timeName": "下午",
                                       "regTotalCount": "27",
                                       "doctortype": "0",
                                       "needMoreInfo": "1",
                                       "regFee": "0.00",
                                       "teamdoctorid": "-1",
                                       "treatFee": "10.00",
                                       "doctorCode": "7834",
                                       "time": "1",
                                       "isTimeReg": "1",
                                       "deptCode": "1131"
                                   }, {
                                       "deptName": "青光眼门诊",
                                       "regStatus": "7834",
                                       "deptParentId": "762",
                                       "regLeaveCount": "4",
                                       "majorId": "青光眼",
                                       "regDate": "2023-08-17",
                                       "title": "主治医师",
                                       "type": "专科",
                                       "regWeekDay": "星期四",
                                       "doctorName": "高凯",
                                       "timeName": "下午",
                                       "regTotalCount": "27",
                                       "doctortype": "0",
                                       "needMoreInfo": "1",
                                       "regFee": "0.00",
                                       "teamdoctorid": "-1",
                                       "treatFee": "100.00",
                                       "doctorCode": "7834",
                                       "time": "1",
                                       "isTimeReg": "1",
                                       "deptCode": "1131"
                                   }
                               ],
                               "teamList": [
                                   {
                                       "teamName": "",
                                       "teamId": "-1"
                                   }
                               ]
                           }
                           )

        raw_reg = get_registration(host)
        r, content = check_registration_result(raw_reg)
        print(content)
        assert r is True
        assert len(content) == 1

    def test_check_registration_has_filter_2(self, requests_mock):
        host = "http://mobile.pku-hit-test.com"

        requests_mock.post("/smc/api/registration/v2/doctorSchedule",
                           json={
                               "code": "0",
                               "msg": "成功",
                               "list": [
                                   {
                                       "deptName": "青光眼门诊",
                                       "regStatus": "7834",
                                       "deptParentId": "762",
                                       "regLeaveCount": "4",
                                       "majorId": "青光眼",
                                       "regDate": "2023-08-16",
                                       "title": "主治医师",
                                       "type": "专科",
                                       "regWeekDay": "星期三",
                                       "doctorName": "高凯",
                                       "timeName": "下午",
                                       "regTotalCount": "27",
                                       "doctortype": "0",
                                       "needMoreInfo": "1",
                                       "regFee": "0.00",
                                       "teamdoctorid": "-1",
                                       "treatFee": "10.00",
                                       "doctorCode": "7834",
                                       "time": "1",
                                       "isTimeReg": "1",
                                       "deptCode": "1131"
                                   }, {
                                       "deptName": "青光眼门诊",
                                       "regStatus": "7834",
                                       "deptParentId": "762",
                                       "regLeaveCount": "4",
                                       "majorId": "青光眼",
                                       "regDate": "2023-08-17",
                                       "title": "主治医师",
                                       "type": "专科",
                                       "regWeekDay": "星期四",
                                       "doctorName": "高凯",
                                       "timeName": "下午",
                                       "regTotalCount": "27",
                                       "doctortype": "0",
                                       "needMoreInfo": "1",
                                       "regFee": "0.00",
                                       "teamdoctorid": "-1",
                                       "treatFee": "100.00",
                                       "doctorCode": "7834",
                                       "time": "1",
                                       "isTimeReg": "1",
                                       "deptCode": "1131"
                                   },
                                   {
                                       "deptName": "青光眼门诊",
                                       "regStatus": "7834",
                                       "deptParentId": "762",
                                       "regLeaveCount": "4",
                                       "majorId": "青光眼",
                                       "regDate": "2023-08-17",
                                       "title": "主治医师",
                                       "type": "专科",
                                       "regWeekDay": "星期五",
                                       "doctorName": "高凯",
                                       "timeName": "上午",
                                       "regTotalCount": "27",
                                       "doctortype": "0",
                                       "needMoreInfo": "1",
                                       "regFee": "0.00",
                                       "teamdoctorid": "-1",
                                       "treatFee": "10.00",
                                       "doctorCode": "7834",
                                       "time": "0",
                                       "isTimeReg": "1",
                                       "deptCode": "1131"
                                   }
                               ],
                               "teamList": [
                                   {
                                       "teamName": "",
                                       "teamId": "-1"
                                   }
                               ]
                           }
                           )

        raw_reg = get_registration(host)
        r, content = check_registration_result(raw_reg)
        print(content)
        assert r is True
        assert len(content) == 1