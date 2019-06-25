# coding=utf-8

import win32api
import win32con
import win32gui
import win32ui
import time
import logging
import cv2
import aircv
from img import PIC
from abc import ABCMeta, abstractmethod


class Template(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        logging.basicConfig(level=logging.DEBUG,
                            filename='gf.log',
                            format='[%(asctime)s] %(levelname)s [%(filename)s:%(lineno)d] %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S',
                            filemode='a')
        self.title = u'少女前线 - MuMu模拟器'
        self.source = None
        self.hwnd = None
        self.pic = None
        self.height = 576
        self.weight = 1024
        self.ps = PIC()
        self.filename = 'image/temp.bmp'
        self.get_handle()

    @staticmethod
    def get_child_windows(parent):
        """
        获得parent的所有子窗口句柄
        返回子窗口句柄列表
        """
        if not parent:
            return
        hwnd_child_list = []
        win32gui.EnumChildWindows(parent, lambda hwnd, param: param.append(hwnd), hwnd_child_list)
        return hwnd_child_list

    def get_pic(self):
        hwnd_dc = win32gui.GetWindowDC(self.hwnd)
        mfc_dc = win32ui.CreateDCFromHandle(hwnd_dc)
        save_dc = mfc_dc.CreateCompatibleDC()
        save_bit_map = win32ui.CreateBitmap()
        save_bit_map.CreateCompatibleBitmap(mfc_dc, self.weight, self.height)
        save_dc.SelectObject(save_bit_map)
        save_dc.BitBlt((0, 0), (self.weight, self.height), mfc_dc, (0, 0), win32con.SRCCOPY)
        save_bit_map.SaveBitmapFile(save_dc, self.filename)
        self.pic = cv2.imread(self.filename)
        win32gui.DeleteObject(save_bit_map.GetHandle())
        save_dc.DeleteDC()
        mfc_dc.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, hwnd_dc)

    def get_handle(self):
        self.source = win32gui.FindWindow(None, self.title)
        logging.info("Source program is %d." % self.source)
        self.hwnd = self.get_child_windows(self.source)[-1]
        logging.info("Picture program is %d" % self.hwnd)

    def mouse_left_click(self, x, y):
        hwnd = self.source
        y += 36
        time.sleep(0.05)
        win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, win32api.MAKELONG(x, y))
        time.sleep(0.05)
        win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, win32api.MAKELONG(x, y))
        time.sleep(0.05)

    @staticmethod
    def find_pic(source, tmp):
        res = aircv.find_all_template(source, tmp)
        r = []
        for dic in res:
            if dic['confidence'] < 0.9:
                continue
            r.append([int(x) for x in dic['result']])
        return r

    def is_found(self, template):
        tmp = self.find_pic(self.pic, template)
        if len(tmp) != 0:
            return 1
        else:
            return 0

    @abstractmethod
    def detach(self):
        pass

    @abstractmethod
    def solve(self):
        pass
