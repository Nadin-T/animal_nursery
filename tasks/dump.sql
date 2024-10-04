-- MySQL dump 10.13  Distrib 8.0.39, for Linux (x86_64)
--
-- Host: localhost    Database: friends_of_humans
-- ------------------------------------------------------
-- Server version	8.0.39-0ubuntu0.24.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `AllAnimals`
--

DROP TABLE IF EXISTS `AllAnimals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `AllAnimals` (
  `name` varchar(50) NOT NULL DEFAULT '',
  `command` varchar(50) DEFAULT NULL,
  `birth_date` date DEFAULT NULL,
  `type` varchar(10) NOT NULL DEFAULT ''
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AllAnimals`
--

LOCK TABLES `AllAnimals` WRITE;
/*!40000 ALTER TABLE `AllAnimals` DISABLE KEYS */;
INSERT INTO `AllAnimals` VALUES ('Rex','Sit','2021-05-01','Dog'),('Buddy','Stay','2022-03-01','Dog'),('Whiskers','Jump','2020-07-01','Cat'),('Mittens','Paw','2021-02-15','Cat'),('Hammy','Run','2021-08-10','Hamster'),('Thunder','Gallop','2018-04-15','Horse'),('Donny','Hee-Haw','2020-12-12','Donkey'),('Thunder','Gallop','2018-04-15','PackAnimal'),('Donny','Hee-Haw','2020-12-12','PackAnimal');
/*!40000 ALTER TABLE `AllAnimals` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Animal`
--

DROP TABLE IF EXISTS `Animal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Animal` (
  `id` int NOT NULL AUTO_INCREMENT,
  `type` enum('DomesticAnimal','PackAnimal') NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Animal`
--

LOCK TABLES `Animal` WRITE;
/*!40000 ALTER TABLE `Animal` DISABLE KEYS */;
/*!40000 ALTER TABLE `Animal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Camel`
--

DROP TABLE IF EXISTS `Camel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Camel` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `command` varchar(50) DEFAULT NULL,
  `birth_date` date DEFAULT NULL,
  `age_years` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Camel`
--

LOCK TABLES `Camel` WRITE;
/*!40000 ALTER TABLE `Camel` DISABLE KEYS */;
/*!40000 ALTER TABLE `Camel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Cat`
--

DROP TABLE IF EXISTS `Cat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Cat` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `command` varchar(50) DEFAULT NULL,
  `birth_date` date DEFAULT NULL,
  `age_years` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cat`
--

LOCK TABLES `Cat` WRITE;
/*!40000 ALTER TABLE `Cat` DISABLE KEYS */;
INSERT INTO `Cat` VALUES (1,'Whiskers','Jump','2020-07-01',3),(2,'Mittens','Paw','2021-02-15',2);
/*!40000 ALTER TABLE `Cat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Dog`
--

DROP TABLE IF EXISTS `Dog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Dog` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `command` varchar(50) DEFAULT NULL,
  `birth_date` date DEFAULT NULL,
  `age_years` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Dog`
--

LOCK TABLES `Dog` WRITE;
/*!40000 ALTER TABLE `Dog` DISABLE KEYS */;
INSERT INTO `Dog` VALUES (1,'Rex','Sit','2021-05-01',2),(2,'Buddy','Stay','2022-03-01',1);
/*!40000 ALTER TABLE `Dog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DomesticAnimal`
--

DROP TABLE IF EXISTS `DomesticAnimal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `DomesticAnimal` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `command` varchar(50) DEFAULT NULL,
  `birth_date` date DEFAULT NULL,
  `age_years` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `DomesticAnimal_ibfk_1` FOREIGN KEY (`id`) REFERENCES `Animal` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DomesticAnimal`
--

LOCK TABLES `DomesticAnimal` WRITE;
/*!40000 ALTER TABLE `DomesticAnimal` DISABLE KEYS */;
/*!40000 ALTER TABLE `DomesticAnimal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Donkey`
--

DROP TABLE IF EXISTS `Donkey`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Donkey` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `command` varchar(50) DEFAULT NULL,
  `birth_date` date DEFAULT NULL,
  `age_years` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Donkey`
--

LOCK TABLES `Donkey` WRITE;
/*!40000 ALTER TABLE `Donkey` DISABLE KEYS */;
INSERT INTO `Donkey` VALUES (1,'Donny','Hee-Haw','2020-12-12',2);
/*!40000 ALTER TABLE `Donkey` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Hamster`
--

DROP TABLE IF EXISTS `Hamster`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Hamster` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `command` varchar(50) DEFAULT NULL,
  `birth_date` date DEFAULT NULL,
  `age_years` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Hamster`
--

LOCK TABLES `Hamster` WRITE;
/*!40000 ALTER TABLE `Hamster` DISABLE KEYS */;
INSERT INTO `Hamster` VALUES (1,'Hammy','Run','2021-08-10',2);
/*!40000 ALTER TABLE `Hamster` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Horse`
--

DROP TABLE IF EXISTS `Horse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Horse` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `command` varchar(50) DEFAULT NULL,
  `birth_date` date DEFAULT NULL,
  `age_years` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Horse`
--

LOCK TABLES `Horse` WRITE;
/*!40000 ALTER TABLE `Horse` DISABLE KEYS */;
INSERT INTO `Horse` VALUES (1,'Thunder','Gallop','2018-04-15',5);
/*!40000 ALTER TABLE `Horse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PackAnimal`
--

DROP TABLE IF EXISTS `PackAnimal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PackAnimal` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `command` varchar(50) DEFAULT NULL,
  `birth_date` date DEFAULT NULL,
  `age_years` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `PackAnimal_ibfk_1` FOREIGN KEY (`id`) REFERENCES `Animal` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PackAnimal`
--

LOCK TABLES `PackAnimal` WRITE;
/*!40000 ALTER TABLE `PackAnimal` DISABLE KEYS */;
/*!40000 ALTER TABLE `PackAnimal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PackAnimals`
--

DROP TABLE IF EXISTS `PackAnimals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PackAnimals` (
  `name` varchar(50) NOT NULL DEFAULT '',
  `command` varchar(50) DEFAULT NULL,
  `birth_date` date DEFAULT NULL,
  `age_years` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PackAnimals`
--

LOCK TABLES `PackAnimals` WRITE;
/*!40000 ALTER TABLE `PackAnimals` DISABLE KEYS */;
INSERT INTO `PackAnimals` VALUES ('Thunder','Gallop','2018-04-15',5),('Donny','Hee-Haw','2020-12-12',2);
/*!40000 ALTER TABLE `PackAnimals` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `YoungAnimal`
--

DROP TABLE IF EXISTS `YoungAnimal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `YoungAnimal` (
  `name` varchar(50) NOT NULL,
  `command` varchar(50) DEFAULT NULL,
  `birth_date` date DEFAULT NULL,
  `age_years` bigint DEFAULT NULL,
  `age_months` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `YoungAnimal`
--

LOCK TABLES `YoungAnimal` WRITE;
/*!40000 ALTER TABLE `YoungAnimal` DISABLE KEYS */;
/*!40000 ALTER TABLE `YoungAnimal` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-04 14:39:48
