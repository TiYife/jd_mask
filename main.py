import sys
import time

from jd_mask_spider_requests import Jd_Mask_Spider
from util import send_wechat

if __name__ == '__main__':
    a = """
  ________  __   __   _______
 |___  ___| \ \ / /   | |____|
     | |     \ V /    | |____
     | |      | |     | |____|
     | |      | |     | |       1.预约商品
     |_|      |_|     |_|       2.秒杀抢购商品 
    """
    start_tool = Jd_Mask_Spider()
    print(a)
    choice_function = input('选择功能:')
    if choice_function == '1':
        start_tool.login()
        start_tool.make_reserve()
    elif choice_function == '2':
        start_tool.request_seckill_url()
        start_tool.request_seckill_checkout_page()
        for i in range(200):
            print("第"+str(i)+"次提交订单：")
            if start_tool.submit_seckill_order():
                break
            time.sleep(0.01)
        send_wechat(start_tool.result_message)
    else:
        print('没有此功能')
        sys.exit(1)
