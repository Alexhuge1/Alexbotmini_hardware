@echo off
"%~dp0installs.exe" -c "%~dp0sw_d_SSQ.lic" -e "%~dp0lmgrd.exe" -l "%~dp0sw_d_SSQ.log" -n "SolidWorks Flexnet Server"
net start "SolidWorks Flexnet Server"
pause