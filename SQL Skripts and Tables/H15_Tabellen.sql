CREATE DATABASE  IF NOT EXISTS `h15`;
USE `h15`;
-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: h15
-- ------------------------------------------------------
-- Server version	8.0.19

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
-- Table structure for table `abrechnung`
--

DROP TABLE IF EXISTS `abrechnung`;
CREATE TABLE `abrechnung` (
  `username` varchar(30) DEFAULT NULL,
  `machine` varchar(30) DEFAULT NULL,
  `Strom_von` int DEFAULT NULL,
  `Strom_bist` int DEFAULT NULL,
  FULLTEXT(machine)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `abrechnung`
--

LOCK TABLES `abrechnung` WRITE;
/*!40000 ALTER TABLE `abrechnung` DISABLE KEYS */;
INSERT INTO `abrechnung` VALUES ('testus','Altbau',234, 235),('testus','Altbau',235, 237),('testus','Altbau',237, 239),('testus','Altbau',239, 245),('agfsd','Rechte_Maschine',3000, 3003);
/*!40000 ALTER TABLE `abrechnung` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `benutzer`
--

DROP TABLE IF EXISTS `benutzer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `benutzer` (
  `id` int DEFAULT NULL,
  `vorname` varchar(30) DEFAULT NULL,
  `nachname` varchar(30) DEFAULT NULL,
  `passwort` varchar(30) DEFAULT NULL,
  `username` varchar(30) DEFAULT NULL,
  `etage` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `benutzer`
--

LOCK TABLES `benutzer` WRITE;
/*!40000 ALTER TABLE `benutzer` DISABLE KEYS */;
INSERT INTO `benutzer` VALUES (3,'tst','nachn','lol','testus',NULL),(6,'ly','asfvv','sfg','agfsd','1'),(4,'eshat','funktioniert','lolol','imatest','33'),(7,'maxi','faxi','lolol','imasecond gtest','5'),(4,'mister','green','pw','doppelnässchen','33');
/*!40000 ALTER TABLE `benutzer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `strom`
--

DROP TABLE IF EXISTS `strom`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `strom` (
  `Waschmachine` varchar(30) DEFAULT NULL,
  `Kwh` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `strom`
--

LOCK TABLES `strom` WRITE;
/*!40000 ALTER TABLE `strom` DISABLE KEYS */;
INSERT INTO `strom` VALUES ('Altbau',245),('Linke_Maschine',20000),('Mittlere_Maschine',40000),('Rechte_Maschine',3003),('Trockner_Oben',50000),('Trockner_Unten',60000);
/*!40000 ALTER TABLE `strom` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-04-16 18:42:15
