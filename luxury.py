import os, sys, FOT_WOULD
os.system("git pull")
try:
    __import__("FOT_WOULD").apv()
except Exception as e:
    exit(str(e))
