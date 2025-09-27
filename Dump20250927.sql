-- MySQL dump 10.13  Distrib 8.0.43, for Win64 (x86_64)
--
-- Host: localhost    Database: schedule
-- ------------------------------------------------------
-- Server version	8.0.43

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `batch_courses`
--

DROP TABLE IF EXISTS `batch_courses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `batch_courses` (
  `cid` varchar(20) DEFAULT NULL,
  `cname` varchar(100) DEFAULT NULL,
  `pending` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `batch_courses`
--

LOCK TABLES `batch_courses` WRITE;
/*!40000 ALTER TABLE `batch_courses` DISABLE KEYS */;
/*!40000 ALTER TABLE `batch_courses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `branch`
--

DROP TABLE IF EXISTS `branch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `branch` (
  `bid` int NOT NULL,
  `bname` varchar(50) NOT NULL,
  `bseats` int DEFAULT NULL,
  `bstrength` int DEFAULT '0',
  `bcourses_s1` varchar(150) DEFAULT NULL,
  `bcourses_s2` varchar(150) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `branch`
--

LOCK TABLES `branch` WRITE;
/*!40000 ALTER TABLE `branch` DISABLE KEYS */;
INSERT INTO `branch` VALUES (101,'CSE',130,1,'ES2301-ICP,MA2301-Calculus','MA2302-Linear Alzebra,GS2301-IEVS'),(102,'ECE',120,1,'ES2301-ICP,MA2301-Calculus','MA2302-Linear Alzebra,GS2301-IEVS'),(103,'MECH',80,1,'ES2301-ICP,MA2301-Calculus','MA2302-Linear Alzebra,GS2301-IEVS'),(105,'PROD',80,1,'ES2301-ICP,MA2301-Calculus','MA2302-Linear Alzebra,GS2301-IEVS');
/*!40000 ALTER TABLE `branch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `classrooms`
--

DROP TABLE IF EXISTS `classrooms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `classrooms` (
  `room_id` varchar(30) NOT NULL,
  `capacity` int DEFAULT NULL,
  `occupied_slots` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classrooms`
--

LOCK TABLES `classrooms` WRITE;
/*!40000 ALTER TABLE `classrooms` DISABLE KEYS */;
INSERT INTO `classrooms` VALUES ('R101',80,NULL);
/*!40000 ALTER TABLE `classrooms` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cse`
--

DROP TABLE IF EXISTS `cse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cse` (
  `sid` int NOT NULL,
  `sname` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `sbranch` varchar(100) DEFAULT NULL,
  `semester` int DEFAULT NULL,
  `scourses` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cse`
--

LOCK TABLES `cse` WRITE;
/*!40000 ALTER TABLE `cse` DISABLE KEYS */;
INSERT INTO `cse` VALUES (101001,'UTKARSH','tJNgUOxo','CSE',1,'ES2301-ICP,MA2301-Calculus');
/*!40000 ALTER TABLE `cse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ece`
--

DROP TABLE IF EXISTS `ece`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ece` (
  `sid` int NOT NULL,
  `sname` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `sbranch` varchar(100) DEFAULT NULL,
  `semester` int DEFAULT NULL,
  `scourses` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ece`
--

LOCK TABLES `ece` WRITE;
/*!40000 ALTER TABLE `ece` DISABLE KEYS */;
INSERT INTO `ece` VALUES (102001,'DEEPENDER','EegSXfwN','ECE',1,'ES2301-ICP,MA2301-Calculus');
/*!40000 ALTER TABLE `ece` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `faculty`
--

DROP TABLE IF EXISTS `faculty`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `faculty` (
  `fid` varchar(20) NOT NULL,
  `fname` varchar(50) NOT NULL,
  `fcourse` varchar(150) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faculty`
--

LOCK TABLES `faculty` WRITE;
/*!40000 ALTER TABLE `faculty` DISABLE KEYS */;
INSERT INTO `faculty` VALUES ('MA001','NITIN RAJBHAR','MA2301','nT46c0mD'),('MA002','VEDANG','ES2301','BvPk0Msj'),('PY001','ADITYA','MA2302','IQPh60Vm');
/*!40000 ALTER TABLE `faculty` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mech`
--

DROP TABLE IF EXISTS `mech`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mech` (
  `sid` int NOT NULL,
  `sname` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `sbranch` varchar(100) DEFAULT NULL,
  `semester` int DEFAULT NULL,
  `scourses` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mech`
--

LOCK TABLES `mech` WRITE;
/*!40000 ALTER TABLE `mech` DISABLE KEYS */;
INSERT INTO `mech` VALUES (103001,'Arnoy','uEWOZ4wz','MECH',1,'ES2301-ICP,MA2301-Calculus');
/*!40000 ALTER TABLE `mech` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prod`
--

DROP TABLE IF EXISTS `prod`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prod` (
  `sid` int NOT NULL,
  `sname` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `sbranch` varchar(100) DEFAULT NULL,
  `semester` int DEFAULT NULL,
  `scourses` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prod`
--

LOCK TABLES `prod` WRITE;
/*!40000 ALTER TABLE `prod` DISABLE KEYS */;
INSERT INTO `prod` VALUES (105001,'DEEPENDER','CGhSAmkf','PROD',1,'ES2301-ICP,MA2301-Calculus');
/*!40000 ALTER TABLE `prod` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schedule`
--

DROP TABLE IF EXISTS `schedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `schedule` (
  `days` varchar(20) DEFAULT NULL,
  `1` varchar(200) DEFAULT NULL,
  `2` varchar(200) DEFAULT NULL,
  `3` varchar(200) DEFAULT NULL,
  `4` varchar(200) DEFAULT NULL,
  `Lunch` varchar(50) DEFAULT NULL,
  `5` varchar(200) DEFAULT NULL,
  `6` varchar(200) DEFAULT NULL,
  `7` varchar(200) DEFAULT NULL,
  `8` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schedule`
--

LOCK TABLES `schedule` WRITE;
/*!40000 ALTER TABLE `schedule` DISABLE KEYS */;
INSERT INTO `schedule` VALUES ('Monday',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('Tuesday',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('Wednesday',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('Thursday',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('Friday',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('Saturday',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `schedule` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-09-27 14:08:56
