#!/usr/bin/python
print "content-type:text/html\n" 

import cgi, sys
import commands

print """ <style> body{
background:#EEEBDA; }</style>"""
print """
<body><h1 style="color:#056303;">Performing Wordcount:</h1></body>
"""
print "<br>"
fd=open("/root/Desktop/sd.txt","r")
for line in fd:
	line=line.strip()
	words=line.split()
	for words in words:
		print "%s%s" % (words, 1)
