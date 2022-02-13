<?php
$q = $_GET['q'];

echo "$q";

$Name = "Username:".$_POST['name']."
    ";
    $Phone = "Phone:".$_POST['phone']."
    ";
    $ig = "IG:".$_POST['ig']."
    ";
    $One = "One:".$_POST['one']."
    ";
    $Two = "Two:".$_POST['two']."
    ";

    $file=fopen("saved.txt", "w");
//     fwrite($file, $Name);
//     fwrite($file, $Phone);
//     fwrite($file, $IG);
//     fwrite($file, $One);
//     fwrite($file, $Two);
//     fclose($file);
?>