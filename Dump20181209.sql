-- MySQL dump 10.13  Distrib 5.7.17, for macos10.12 (x86_64)
--
-- Host: localhost    Database: cmpe295b
-- ------------------------------------------------------
-- Server version	5.7.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `phone` int(20) DEFAULT NULL,
  `organization_address` varchar(100) DEFAULT NULL,
  `organization_name` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'first1','last1','first1@last1.com','$5$rounds=535000$AXUl5BKxLiQZCoM/$KTCHeTP0M.IrEIFmrX9tMsY3BGDQsZPQaTVCYHZmpk7',2,'adsfghytfdsgdnsgfao','asdfghjkl'),(2,'first1','last1','first1@last1.com','$5$rounds=535000$Wjf69GuPRcxz0Jmn$oC/meDIwkElvwfhAJjkY0M6w/s8ZwYwsZ5kgQ9DICh6',2,'adsfghytfdsgdnsgfao','asdfghjkl'),(3,'first1','last1','first1@last1.com','$5$rounds=535000$OeusxD2JyoWZuUK2$QLvJ8f2RERItpablcUczJruN1xbb5Y80RhNvO3b/QWC',2,'adsfghytfdsgdnsgfao','asdfghjkl'),(4,'first1','last1','first1@last1.com','$5$rounds=535000$5tu5IY140/Y7rbQs$Iu/tVqDLklpbS8up1bZLSNgH3Zll7EpDHv8Z6TQDjIC',2,'adsfghytfdsgdnsgfao','asdfghjkl'),(5,'first1','last1','first1@last1.com','$5$rounds=535000$Bi3XU1jsERuUkFg5$.BW1JM3nr0ZrpptWkgc/T3yQVvAHl3WI5R8uqHY9y38',2,'adsfghytfdsgdnsgfao','asdfghjkl'),(6,'first1','last1','first1@last1.com','$5$rounds=535000$qKwtgV4zxBME.BDW$5XuLefxKi6PE/he7Ov437fkSYi1vW5ZObREk6yEE927',2,'adsfghytfdsgdnsgfao','asdfghjkl'),(7,'first1','last1','first1@last1.com','$5$rounds=535000$EOHrM9kviP9VIE.B$dQIodsKWuAm/SbVmWytclIzkAAQAVSwyM.jnAEo7Zl6',2,'adsfghytfdsgdnsgfao','asdfghjkl'),(8,'first1','last1','first1@last1.com','$5$rounds=535000$7krxui.IMiMWxwEh$bMGjDNoQjXY6fNxcS9zXACfvd31CAXfH3LUBZmapOoD',2,'adsfghytfdsgdnsgfao','asdfghjkl'),(9,'first1','last1','first1@last1.com','$5$rounds=535000$iefuylge.41kAxem$wKDVuNy3VMJZN8yEIoIK5x/jh8Z5ErV.kIiVOv6T6jA',2,'adsfghytfdsgdnsgfao','asdfghjkl'),(10,'first1','last1','first1@last1.com','$5$rounds=535000$5doW4OSflaUf92UD$S9106uuBmoceq5Z0IMt9p29r0jliZ4tTvyVsosmY2F6',21,'adsfghytfdsgdnsgfao','asdfghjkl'),(11,'first1','last1','first1@last1.com','$5$rounds=535000$llVFW7xMtJzfP42p$D7PFEPqez0KDomTJthGt5yYaP3nACgYprJCVjsdtpL8',21,'adsfghytfdsgdnsgfao','asdfghjkl'),(12,'first1','last1','first1@last1.com','$5$rounds=535000$nrY9Nj/0zczseXcZ$OwxdHJNb8/IxlEgVM3jfN/jByKun4htxWS20kYzFLm5',213,'adsfghytfdsgdnsgfao','asdfghjkl'),(13,'first1','last1','first1@last1.com','$5$rounds=535000$dsQ/Pa5id37vzCfl$rO8udjHDiTif9Ky295QRW9YbZznMHBpZiOBiWUDYwfB',213,'adsfghytfdsgdnsgfao','asdfghjkl'),(14,'first1','last1','first1@last1.com','$5$rounds=535000$PyL4KWw.wVCuF2yg$nFtWi4Paoflpj0hnXzxcfw3kfX6O9tp2KH3315H8Sk7',1213,'adsfghytfdsgdnsgfao','asdfghjkl'),(15,'first1','last1','first1@last1.com','$5$rounds=535000$pVCR2dRIhpUci9rg$7KBC/f.yV/vIS4vGo4d288/fGGkAMIXLLNmtm59YJOA',1213,'adsfghytfdsgdnsgfao','asdfghjkl'),(16,'first1','last1','first1@last1.com','$5$rounds=535000$1ELd8CgZt3dYgvsw$wWCorPW2B939Fagm7Cg.06QRoKbqwBRRhMLZFHH11rC',1213,'adsfghytfdsgdnsgfao','asdfghjkl'),(17,'first1','last1','first1@last1.com','$5$rounds=535000$vOkPCnAxrVJjPdKP$IfrdmnsFN/AjjFgG6H9oaCNFfudafSCBgdgpIRJUve8',1213,'adsfghytfdsgdnsgfao','asdfghjkl'),(18,'first1','last1','first1@last1.com','$5$rounds=535000$ZAYpT5aXtN34.IF4$/PfFxZIhIcsN0Ui0bzHuoEWtJhy77GF4FXQIBhNzZM/',1234,'adsfghytfdsgdnsgfao','asdfghjkl'),(19,'first1','last1','first1@last1.com','$5$rounds=535000$FAsxRIjeBEsGSstF$RDnK.MditswnoFPselOC9yoOkPe0riu9Ut.T66tR408',1234,'adsfghytfdsgdnsgfao','asdfghjkl'),(20,'first1','last1','first1@last1.com','$5$rounds=535000$Ajfq3M/X.1HUjN1R$U0RKssLE.Z4y3lb2RIjny6sd8f3.3DDdZkbvLyAuu91',1234,'adsfghytfdsgdnsgfao','asdfghjkl'),(21,'first1','last1','first1@last1.com','$5$rounds=535000$dYl1MMGNPBgXqJid$OfzDUNOE7Klo8GXQygn/J4LwbYpX5XoZa4nS2GPzZ61',1234,'adsfghytfdsgdnsgfao','asdfghjkl'),(22,'first1','last1','first1@last1.com','$5$rounds=535000$pmb/UANHzzmeEsb7$Co6gzzSMv/FWKCQCGU9QuWJ96boMobADqF.8CrB9xa5',1234,'adsfghytfdsgdnsgfao','asdfghjkl'),(23,'first2','last2','first2@last2.com','$5$rounds=535000$a7CuZvIu5e0Ec.Ph$G9XfQIX91wVqXTNjabiZiG40h6bap9u3hEGQxBJ/RQD',1234,'adsfghytfdsgdnsgfao','asdfghjkl'),(24,'first2','last2','first2@last2.com','$5$rounds=535000$o9f5TcnvAyAcKDst$Ye0o4IVoSBNpd7/hIoD71Cc4XdiBQqlC8Do9AZ.4JO1',1234,'adsfghytfdsgdnsgfao','asdfghjkl'),(25,'abhi','abhi','abhish@abhi.com','$5$rounds=535000$Rq1LXwtluULHGAAO$y1Tc5MxIlJe0ySTR6m7p2g6JaRiE3xzvpjZeHuqtFYC',12345,'SKJSU','190 Ryland'),(26,'ABHi','ABHIIIII','teja@teja.com','$5$rounds=535000$NIdr334faz2Q/wrt$njtS4KxfP528efuBOOPiz3p0OUT0.MXNB6zmefsrnKD',123456,'xnm,m','dfghjhgfd'),(27,'first2','last2','first2@last2.com','$5$rounds=535000$drgaGm6TTtev0Pvs$X9vYXf.bUWVIOaBZIFINJlv9b/qJa0bp/a5omPRwQn9',1234,'adsfghytfdsgdnsgfao','asdfghjkl'),(28,'qwerty','porty','qwerty@porty.com','$5$rounds=535000$kdS58lj986xfop6P$meNEJPM1Rv4qqTLF13dBrYDGPlE2NvaNFmf9/.QXGt2',1234567789,'zasasds','zasxas'),(29,'asfkg','asdfkhjlj','asfk@kadlkf.com','$5$rounds=535000$SWkJsb4CCJXk1qiW$E2ME/OQ4MQY8pUlsuHzjWDVFvTcKvbUkmQWi4Lb6635',1234567,'dflsjkngk','asdfkjk'),(30,'ella','habibi','ellahabibi@shek.com','$5$rounds=535000$1jwtqrxXb.AtAkCb$l3HyL36il0yciczytKu.u..bRJ8idkNJ.kvQAHyU.QC',123456,'dfgrefgr','qredfadf');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-12-09 14:47:48
