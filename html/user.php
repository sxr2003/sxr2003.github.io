<?php
    $user=$_GET["user"];
    $pass=$_GET["pass"];
    
    file_put_contents("user.json","{\"user\":\"$user\",\"pass\":\"$pass\"}");
    echo $user
?>