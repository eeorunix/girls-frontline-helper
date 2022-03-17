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

def click(pos):
    x, y = pos
    a = random.randint(0, 4) - 2
    b = random.randint(0, 4) - 2
    touch((x + a, y + b))
    sleep(0.2)

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
    while 1:
        screen = G.DEVICE.snapshot()
        if is_found(template, rect):
            return
        sleep(0.2)
    assert 0

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
    elif is_found(Template(r"tpl1647025537096.png", record_pos=(-0.307, -0.196), resolution=(1024, 576)), g((141, 68), (141, 107), (255, 107))):
        return 3
    elif is_found(Template(r"tpl1647025901008.png", record_pos=(-0.283, -0.194), resolution=(1024, 576)), g((145, 73), (145, 105), (299, 105))):
        return 3
    elif is_found(Template(r"tpl1644771635172.png", record_pos=(0.297, 0.185), resolution=(1024, 576)), g((771, 466), (771, 489), (862, 489))):
        return 0
    elif is_found(Template(r"tpl1644771405564.png", record_pos=(-0.198, -0.237), resolution=(1024, 576)), g((261, 21), (261, 69), (357, 69))):
        return 2
    elif is_found(Template(r"tpl1644771706558.png", record_pos=(-0.151, -0.247), resolution=(1024, 576)), g((338, 6), (338, 65), (377, 65))) and is_found(Template(r"tpl1644771774441.png", record_pos=(0.386, 0.221), resolution=(1024, 576)), g((842, 500), (842, 529), (972, 529))):
        return 4
    elif is_found(Template(r"tpl1647063538393.png", record_pos=(-0.149, -0.234), resolution=(1024, 576)), g((341, 29), (341, 67), (378, 67))) and is_found(Template(r"tpl1647063577054.png", threshold=0.75, rgb=True, record_pos=(0.311, 0.241), resolution=(1024, 576)), g((797, 518), (797, 552), (863, 552))):
        return 5
    elif is_found(Template(r"tpl1647063538393.png", record_pos=(-0.149, -0.234), resolution=(1024, 576)), g((341, 29), (341, 67), (378, 67))) and is_found(Template(r"tpl1647450033644.png", record_pos=(0.311, 0.242), resolution=(1024, 576)), g((801, 517), (801, 555), (861, 555))) and is_found(Template(r"tpl1647066298630.png", record_pos=(-0.439, 0.179), resolution=(1024, 576)), g((2, 456), (2, 487), (122, 487))):
        return 6
    elif is_found(Template(r"tpl1647063538393.png", record_pos=(-0.149, -0.234), resolution=(1024, 576)), g((341, 29), (341, 67), (378, 67))) and is_found(Template(r"tpl1647144019805.png", record_pos=(0.311, 0.242), resolution=(1024, 576)), g((801, 517), (801, 555), (861, 555))):
        return 7
    elif is_found(Template(r"tpl1644773664247.png", record_pos=(-0.437, -0.248), resolution=(1024, 576)), g((31, 18), (31, 51), (100, 51))):
        XY = (XY[0] + 100, XY[1])
        return 0
    elif is_found(Template(r"tpl1644775198955.png", record_pos=(-0.076, 0.223), resolution=(1024, 576)), g((408, 509), (408, 524), (461, 524))):
        XY = (XY[0] + 100, XY[1])
        for _ in range(4):
            click(XY)
            sleep(0.5)
        return 0
    elif is_found(Template(r"tpl1647069986280.png", record_pos=(-0.246, -0.121), resolution=(1024, 576)), g((194, 153), (194, 175), (327, 175))) and is_found(Template(r"tpl1647070154857.png", target_pos=8, record_pos=(-0.002, 0.046), resolution=(1024, 576)), g((443, 251), (443, 419), (578, 419))):
        return 0
    elif is_found(Template(r"tpl1647070306739.png", record_pos=(-0.2, -0.237), resolution=(1024, 576)), g((258, 20), (258, 71), (359, 71))) and is_found(Template(r"tpl1647070328462.png", record_pos=(-0.064, -0.126), resolution=(1024, 576)), g((427, 140), (427, 179), (465, 179))):
        return 0
    elif is_found(Template(r"tpl1647070542885.png", record_pos=(0.393, 0.199), resolution=(1024, 576)), g((884, 474), (884, 510), (944, 510))):
        click(XY)
        sleep(1.0)
        click(XY)
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
        click(XY)
    elif index == 1:
        logger.debug("============>" + str(XY))
    elif index == 2:
        click((75, 188))  # 作战任务
        wait_to(Template(r"tpl1647447498252.png", record_pos=(0.427, -0.185), resolution=(1024, 576)), g((938, 87), (938, 112), (961, 112)))
        swipe((200, 283), vector=[0.0, -0.4], steps=3, duration=0.2)
    elif index == 3:
        click(XY)
        wait_to(Template(r"tpl1647447972805.png", record_pos=(-0.145, -0.052), resolution=(1024, 576)), g((343, 204), (343, 267), (386, 267)))
        click((970, 153))
        wait_to(Template(r"tpl1647447972805.png", record_pos=(-0.145, -0.052), resolution=(1024, 576)), g((343, 204), (343, 267), (386, 267)))
        click((540, 237))
    elif index == 4:
        pinch(in_or_out='in', center=None, percent=0.5)  # 缩放
        sleep(1.0)
        swipe((200, 283), vector=[1.0, 1.0], steps=50, duration=0.1)  # 右下滑动
        wait_to(Template(r"tpl1647448741476.png", record_pos=(-0.075, 0.19), resolution=(1024, 576)), g((402, 444), (402, 523), (469, 523)))
        click((224, 118))  # 左上机场
        wait_to(Template(r"tpl1647277864179.png", record_pos=(-0.302, 0.208), resolution=(1024, 576)), g((142, 489), (142, 514), (264, 514)))
        click((932, 508))  # 第一梯队部署
        wait_to(Template(r"tpl1647448741476.png", record_pos=(-0.075, 0.19), resolution=(1024, 576)), g((402, 444), (402, 523), (469, 523)))
        click((178, 493))  # 左下机场
        wait_to(Template(r"tpl1647277864179.png", record_pos=(-0.302, 0.208), resolution=(1024, 576)), g((142, 489), (142, 514), (264, 514)))
        click((932, 508))  # 第二梯队部署
        wait_to(Template(r"tpl1647448741476.png", record_pos=(-0.075, 0.19), resolution=(1024, 576)), g((402, 444), (402, 523), (469, 523)))
        click((932, 508))  # 开始作战
        click((932, 508))  # 开始作战
        if time.time() - start > 2:
            cnt += 1
            start = time.time()
            logger.error("无限脚本开始，当前进行第%d轮" % cnt)
        sleep(1.5)
    elif index == 5:
        wait_to(Template(r"tpl1647449130009.png", record_pos=(-0.429, -0.168), resolution=(1024, 576)), g((56, 99), (56, 133), (90, 133)))
        click((74, 116))  # 点击说明
        wait_to(Template(r"tpl1647449181778.png", record_pos=(-0.428, -0.166), resolution=(1024, 576)), g((61, 102), (61, 135), (87, 135)))
        click((74, 116))  # 点击说明
        sleep(0.2)
        wait_to(Template(r"tpl1647278147416.png", record_pos=(-0.44, 0.181), resolution=(1024, 576)), g((7, 460), (7, 486), (115, 486)))
        click((224, 135))  # 左上机场
        wait_to(Template(r"tpl1647278748100.png", record_pos=(0.424, -0.172), resolution=(1024, 576)), g((934, 99), (934, 126), (958, 126)))
        click((60, 472))  # 计划模式
        wait_to(Template(r"tpl1647278941881.png", record_pos=(-0.443, 0.181), resolution=(1024, 576)), g((5, 463), (5, 483), (112, 483)))
        click((155, 243))  # 左上白点
        wait_to(Template(r"tpl1647449520081.png", record_pos=(-0.351, -0.044), resolution=(1024, 576)), g((133, 222), (133, 265), (173, 265)))
        click((178, 493))  # 左下机场
        wait_to(Template(r"tpl1647449602282.png", record_pos=(-0.25, 0.198), resolution=(1024, 576)), g((213, 480), (213, 503), (300, 503)))
        click((168, 493))  # 移动
        wait_to(Template(r"tpl1647449673833.png", record_pos=(-0.341, 0.089), resolution=(1024, 576)), g((142, 358), (142, 401), (184, 401)))
        click((900, 510))  # 执行计划
        sleep(10.0)
    elif index == 6:
        click((183, 428))  # 左下机场
        wait_to(Template(r"tpl1647277864179.png", record_pos=(-0.302, 0.208), resolution=(1024, 576)), g((142, 489), (142, 514), (264, 514)))
        click((783, 509))  # 撤离
        wait_to(Template(r"tpl1647450113336.png", record_pos=(0.081, 0.106), resolution=(1024, 576)), g((540, 379), (540, 415), (651, 415)))
        click((594, 396))  # 确认撤离
        wait_to(Template(r"tpl1647450191589.png", record_pos=(-0.326, 0.141), resolution=(1024, 576)), g((164, 418), (164, 446), (192, 446)))
        click((183, 428))  # 左下机场
        wait_to(Template(r"tpl1647277864179.png", record_pos=(-0.302, 0.208), resolution=(1024, 576)), g((142, 489), (142, 514), (264, 514)))
        click((201, 502))  # 队伍编成
        wait_to(Template(r"tpl1647450267553.png", record_pos=(-0.168, -0.245), resolution=(1024, 576)), g((265, 23), (265, 52), (415, 52)))
        click((949, 544))  # 阵型编成
        wait_to(Template(r"tpl1647450327595.png", record_pos=(0.341, -0.054), resolution=(1024, 576)), g((834, 206), (834, 260), (888, 260)))
        click((861, 234))  # 梯队预设
        wait_to(Template(r"tpl1647450393651.png", record_pos=(0.39, 0.138), resolution=(1024, 576)), g((831, 410), (831, 448), (992, 448)))
        click((687, 159))  # 预设2
        wait_to(Template(r"tpl1647450515144.png", record_pos=(0.008, -0.003), resolution=(1024, 576)), g((512, 240), (512, 329), (552, 329)))
        click((906, 507))  # 套用预设
        wait_to(Template(r"tpl1647450580716.png", record_pos=(-0.061, 0.051), resolution=(1024, 576)), g((432, 323), (432, 357), (468, 357)))
        click((452, 340))  # 强制替换
        wait_to(Template(r"tpl1647450629017.png", record_pos=(-0.06, 0.052), resolution=(1024, 576)), g((432, 323), (432, 357), (468, 357)))
        click((657, 399))  # 确认
        wait_to(Template(r"tpl1647450327595.png", record_pos=(0.341, -0.054), resolution=(1024, 576)), g((834, 206), (834, 260), (888, 260)))
        click((928, 507))  # 确定
        wait_to(Template(r"tpl1647450267553.png", record_pos=(-0.168, -0.245), resolution=(1024, 576)), g((265, 23), (265, 52), (415, 52)))
        click((87, 42))  # 后退
        wait_to(Template(r"tpl1647278147416.png", record_pos=(-0.44, 0.181), resolution=(1024, 576)), g((7, 460), (7, 486), (115, 486)))
        click((183, 428))  # 左下机场
        wait_to(Template(r"tpl1647277864179.png", record_pos=(-0.302, 0.208), resolution=(1024, 576)), g((142, 489), (142, 514), (264, 514)))
        click((932, 508))  # 确认部署
        wait_to(Template(r"tpl1647278147416.png", record_pos=(-0.44, 0.181), resolution=(1024, 576)), g((7, 460), (7, 486), (115, 486)))
        sleep(0.2)
        click((183, 428))  # 左下机场
        wait_to(Template(r"tpl1647278748100.png", record_pos=(0.424, -0.172), resolution=(1024, 576)), g((934, 99), (934, 126), (958, 126)))
        click((183, 428))  # 左下机场
        wait_to(Template(r"tpl1647277864179.png", record_pos=(-0.302, 0.208), resolution=(1024, 576)), g((142, 489), (142, 514), (264, 514)))
        click((932, 447))  # 补给
        wait_to(Template(r"tpl1647278748100.png", record_pos=(0.424, -0.172), resolution=(1024, 576)), g((934, 99), (934, 126), (958, 126)))
        click((183, 428))  # 左下机场
        wait_to(Template(r"tpl1647277864179.png", record_pos=(-0.302, 0.208), resolution=(1024, 576)), g((142, 489), (142, 514), (264, 514)))
        click((783, 509))  # 撤离
        wait_to(Template(r"tpl1647450113336.png", record_pos=(0.081, 0.106), resolution=(1024, 576)), g((540, 379), (540, 415), (651, 415)))
        click((594, 396))  # 确认撤离
        wait_to(Template(r"tpl1647450191589.png", record_pos=(-0.326, 0.141), resolution=(1024, 576)), g((164, 418), (164, 446), (192, 446)))
        click((183, 428))  # 左下机场
        wait_to(Template(r"tpl1647277864179.png", record_pos=(-0.302, 0.208), resolution=(1024, 576)), g((142, 489), (142, 514), (264, 514)))
        click((201, 502))  # 队伍编成
        wait_to(Template(r"tpl1647450267553.png", record_pos=(-0.168, -0.245), resolution=(1024, 576)), g((265, 23), (265, 52), (415, 52)))
        click((949, 544))  # 阵型编成
        wait_to(Template(r"tpl1647450327595.png", record_pos=(0.341, -0.054), resolution=(1024, 576)), g((834, 206), (834, 260), (888, 260)))
        click((861, 234))  # 梯队预设
        wait_to(Template(r"tpl1647450393651.png", record_pos=(0.39, 0.138), resolution=(1024, 576)), g((831, 410), (831, 448), (992, 448)))
        click((687, 89))  # 预设1
        wait_to(Template(r"tpl1647450515144.png", record_pos=(0.008, -0.003), resolution=(1024, 576)), g((512, 240), (512, 329), (552, 329)))
        click((906, 507))  # 套用预设
        wait_to(Template(r"tpl1647450327595.png", record_pos=(0.341, -0.054), resolution=(1024, 576)), g((834, 206), (834, 260), (888, 260)))
        click((928, 507))  # 确定
        wait_to(Template(r"tpl1647450267553.png", record_pos=(-0.168, -0.245), resolution=(1024, 576)), g((265, 23), (265, 52), (415, 52)))
        click((87, 42))  # 后退
    elif index == 7:
        click((253, 35))  # 终止作战
        wait_to(Template(r"tpl1647451075150.png", record_pos=(-0.118, 0.1), resolution=(1024, 576)), g((324, 366), (324, 415), (458, 415)))
        click((393, 394))  # 重新作战
        if time.time() - start > 2:
            logger.error("第%d轮结束，耗时%.2lfs" % (cnt, time.time() - start))
            start = time.time()
        sleep(1.0)
    else:
        logger.debug("============>" + str(XY))
    sleep(1.0)
    return 

if DEBUG:
    attach()
else:
    while True:
        attach()
