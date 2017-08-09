#!/usr/bin/python
print "content-type:text/html\n" 

import cgi
import commands,os

print """
<!doctype html>
<html>
<head>
<style>

body {
	margin: 0;
	padding: 0;
	background: #EEEBDA; 
	 box-sizing: border-box;
	font-family: Arial, Helvetica, sans-serif;
	font-size: 14px;
	color: #4D4D4D;
}

h1, h2, h3 {
	margin: 0;
	padding: 0;
	font-weight: normal;
	font-family: 'Arvo', serif;
	color: #056303;
}

"""
print """

h1 {
	font-size: 2em;
}

h2 {
	font-size: 2.8em;
}

h3 {
	font-size: 1.6em;
}

p, ul, ol {
	margin-top: 0;
	line-height: 240%;
}


"""
print """

a {
	color: #056303;
}


#wrapper {
	background: url(img.jpg) no-repeat top  ;
	background-size: 495px 500px;
}

.container {
	width: 1000px;
	margin: 0px auto;
}
"""
print """

/* Header */

#header {
	height: 100px;
	width:100%;
	border:6px;
	 color:blue;
	
}

#btn {
    -webkit-transition-duration: 0.4s; 
    transition-duration: 0.4s;
    border-radius: 4px;
    background-color: #4CAF50;
  left:30px;
   position:relative;
    
}
#btn:hover{
background-color: #4CAF50;
    color: white;
    box-shadow: 10px 10px 10px lightgreen;
} """
print """


#logo {
	float: left;
	width: 288px;
	height: 100px;
	padding-left:125px;
	color: #FFFFFF;
	padding-right:90px;
}



#logo h1 {
	padding: 30px 20px 6px 2px;
	letter-spacing: -3px;
	text-align: center;
	font-size: 40px;
	padding-right:200px;	
}

#logo h1 span {
	color: #8AD500;
	
}

#logo h1 a {
	color: #FFFFFF;
	
	
}
#logo a:hover{
	text-shadow: 0 0 8px #AAF861;
	box-shadow: 10px 10px 10px lightgreen;

}


#logo a {
    border:30px;
    
    
	}
"""
print """

/* Menu */

#menu {
	
}

#menu ul {
	float: left;
	margin: 0;
	
	top:900px;
	list-style:none;
}

#menu li {
	f
loat: left;
	top:900px;
	
	
}

#menu a {
	
	
	margin-right: 40px;
	text-align: right;
	text-transform: uppercase;
	font-family: 'Arvo', serif;
	font-size: 20px;
	font-weight: normal;
	color: white;
	float:center;
	
}

#menu a:hover {
	text-shadow: 0 0 8px #AAF861;
	box-shadow: 10px 10px 10px lightgreen;
	
}




#page {
	width:940px;
	margin: 0px auto;
	padding: 30px 0px;
}



#content {
	float: right;
	width:542px;
	font-size:100%;
}
.entry{
	
}




#footer {
	width: 940px;
	margin: 0px auto;
	padding: 20px 0px;
	background: #3D3630;
	color: #949085;
}

#footer p {
	margin: 0;
	line-height: normal;
	letter-spacing: 2px;
	text-align: center;
	text-decoration: none;
	text-align: center;
	text-transform: uppercase;
	font-family: 'Arvo', serif;
	font-weight: normal;
	font-size: 10px;
}

#footer a {
	color: #949085;
}

#banner {
	width: 940px;
	margin: 0px auto;
	height: 150px;
}
</style>
</head>
"""


print """
<title>My site</title>
<body>
<div id="wrapper">
	<div id="wrapper2">
		<div id="header" class="container">
			<div id="logo">
				<h1><a href="#"> Big Data&nbsp;<span>Hadoop</span></a></h1>
			</div>
			<div id="menu">
				<ul style="float:right;
	
	height: 100px;
	padding-bottom:90px;position:absolute;top:50px;right:70px;">
					<li><a href="abc.html">Home</a></li>
					
					<li><a href="manual.html">Manual</a></li>
					<li><a href="auto.html">Automatic</a></li><li>
					<a href="demand.html">On Demand</a></li>
					
					
				</ul>
			</div>
		</div>
		<div id="banner"></div>
		<!-- end #header -->
		<div id="page">
			<div id="content">
				<div class="post">
					<h2 class="title"><a href="#"></a>Manual Cluster</h2>
					<div style="clear: both;">&nbsp;</div>
					<div class="entry">
						<br><p><br>
							
							</ul>
						<p>
                                           <form action="http://192.168.43.197/cgi-bin/manu.py" >
						Enter IP of Namenode:<br>
						<input type="text" name=nip><br>
						Enter Folder name for Namenode:<br>
						<input type="text" name=folder><br>

						Enter IP of Job Tracker:<br>
						<input type="text" name=jip><br>

						Shared Folder for Datanode:<br>
						<input type="text" name=fo1><br>
						<input type="text" name=fo2><br>
						<input type="text" name=fo3><br>
						<input type="text" name=fo4><br>
						<br> 
						<input id="btn" type="submit" value="Submit">
						<input id="btn" type="reset" value="Reset">
						</form>
                                                </p>
											</div>
				</div>
				<div class="post">
					<h2 class="title"><a href="#"></a></h2>
					<div style="clear: both;">&nbsp;</div>
					<div class="entry">
						<p></p>
					</div>
				</div>
				<div class="post">
					<h2 class="title"><a href="#"> </a></h2>
					<div style="clear: both;">&nbsp;</div>
					<div class="entry">
						<p></p>
					</div>
				</div>
				<div style="clear: both;">&nbsp;</div>
			</div>
			<!-- end #content -->
			<div id="sidebar">
				
			</div>
			<!-- end #sidebar -->
			<div style="clear: both;">&nbsp;</div>
		</div>
		<!-- end #page -->
		<div id="footer">
			<p></p>
		</div>
	</div>
</html> """
