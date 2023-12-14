python3 -m PyInstaller src/client.py --onefile
python3 -m PyInstaller src/server.py --onefile

# distフォルダにclient、serverが作られます。
# 使い方は、ソースコードがsrcにあるのでそれ見てください。