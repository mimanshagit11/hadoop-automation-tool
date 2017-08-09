#!/usr/bin/python
print "content-type:text/html\n"

from operator import itemgetter
import cgi, sys
import commands

print """ <style> body{
background:#EEEBDA; }</style>"""
print """
<body><h1 style="color:#056303;">Performing Wordcount:</h1></body>
"""
print "<br>"
current_word= None
current_count = 0
word = None
fd=open("/root/Desktop/sd.txt","r")
for line in fd:
	try:
		line = line.strip()
		word, count= line.split('\t',1)
	
		count= int(count)
	except ValueError:
		continue
	if current_word==word:
		current_count+=count
	else:
		if current_word:
			print "%s\t%s" %(current_word,current_count)
		current_count=count
		current_word=word
if current_word==word:
	print "%s\t%s"%(current_word,current_count)
