# -*- coding:utf-8 -*-
import time
from datetime import datetime
from jdlogger import logger
from config import global_config


class Timer(object):
    def __init__(self, timer_type="buy", sleep_interval=0.5):
        # '2018-09-28 22:45:50.000'
        if timer_type == "buy":
            self.preset_time = datetime.strptime(global_config.getRaw('config', 'buy_time'), "%Y-%m-%d %H:%M:%S.%f")
        elif timer_type == "reserve":
            self.preset_time = datetime.strptime(global_config.getRaw('config', 'reserve_time'), "%Y-%m-%d %H:%M:%S.%f")
        self.sleep_interval = sleep_interval

    def start(self):
        logger.info('正在等待到达设定时间:%s' % self.preset_time)
        now_time = datetime.now
        while True:
            if now_time() >= self.preset_time:
                logger.info('时间到达，开始执行……')
                break
            else:
                time.sleep(self.sleep_interval)
