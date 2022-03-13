# -*- encoding=utf8 -*-
__author__ = "eeorunix"

import time
from airtest.core.api import *
from airtest.aircv import *
from airtest.core.settings import Settings as ST
ST.CVSTRATEGY = ["tpl"]
ST.THRESHOLD = 0.8
ST.SAVE_IMAGE = False
ST.RESIZE_METHOD = None
DEBUG = 0

import logging
logger = logging.getLogger("airtest")
if not DEBUG:
    logger.setLevel(logging.ERROR)

auto_setup(__file__)

# 全局当前图片坐标中心点位置
XY = None
screen = None
start = time.time()
cnt = 0

def g(a, b, c):
    # (767, 498), (767, 531), (868, 531)
    res = (
        max(0, a[0] - 20),
        max(0, a[1] - 20), 
        c[0] + 20,
        b[1] + 20
    )
    return res
    

def is_found(tempalte, rect=None):
    '''
    @param filename: 图片文件
    @return 是否查找到，并更新全局变量XY
    '''
    global XY
    global screen
    logger.debug(str(tempalte))
    if rect is not None:
        new_screen = aircv.crop_image(screen, rect)
        XY = tempalte.match_in(new_screen)
        if XY is not None:
            XY = (XY[0] + rect[0], XY[1] + rect[1])
    else:
        XY = tempalte.match_in(screen)
    return XY is not None

def detach():
    '''检索当前图片，更新全局坐标点，返回图片策略序号'''
    global XY
    global screen
    global cnt
    global start
    screen = G.DEVICE.snapshot()
    if is_found(Template(r"tpl1644856635384.png", record_pos=(0.41, -0.223), resolution=(1024, 576)), g((925, 51), (925, 70), (940, 70))):
        return 0
    elif is_found(Template(r"tpl1644856716623.png", target_pos=4, record_pos=(-0.354, -0.255), resolution=(1024, 576)), g((57, 12), (57, 43), (242, 43))):
        return 0
    elif is_found(Template(r"tpl1647070771440.png", record_pos=(0.029, -0.055), resolution=(1024, 576)), g((430, 204), (430, 261), (655, 261))):
        return 0
    elif is_found(Template(r"tpl1644764815224.png", threshold=0.97, target_pos=5, record_pos=(-0.479, -0.009), resolution=(1024, 665))):
        return 0
    elif is_found(Template(r"tpl1644771271544.png", record_pos=(-0.409, -0.074), resolution=(1024, 576)), g((61, 198), (61, 226), (125, 226))):
        return 0
    elif is_found(Template(r"tpl1644766848271.png", rgb=False, record_pos=(0.081, 0.097), resolution=(1024, 665)), g((537, 377), (537, 416), (653, 416))):
        return 0
    elif is_found(Template(r"tpl1644771347927.png", record_pos=(0.209, 0.047), resolution=(1024, 576)), g((648, 298), (648, 375), (805, 375))):
        return 0
    elif is_found(Template(r"tpl1647058363696.png", record_pos=(-0.292, 0.015), resolution=(1024, 576))):
        return 10
    elif is_found(Template(r"tpl1647025537096.png", record_pos=(-0.307, -0.196), resolution=(1024, 576)), g((141, 68), (141, 107), (255, 107))):
        return 10
    elif is_found(Template(r"tpl1647025901008.png", record_pos=(-0.283, -0.194), resolution=(1024, 576)), g((145, 73), (145, 105), (299, 105))):
        return 10
    elif is_found(Template(r"tpl1644771635172.png", record_pos=(0.297, 0.185), resolution=(1024, 576)), g((771, 466), (771, 489), (862, 489))):
        return 0
    elif is_found(Template(r"tpl1644771405564.png", record_pos=(-0.198, -0.237), resolution=(1024, 576)), g((261, 21), (261, 69), (357, 69))):
        return 3
    elif is_found(Template(r"tpl1644771706558.png", record_pos=(-0.151, -0.247), resolution=(1024, 576)), g((338, 6), (338, 65), (377, 65))) and is_found(Template(r"tpl1644771774441.png", record_pos=(0.386, 0.221), resolution=(1024, 576)), g((842, 500), (842, 529), (972, 529))):
        if is_found(Template(r"tpl1647058842350.png", record_pos=(-0.011, 0.06), resolution=(1024, 576)), g((340, 218), (340, 480), (662, 480))):
            if time.time() - start > 2:
                cnt += 1
                start = time.time()
                logger.error("无限脚本开始，当前进行第%d轮" % cnt)
            return 8
        else:
            return 4
    elif is_found(Template(r"tpl1647063538393.png", record_pos=(-0.149, -0.234), resolution=(1024, 576)), g((341, 29), (341, 67), (378, 67))) and is_found(Template(r"tpl1647063577054.png", record_pos=(0.311, 0.241), resolution=(1024, 576)), g((797, 518), (797, 552), (863, 552))):
        return 5
    elif is_found(Template(r"tpl1647063538393.png", record_pos=(-0.149, -0.234), resolution=(1024, 576)), g((341, 29), (341, 67), (378, 67))) and is_found(Template(r"tpl1644773034403.png", record_pos=(0.311, 0.243), resolution=(1024, 576)), g((801, 517), (801, 555), (861, 555))) and is_found(Template(r"tpl1647144133863.png", record_pos=(-0.325, 0.142), resolution=(1024, 576)), g((170, 419), (170, 448), (188, 448))):
        return 13
    elif is_found(Template(r"tpl1647063538393.png", record_pos=(-0.149, -0.234), resolution=(1024, 576)), g((341, 29), (341, 67), (378, 67))) and is_found(Template(r"tpl1644773034403.png", record_pos=(0.311, 0.243), resolution=(1024, 576)), g((801, 517), (801, 555), (861, 555))) and is_found(Template(r"tpl1647066298630.png", record_pos=(-0.439, 0.179), resolution=(1024, 576)), g((2, 456), (2, 487), (122, 487))):
        return 11
    elif is_found(Template(r"tpl1647063538393.png", record_pos=(-0.149, -0.234), resolution=(1024, 576)), g((341, 29), (341, 67), (378, 67))) and is_found(Template(r"tpl1647144019805.png", record_pos=(0.311, 0.242), resolution=(1024, 576)), g((801, 517), (801, 555), (861, 555))) and is_found(Template(r"tpl1647144133863.png", record_pos=(-0.325, 0.142), resolution=(1024, 576)), g((170, 419), (170, 448), (188, 448))):
        return 12
    elif is_found(Template(r"tpl1644773664247.png", record_pos=(-0.437, -0.248), resolution=(1024, 576)), g((31, 18), (31, 51), (100, 51))):
        XY = (XY[0] + 100, XY[1])
        return 0
    elif is_found(Template(r"tpl1644775198955.png", record_pos=(-0.076, 0.223), resolution=(1024, 576)), g((408, 509), (408, 524), (461, 524))):
        XY = (XY[0] + 100, XY[1])
        touch(XY)
        sleep(0.5)
        touch(XY)
        sleep(0.5)
        touch(XY)
        sleep(0.5)
        touch(XY)
        sleep(0.5)
        touch(XY)
        sleep(0.5)
        touch(XY)
        sleep(0.5)
        return 0
    elif is_found(Template(r"tpl1647069986280.png", record_pos=(-0.246, -0.121), resolution=(1024, 576)), g((194, 153), (194, 175), (327, 175))) and is_found(Template(r"tpl1647070154857.png", target_pos=8, record_pos=(-0.002, 0.046), resolution=(1024, 576)), g((443, 251), (443, 419), (578, 419))):
        return 0
    elif is_found(Template(r"tpl1647070306739.png", record_pos=(-0.2, -0.237), resolution=(1024, 576)), g((258, 20), (258, 71), (359, 71))) and is_found(Template(r"tpl1647070328462.png", record_pos=(-0.064, -0.126), resolution=(1024, 576)), g((427, 140), (427, 179), (465, 179))):
        return 0
    elif is_found(Template(r"tpl1647070542885.png", record_pos=(0.393, 0.199), resolution=(1024, 576)), g((884, 474), (884, 510), (944, 510))):
        touch(XY)
        sleep(1.0)
        touch(XY)
        sleep(1.0)
        return 0
    elif is_found(Template(r"tpl1644856432544.png", threshold=0.9500000000000002, record_pos=(-0.281, -0.102), resolution=(1024, 576)), g((193, 153), (193, 216), (256, 216))):
        XY = (XY[0] - 100, XY[1])
        return 0
    elif is_found(Template(r"tpl1644779677165.png", record_pos=(-0.415, -0.241), resolution=(1024, 576))):
        return 0
    return -1
    

def attach():
    '''根据当前策略号作相应策略'''
    global XY
    global cnt
    global start
    index = detach()
    logger.debug("index============>" + str(index))
    if index == 0:
        touch(XY)
    elif index == 1:
        logger.debug("============>" + str(XY))
    elif index == 3:
        touch((75, 188))
        sleep(1.0)
        swipe((200, 283), vector=[0.0, -0.4], steps=3, duration=0.2)
        sleep(3.0)
    elif index == 4:
        pinch(in_or_out='in', center=None, percent=0.5)
        sleep(2.0)
    elif index == 5:
        sleep(2.0)
        touch((60, 472))
        sleep(0.2)
        touch((224, 140))
        sleep(0.2)
        touch((155, 243))
        sleep(0.2)
        touch((178, 493))
        sleep(0.2)
        touch((170, 493))
        sleep(0.2)
        touch((900, 510))
        sleep(7.0)
    elif index == 8:
        touch((224, 118))  # 左上机场
        sleep(2.0)
        touch((932, 508))  # 第一梯队部署
        sleep(0.5)
        touch((178, 493))  # 左下机场
        sleep(1.0)
        touch((932, 508))  # 第一梯队部署
        sleep(0.5)
        touch((932, 508))  # 开始作战
        sleep(2.0)
    elif index == 10:
        touch(XY)
        sleep(2.0)
        touch((970, 153))
        sleep(1.0)
        touch((540, 237))
    elif index == 11:
        touch((183, 428))  # 机场
        sleep(2.0)
        touch((783, 509))  # 撤离
        sleep(1.0)
        touch((594, 396))  # 确认撤离
        sleep(1.0)
        touch((183, 428))  # 机场
        sleep(1.0)
        touch((201, 502))  # 队伍编成
        sleep(3.0)
        touch((949, 544))  # 阵型编成
        sleep(1.0)
        touch((861, 234))  # 梯队预设
        sleep(1.0)
        touch((687, 159))  # 预设2
        sleep(1.0)
        touch((906, 507))  # 套用预设
        sleep(1.0)
        touch((452, 340))  # 强制替换
        sleep(1.0)
        touch((657, 399))  # 确认
        sleep(1.0)
        touch((928, 507))  # 确定
        sleep(1.0)
        touch((87, 42))  # 后退
    elif index == 13:
        touch((183, 428))  # 机场
        sleep(1.0)
        touch((932, 508))  # 确认部署
        sleep(1.0)
        touch((183, 428))  # 机场
        sleep(0.5)
        touch((183, 428))  # 机场
        sleep(1.0)
        touch((932, 447))  # 补给
        sleep(1.0)
        touch((183, 428))  # 机场
        sleep(1.0)
        touch((783, 509))  # 撤离
        sleep(1.0)
        touch((594, 396))  # 确认撤离
        sleep(1.0)
        touch((183, 428))  # 机场
        sleep(1.0)
        touch((201, 502))  # 队伍编成
        sleep(3.0)
        touch((949, 544))  # 阵型编成
        sleep(1.0)
        touch((861, 234))  # 梯队预设
        sleep(1.0)
        touch((687, 89))  # 预设1
        sleep(1.0)
        touch((906, 507))  # 套用预设
        sleep(1.0)
        touch((657, 399))  # 确认
        sleep(1.0)
        touch((928, 507))  # 确定
        sleep(1.0)
        touch((87, 42))  # 后退
    elif index == 12:
        touch((253, 35))  # 终止作战
        sleep(1.0)
        touch((393, 394))  # 重新作战
        if time.time() - start > 2:
            logger.error("第%d轮结束，耗时%.2lfs" % (cnt, time.time() - start))
            start = time.time()
    else:
        logger.debug("============>" + str(XY))
    sleep(1.0)
    return 

if DEBUG:
    attach()
else:
    while True:
        attach()
