#!/usr/bin/python

import logging

class Logger():
    def setLogger(self,app_name):
        filelog = logging.FileHandler(app_name + ".log")
        filelog.setFormatter(logging.Formatter(
            '%(asctime)s [%(process)d]: %(levelname)s %(message)s'))
        logger = logging.getLogger(app_name)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(filelog)
        return logger
