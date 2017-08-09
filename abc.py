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



a {
	color: #056303;
}


#wrapper {
	background: url(img.jpg) no-repeat top ;
	background-size: 495px 500px;
	
	 
	
}

.container {
	width: 1000px;
	margin: 0px auto;
}

/* Header */

#header {
	height: 100px;
	width:100%;
	border:6px;
	 color:blue;
	
}

/* Logo */

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

/* Menu */

#menu {
	

}

#menu ul {
	float: left;
	margin: 0;
	padding: -30px 200px 20px 0px;
	list-style: none;
	line-height: normal;
	
}

#menu li {
	float: left;
	list-spacing:30px;
	padding-bottom:50px;
	
}

#menu a {
	display: block;
	height: 20px;
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

#menu .current_page_item a {

}

/* Page */

#page {
	width: 940px;
	margin: 0px auto;
	padding: 30px 0px;
}

/* Content */

#content {
	float: right;
	width: 592px;
	padding: 0px 30px;
	font-size:100%;
}
.entry{
	
}

/* Sidebar */

#sidebar {
	float: left;
	width: 288px;
	margin: 0px;
	color: #726B63;
		
}
#sidebar p {
padding-left:70px;
font-size:200%;
padding-bottom:20px;
}

#sidebar form input{
    color:#056303;
	width: 170px;
	border-radius: 4px;
    height: 35px;
    
}

#sidebar form placeholder{
font-size:50px;
}
#sidebar form button {
	-webkit-transition-duration: 0.4s; 
    transition-duration: 0.4s;
    border-radius: 4px;
    background-color: #4CAF50;
  left:70px;
   position:relative;
    
}
#sidebar form button:hover{
	background-color: #4CAF50;
    color: white;
    box-shadow: 10px 10px 10px lightgreen;
}
/* Footer */

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
<link href="style.css" rel="stylesheet" type="text/css" media="all" />
<title>My site</title>
<body>
<div id="wrapper">
	<div id="wrapper2">
		<div id="header" class="container">
			<div id="logo">
				<h1><a href="abc.html">Big Data&nbsp;<span>Hadoop</span></a></h1>
			</div>
			<div id="menu">
				<ul style="float:right;
	
	height: 100px;
	padding-bottom:90px;position:absolute;top:50px;right:70px;">
					<li class="current_page_item"><a href="">Home</a></li>
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
					<h2 class="title"><a href="#">Welcome to Hadoop!</a></h2>
					<div style="clear: both;">&nbsp;</div>
					<div class="entry">
						<p></p>
						<p></p>
											</div>
				</div>
				<div class="post">
					
					<p></p>
					<div style="clear: both;">&nbsp;</div>
					<div class="entry">
						<p></p>
					</div>
				</div>
				<div class="post">
					
					<p></p>
					<div style="clear: both;">&nbsp;</div>
					<div class="entry">
					
						<p><img src="hadoop.png" alt="Mountain View" style="width:350px;
	height:278px;
	padding-left:80px;
     "></p>
					</div>
				</div>
				<div style="clear: both;">&nbsp;</div>
			</div>
			<!-- end #content -->
			<div id="sidebar">
				<p>Login Here!</p>
				<form>
				<p>Username<input type="text" name="login" value="" placeholder="Username"></p>
        <p>Password<input type="password" name="password" value="" placeholder="Password"></p>
        <button type="button">Login</button>
        <button type="reset" value"reset">Reset</button>
				</form>
				
			</div>
			<!-- end #sidebar -->
			<div style="clear: both;">&nbsp;</div>
		</div>
		<!-- end #page -->
		<div id="footer">
			<p></p>
		</div>
	</div>
</div>
<!-- end #footer -->
</body>
</html>
