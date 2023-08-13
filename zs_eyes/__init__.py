import logging
import os


host = os.getenv('HOST')
doctorCode = os.getenv('DOCTOR_CODE')
deptCode = os.getenv('DEPT_CODE')
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

