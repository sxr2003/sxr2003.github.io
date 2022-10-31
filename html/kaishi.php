<?php
    $TF=$_GET["TF"];

    
    file_put_contents("kaishi.txt","$TF");
    echo $TF;
?>