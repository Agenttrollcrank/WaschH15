CREATE DATABASE  IF NOT EXISTS `h15` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
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
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `benutzer`
--

DROP TABLE IF EXISTS benutzer;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE benutzer (
  id int DEFAULT NULL,
  vorname varchar(30) DEFAULT NULL,
  nachname varchar(30) DEFAULT NULL,
  zimmernummer int DEFAULT NULL,
  passwort varchar(30) DEFAULT NULL,
  Username varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `benutzer`
--

INSERT INTO benutzer VALUES (1,'Max','Mustermann',1,'1234',NULL);
INSERT INTO benutzer VALUES (2,'Peter','Ludolf',2,'passwort',NULL);
INSERT INTO benutzer VALUES (1,'Max','Mustermann',1,'1234',NULL);
INSERT INTO benutzer VALUES (2,'Peter','Ludolf',2,'passwort',NULL);

--
-- Table structure for table `strom`
--

DROP TABLE IF EXISTS strom;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE strom (
  Waschmachine varchar(30) DEFAULT NULL,
  Kwh int DEFAULT NULL,
  Kwh_vor int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `strom`
--

INSERT INTO strom VALUES ('Altbau',80000,NULL);
INSERT INTO strom VALUES ('Linke_Maschine',80000,NULL);
INSERT INTO strom VALUES ('Mittlere_Maschine',80000,NULL);
INSERT INTO strom VALUES ('Rechte_Maschine',80000,NULL);
INSERT INTO strom VALUES ('Trockner_Oben',80000,NULL);
INSERT INTO strom VALUES ('Trockner_Unten',80000,NULL);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed