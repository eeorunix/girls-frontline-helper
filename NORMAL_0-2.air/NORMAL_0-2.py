# -*- encoding=utf8 -*-
__author__ = "eeorunix"

import time
import random
from airtest.core.api import *
from airtest.aircv import *
from airtest.core.settings import Settings as ST
ST.CVSTRATEGY = ["tpl"]
ST.THRESHOLD = 0.8
ST.SAVE_IMAGE = False
ST.RESIZE_METHOD = None
DEBUG = 0
RETRY = 50

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
retry = RETRY

def g(a, b, c):
    # (767, 498), (767, 531), (868, 531)
    res = (
        max(0, a[0] - 20),
        max(0, a[1] - 20), 
        c[0] + 20,
        b[1] + 20
    )
    return res

def click(pos):
    x, y = pos
    a = random.randint(0, 4) - 2
    b = random.randint(0, 4) - 2
    touch((x + a, y + b))

def is_found(template, rect=None):
    global XY
    global screen
    logger.debug(str(template))
    if rect is not None:
        new_screen = aircv.crop_image(screen, rect)
        XY = template.match_in(new_screen)
        if XY is not None:
            XY = (XY[0] + rect[0], XY[1] + rect[1])
    else:
        XY = template.match_in(screen)
    return XY is not None

def wait_to(template, rect=None):
    global screen
    global retry
    retry = RETRY
    while retry > 0:
        screen = G.DEVICE.snapshot()
        if is_found(template, rect):
            return
        sleep(0.2)
        retry -= 1
    assert 0

