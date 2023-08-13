from zs_eyes.scanner import *
from zs_eyes import host, logger, callTel, pushToken
from zs_eyes.senter import *
import random
import os

if __name__ == "__main__":
    print("------------start-----------------\n")
    logger.info("------------start: %s-----------------\n" % time.strftime("%c"))
    h = time.strftime("%H")

    time.sleep(random.randint(1, 10))

    for retry in range(int(os.getenv('RUN_TIMES', 20))):
        logger.info("--- check times:%d ---", retry)
        r, content = check_registration_result(get_registration(host))
        if r:
            has_recodes = check_info_result(get_reg_more_info(host, content))
            h_content = human_read(has_recodes)
            print(h_content)
            logger.info(h_content)

            logger.info("start send....")
            send_result = message(callTel, h_content)
            if send_result:
                # call(callTel, 20)
                pushpush("发现订单", h_content, pushToken)
                break
            else:
                logger.error("send mms failure...")

        wait = 10 + random.randint(1, 10)
        print("wait: %d." % wait)
        logger.info("wait: %d." % wait)
        time.sleep(wait)

    if h in ['17', '22', '10', '15']:
        pushpush("状态检查", "OK", pushToken)

    print("\n------------end: %s-----------------" % time.strftime("%c"))
    logger.info("------------end: %s-----------------" % time.strftime("%c"))
