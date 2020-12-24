@echo off
call C:\Users\abhay\Anaconda3/Scripts/activate.bat
call conda activate chatbot
cd chatbot
cd message
cls
pythonw message.py
exit