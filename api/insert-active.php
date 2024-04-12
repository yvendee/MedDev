<?php

$host = "localhost";
$user = "root";
$password = "";
$database = "gripdespro";

try {
    // Establishing the connection to MySQL
    $connection = mysqli_connect($host, $user, $password, $database);

    if (!$connection) {
        die("Connection failed: " . mysqli_connect_error());
    }

    // Sample data to insert
    $role = "admin";
    $ptname = "";
    $status = "inactive";

    // SQL query to insert data into the "grip_active" table
    $insert_query = "
    INSERT INTO grip_active (role, ptname, status)
    VALUES ('$role', '$ptname', '$status')
    ";

    // Execute the SQL query
    if (mysqli_query($connection, $insert_query)) {
        echo "Data inserted successfully!";
    } else {
        echo "Error inserting data: " . mysqli_error($connection);
    }

    // Closing the connection
    mysqli_close($connection);
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}

?>
