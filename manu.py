#!/usr/bin/python
print "Content-Type: text/html\n"

import commands,cgi

#print nnip
#print jtip
dict={}
l=()
form=cgi.FormContent()
cmd="nmap -n -sP -T5 192.168.43.0-255  |grep 'Nmap scan' |awk '{print $5}'"
ipout=commands.getstatusoutput(cmd)
if ipout[0]==0:
        iplist=ipout[1].split("\n")
        #print iplist
print """ <style> body{
background:#EEEBDA; }</style>"""
print """
<body><h1 style="color:#056303;">Creating Manual Cluster:</h1></body>
"""
fol=form['folder'][0]
nnip=form['nip'][0]
jtip=form['jip'][0]
fol1=form['fo1'][0]
fol2=form['fo2'][0]
fol3=form['fo3'][0]
fol4=form['fo4'][0]
#print "Enter IP of Namenode"
#nnip=raw_input()
#print "Enter folder name"
#fol=raw_input()
f=open("/tmp/fileupload.txt","w")
f.write(nnip)
f.close()
print """<h3 style="color:#726B63;">Creating Namenode:</h3>"""
commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+nnip+" rpm -q hadoop")
commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+nnip+" rpm -q jdk")
f=open("/tmp/core-site.xml","w+")
f.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://'+nnip+':9001</value>\n</property>\n</configuration>\n')
f.close()
commands.getstatusoutput("sshpass -p 12345 scp /tmp/core-site.xml -l root "+nnip+":/etc/hadoop")
fo=open("/tmp/hdfs-site.xml","w+")
fo.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>/'+fol+'</value>\n</property>\n</configuration>\n')
fo.close()
commands.getstatusoutput("sudo sshpass -p 12345 scp /tmp/hdfs-site.xml -l root "+nnip+":/etc/hadoop")
commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+nnip+" hadoop-daemon.sh stop jobtracker")
commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+nnip+" hadoop-daemon.sh stop datanode")
commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+nnip+" hadoop-daemon.sh stop tasktracker")
commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+nnip+" systemctl stop firewalld")
commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+nnip+" setenforce 0")
commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+nnip+" iptables -F")
commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+nnip+" hadoop namenode -format y")
commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+nnip+" hadoop-daemon.sh start namenode")
print "<br>"
print commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+nnip+" /usr/java/jdk1.7.0_79/bin/jps") 
print """<br><h3 style="color:#726B63;">Namenode successfully created!</h3>"""

print """<br><h3 style="color:#726B63;">Creating Jobtracker:</h3>"""
#print "Enter IP of Job Tracker"
#jtip=raw_input()
commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+jtip+" rpm -q hadoop")
commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+jtip+" rpm -q jdk")
commands.getstatusoutput("sudo sshpass -p 12345 scp /root/Desktop/mapred-site.xml -l root "+jtip+":/etc/hadoop")
f=open("/tmp/mapred-site.xml","w")
f.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>mapred.job.tracker</name> \n<value>'+jtip+':9002</value>\n</property>\n</configuration>\n')
f.close()
commands.getstatusoutput("sudo sshpass -p 12345 scp /tmp/mapred-site.xml -l root "+jtip+":/etc/hadoop")
f=open("/tmp/core-site.xml","w")
f.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs:'+nnip+':9001</value> \n</property>\n</configuration>\n')
f.close()
commands.getstatusoutput("sudo sshpass -p 12345 scp /tmp/core-site.xml -l root "+jtip+":/etc/hadoop")
commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+jtip+" systemctl stop firewalld")
commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+jtip+" setenforce 0")
commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+jtip+" iptables -F")
commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+jtip+" hadoop-daemon.sh stop datanode")
commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+jtip+" hadoop-daemon.sh stop namenode")
commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+jtip+" hadoop-daemon.sh start jobtracker")
commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+jtip+" hadoop-daemon.sh stop datanode")
print "\n"
print commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+jtip+" /usr/java/jdk1.7.0_79/bin/jps")
print """<br><br><h3 style="color:#726B63;">Job Tracker successfully created!</h3>"""

print """<br><br><h3 style="color:#726B63;">Creating Datanode and TaskTracker:</h3>"""

j=0
for i in iplist:
	if i==nnip or i==jtip or i=="192.168.43.1" or i=="192.168.43.250":
		pass
	else:
		#print "Enter folder name for Datanode:"
		#fold=raw_input()
		j=j+1
		print "<br>"
		print "Creating Datanode and Tasktracker for IP:"+i
		commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+i+" rpm -q hadoop")
		commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no  -l root "+i+" rpm -q jdk")
		commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+i+" hadoop-daemon.sh stop jobtracker")
		commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+i+" hadoop-daemon.sh stop namenode")
		f=open("/tmp/core-site.xml","w")
		f.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://'+nnip+':9001</value>\n</property>\n</configuration>\n')
		f.close()
		commands.getstatusoutput("sudo sshpass -p 12345 scp /tmp/core-site.xml -l root "+i+":/etc/hadoop")

		fo=open("/tmp/hdfs-site.xml","w ")
		fo.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>dfs.data.dir</name>\n<value>/'+fol+str(j)+'</value>\n</property>\n</configuration>\n')
		fo.close()
		commands.getstatusoutput("sudo sshpass -p 12345 scp /tmp/hdfs-site.xml -l root "+i+":/etc/hadoop")
		commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+i+" systemctl stop firewalld")
		commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+i+" setenforce 0")
		commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+i+" iptables -F")
		commands.getstatusoutput("sudo sshpass -p 12345 ssh -l root "+i+" hadoop-daemon.sh start datanode")
		commands.getstatusoutput("sudo sshpass -p 12345 ssh -l root "+i+" /usr/java/jdk1.7.0_79/bin/jps")
		f=open("/tmp/mapred-site.xml","w")
		f.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>mapred.job.tracker</name> \n<value>'+jtip+':9002</value>\n</property>\n</configuration>\n')
		f.close()
		commands.getstatusoutput("sudo sshpass -p 12345 scp /tmp/mapred-site.xml -l root "+i+":/etc/hadoop")
		commands.getstatusoutput("sudo sshpass -p 12345 ssh -l root "+i+" hadoop-daemon.sh start tasktracker")
		print "<br>\n"
		print commands.getstatusoutput("sudo sshpass -p 12345 ssh -l root "+i+" /usr/java/jdk1.7.0_79/bin/jps")
		print "<br>"
		
print """<br><h3 style="color:#726B63;">Datanodes and Task Trackers successfully created!</h3>"""	
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
fn=open("/tmp/fileup.txt","r+")
asl=fn.read()
#print asl
#commands.getstatusoutput("sudo sshpass -p 12345 ssh -o StrictHostKeyChecking=no -l root "+nnip+" hadoop fs -put /tmp/"+asl+" /")

