<?php
$q = $_GET['q'];

echo "hmm"

$con = mysqli_connect('34.122.13.220','root','Violentwinds212!','your_love');

if (!$con) {
  die('Could not connect: ' . mysqli_error($con));
}

$sql="SELECT * FROM user WHERE id = '".$q."'";
$result = mysqli_query($con,$sql);


echo "<script>console.log("Logged in")<script\>"
//     fwrite($file, $Name);
//     fwrite($file, $Phone);
//     fwrite($file, $IG);
//     fwrite($file, $One);
//     fwrite($file, $Two);
//     fclose($file);
?>