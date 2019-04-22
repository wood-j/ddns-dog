# -*- coding:utf-8 -*-
import logging
import logging.config
import os
from datetime import datetime

from common.paths import get_data_root


def new_logger(name):
    root = get_data_root()
    log_root = os.path.join(root, 'logs')
    if not os.path.exists(log_root):
        os.makedirs(log_root)
    result = logging.getLogger(name)
    result.setLevel(logging.DEBUG)
    # format
    basic_format = "%(asctime)s %(levelname)s %(filename)s(line %(lineno)s)： %(message)s"
    date_format = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter(basic_format, date_format)
    # console stream
    steam_handler = logging.StreamHandler()
    steam_handler.setFormatter(formatter)
    result.addHandler(steam_handler)
    # file stream
    date_str = datetime.now().strftime('%Y-%m-%d')
    path = os.path.join(log_root, f'{name}.{date_str}.log')
    file_handler = logging.FileHandler(path)
    file_handler.setFormatter(formatter)
    result.addHandler(file_handler)
    return result


logger = new_logger('controller')


if __name__ == '__main__':
    logger = new_logger('main')
    logger.debug('hello world!')
