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
-- Table structure for table `archive_session`
--

DROP TABLE IF EXISTS `archive_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `archive_session` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pt` text DEFAULT NULL,
  `firstname` text DEFAULT NULL,
  `lastname` text DEFAULT NULL,
  `date` text DEFAULT NULL,
  `hand` text DEFAULT NULL,
  `f1` text DEFAULT NULL,
  `f2` text DEFAULT NULL,
  `f3` text DEFAULT NULL,
  `f4` text DEFAULT NULL,
  `f5` text DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `archive_session`
--

LOCK TABLES `archive_session` WRITE;
/*!40000 ALTER TABLE `archive_session` DISABLE KEYS */;
INSERT INTO `archive_session` VALUES (1,'helloworld','john','dee','2024-04-16','Left','10','20','30','40','50'),(2,'helloworld','john','dee','2024-04-16','Right','10','20','30','40','50'),(3,'helloworld','john','dee','2024-04-16','Left','10','20','30','40','50'),(4,'helloworld','john','dee','2024-04-16','Right','10','20','30','40','50'),(5,'helloworld','sarah','dee','2024-04-16','Left','10','20','30','40','50'),(6,'helloworld','sarah','dee','2024-04-16','Right','10','20','30','40','50'),(7,'helloworld','sarah','dee','2024-04-16','Left','10','20','30','40','50'),(8,'helloworld','sarah','dee','2024-04-16','Right','10','20','30','40','50'),(9,'helloworld','alice','stewart','2024-04-16','Left','10','20','30','40','50'),(10,'helloworld','john','dee','2024-04-16','Left','10','20','30','40','50'),(11,'helloworld','john','dee','2024-04-16','Right','10','20','30','40','50');
/*!40000 ALTER TABLE `archive_session` ENABLE KEYS */;
UNLOCK TABLES;

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
INSERT INTO `grip_active` VALUES ('Admin','hello','world','1');
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grip_signup`
--

LOCK TABLES `grip_signup` WRITE;
/*!40000 ALTER TABLE `grip_signup` DISABLE KEYS */;
INSERT INTO `grip_signup` VALUES (1,'hello','world','test'),(2,'hello100','world100','test100');
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient_active`
--

LOCK TABLES `patient_active` WRITE;
/*!40000 ALTER TABLE `patient_active` DISABLE KEYS */;
INSERT INTO `patient_active` VALUES (1,'helloworld','john','dee');
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient_details`
--

LOCK TABLES `patient_details` WRITE;
/*!40000 ALTER TABLE `patient_details` DISABLE KEYS */;
INSERT INTO `patient_details` VALUES (1,'helloworld','john','dee','30','24/17/4','6','2024-04-16','Active',NULL),(2,'helloworld','sarah','dee','20','24/9/4','4','2024-04-16','Active',NULL),(3,'helloworld','alice','stewart','30','24/9/4','1','2024-04-16','Active',NULL);
/*!40000 ALTER TABLE `patient_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `session_active`
--

DROP TABLE IF EXISTS `session_active`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `session_active` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pt` text DEFAULT NULL,
  `firstname` text DEFAULT NULL,
  `lastname` text DEFAULT NULL,
  `current_session` text DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `session_active`
--

LOCK TABLES `session_active` WRITE;
/*!40000 ALTER TABLE `session_active` DISABLE KEYS */;
INSERT INTO `session_active` VALUES (1,'helloworld','john','dee','Session6');
/*!40000 ALTER TABLE `session_active` ENABLE KEYS */;
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
  `date` text DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `session_details`
--

LOCK TABLES `session_details` WRITE;
/*!40000 ALTER TABLE `session_details` DISABLE KEYS */;
INSERT INTO `session_details` VALUES (1,'helloworld','john','dee','Session1','100','100','100','100','100','60','70','80','90','10','2024-04-16'),(2,'helloworld','john','dee','Session2','100','100','100','100','100','60','70','80','90','10','2024-04-16'),(3,'helloworld','john','dee','Session3','1','2','3','4','5','6','7','8','9','10','2024-04-16'),(4,'helloworld','john','dee','Session4','1','2','3','4','5','6','7','8','9','10','2024-04-16'),(5,'helloworld','sarah','dee','Session1','1','2','3','4','5','6','7','8','9','10','2024-04-16'),(6,'helloworld','sarah','dee','Session2','1','2','3','4','5','6','7','8','9','10','2024-04-16'),(7,'helloworld','sarah','dee','Session3','1','2','3','4','5','6','7','8','9','10','2024-04-16'),(8,'helloworld','sarah','dee','Session4','1','2','3','4','5','6','7','8','9','10','2024-04-16'),(9,'helloworld','alice','stewart','Session1','1','2','3','4','5','6','7','8','9','10','2024-04-16'),(10,'helloworld','john','dee','Session5','100','100','100','100','100','6','7','8','9','10','2024-04-16'),(11,'helloworld','john','dee','Session6','100','100','100','100','100','6','7','8','9','10','2024-04-16');
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

-- Dump completed on 2024-04-16 14:56:23
