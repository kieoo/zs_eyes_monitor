import pytest
from zs_eyes.main import human_read


class TestM(object):
    def test_human_read(self):

        test_raw = [{'key': '2023-08-16_星期三_高凯', 'key_info': '日期:2023-08-16, 星期:星期三, 医生:高凯', 'more_info': [{'startTime': '16:00', 'endTime': '16:30', 'data_range': '16:00-16:30', 'regLeaveCount': '1'}, {'startTime': '16:30', 'endTime': '17:00', 'data_range': '16:30-17:00', 'regLeaveCount': '2'}]}, {'key': '2023-08-17_星期四_高凯', 'key_info': '日期:2023-08-17, 星期:星期四, 医生:高凯', 'more_info': [{'startTime': '16:00', 'endTime': '16:30', 'data_range': '16:00-16:30', 'regLeaveCount': '1'}, {'startTime': '16:30', 'endTime': '17:00', 'data_range': '16:30-17:00', 'regLeaveCount': '2'}]}]

        h_content = human_read(test_raw)

        print(h_content)
        assert len(h_content) > 0

