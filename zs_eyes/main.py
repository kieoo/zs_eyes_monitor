from zs_eyes.scanner import *
from zs_eyes import host, logger, callTel, pushToken
from zs_eyes.senter import *
import random
import os

if __name__ == "__main__":
    print("------------start-----------------\n")
    logger.info("------------start: %s-----------------\n" % time.strftime("%c"))

    data = time.strftime("%Y%m%d")

    try:
        for reg_data in os.listdir("reg_data"):
            if reg_data > data:
                logger.info("------------end: has register %s-----------------\n" % data)
                exit(0)
    except Exception:
        pass

    h = time.strftime("%H")

    time.sleep(random.randint(55, 58))

    for retry in range(int(os.getenv('RUN_TIMES', 20))):
        logger.info("--- check times:%d ---", retry)
        r, content = check_registration_result(get_registration(host))
        if r:
            has_recodes = check_info_result(get_reg_more_info(host, content))
            if len(has_recodes) <= 0:
                continue
            h_content = human_read(has_recodes)
            print(h_content)
            logger.info(h_content)

            logger.info("start send....")
            call(callTel, 20)
            send_result = message(callTel, h_content)
            send_result = pushpush("发现订单", h_content, pushToken)
            send_result = pushpush("发现订单", h_content, pushToken, os.getenv("TO_TOKEN", None))
            if send_result:
                break
            else:
                logger.error("send mms failure...")
                break

        wait = random.randint(1, 10)
        # wait = 1
        print("wait: %d." % wait)
        logger.info("wait: %d." % wait)
        time.sleep(float(wait)*0.3)

    # if h in ['17', '23', '9', '7']:
    pushpush("状态检查", "OK", pushToken)

    print("\n------------end: %s-----------------" % time.strftime("%c"))
    logger.info("------------end: %s-----------------" % time.strftime("%c"))