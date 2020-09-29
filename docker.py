#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess as sp
import cgi

form = cgi.FieldStorage()
osname = form.getvalue("x")
ostype = form.getvalue("y")
cmd = "sudo docker run -d -i -t --name {0} {1} ".format(osname,ostype)
output=sp.getoutput(cmd)
print(" OS Launched {0}".format(osname))

