import os, sys
os.system("git pull")
try:
    __import__("FOT_WOULD.so").apv()
except Exception as e:
    exit(str(e))
