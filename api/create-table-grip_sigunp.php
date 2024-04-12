<?php

$host = "localhost";
$user = "root";
$password = "";
$database = "gripdespro";

// Establishing the connection to MySQL
$connection = mysqli_connect($host, $user, $password, $database);

if (!$connection) {
    die("Connection failed: " . mysqli_connect_error());
}

try {
    // SQL query to create a table named "grip_signup" with TEXT data type for columns
    $create_table_query = "
    CREATE TABLE grip_signup (
        id INT AUTO_INCREMENT PRIMARY KEY,
        firstname TEXT,
        lastname TEXT,
        password TEXT
    )
    ";

    // Execute the SQL query
    if (mysqli_query($connection, $create_table_query)) {
        echo "Table 'grip_signup' created successfully!";
    } else {
        echo "Error creating table: " . mysqli_error($connection);
    }
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
} finally {
    // Closing the connection
    mysqli_close($connection);
}

?>
