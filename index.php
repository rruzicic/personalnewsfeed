<?php
	include_once 'mysql-connect.php';
?>
<html lang="en">
<head>
	<!-- Required meta tags -->
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <title>Vesti</title>
</head>
<body>
	<div class="container-fluid">
	<div class="row">
		<div class='col'>
			<table class="table">
			<thead>
			<tr>
				<th scope="col">Portal</th>
				<th scope="col">Naslov</th>
				<th scope="col">Isečak</th>
				<th scope="col">Datum</th>
			</tr>
			</thead>
			<tbody>
			<?php
			$sql = "SELECT * FROM articles;";
			mysqli_query ($conn, "SET NAMES 'utf8' COLLATE 'utf8_unicode_ci';");
			$result = mysqli_query($conn, $sql);
			$result_check = mysqli_num_rows($result);
			
				if($result_check > 0){
				while( $row = mysqli_fetch_assoc($result)){
					echo "<tr>
					<td>" . $row['agency'] . "</td>
					<td><a href='" . $row['link'] . "' target='_blank' >" . $row['title'] . "</title></td>
					<td>" . $row['summary'] . "</td>
					<td>" . $row['date'] . "</td>
					</tr>";
					}
				}
			?>
			</tbody>
			</table>
		<!--</div>
		
		<div class="col">

		<iframe src="" id="myIframe" scrolling="no" frameborder="0" style="position: relative; height: 100%; width: 100%;">
		</iframe>
		
		</div>
		-->
	</div>
	</div>
</body>
</html>