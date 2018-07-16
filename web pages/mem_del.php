<?php include('log_details.php');?>
<html>
	<head>
		<title>Delete Members</title>
		<style>
			center{font-size:28px;font-weight:bold;text-decoration:underline;padding:10px 0 10px 0;}
			ul{list-style-type: none;}
			li{margin-top:8px;}
		</style>
	</head>
	<body>
		<center>Delete Members</center>
		<?php
			include('db.php');
			// Create connection
			$conn = new mysqli($servername, $username, $password, $dbname);
			// Check connection
			if ($conn->connect_error)
			{
				die("Connection failed: " . $conn->connect_error);
			}
			if(isset($_POST['memb']))
			{
				$id=$_POST['memb'];
				$rec=0;
			}
			else
			{
				echo "<script>alert('none of element selected');history.go(-1);</script>";
				exit;
			}
			foreach($id as $key=>$values)
			{
				$sql="delete from members where id=$key";
				$conn->query($sql);
				if(mysqli_affected_rows($conn)>0)
				{
					$rec++;
				}
				//echo mysqli_affected_rows($conn);
			}
			echo "<script>alert('$rec record deleted');history.go(-1);</script>";
			$conn->close();
		?>
	</body>
</html>

