# Girls Frontline Helper

少女前线（Girls Frontline）辅助脚本

**在2022年2月19日进行版本更新，使用网易AirtestIDE（V1.2.13）进行执行。** 由于该软件把我想做的前端改进都做了，改代码起来也比较方便（特别是图像判断直接能在代码里面看到，而不用费时命名新的图像）

（PS：我就不需要再包装win32gui这些接口了）

不过该软件还是有缺点，缺少的都是非常实用的功能：
1. 看不到设备中鼠标的坐标位置
2. 不能直接识别像素点的颜色
3. 无法导出exe
4. 无法自定义前端操作界面类似于按键精灵

## 最大特点

- 纯后台进行，后台截图，后台按键，无限刷关卡的同时，可以干任何事
- 自动修理，自动分解三星，~~自动使用二星强化当前首位枪娘~~（TODO）
- ~~脚本稳定，有错误自动回正功能，实现无限挂机不卡死~~（TODO）

## 使用流程

- ~~安装[python2.7](https://www.python.org/ftp/python/2.7.16/python-2.7.16.amd64.msi)~~（该步貌似可以省）
- 安装[AirtestIDE](https://airtest.netease.com/changelog.html)
- 安装[mumu模拟器](https://mumu.163.com/)，模拟器分辨率大小需设为1024x576
- [AirtestIDE连接mumu模拟器](https://airtest.doc.io.netease.com/IDEdocs/3.2device_connection/2_emulator_connection/)
- 在IDE中打开`.air`文件夹
- mumu模拟器在`少女前线`主界面上，并在IDE中按`运行`键（F5）

## 注意事项

- 在游戏主界面运行脚本
- 需要默认打开自动补给
- 现在仅能刷`Normal 0-1`，在刷的同时出去修理的时候顺便收后勤
