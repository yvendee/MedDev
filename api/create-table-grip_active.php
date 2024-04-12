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

    // SQL query to create a new table "grip_active"
    $create_table_query = "
    CREATE TABLE grip_active (
        role VARCHAR(255),
        ptname VARCHAR(255),
        status VARCHAR(255)
    )
    ";

    // Execute the SQL query
    if (mysqli_query($connection, $create_table_query)) {
        echo "Table 'grip_active' created successfully!";
    } else {
        echo "Error creating table: " . mysqli_error($connection);
    }

    // Closing the connection
    mysqli_close($connection);
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}

?>
