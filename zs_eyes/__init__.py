import logging

FORMAT = '%(asctime)s  %(message)s'

logger = logging.getLogger('log')
logger.setLevel(logging.INFO)
handler = logging.FileHandler("check.log", 'w', encoding='utf-8')
handler.setFormatter(logging.Formatter(FORMAT))
logger.addHandler(handler)

logger.info("set log ....")

host = "xxx"
doctorCode = "xxx"
deptCode = "xxx"
