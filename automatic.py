#!/usr/bin/python
print "content-type:text/html\n"
import cgi
import commands
import random



print """ <style> body{
background:#EEEBDA; }</style>"""
print """
<body><h1 style="color:#056303;">Creating Automatic Cluster:</h1></body>
"""


cmd1 = "nmap -sP 192.168.43.1-254 -n | grep 'Nmap scan' |awk '{print $5}'"

lnodes = commands.getstatusoutput(cmd1)
dict2 = {}
ip=lnodes[1].split("\n")

totRAM=0
totDISK=0
l=()
#print "Available IPs are:"
for i in ip :
	

		#print i
		cmd2="sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+i+" free -mh | grep Mem | awk '{print ($4*100)/($2*1024)}'"
		
		cmd5="sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+i+" free -m | grep Mem | awk '{print $4}'"
		
		try:
			freemper=float(commands.getstatusoutput(cmd2)[1])
	 		availRAM=int(commands.getstatusoutput(cmd5)[1])	
			#print availRAM
			dict2[i]=availRAM
			#print dict2[i]
		except:
			pass
#print "Available Ram and IPs:"
#print dict2


l=sorted(dict2.items(),key=lambda x :x[1],reverse=True)
print "<br>"
print """<br><h3 style="color:#726B63;">Available IPs and RAM:</h3>"""
print l
#print l[0][0]
#print l[1][0]

nnip=l[0][0]
print """<br><br><h3 style="color:#726B63;">Creating Namenode:</h3>"""
commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+nnip+" rpm -q hadoop")
commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+nnip+" rpm -q jdk")
commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+nnip+" hadoop fs namenode -format y")
f=open("/tmp/core-site.xml","w")
f.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://'+nnip+':9001</value>\n</property>\n</configuration>\n')
f.close()
commands.getstatusoutput("sshpass -p 12345 scp /tmp/core-site.xml -l root "+nnip+":/etc/hadoop")
fo=open("/tmp/hdfs-site.xml","w ")
fo.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>/aaaabc</value>\n</property>\n</configuration>\n')
fo.close()
commands.getstatusoutput("sudo sshpass -p 12345 scp /tmp/hdfs-site.xml -l root "+nnip+":/etc/hadoop")
commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+nnip+" hadoop-daemon.sh stop jobtracker")
commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+nnip+" hadoop-daemon.sh stop datanode")
commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+nnip+" hadoop-daemon.sh stop tasktracker")
commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+nnip+" systemctl stop firewalld")
commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+nnip+" setenforce 0")
commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+nnip+" iptables -F")
commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+nnip+" hadoop-daemon.sh start namenode")
print "<br>"
print commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+nnip+" /usr/java/jdk1.7.0_79/bin/jps") 
print """<br><h3 style="color:#726B63;">Namenode successfully created!</h3>"""

print """<br><h3 style="color:#726B63;">Creating Jobtracker:</h3>"""

jtip=l[1][0]
commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+jtip+" rpm -q hadoop")
commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+jtip+" rpm -q jdk")
commands.getstatusoutput("sudo sshpass -p 12345 scp /tmp/mapred-site.xml -l root "+jtip+":/etc/hadoop")
f=open("/tmp/mapred-site.xml","w")
f.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>mapred.job.tracker</name> \n<value>'+jtip+':9002</value>\n</property>\n</configuration>\n')
f.close()
commands.getstatusoutput("sudo sshpass -p 12345 scp /tmp/mapred-site.xml -l root "+jtip+":/etc/hadoop")
commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+jtip+" hadoop-daemon.sh stop namenode")
commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+jtip+" hadoop-daemon.sh stop datanode")
commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+jtip+" hadoop-daemon.sh stop tasktracker")
commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+jtip+" systemctl stop firewalld")
commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+jtip+" setenforce 0")
commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+jtip+" iptables -F")
commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+jtip+" hadoop-daemon.sh start jobtracker")
print "<br>"
print commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+jtip+" /usr/java/jdk1.7.0_79/bin/jps")
print """<br><br><h3 style="color:#726B63;">Job Tracker successfully created!</h3>"""

print """<br><br><h3 style="color:#726B63;">Creating Datanode and TaskTracker:</h3>"""

for i in ip:
	if i==nnip or i==jtip or i=="192.168.43.1" or i=="192.168.43.250":
		pass
	else:

		commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+i+" rpm -q hadoop")
		commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no  -l root "+i+" rpm -q jdk")
		f=open("/tmp/core-site.xml","w")
		f.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://'+nnip+':9001</value>\n</property>\n</configuration>\n')
		f.close()
		commands.getstatusoutput("sshpass -p 12345 scp /tmp/core-site.xml -l root "+i+":/etc/hadoop")

		fo=open("/tmp/hdfs-site.xml","w ")
		fo.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>dfs.data.dir</name>\n<value>/aac</value>\n</property>\n</configuration>\n')
		fo.close()
		commands.getstatusoutput("sshpass -p 12345 scp /tmp/hdfs-site.xml -l root "+i+":/etc/hadoop")
		commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+i+" hadoop-daemon.sh stop jobtracker")
		commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+i+" hadoop-daemon.sh stop namenode")
		commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+i+" systemctl stop firewalld")
		commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+i+" setenforce 0")
		commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+i+" iptables -F")
		commands.getstatusoutput("sudo sshpass -p 12345 ssh -l root "+i+" hadoop-daemon.sh start datanode")
		print "<br>"		
		print commands.getstatusoutput("sudo sshpass -p 12345 ssh -l root "+i+" /usr/java/jdk1.7.0_79/bin/jps")
		
		f=open("/tmp/mapred-site.xml","w")
		f.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>mapred.job.tracker</name>\n<value>'+jtip+':9002</value>\n</property>\n</configuration>\n')
		f.close()
		commands.getstatusoutput("sshpass -p 12345 scp /tmp/mapred-site.xml -l root "+i+":/etc/hadoop")
		commands.getstatusoutput("sudo sshpass -p 12345 ssh -l root "+i+" hadoop-daemon.sh start tasktracker")
		print "<br>"
		print commands.getstatusoutput("sudo sshpass -p 12345 ssh -l root "+i+" /usr/java/jdk1.7.0_79/bin/jps")

print """<br><h3 style="color:#726B63;">Task Trackers and Datanodes successfully created!</h3>"""

print """<br><h2 style="color:#056303;">Your Cluster is ready!!!</h2>"""

print """ <html>
	<body>
	<form enctype="multipart/form-data" action="http://192.168.43.197/cgi-bin/fup.py" method="post">
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

