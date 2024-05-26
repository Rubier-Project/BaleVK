import sys
import site
import os

class PythonVersionError(Exception):
    ...

def requirements_checker():
    dbs = set()
    for path in site.getsitepackages():
        for fols in os.listdir(path):
            dbs.add(fols)

    if not "httpx" in dbs:
        os.system("pip install httpx")

    if not "requests" in dbs:
        os.system("pip install requests")

    if not sys.version[0] == "3":
        raise PythonVersionError("Your Python Version is not work for BaleVK, needed: 3.xx")