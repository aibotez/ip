@echo off
:a
echo %time%
echo "����IPУ��"
start /min checkips.exe
start /min checkip.exe
ping -n 1 127.0.0.1>nul
:b
tasklist|find /i "checkips.exe">nul && goto b
tasklist|find /i "checkip.exe">nul && goto b
echo %time%
echo "����IP��ȡ"
tasklist|find /i "checkips.exe">nul || tasklist|find /i "checkip.exe">nul || start /min paip.exe
ping -n 1 127.0.0.1>nul
:c
tasklist|find /i "paip.exe">nul && goto c
echo %time%
echo "����ipɸѡ"
tasklist|find /i "checkips.exe">nul || tasklist|find /i "checkip.exe">nul || tasklist|find /i "paip.exe">nul || (start /min ipsɸѡ.exe & start /min ippɸѡ.exe)

:d
tasklist|find /i "ipsɸѡ">nul && goto d
tasklist|find /i "ippɸѡ">nul && goto d
echo "������һ��" 
ping -n 1 127.0.0.1>nul
goto a

