-- MariaDB dump 10.19  Distrib 10.4.32-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: gripdespro
-- ------------------------------------------------------
-- Server version	10.4.32-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `grip_active`
--

DROP TABLE IF EXISTS `grip_active`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `grip_active` (
  `role` varchar(255) DEFAULT NULL,
  `ptname` varchar(255) DEFAULT NULL,
  `ptlastname` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grip_active`
--

LOCK TABLES `grip_active` WRITE;
/*!40000 ALTER TABLE `grip_active` DISABLE KEYS */;
INSERT INTO `grip_active` VALUES ('admin','hello','world','1');
/*!40000 ALTER TABLE `grip_active` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grip_signup`
--

DROP TABLE IF EXISTS `grip_signup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `grip_signup` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `firstname` text DEFAULT NULL,
  `lastname` text DEFAULT NULL,
  `password` text DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grip_signup`
--

LOCK TABLES `grip_signup` WRITE;
/*!40000 ALTER TABLE `grip_signup` DISABLE KEYS */;
INSERT INTO `grip_signup` VALUES (1,'hello','world','test'),(2,'hello1','world1','test1'),(3,'hello2','world2','test2'),(4,'hello4','hello4','test4'),(5,'hello4','hello4','test4'),(6,'asdasd','fdafs','1234'),(7,'','',''),(8,'hello7','world7','test7'),(9,'hello8','world8','test8'),(10,'hello10','world10','test10'),(11,'John','Doe','password123'),(12,'John','Doe','password123'),(13,'hello10','world10','test10');
/*!40000 ALTER TABLE `grip_signup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patient_active`
--

DROP TABLE IF EXISTS `patient_active`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `patient_active` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pt` varchar(255) DEFAULT NULL,
  `firstname` varchar(255) DEFAULT NULL,
  `lastname` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient_active`
--

LOCK TABLES `patient_active` WRITE;
/*!40000 ALTER TABLE `patient_active` DISABLE KEYS */;
INSERT INTO `patient_active` VALUES (1,'helloworld','sarah','dee'),(2,'helloworldx','john','dee');
/*!40000 ALTER TABLE `patient_active` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patient_details`
--

DROP TABLE IF EXISTS `patient_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `patient_details` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pt` text DEFAULT NULL,
  `firstname` text DEFAULT NULL,
  `lastname` text DEFAULT NULL,
  `age` text DEFAULT NULL,
  `startoftherapy` text DEFAULT NULL,
  `totalsession` text DEFAULT NULL,
  `lastsession` text DEFAULT NULL,
  `status` text DEFAULT NULL,
  `physician` text DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient_details`
--

LOCK TABLES `patient_details` WRITE;
/*!40000 ALTER TABLE `patient_details` DISABLE KEYS */;
INSERT INTO `patient_details` VALUES (1,'helloworld','joe','dee','40','4321',NULL,NULL,NULL,NULL),(2,'helloworld','john','dee','31','1234',NULL,NULL,NULL,NULL),(3,'helloworld','sarah','dee','32','1234',NULL,NULL,NULL,NULL),(4,'helloworld','alice','alison','29','1234',NULL,NULL,NULL,NULL),(5,'helloworld','','','','',NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `patient_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `session_details`
--

DROP TABLE IF EXISTS `session_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `session_details` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pt` text DEFAULT NULL,
  `firstname` text DEFAULT NULL,
  `lastname` text DEFAULT NULL,
  `session_number` text DEFAULT NULL,
  `l1` text DEFAULT NULL,
  `l2` text DEFAULT NULL,
  `l3` text DEFAULT NULL,
  `l4` text DEFAULT NULL,
  `l5` text DEFAULT NULL,
  `r1` text DEFAULT NULL,
  `r2` text DEFAULT NULL,
  `r3` text DEFAULT NULL,
  `r4` text DEFAULT NULL,
  `r5` text DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `session_details`
--

LOCK TABLES `session_details` WRITE;
/*!40000 ALTER TABLE `session_details` DISABLE KEYS */;
INSERT INTO `session_details` VALUES (1,'helloworld','john','dee','Session1','5','10','15','20','25','30','35','40','50','60');
/*!40000 ALTER TABLE `session_details` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-13  0:47:46
