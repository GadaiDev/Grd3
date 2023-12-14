import ginfo
import sys
import time
from flask import Flask

app = Flask(__name__)

ginfo.setup("https://info.gadaidev.repl.co/")

def fileload(fname):
    return open(fname,"r").read()

@app.route("/")
def index():
    return fileload("html/index.html")
@app.route("/gco/<url>")
def access(url):
    return ginfo.read(f"grd3--{url}.gco")

app.run("127.0.0.1",8100,True)