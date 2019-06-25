# coding=utf-8

import time
import logging
from template import Template


class KO(Template):
    def __init__(self):
        self.index = -1
        self.repair_flag = 0
        super(KO, self).__init__()

    def detach(self):
        self.get_pic()
        if self.is_found(self.ps.battle) and not self.is_found(self.ps.restore):
            logging.info("主界面且无修理")
            return 1
        elif self.is_found(self.ps.aim) and not self.repair_flag and self.is_found(self.ps.combat):
            logging.info("任务选择，且无大破")
            return 2
        elif self.is_found(self.ps.normal):
            logging.info("开始战斗")
            return 3
        elif self.is_found(self.ps.command) and self.is_found(self.ps.round0):
            logging.info("初始任务地图")
            return 4
        elif self.is_found(self.ps.round1) and self.is_found(self.ps.three2zero):
            logging.info("第一回合3-0")
            return 5
        elif self.is_found(self.ps.settlement) or self.is_found(self.ps.share) or self.is_found(self.ps.over):
            logging.info("结算")
            return 6
        elif self.is_found(self.ps.round1) and self.is_found(self.ps.two2one):
            logging.info("第一回合2-1")
            return 7
        elif self.is_found(self.ps.round2) and self.is_found(self.ps.two2one):
            logging.info("第二回合2-1")
            return 8
        elif self.is_found(self.ps.round3) and self.is_found(self.ps.two2one):
            logging.info("第三回合2-1")
            return 9
        elif self.is_found(self.ps.round3) and self.is_found(self.ps.one2two):
            logging.info("第三回合1-2")
            return 10
        elif self.is_found(self.ps.round3) and self.is_found(self.ps.zero2three):
            logging.info("第三回合0-3")
            return 11
        elif self.is_found(self.ps.combat) and self.repair_flag:
            logging.info("第三回合0-3")
            return 12
        elif self.is_found(self.ps.battle) and self.is_found(self.ps.restore):
            logging.info("位于主界面且需要修理")
            return 13
        elif self.is_found(self.ps.fast):
            logging.info("快速修理")
            return 14
        elif self.is_found(self.ps.full):
            logging.info("仓库满了")
            return 15
        elif self.is_found(self.ps.factory):
            logging.info("仓库界面")
            return 16
        elif self.is_found(self.ps.back) or self.is_found(self.ps.pre):
            logging.info("后勤任务完成")
            return 19
        elif self.is_found(self.ps.combat) and not self.repair_flag:
            logging.info("位于任务选择界面且不需要修理")
            return 17
        elif self.is_found(self.ps.emergency):
            logging.info("队伍重创")
            return 18
        else:
            return 0

    def solve(self):
        while 1:
            index = self.detach()
            if index == 1:
                self.mouse_left_click(742, 399)
                time.sleep(2)
            elif index == 2:
                self.mouse_left_click(532, 212)
            elif index == 3:
                self.mouse_left_click(610, 465)
            elif index == 4:
                self.mouse_left_click(374, 298)
                time.sleep(0.5)
                self.mouse_left_click(900, 517)
                time.sleep(0.5)
                self.mouse_left_click(900, 517)
                time.sleep(3.0)
            elif index == 5:
                self.mouse_left_click(369, 292)
                time.sleep(0.5)
                self.mouse_left_click(369, 292)
                time.sleep(0.2)
                self.mouse_left_click(929, 450)
                time.sleep(0.2)
                self.mouse_left_click(501, 390)
                time.sleep(1.5)
                self.mouse_left_click(586, 205)
            elif index == 6:
                for _ in range(10):
                    self.mouse_left_click(900, 517)
                    time.sleep(0.06)
            elif index == 7:
                self.mouse_left_click(935, 526)
                time.sleep(12)
            elif index == 8:
                self.mouse_left_click(511, 288)
                time.sleep(0.2)
                self.mouse_left_click(377, 169)
                time.sleep(1.5)
                self.mouse_left_click(573, 108)
                time.sleep(1.5)
                self.mouse_left_click(935, 526)
            elif index == 9:
                self.mouse_left_click(573, 108)
                time.sleep(0.2)
                self.mouse_left_click(687, 215)
            elif index == 10:
                self.mouse_left_click(551, 289)
                time.sleep(0.2)
                self.mouse_left_click(687, 158)
            elif index == 11:
                self.mouse_left_click(693, 258)
                time.sleep(0.2)
                self.mouse_left_click(551, 400)
                time.sleep(1.5)
                self.mouse_left_click(900, 517)
            elif index == 12:
                self.mouse_left_click(51, 41)
                time.sleep(1.0)
            elif index == 13:
                self.mouse_left_click(735, 189)
                time.sleep(1.0)
            elif index == 14:
                self.mouse_left_click(112, 252)
                time.sleep(0.5)
                self.mouse_left_click(73, 200)
                time.sleep(0.2)
                self.mouse_left_click(215, 198)
                time.sleep(0.2)
                self.mouse_left_click(944, 437)
                time.sleep(0.3)
                self.mouse_left_click(252, 408)
                time.sleep(0.2)
                self.mouse_left_click(735, 404)
                time.sleep(2.0)
                self.mouse_left_click(51, 41)
                time.sleep(2.0)
                self.mouse_left_click(51, 41)
                time.sleep(4)
                self.repair_flag = 0
            elif index == 15:
                self.mouse_left_click(637, 398)
                time.sleep(0.5)
            elif index == 16:
                self.mouse_left_click(74, 348)
                time.sleep(0.5)
                self.mouse_left_click(244, 144)
                time.sleep(0.5)
                for _ in range(3):
                    self.mouse_left_click(938, 482)
                    time.sleep(0.4)
                time.sleep(1.0)
                self.mouse_left_click(47, 32)
                time.sleep(1.0)
            elif index == 17:
                self.mouse_left_click(73, 120)
                time.sleep(0.1)
                self.mouse_left_click(220, 121)
                time.sleep(0.1)
                self.mouse_left_click(784, 144)
                time.sleep(0.3)
                self.mouse_left_click(532, 212)
            elif index == 18:
                self.repair_flag = 1
            elif index == 19:
                self.mouse_left_click(601, 399)
            else:
                pass
            time.sleep(0.2)
