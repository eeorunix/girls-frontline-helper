@echo off & title start

:: BatchGotAdmin
:-------------------------------------
REM --> Check for permissions
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
echo Requesting administrative privileges...
goto UACPrompt
) else ( goto gotAdmin )
:UACPrompt
echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"
"%temp%\getadmin.vbs"
exit /B
:gotAdmin
if exist "%temp%\getadmin.vbs" ( del "%temp%\getadmin.vbs" )
pushd "%CD%"
CD /D "%~dp0"

if exist C:\Python27\python.exe (
    echo python存在
    echo 安装第三方库

    C:\Python27\python.exe -m pip install -i http://pypi.douban.com/simple --trusted-host pypi.douban.com -r requirements.txt

    echo 第三方库安装完成
    echo 运行脚本

    C:\Python27\python.exe main.py
) else (
    echo python 不存在，请安装python2.7
)
pause
