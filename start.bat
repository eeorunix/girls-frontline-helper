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
) else (
    echo python 不存在
    echo python 2.7 下载中...

    set Url=http://www.python.org/ftp/python/2.7.16/python-2.7.16.amd64.msi
    set Save=
    for %%a in ("%Url%") do set "FileName=%%~nxa"
    if not defined Save set "Save=%cd%"
    (echo Download Wscript.Arguments^(0^),Wscript.Arguments^(1^)
    echo Sub Download^(url,target^)
    echo   Const adTypeBinary = 1
    echo   Const adSaveCreateOverWrite = 2
    echo   Dim http,ado
    echo   Set http = CreateObject^("Msxml2.ServerXMLHTTP"^)
    echo   http.open "GET",url,False
    echo   http.send
    echo   Set ado = createobject^("Adodb.Stream"^)
    echo   ado.Type = adTypeBinary
    echo   ado.Open
    echo   ado.Write http.responseBody
    echo   ado.SaveToFile target
    echo   ado.Close
    echo End Sub)>DownloadFile.vbs
    DownloadFile.vbs "%Url%" "%Save%\%FileName%"
    del DownloadFile.vbs

    echo python 2.7 下载完成 请按提示安装 并按默认路径安装python

    python-2.7.16.amd64.msi

    echo python 2.7 安装完成
)
echo 安装第三方库

C:\Python27\python.exe -m pip install -i http://pypi.douban.com/simple --trusted-host pypi.douban.com -r requirements.txt

echo 第三方库安装完成
echo 运行脚本

C:\Python27\python.exe main.py
