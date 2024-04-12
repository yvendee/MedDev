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

    // SQL query to select all data from the "grip_signup" table
    $select_query = "SELECT * FROM grip_signup";

    // Execute the SQL query
    $result = mysqli_query($connection, $select_query);

    if (mysqli_num_rows($result) > 0) {
        echo "<table border='1'>";
        echo "<tr><th>ID</th><th>Firstname</th><th>Lastname</th><th>Password</th></tr>";
        // Output data of each row
        while ($row = mysqli_fetch_assoc($result)) {
            echo "<tr>";
            echo "<td>" . $row["id"] . "</td>";
            echo "<td>" . $row["firstname"] . "</td>";
            echo "<td>" . $row["lastname"] . "</td>";
            echo "<td>" . $row["password"] . "</td>";
            echo "</tr>";
        }
        echo "</table>";
    } else {
        echo "No data found";
    }

    // Free result set
    mysqli_free_result($result);
    // Closing the connection
    mysqli_close($connection);
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}

?>
