#!/usr/bin/python
print "content-type: text/html\n"
import commands,cgi
form=cgi.FormContent()


print """ <style> body{
background:#EEEBDA; }</style>"""
print """
<body><h1 style="color:#056303;">Creating On Demand Cluster:</h1></body>
"""


commands.getstatusoutput("sudo systemctl restart docker")
print """<br><br><h3 style="color:#726B63;">Creating Namenode:</h3>"""
s1=commands.getstatusoutput("sudo docker run -i -d 62ca8576a274  /bin/bash")[1]
f=open("/tmp/docker.txt","w")
f.write(s1)
f.close()
commands.getstatusoutput("sudo docker run -i -d -v /root/Desktop/hadoopfiles:/etc/hadoop"+s1) [1]
commands.getstatusoutput("sudo docker exec -i "+s1+" hadoop namenode -format")[1]
commands.getstatusoutput("sudo docker exec -i "+s1+" hadoop-daemon.sh start namenode")[1]
print "<br>"
print commands.getstatusoutput("sudo docker exec -i "+s1+" /usr/java/jdk1.7.0_51/bin/jps")[1]

print """<br><h3 style="color:#726B63;">Namenode successfully created!</h3>"""

print """<br><h3 style="color:#726B63;">Creating Jobtracker:</h3>"""

s2=commands.getstatusoutput("sudo docker run -i -d fe8c89970f77 /bin/bash")[1]
commands.getstatusoutput("sudo docker run -i -d -v /root/Desktop/hadoopfiles:/etc/hadoop"+s2) [1]
commands.getstatusoutput("sudo docker exec -i "+s2+" hadoop-daemon.sh start jobtracker")[1]
print "<br>"
print commands.getstatusoutput("sudo docker exec -i "+s2+" /usr/java/jdk1.7.0_51/bin/jps")[1]

print """<br><br><h3 style="color:#726B63;">Job Tracker successfully created!</h3>"""

print """<br><br><h3 style="color:#726B63;">Creating Datanode and TaskTracker:</h3>"""

node=form['nodes'][0]

for i in range(int(node)):
	
	s3=commands.getstatusoutput("sudo docker run -i -d 3d02c9ab229e /bin/bash")[1]
	commands.getstatusoutput("sudo docker run -i -d -v /root/Desktop/hadoopfiles:/etc/hadoop"+s3) [1]
	commands.getstatusoutput("sudo docker exec -i "+s3+" hadoop-daemon.sh start datanode")[1]
	commands.getstatusoutput("sudo docker exec -i "+s3+" hadoop-daemon.sh start tasktracker")[1]
	print "<br>"
	print commands.getstatusoutput("sudo docker exec -i "+s3+" /usr/java/jdk1.7.0_51/bin/jps")[1]

print """<br><h3 style="color:#726B63;">Datanodes and Task Trackers successfully created!</h3>"""
print """<br><h2 style="color:#056303;">Your Cluster is ready!!!</h2>"""

print """ <html>
	<body>
	<form enctype="multipart/form-data" action="http://192.168.43.197/cgi-bin/fupd.py" method="post">
        <p>File:<input type="file" name="file1"></p>
	<p><input style="-webkit-transition-duration: 0.4s; 
    transition-duration: 0.4s;
    border-radius: 4px;
    background-color: #4CAF50;
  left:30px;
   position:relative;" type="submit" value="Upload"></p>
		</form>
		</body>
		</html> """

