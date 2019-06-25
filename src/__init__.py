# coding=utf-8

import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='gf.log',
                    format='[%(asctime)s] %(levelname)s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filemode='a')
