-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: cyber_defense
-- ------------------------------------------------------
-- Server version	8.0.40

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
-- Table structure for table `backup_logs`
--

DROP TABLE IF EXISTS `backup_logs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `backup_logs` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `backup_type` varchar(100) NOT NULL,
  `location` varchar(255) NOT NULL,
  `status` varchar(50) DEFAULT 'Successful',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `backup_logs`
--

LOCK TABLES `backup_logs` WRITE;
/*!40000 ALTER TABLE `backup_logs` DISABLE KEYS */;
INSERT INTO `backup_logs` (`id`, `backup_type`, `location`, `status`, `created_at`) VALUES (1,'Full','Local','Successful','2025-03-09 15:13:05'),(2,'Incremental','AWS S3','Successful','2025-03-09 15:13:05'),(3,'Differential','Azure Blob Storage','Successful','2025-03-09 15:13:05');
/*!40000 ALTER TABLE `backup_logs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_assets`
--

DROP TABLE IF EXISTS `company_assets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `company_assets` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `asset_name` varchar(255) NOT NULL,
  `asset_type` varchar(100) NOT NULL,
  `owner` varchar(100) NOT NULL,
  `status` varchar(50) DEFAULT 'Active',
  `last_updated` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_assets`
--

LOCK TABLES `company_assets` WRITE;
/*!40000 ALTER TABLE `company_assets` DISABLE KEYS */;
INSERT INTO `company_assets` (`id`, `asset_name`, `asset_type`, `owner`, `status`, `last_updated`) VALUES (1,'Main Database Server','Database','Alice Johnson','Active','2025-03-09 15:12:45'),(2,'Financial Records System','Application','Bob Smith','Active','2025-03-09 15:12:45'),(3,'HR Management Portal','Application','Charlie Davis','Active','2025-03-09 15:12:45'),(4,'DevOps Build Server','Server','David Lee','Active','2025-03-09 15:12:45'),(5,'Company Website','Website','Eva Brown','Active','2025-03-09 15:12:45');
/*!40000 ALTER TABLE `company_assets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employees` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `department` varchar(100) NOT NULL,
  `role` varchar(100) NOT NULL,
  `status` varchar(50) DEFAULT 'Active',
  `last_updated` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` (`id`, `name`, `email`, `department`, `role`, `status`, `last_updated`) VALUES (1,'Alice Johnson','alice.johnson@company.com','IT','System Administrator','Active','2025-03-09 15:12:20'),(2,'Bob Smith','bob.smith@company.com','Finance','Finance Manager','Active','2025-03-09 15:12:20'),(3,'Charlie Davis','charlie.davis@company.com','HR','HR Executive','Active','2025-03-09 15:12:20'),(4,'David Lee','david.lee@company.com','Engineering','Software Engineer','Active','2025-03-09 15:12:20'),(5,'Eva Brown','eva.brown@company.com','Marketing','Marketing Analyst','Active','2025-03-09 15:12:20');
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phishing_attempts`
--

DROP TABLE IF EXISTS `phishing_attempts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `phishing_attempts` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `employee_id` int DEFAULT NULL,
  `email_sent` tinyint(1) DEFAULT '0',
  `link_clicked` tinyint(1) DEFAULT '0',
  `credentials_compromised` tinyint(1) DEFAULT '0',
  `attempt_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phishing_attempts`
--

LOCK TABLES `phishing_attempts` WRITE;
/*!40000 ALTER TABLE `phishing_attempts` DISABLE KEYS */;
INSERT INTO `phishing_attempts` (`id`, `employee_id`, `email_sent`, `link_clicked`, `credentials_compromised`, `attempt_time`) VALUES (1,1,1,0,0,'2025-03-09 15:13:24'),(2,2,1,1,0,'2025-03-09 15:13:24'),(3,3,1,1,1,'2025-03-09 15:13:24'),(4,4,1,0,0,'2025-03-09 15:13:24'),(5,5,1,1,1,'2025-03-09 15:13:24');
/*!40000 ALTER TABLE `phishing_attempts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recovery_logs`
--

DROP TABLE IF EXISTS `recovery_logs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recovery_logs` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `asset_id` int DEFAULT NULL,
  `backup_id` int DEFAULT NULL,
  `recovery_status` varchar(50) DEFAULT 'In Progress',
  `restored_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recovery_logs`
--

LOCK TABLES `recovery_logs` WRITE;
/*!40000 ALTER TABLE `recovery_logs` DISABLE KEYS */;
INSERT INTO `recovery_logs` (`id`, `asset_id`, `backup_id`, `recovery_status`, `restored_at`) VALUES (1,3,1,'Success','2025-03-09 15:13:47'),(2,5,2,'In Progress','2025-03-09 15:13:47');
/*!40000 ALTER TABLE `recovery_logs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `security_breaches`
--

DROP TABLE IF EXISTS `security_breaches`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `security_breaches` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `asset_id` int DEFAULT NULL,
  `employee_id` int DEFAULT NULL,
  `breach_type` varchar(255) NOT NULL,
  `breach_details` text,
  `detected_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `security_breaches`
--

LOCK TABLES `security_breaches` WRITE;
/*!40000 ALTER TABLE `security_breaches` DISABLE KEYS */;
INSERT INTO `security_breaches` (`id`, `asset_id`, `employee_id`, `breach_type`, `breach_details`, `detected_at`) VALUES (1,3,3,'Phishing Attack','Charlie Davis entered credentials on a fake HR portal.','2025-03-09 15:13:37'),(2,5,5,'Phishing Attack','Eva Brown entered credentials on a fake marketing portal.','2025-03-09 15:13:37');
/*!40000 ALTER TABLE `security_breaches` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_credentials`
--

DROP TABLE IF EXISTS `user_credentials`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_credentials` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `employee_id` int DEFAULT NULL,
  `username` varchar(255) NOT NULL,
  `password_hash` text NOT NULL,
  `last_changed` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_credentials`
--

LOCK TABLES `user_credentials` WRITE;
/*!40000 ALTER TABLE `user_credentials` DISABLE KEYS */;
INSERT INTO `user_credentials` (`id`, `employee_id`, `username`, `password_hash`, `last_changed`) VALUES (1,1,'alice_admin','hashed_password_123','2025-03-09 15:12:52'),(2,2,'bob_finance','hashed_password_456','2025-03-09 15:12:52'),(3,3,'charlie_hr','hashed_password_789','2025-03-09 15:12:52'),(4,4,'david_dev','hashed_password_abc','2025-03-09 15:12:52'),(5,5,'eva_marketing','hashed_password_xyz','2025-03-09 15:12:52');
/*!40000 ALTER TABLE `user_credentials` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'cyber_defense'
--

--
-- Dumping routines for database 'cyber_defense'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-10 10:18:13
