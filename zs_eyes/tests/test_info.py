import pytest
import requests_mock
from zs_eyes.scanner import get_reg_more_info, check_info_result, human_read


class TestInfo(object):
    def test_check_info_has(self, requests_mock):
        host = "http://mobile.pku-hit-test.com"

        reg_result = [{'regDate': '2023-08-16', 'regWeekDay': '星期三', 'doctorName': '高凯'},
                      {'regDate': '2023-08-17', 'regWeekDay': '星期四', 'doctorName': '高凯'}]

        requests_mock.post("/smc/api/org/regMoreInfo",
                           json={
                            "code": "0",
                            "msg": "成功",
                            "infoName": "选择时段",
                            "list": [
                                {
                                    "regTotalCount": "6",
                                    "regLeaveCount": "0",
                                    "param": "{\n  \"infoName\" : \"时段\",\n  \"startTime\" : \"14:30\",\n  \"endTime\" : \"15:00\",\n  \"title\" : \"14:30-15:00\"\n}",
                                    "detail": "总号数: 6 剩余号数: 0",
                                    "title": "14:30-15:00",
                                    "enabled": False
                                },
                                {
                                    "regTotalCount": "6",
                                    "regLeaveCount": "0",
                                    "param": "{\n  \"infoName\" : \"时段\",\n  \"startTime\" : \"15:00\",\n  \"endTime\" : \"15:30\",\n  \"title\" : \"15:00-15:30\"\n}",
                                    "detail": "总号数: 6 剩余号数: 0",
                                    "title": "15:00-15:30",
                                    "enabled": False
                                },
                                {
                                    "regTotalCount": "6",
                                    "regLeaveCount": "0",
                                    "param": "{\n  \"infoName\" : \"时段\",\n  \"startTime\" : \"15:30\",\n  \"endTime\" : \"16:00\",\n  \"title\" : \"15:30-16:00\"\n}",
                                    "detail": "总号数: 6 剩余号数: 0",
                                    "title": "15:30-16:00",
                                    "enabled": False
                                },
                                {
                                    "regTotalCount": "6",
                                    "regLeaveCount": "1",
                                    "param": "{\n  \"infoName\" : \"时段\",\n  \"startTime\" : \"16:00\",\n  \"endTime\" : \"16:30\",\n  \"title\" : \"16:00-16:30\"\n}",
                                    "detail": "总号数: 6 剩余号数: 1",
                                    "title": "16:00-16:30",
                                    "enabled": False
                                },
                                {
                                    "regTotalCount": "6",
                                    "regLeaveCount": "2",
                                    "param": "{\n  \"infoName\" : \"时段\",\n  \"startTime\" : \"16:30\",\n  \"endTime\" : \"17:00\",\n  \"title\" : \"16:30-17:00\"\n}",
                                    "detail": "总号数: 6 剩余号数: 2",
                                    "title": "16:30-17:00",
                                    "enabled": True
                                }
                            ]
                            }
                           )
        raw_info = get_reg_more_info(host, reg_result)
        content = check_info_result(raw_info)
        print(content)
        assert len(content) == 2
        assert len(content[0].get('more_info')) == 2

    def test_human_read(self):

        test_raw = [{'key': '2023-08-16_星期三_高凯', 'key_info': '日期:2023-08-16, 星期:星期三, 医生:高凯', 'more_info': [{'startTime': '16:00', 'endTime': '16:30', 'data_range': '16:00-16:30', 'regLeaveCount': '1'}, {'startTime': '16:30', 'endTime': '17:00', 'data_range': '16:30-17:00', 'regLeaveCount': '2'}]}, {'key': '2023-08-17_星期四_高凯', 'key_info': '日期:2023-08-17, 星期:星期四, 医生:高凯', 'more_info': [{'startTime': '16:00', 'endTime': '16:30', 'data_range': '16:00-16:30', 'regLeaveCount': '1'}, {'startTime': '16:30', 'endTime': '17:00', 'data_range': '16:30-17:00', 'regLeaveCount': '2'}]}]

        h_content = human_read(test_raw)

        print(h_content)
        assert len(h_content) > 0