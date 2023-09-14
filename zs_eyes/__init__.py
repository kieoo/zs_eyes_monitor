import logging
import os


host = os.getenv('HOST')
doctorCode = os.getenv('DOCTOR_CODE')
deptCode = os.getenv('DEPT_CODE', '1131')
regWeekDay = os.getenv('REG_WEEK_DAY', "星期五上午")
callTel = os.getenv('CALL_TEL')
pushToken = os.getenv('PUSH_TOKEN')
logPath = os.getenv('LOG_PATH', 'runtime.log')


FORMAT = '%(asctime)s  %(message)s'

logger = logging.getLogger('log')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(logPath, 'a', encoding='utf-8')
handler.setFormatter(logging.Formatter(FORMAT))
logger.addHandler(handler)

logger.info("set log ....")