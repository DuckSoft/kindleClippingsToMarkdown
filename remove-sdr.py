import sys
import os
import shutil

argc = len(sys.argv)

if argc < 2:
    print(sys.argv[0]+" <path>")
    sys.exit(1)

docdir = os.path.join(sys.argv[1], "documents")
files = os.listdir(docdir)
info = {}

for entry in files:
    base = os.path.splitext(entry)[0]
    val = info.setdefault(base, 0)
    info[base] = val + 1

for (k, v) in info.items():
    if v == 1:
        file = k+".sdr"
        path = os.path.join(docdir, file)
        if os.path.exists(path):
            shutil.rmtree(path)
            print("removed %s" % path)