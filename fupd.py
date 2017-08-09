#!/usr/bin/python
print "content-type:text/html\n" 

import cgi
import commands,os


form = cgi.FieldStorage()
fileitem=form['file1']
#print fileitem
if (fileitem.filename) :

  		fn = os.path.basename(fileitem.filename)
		dp=fn
		open('../hadoop/' + fn, 'wb').write(fileitem.file.read())
		#print nnip//IP of namenode
		f=open("/tmp/docker.txt","r")
		s=f.read()
		f.close()
		print commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+s+" hadoop fs -put /tmp/"+fn+" /")
		message = 'The file "' + fn + '" was uploaded successfully'
		print message
		print """<body style=\"background-color:#EEEBDA;\"><h1  style="color:#056303;>Welcome To Hadoop!!</h1><br><h3 style="color:#056303;>Your File Has Been Successfully Uploaded into HDFS Cluster</h3>
<br>
				<script>
				function alertMsg(){
					alert('File uploaded Successfully');
				} 
				alertMsg();
				</script>
				</body>"""
	
else:
		print """<body style=\"background-color:#EEEDBDA;"><script>
				function alertMsg(){
					alert('Upload Failed. Please  try again later');
				}
				alertMsg();
				</script>
				</body>"""