def detach():
    global XY
    global screen
    global cnt
    global start
    screen = G.DEVICE.snapshot()
    if is_found(Template(r"tpl1644856635384.png", record_pos=(0.41, -0.223), resolution=(1024, 576)), g((925, 51), (925, 70), (940, 70))):
        return 0
    elif is_found(Template(r"tpl1644856716623.png", target_pos=4, record_pos=(-0.354, -0.255), resolution=(1024, 576)), g((57, 12), (57, 43), (242, 43))):
        return 0
    elif is_found(Template(r"tpl1644857386167.png", record_pos=(0.091, 0.047), resolution=(1024, 576)), g((578, 295), (578, 378), (633, 378))):
        return 0
    elif is_found(Template(r"tpl1644857521484.png", threshold=0.9000000000000001, record_pos=(-0.23, -0.24), resolution=(1024, 576)), g((211, 12), (211, 72), (342, 72))) and is_found(Template(r"tpl1644857557368.png", threshold=0.9000000000000001, record_pos=(0.392, 0.242), resolution=(1024, 576)), g((827, 518), (827, 555), (999, 555))):
        return 0
    elif is_found(Template(r"tpl1644857668036.png", record_pos=(-0.264, -0.158), resolution=(1024, 576)), g((204, 117), (204, 135), (280, 135))) and is_found(Template(r"tpl1644857743214.png", record_pos=(0.248, 0.146), resolution=(1024, 576)), g((712, 419), (712, 456), (821, 456))):
        return 9
    elif is_found(Template(r"tpl1644764815224.png", threshold=0.97, target_pos=5, record_pos=(-0.479, -0.009), resolution=(1024, 665))):
        return 0
    elif is_found(Template(r"tpl1644771271544.png", record_pos=(-0.409, -0.074), resolution=(1024, 576)), g((61, 198), (61, 226), (125, 226))):
        return 0
    elif is_found(Template(r"tpl1644766848271.png", rgb=False, record_pos=(0.081, 0.097), resolution=(1024, 665)), g((537, 377), (537, 416), (653, 416))):
        return 0
    elif is_found(Template(r"tpl1644771347927.png", record_pos=(0.209, 0.047), resolution=(1024, 576)), g((648, 298), (648, 375), (805, 375))):
        return 0
    elif is_found(Template(r"tpl1644771493638.png", record_pos=(-0.316, -0.161), resolution=(1024, 576)), g((151, 93), (151, 154), (226, 154))):
        return 0
    elif is_found(Template(r"tpl1647277001584.png", record_pos=(-0.29, -0.159), resolution=(1024, 576)), g((147, 105), (147, 146), (284, 146))):
        return 11
    elif is_found(Template(r"tpl1644771635172.png", record_pos=(0.297, 0.185), resolution=(1024, 576)), g((771, 466), (771, 489), (862, 489))):
        if time.time() - start > 2:
            cnt += 1
            start = time.time()
            logger.error("无限脚本开始，当前进行第%d轮" % cnt)
        return 0
    elif is_found(Template(r"tpl1644771405564.png", record_pos=(-0.198, -0.237), resolution=(1024, 576)), g((261, 21), (261, 69), (357, 69))):
        return 3
    elif is_found(Template(r"tpl1644772066054.png", record_pos=(-0.257, -0.21), resolution=(1024, 576)), g((175, 56), (175, 91), (324, 91))) and is_found(Template(r"tpl1644772384523.png", record_pos=(0.405, 0.215), resolution=(1024, 576)), g((874, 490), (874, 526), (981, 526))):
        touch(XY)
        sleep(2.0)
        return 0
    elif is_found(Template(r"tpl1644771706558.png", record_pos=(-0.151, -0.247), resolution=(1024, 576)), g((338, 6), (338, 65), (377, 65))) and is_found(Template(r"tpl1644771774441.png", record_pos=(0.386, 0.221), resolution=(1024, 576)), g((842, 500), (842, 529), (972, 529))):
        if is_found(Template(r"tpl1647277485938.png", record_pos=(0.011, -0.122), resolution=(1024, 576)), g((508, 145), (508, 181), (538, 181))):
            return 8
        else:
            return 4
    elif is_found(Template(r"tpl1644772671119.png", threshold=0.9500000000000002, record_pos=(-0.15, -0.234), resolution=(1024, 576)), g((341, 28), (341, 69), (375, 69))) and is_found(Template(r"tpl1647277729514.png", record_pos=(0.311, 0.243), resolution=(1024, 576)), g((801, 517), (801, 555), (861, 555))):
        return 5
    elif is_found(Template(r"tpl1644773025491.png", threshold=0.9500000000000002, record_pos=(-0.151, -0.235), resolution=(1024, 576)), g((341, 28), (341, 69), (375, 69))) and is_found(Template(r"tpl1647279542949.png", record_pos=(0.31, 0.242), resolution=(1024, 576)), g((801, 517), (801, 555), (861, 555))) and is_found(Template(r"tpl1644773083422.png", record_pos=(0.418, 0.234), resolution=(1024, 576)), g((889, 516), (889, 540), (992, 540))):
        return 0
    elif is_found(Template(r"tpl1644773599992.png", record_pos=(-0.187, -0.195), resolution=(1024, 576)), g((256, 70), (256, 106), (386, 106))):
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
        if time.time() - start > 2:
            logger.error("第%d轮结束，耗时%.2lfs" % (cnt, time.time() - start))
            start = time.time()
        return 0
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
    elif is_found(Template(r"tpl1644775722879.png", record_pos=(-0.269, -0.122), resolution=(1024, 576)), g((190, 152), (190, 174), (284, 174))) and is_found(Template(r"tpl1644776053543.png", target_pos=4, record_pos=(0.101, 0.128), resolution=(1024, 576)), g((513, 410), (513, 428), (717, 428))):
        return 0
    elif is_found(Template(r"tpl1644776295243.png", record_pos=(-0.199, -0.237), resolution=(1024, 576)), g((258, 20), (258, 71), (359, 71))) and is_found(Template(r"tpl1644776352909.png", record_pos=(-0.411, 0.047), resolution=(1024, 576)), g((45, 324), (45, 349), (138, 349))):
        return 7
    elif is_found(Template(r"tpl1644856432544.png", threshold=0.9500000000000002, record_pos=(-0.281, -0.102), resolution=(1024, 576)), g((193, 153), (193, 216), (256, 216))):
        XY = (XY[0] - 100, XY[1])
        return 0
    elif is_found(Template(r"tpl1644779677165.png", record_pos=(-0.415, -0.241), resolution=(1024, 576))):
        return 0
    return -1
    

