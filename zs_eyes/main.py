from zs_eyes.scanner import *
from zs_eyes import host, logger


def human_read(raw: list) -> str:
    read = "有号, 信息如下:"
    num = 1
    for recode in raw:
        read += '\n' + recode.get('key') + ''
        for info in recode.get('more_info', []):
            read += "\n\t编号:%d, 时间:%s, 剩余:%s" % (num, info.get('data_range', ''), info.get('regLeaveCount', '0'))
            num += 1
    return read


if __name__ == "__main__":
    print("------------start-----------------\n")
    logger.info("------------start-----------------\n")
    r, content = check_registration_result(get_registration(host))
    if r:
        has_recodes = check_info_result(get_reg_more_info(host, content))
        h_content = human_read(has_recodes)
        print(h_content)
        logger.info(h_content)
    print("\n------------end-----------------")
    logger.info("\n------------end-----------------")
