@echo off
:a
echo %time%
echo "启动IP校验"
start /min checkips.exe
start /min checkip.exe
ping -n 1 127.0.0.1>nul
:b
tasklist|find /i "checkips.exe">nul && goto b
tasklist|find /i "checkip.exe">nul && goto b
echo %time%
echo "启动IP爬取"
tasklist|find /i "checkips.exe">nul || tasklist|find /i "checkip.exe">nul || start /min paip.exe
ping -n 1 127.0.0.1>nul
:c
tasklist|find /i "paip.exe">nul && goto c
echo %time%
echo "启动ip筛选"
tasklist|find /i "checkips.exe">nul || tasklist|find /i "checkip.exe">nul || tasklist|find /i "paip.exe">nul || (start /min ips筛选.exe & start /min ipp筛选.exe)

:d
tasklist|find /i "ips筛选">nul && goto d
tasklist|find /i "ipp筛选">nul && goto d
echo "开启下一轮" 
ping -n 1 127.0.0.1>nul
goto a

