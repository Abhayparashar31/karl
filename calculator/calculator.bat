@echo off
call C:\Users\abhay\Anaconda3/Scripts/activate.bat
call conda activate chatbot
cd chatbot
cd calculator
cls
pythonw calculator.py
exit