def attach():
    '''根据当前策略号作相应策略'''
    global XY
    global screen
    index = detach()
    logger.debug("index============>" + str(index))
    if index == 0:
        touch(XY)
    elif index == 1:
        logger.debug("============>" + str(XY))
    elif index == 3:
        # 滑动
        swipe((200, 283), vector=[0.0, 0.4], steps=3, duration=0.2)
        sleep(3.0)
    elif index == 4:
        # 缩放
        pinch(in_or_out='in', center=None, percent=0.5)
        sleep(1.0)
        swipe((512, 288), vector=[0.0, -1.0], steps=5, duration=0.2)
    elif index == 5:
        sleep(1.0)
        click((523, 163))  # 第一梯队
        wait_to(Template(r"tpl1647278748100.png", record_pos=(0.424, -0.172), resolution=(1024, 576)), g((934, 99), (934, 126), (958, 126)))
        click((523, 163))  # 第一梯队
        wait_to(Template(r"tpl1647277864179.png", record_pos=(-0.302, 0.208), resolution=(1024, 576)), g((142, 489), (142, 514), (264, 514)))
        click((940, 449))  # 补给
        sleep(2.0)
        wait_to(Template(r"tpl1647278748100.png", record_pos=(0.424, -0.172), resolution=(1024, 576)), g((934, 99), (934, 126), (958, 126)))
        click((61, 473))  # 计划模式
        wait_to(Template(r"tpl1647278941881.png", record_pos=(-0.443, 0.181), resolution=(1024, 576)), g((5, 463), (5, 483), (112, 483)))
        swipe((512, 288), vector=[0.0, 1.0], steps=100, duration=0.1)
        wait_to(Template(r"tpl1647279057807.png", record_pos=(0.302, 0.104), resolution=(1024, 576)), g((765, 382), (765, 406), (877, 406)))
        click((427, 237))  # 第一位点
        wait_to(Template(r"tpl1647279191707.png", record_pos=(0.019, 0.018), resolution=(1024, 576)), g((501, 279), (501, 333), (562, 333)))
        click((764, 266))  # 第二位点
        wait_to(Template(r"tpl1647279282501.png", record_pos=(0.33, 0.249), resolution=(1024, 576)), g((829, 528), (829, 558), (871, 558)))
        click((946, 526))  # 执行计划
        
        sleep(5.0)
    elif index == 7:
        for i in range(5):
            touch((234, 169))
            sleep(3.0)
            screen = G.DEVICE.snapshot()
            if not is_found(Template(r"tpl1647281945905.png", record_pos=(0.423, 0.227), resolution=(1024, 576))):
                break
            for i in range(2):
                for j in range(6):
                    touch((86 + j * (225 - 86), 202 + i * 200))
                    sleep(0.2)
            touch((974, 520))
            sleep(1.0)
            screen = G.DEVICE.snapshot()
            is_found(Template(r"tpl1644776850830.png", record_pos=(0.386, 0.189), resolution=(1024, 576)))
            touch(XY)
            sleep(2.0)
            screen = G.DEVICE.snapshot()
            if is_found(Template(r"tpl1647281644289.png", record_pos=(0.098, 0.206), resolution=(1024, 576))):
                touch(XY)
                sleep(1.0)
            sleep(2.0)
        screen = G.DEVICE.snapshot()
        is_found(Template(r"tpl1644779677165.png", record_pos=(-0.415, -0.241), resolution=(1024, 576)))
        touch(XY)
        sleep(2.0)
        touch(XY)
        sleep(2.0)
    elif index == 8:
        click((523, 163))  # 指挥部
        wait_to(Template(r"tpl1647277864179.png", record_pos=(-0.302, 0.208), resolution=(1024, 576)), g((142, 489), (142, 514), (264, 514)))
        click((926, 508))  # 确定
        wait_to(Template(r"tpl1647278147416.png", record_pos=(-0.44, 0.181), resolution=(1024, 576)), g((7, 460), (7, 486), (115, 486)))
        click((239, 157))  # 机场
        wait_to(Template(r"tpl1647277864179.png", record_pos=(-0.302, 0.208), resolution=(1024, 576)), g((142, 489), (142, 514), (264, 514)))
        click((926, 508))  # 确定
        wait_to(Template(r"tpl1647278147416.png", record_pos=(-0.44, 0.181), resolution=(1024, 576)), g((7, 460), (7, 486), (115, 486)))
        click((926, 508))  # 开始作战
    elif index == 9:
        touch(XY)
        sleep(5.0)
        touch((87, 41))
        sleep(2.0)
    elif index == 11:
        click((788, 152))
        sleep(1.0)
        click((570, 330))
    else:
        logger.debug("============>" + str(XY))
    sleep(1.0)
    return 

if DEBUG:
    attach()
else:
    while True:
        attach()
    


