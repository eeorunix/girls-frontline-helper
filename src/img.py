# coding=utf-8

import cv2


class PIC(object):
    def __init__(self):
        self.battle = cv2.imread('image/battle.bmp')
        self.combat = cv2.imread('image/combat.bmp')
        self.normal = cv2.imread('image/normal.bmp')
        self.command = cv2.imread('image/command.bmp')
        self.round1 = cv2.imread('image/round1.bmp')
        self.three2zero = cv2.imread('image/3-0.bmp')
        self.settlement = cv2.imread('image/settlement.bmp')
        self.share = cv2.imread('image/share.bmp')
        self.two2one = cv2.imread('image/2-1.bmp')
        self.round2 = cv2.imread('image/round2.bmp')
        self.round3 = cv2.imread('image/round3.bmp')
        self.one2two = cv2.imread('image/1-2.bmp')
        self.zero2three = cv2.imread('image/0-3.bmp')
        self.over = cv2.imread('image/over.bmp')
        self.restore = cv2.imread('image/restore.bmp')
        self.fast = cv2.imread('image/fast.bmp')
        self.full = cv2.imread('image/full.bmp')
        self.factory = cv2.imread('image/factory.bmp')
        self.aim = cv2.imread('image/N_0_1.bmp')
        self.emergency = cv2.imread('image/emergency.bmp')
        self.back = cv2.imread('image/back.bmp')
        self.pre = cv2.imread('image/pre.bmp')
        self.round0 = cv2.imread('image/round0.bmp')
