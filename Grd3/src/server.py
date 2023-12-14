import ginfo
import sys
import time
from flask import Flask

ginfo.setup("https://info.gadaidev.repl.co/")
while True:
    if not ginfo.is_exist(f"grd3--{sys.argv[1]}.gco"):
        x = ginfo.write(f"grd3--{sys.argv[1]}.gco",open(sys.argv[2],"r").read())
