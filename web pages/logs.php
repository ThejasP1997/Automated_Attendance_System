<?php include('log_details.php');?>
<html>
	<head>
		<title>Logs</title>
		<style>
			center{font-size:28px;font-weight:bold;text-decoration:underline;padding:10px 0 10px 0;}
			ul{list-style-type: none;}
			li{margin-top:8px;}
			table *{border:solid silver 1px;}
		</style>
	</head>
	<body>
		<center>LOGS</center>
		<p><b>NOte:</b> Delete both login &amp logout record for selected User ID</p> 
		<?php
			include('db.php');
			// Create connection
			$conn = new mysqli($servername, $username, $password, $dbname);
			// Check connection
			if ($conn->connect_error)
			{
				die("Connection failed: " . $conn->connect_error);
			}
			$sql="select * from logs";
			$conn->query($sql);
			$res=$conn->query($sql);
			if ($res->num_rows > 0) 
			{
				echo "<form action='log_del.php' method='post'>
				<table>
					<tr><th>User ID</th><th>Date</th><th>Time</th><th>Logs</th><th></th></tr>";
				while($row = $res->fetch_assoc()) 
				{
					$uid=$row['id'];
					$date=$row['date'];
					$time=$row['time'];
					$log=$row['log'];
					echo "<tr><td>$uid</td><td>$date</td><td>$time</td><td>$log</td>
					<td><input type='checkbox' name='log[$uid]' value='del' />delete</td></tr>";
				}
				echo "</tr></table><br />
				<input type='submit' value='Delete marked' />
				</form>";
			}
			$conn->close();
		?>
	</body>
</html>

