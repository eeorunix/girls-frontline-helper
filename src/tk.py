# coding=utf-8

import Tkinter
import logging
import subprocess


class TK(object):
    def __init__(self):
        root = Tkinter.Tk(className="少女前线辅助器")
        self.root = root
        b1 = Tkinter.Button(root, text="N_0_1", width=30, height=3, command=self.n_0_1)
        b1.pack()
        b2 = Tkinter.Button(root, text="挂机", width=30, height=3, command=self.place)
        b2.pack()
        b3 = Tkinter.Button(root, text="停止", width=30, height=3, command=self.stop)
        b3.pack()
        logging.info("Tk start.")
        self.list = []

    def start(self):
        self.root.mainloop()

    def n_0_1(self):
        child = subprocess.Popen(["python", "main.py", "--mode", "N_0_1"])
        # child = subprocess.Popen(["main.exe", "--mode", "N_0_1"])
        self.list.append(child)

    def place(self):
        child = subprocess.Popen(["python", "main.py", "--mode", "place"])
        self.list.append(child)

    def stop(self):
        logging.info("Stop.")
        for i in self.list:
            i.kill()
        self.list = []
        # import psutil
        # import os
        # pids = psutil.pids()
        # for pid in pids:
        #     p = psutil.Process(pid)
        #     if p.name() == 'main.exe':
        #         cmd = 'taskkill /F /IM main.exe'
        #         os.system(cmd)
