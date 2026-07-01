@echo off
icacls "D:\BIO-WEB" /grant "Everyone:(OI)(CI)F" /T /C /L
mkdir "D:\BIO-WEB\src\components"
echo Directory created successfully.
