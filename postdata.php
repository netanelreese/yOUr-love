<?php
echo "step1"

$con = mysql_connect('34.122.13.220','root','Violentwinds212!');
print "step2"
$sql=("INSERT INTO user_data (name, phone, insta, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20) VALUES ( 'Aaron Pierce', '+14053250566', '@aaron', 4, 5, 5, 4, 5, 1, 2, 4, 3, 1, 2, 5, 3, 5, 4, 2, 5, 1, 1, 1);
;");
print "step 3"
if (!$con) {
  die('Could not connect: ' . mysqli_error($con));
}
print "step 4"
$set = "USE your_love";

mysql_query($set, $con);

mysql_query($sql, $con);
?>
