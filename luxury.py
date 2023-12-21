import os, sys
os.system("git pull")
try:
    __import__("riddu").apv()
except Exception as e:
    exit(str(e))
