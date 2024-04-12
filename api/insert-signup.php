<?php

$host = "localhost";
$user = "root";
$password_db = "";
$database = "gripdespro";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $firstname = $_POST["firstname"];
    $lastname = $_POST["lastname"];
    $password = $_POST["password"];

    // Establishing the connection to MySQL
    $connection = mysqli_connect($host, $user, $password_db, $database);

    if (!$connection) {
        die("Connection failed: " . mysqli_connect_error());
    }

    try {
        // SQL query to insert data into the "grip_signup" table
        $insert_query = "
        INSERT INTO grip_signup (firstname, lastname, password) 
        VALUES ('$firstname', '$lastname', '$password')
        ";

        // Execute the SQL query
        if (mysqli_query($connection, $insert_query)) {
            echo "Data inserted successfully!";
        } else {
            echo "Error: " . mysqli_error($connection);
        }
    } catch (Exception $e) {
        echo "Error: " . $e->getMessage();
    } finally {
        // Closing the connection
        mysqli_close($connection);
    }
}

?>
