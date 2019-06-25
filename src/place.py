# coding=utf-8

import time
import logging
from template import Template


class KO(Template):
    def __init__(self):
        self.index = -1
        super(KO, self).__init__()

    def detach(self):
        self.get_pic()
        if self.is_found(self.ps.back) or self.is_found(self.ps.pre):
            logging.info("后勤任务完成")
            return 1
        else:
            return 0

    def solve(self):
        while 1:
            index = self.detach()
            if index == 1:
                self.mouse_left_click(601, 399)
            else:
                pass
            time.sleep(5.0)
