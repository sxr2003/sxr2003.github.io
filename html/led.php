<?php
    $LED=$_GET["led"];

    
    file_put_contents("led.txt","$LED");
    echo $LED
?>