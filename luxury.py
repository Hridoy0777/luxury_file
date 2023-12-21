import os, sys
os.system("git pull")
try:
    __import__("int_enc").apv()
except Exception as e:
    exit(str(e))
