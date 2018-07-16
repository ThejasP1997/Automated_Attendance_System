<?php include('log_details.php');?>
<html>
	<head>
		<title>Membrs</title>
		<style>
			center{font-size:28px;font-weight:bold;text-decoration:underline;padding:10px 0 10px 0;}
			ul{list-style-type: none;}
			li{margin-top:8px;}
			table *{border:solid silver 1px;}
		</style>
	</head>
	<body>
		<center>Members</center>
		<p><b>Note:</b>You need to first delete the record in logs,because members id is reffered</p>
		<?php
			include('db.php');
			// Create connection
			$conn = new mysqli($servername, $username, $password, $dbname);
			// Check connection
			if ($conn->connect_error)
			{
				die("Connection failed: " . $conn->connect_error);
			}
			$sql="select * from members";
			$conn->query($sql);
			$res=$conn->query($sql);
			if ($res->num_rows > 0) 
			{
				echo "<form action='mem_del.php' method='post'>
				<table>
					<tr><th>Name</th><th>User ID</th><th>Path to image file</th><th></th></tr>";
				while($row = $res->fetch_assoc()) 
				{
					$name=$row['name'];
					$uid=$row['id'];
					$path=$row['path'];
					echo "<tr><td>$name</td><td>$uid</td><td>$path</td>
					<td><input type='checkbox' name='memb[$uid]' value='del' />delete</td></tr>";
				}
				echo "</tr></table><br />
				<input type='submit' value='Delete marked' />
				</form>";
			}
			$conn->close();
		?>
	</body>
</html>

