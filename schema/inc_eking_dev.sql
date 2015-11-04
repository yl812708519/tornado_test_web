CREATE DATABASE  IF NOT EXISTS `inc_eking_dev` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin */;
USE `inc_eking_dev`;
-- MySQL dump 10.13  Distrib 5.5.38, for debian-linux-gnu (x86_64)
--
-- Host: 192.168.1.136    Database: inc_eking_dev
-- ------------------------------------------------------
-- Server version	5.5.40-0ubuntu0.14.04.1

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
-- Table structure for table `attachments`
--

DROP TABLE IF EXISTS `attachments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `attachments` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) COLLATE utf8mb4_bin NOT NULL COMMENT '文件真实名称，非oss上的文件名',
  `upload_time` datetime NOT NULL COMMENT '文件上传到oss上的时间',
  `operator_id` bigint(20) NOT NULL,
  `module` varchar(45) COLLATE utf8mb4_bin NOT NULL COMMENT '所属模块',
  `entity_id` bigint(20) NOT NULL COMMENT '所属模块实体id',
  `is_deleted` bigint(20) DEFAULT '0',
  `created_at` bigint(20) DEFAULT NULL,
  `updated_at` bigint(20) DEFAULT NULL,
  `oss_url` varchar(100) COLLATE utf8mb4_bin DEFAULT NULL,
  `file_size` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=228 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attachments`
--

LOCK TABLES `attachments` WRITE;
/*!40000 ALTER TABLE `attachments` DISABLE KEYS */;
INSERT INTO `attachments` VALUES (1,'测试修改了.xslx','2014-10-10 10:19:00',1,'contract',11,1,12312414,1412908789006,NULL,NULL),(2,'测试修改了.xslx','2014-10-10 10:19:00',1,'contract',2,0,NULL,NULL,NULL,NULL),(3,'测试修改了.xslx','2014-10-10 10:19:00',1,'contract',11,0,1412908988514,1412908988514,NULL,NULL),(4,'adfadf','2014-10-10 18:55:25',2,'customer',158,0,1412938597716,1412938597716,'asdfadsf',NULL),(5,'logo.jpg','2014-10-10 18:52:59',2,'customer',167,1,1412938603295,1413264748737,'1o/kl/i13f0yz4n31.jpg',NULL),(6,'u=1475543376,3671370006&fm=56.jpeg','2014-10-10 18:52:59',2,'customer',167,1,1412938603386,1413264748737,'k/m3/i13f13407at.jpeg',NULL),(7,'adfadf','2014-10-10 18:55:25',2,'customer',158,0,1412994210947,1412994210947,'asdfadsf',123),(8,'1412749557248.xlsx','2014-10-11 14:48:15',9,'customer',169,0,1413010108034,1413010108034,'1y/qa/i14lq6vi53k.xlsx',6),(9,'1412749562430.xlsx','2014-10-11 14:48:15',9,'customer',169,0,1413010108123,1413010108123,'1r/ql/i14lq7pv53j.xlsx',6),(10,'files-2b-4d-i14bdp8n7ou.jpg','2014-10-11 14:48:16',9,'customer',169,0,1413010108178,1413010108178,'15/qn/i14lq7ut7ou.jpg',10),(11,'files-15-qn-i14lq7ut7ou.jpg','2014-10-11 16:54:22',9,'customer',169,0,1413017667189,1413017667189,'1r/hd/i14q8ear7ou.jpg',10),(12,'files-15-qn-i14lq7ut7ou (2).jpg','2014-10-11 16:54:42',9,'customer',169,0,1413017691219,1413017691219,'11/my/i14q8tsd7ou.jpg',10),(13,'files-2b-4d-i14bdp8n7ou.jpg','2014-10-13 15:06:12',9,'customer',170,0,1413184098842,1413184098842,'files/1b/k5/i17h8zwj7ou.jpg',9966),(14,'files-2b-4d-i14bdp8n7ou.jpg','2014-10-13 15:07:58',9,'customer',170,0,1413184098889,1413184098890,'files/1q/ln/i17hb98q7ou.jpg',9966),(15,'files-2b-4d-i14bdp8n7ou.jpg','2014-10-13 15:07:58',9,'customer',170,0,1413184098938,1413184098938,'files/15/lp/i17hb9dp7ou.jpg',9966),(16,'files-11-my-i14q8tsd7ou (1).jpg','2014-10-13 15:07:58',9,'customer',170,0,1413184098986,1413184098986,'files/v/lr/i17hb9iz7ou.jpg',9966),(17,'files-11-my-i14q8tsd7ou (2).jpg','2014-10-13 18:09:24',9,'customer',169,0,1413194972214,1413194972214,'files/o/hj/i17nskac7ou.jpg',9966),(18,'id_rsa','2014-10-13 18:23:59',2,'customer',169,0,1413195846172,1413195846172,'files/v/aw/i17obcan1an.',1679),(19,'易清互动编码规范.wps','2014-10-14 13:18:21',2,'customer',167,1,1413263853449,1413264184550,'files/1d/eu/i18st4eh7i8/易清互动编码规范.wps',9728),(20,'易清互动编码规范.wps','2014-10-14 13:19:01',2,'customer',167,1,1413263853449,1413264184550,'files/1d/eu/i18st4eh7i8/易清互动编码规范.wps',9728),(21,'logo.jpg','2014-10-14 13:33:11',2,'customer',167,1,1413264748737,1413278348086,'files/11/dj/i18tcb7ln31/logo.jpg',29917),(22,'易清互动编码规范.wps','2014-10-14 13:34:53',2,'customer',167,1,1413264748737,1413278348086,'files/11/dj/i18tcb7l7i8/易清互动编码规范.wps',9728),(23,'logo.jpg','2014-10-14 13:35:35',2,'customer',167,1,1413264748737,1413278348086,'files/11/dj/i18tcb7ln31/logo.jpg',29917),(24,'logo.jpg','2014-10-14 13:40:21',9,'customer',167,1,1413265163211,1413274275697,'files/b/hk/i18tl70rn31/logo.jpg',29917),(25,'易清互动编码规范.wps','2014-10-14 13:40:21',9,'customer',167,1,1413265163211,1413278353802,'files/b/hk/i18tl70r7i8/易清互动编码规范.wps',9728),(26,'u=1475543376,3671370006&fm=56.jpeg','2014-10-14 13:43:03',2,'customer',167,1,1413265163211,1413278348086,'files/b/hk/i18tl70r7at/u=1475543376,3671370006&fm=56.jpeg',9461),(27,'易清互动编码规范.wps','2014-10-14 13:49:02',2,'customer',167,1,1413265163211,1413278348086,'files/b/hk/i18tl70r7i8/易清互动编码规范.wps',9728),(28,'logo.jpg','2014-10-14 13:51:01',9,'customer',167,1,1413265845488,1413274275697,'files/2g/cm/i18tztgwn31/logo.jpg',29917),(29,'1412749557248.xlsx','2014-10-14 14:27:12',9,'customer',171,0,1413255317970,1413255317970,'files/1y/4z/i18nq6du53k.xlsx',6608),(30,'1412749562430.xlsx','2014-10-14 14:27:12',9,'customer',171,0,1413255317970,1413255317970,'files/1y/4z/i18nq6du53k.xlsx',6607),(31,'1412749557248.xlsx','2014-10-14 14:28:09',9,'customer',171,0,1413255317970,1413255317970,'files/1y/4z/i18nq6du53k.xlsx',9966),(32,'新建文本文档.txt','2014-10-14 14:55:12',9,'customer',172,1,1413269656794,1413274275697,'files/2m/fr/i18w9iaisfv.txt',36859),(33,'text.html','2014-10-14 14:55:13',9,'customer',172,1,1413269656794,1413274275697,'files/2m/fr/i18w9iaisfv.txt',135),(34,'text.html','2014-10-14 16:44:42',9,'customer',173,1,1413276154759,1413274275697,'files/1n/f7/i1904s5j3r/text.html',135),(35,'2icon_znhf.jpg','2014-10-14 16:44:50',9,'customer',173,1,1413276154759,1413274275697,'files/1n/f7/i1904s5jotz/2icon_znhf.jpg',32183),(36,'text.html','2014-10-14 16:46:54',9,'customer',173,1,1413272951374,1413274275697,'files/22/e9/i18y84emux/arrow_down.png',1113),(37,'arrow_up.png','2014-10-15 10:30:37',2,'contract',159,0,1413340220722,1413340220722,'files/m/5r/i1a29xrm282/arrow_up.png',2882),(38,'arrow_up.png','2014-10-15 10:31:52',2,'contract',159,0,1413340220722,1413340220722,'files/m/5r/i1a29xrmux/arrow_down.png',1113),(39,'arrow_up.png','2014-10-15 10:32:18',2,'contract',159,0,1413340220722,1413340220722,'files/m/5r/i1a29xrmux/arrow_down.png',1113),(40,'arrow_up.png','2014-10-15 10:32:43',2,'contract',159,0,1413340220722,1413340220722,'files/m/5r/i1a29xrm282/arrow_up.png',1104),(41,'arrow_up.png','2014-10-15 10:34:36',2,'contract',159,0,1413340220722,1413340220722,'files/m/5r/i1a29xrm282/arrow_up.png',1113),(42,'1.jpg','2014-10-15 10:44:55',2,'contract',158,0,1413340933137,1413340933137,'files/11/97/i1a2p7gx2sbe/1.jpg',130010),(43,'files-11-my-i14q8tsd7ou (2).jpg','2014-10-15 14:31:51',9,'customer',173,0,1413354649268,1413354649268,'files/1w/do/i1aav6wk7ou/files-11-my-i14q8tsd7ou (2).jpg',9966),(44,'files-11-my-i14q8tsd7ou (2).jpg','2014-10-15 14:33:32',2,'customer',173,0,1413354522228,1413354522228,'files/s/66/i1aasgvoux/arrow_down.png',1113),(50,'arrow_down.png','2014-10-15 15:05:18',2,'customer',175,1,1413356677322,1413356677322,'files/m/lh/i1ac2nreux/arrow_down.png',1113),(51,'arrow_up.png','2014-10-15 15:05:18',2,'customer',175,0,1413356677322,1413356677322,'files/m/lh/i1ac2nre282/arrow_up.png',2882),(52,'ban.html','2014-10-15 15:05:36',2,'customer',175,0,1413356677322,1413356677322,'files/m/lh/i1ac2nre56z/ban.html',6731),(53,'block.html','2014-10-15 15:05:36',2,'customer',175,0,1413356677322,1413356677322,'files/m/lh/i1ac2nre2gg/block.html',3184),(54,'city.html','2014-10-15 15:07:14',2,'customer',175,0,1413356677322,1413356677322,'files/m/lh/i1ac2nreux/arrow_down.png',1955),(55,'1412749557248.xlsx','2014-10-15 15:20:50',9,'customer',174,0,1413356497802,1413356497802,'files/2/r6/i1abyt8q53k/1412749557248.xlsx',6608),(56,'1412749562430.xlsx','2014-10-15 15:20:51',9,'customer',174,0,1413356497802,1413356497802,'files/2/r6/i1abyt8q53j/1412749562430.xlsx',6607),(57,'1412749557248.xlsx','2014-10-15 15:51:28',9,'customer',174,0,1413359437086,1413359437086,'files/2e/aa/i1adpt7i7r0/chenggong.jpg',10044),(58,'arrow_up.png','2014-10-15 16:01:40',2,'customer',175,0,1413360039029,1413360039029,'files/t/au/i1ae2po5ux/arrow_down.png',1113),(59,'2icon_znhf.jpg','2014-10-15 17:17:54',10,'contract',162,0,1413364526897,1413364526897,'files/2p/7g/i1agqwj5otz/2icon_znhf.jpg',32183),(60,'xixihaha','2014-10-15 17:33:37',5,'workflow',70,1,1413365375886,1413365375886,'files/2e/l2/i1ah93m6d/xixihaha',13),(61,'arrow_down.png','2014-10-15 17:37:04',2,'customer',176,0,1413361068529,1413361068529,'files/t/j1/i1aeos1dux/arrow_down.png',1113),(62,'屏幕快照 2014-09-04 上午8.22.30.png','2014-10-15 19:17:11',13,'contract',174,0,1413371367513,1413371367513,'files/d/ir/i1aktis98q41/屏幕快照 2014-09-04 上午8.22.30.png',407089),(63,'11icon_dzp.jpg','2014-10-16 14:05:14',10,'contract',178,0,1413432058961,1413432058961,'files/1p/gd/i1bkycltkzp/11icon_dzp.jpg',27205),(64,'12icon_ggl.jpg','2014-10-16 14:05:40',10,'contract',178,0,1413432058961,1413432058961,'files/1p/gd/i1bkycltos0/12icon_ggl.jpg',32112),(65,'16icon_wtg.jpg','2014-10-16 14:05:51',10,'contract',178,0,1413432058961,1413432058961,'files/1p/gd/i1bkycltlyx/16icon_wtg.jpg',28473),(66,'21icon_wmdc.jpg','2014-10-16 14:06:31',10,'contract',178,0,1413432058961,1413432058961,'files/1p/gd/i1bkycltjia/21icon_wmdc.jpg',25282),(67,'17icon_hyk.jpg','2014-10-16 14:06:31',10,'contract',178,0,1413432058961,1413432058961,'files/1p/gd/i1bkycltk9v/17icon_hyk.jpg',26275),(68,'1412749557248.xlsx','2014-10-16 14:30:42',9,'customer',174,0,1413431268874,1413431268874,'files/22/j4/i1bkheyy7ou/files-2b-4d-i14bdp8n7ou.jpg',9966),(69,'1412749557248.xlsx','2014-10-16 14:30:42',9,'customer',174,0,1413431268874,1413431268874,'files/22/j4/i1bkheyy7ou/files-11-my-i14q8tsd7ou.jpg',9966),(70,'1412749562430.xlsx','2014-10-16 14:30:43',9,'customer',174,0,1413431268874,1413431268874,'files/22/j4/i1bkheyy7ou/files-11-my-i14q8tsd7ou (1).jpg',9966),(71,'files-2b-4d-i14bdp8n7ou.jpg','2014-10-16 14:30:43',9,'customer',174,0,1413431268874,1413431268874,'files/22/j4/i1bkheyy7ou/files-11-my-i14q8tsd7ou (2).jpg',9966),(72,'1412749557248.xlsx','2014-10-16 14:42:20',9,'customer',174,0,1413431268874,1413431268874,'files/22/j4/i1bkheyy7sf/cuowu.jpg',10044),(73,'1412749557248.xlsx','2014-10-16 14:42:21',9,'customer',174,0,1413431268874,1413431268874,'files/22/j4/i1bkheyy81a/demo.html',10095),(74,'新建文本文档.txt','2014-10-16 14:57:50',10,'workflow',81,0,1413432058961,1413432058961,'files/1p/gd/i1bkycltsfv/新建文本文档.txt',36859),(75,'cuowu.jpg','2014-10-16 15:03:12',9,'customer',178,0,1413431268874,1413431268874,'files/22/j4/i1bkheyy7sf/cuowu.jpg',10095),(76,'demo.html','2014-10-16 15:03:13',9,'customer',178,0,1413431268874,1413431268874,'files/22/j4/i1bkheyy81a/demo.html',10414),(77,'cuowu.jpg','2014-10-16 15:07:47',9,'customer',178,0,1413431268874,1413431268874,'files/22/j4/i1bkheyy7r0/chenggong.jpg',10044),(78,'demo.html','2014-10-16 15:07:48',9,'customer',178,0,1413431268874,1413431268874,'files/22/j4/i1bkheyy7ou/shanchu.jpg',9966),(79,'cuowu.jpg','2014-10-16 15:09:42',9,'customer',177,0,1413431268874,1413431268874,'files/22/j4/i1bkheyy7sf/cuowu.jpg',10095),(80,'demo.html','2014-10-16 15:09:42',9,'customer',177,0,1413431268874,1413431268874,'files/22/j4/i1bkheyy81a/demo.html',10414),(81,'shanchu.jpg','2014-10-16 15:09:43',9,'customer',177,0,1413431268874,1413431268874,'files/22/j4/i1bkheyy7ou/shanchu.jpg',9966),(82,'xiazai.jpg','2014-10-16 15:09:43',9,'customer',177,0,1413431268874,1413431268874,'files/22/j4/i1bkheyy7of/xiazai.jpg',9951),(83,'cuowu.jpg','2014-10-16 15:15:52',9,'customer',177,0,1413431268874,1413431268874,'files/22/j4/i1bkheyybr/header-bg.jpg',423),(84,'demo.html','2014-10-16 15:15:53',9,'customer',177,0,1413431268874,1413431268874,'files/22/j4/i1bkheyy8wc/logo.gif',11532),(85,'cuowu.jpg','2014-10-16 15:31:13',9,'customer',177,0,1413431268874,1413431268874,'files/22/j4/i1bkheyy934/Thumbs.db',11776),(86,'demo.html','2014-10-16 15:31:14',9,'customer',177,0,1413431268874,1413431268874,'files/22/j4/i1bkheyyxx/cancelbutton.gif',1221),(87,'header-bg.jpg','2014-10-16 15:33:09',9,'customer',167,0,1413431268874,1413431268874,'files/22/j4/i1bkheyybr/header-bg.jpg',423),(88,'logo.gif','2014-10-16 15:33:10',9,'customer',167,0,1413431268874,1413431268874,'files/22/j4/i1bkheyy8wc/logo.gif',11532),(89,'header-bg.jpg','2014-10-16 15:34:07',9,'customer',167,0,1413431268874,1413431268874,'files/22/j4/i1bkheyyxx/cancelbutton.gif',1221),(90,'cuowu.jpg','2014-10-16 15:34:58',8,'customer',178,0,1413444200819,1413444200819,'files/j/8/i1bs6lbn1mr/noimage.png',2115),(91,'header-bg.jpg','2014-10-16 15:36:58',9,'customer',167,0,1413431268874,1413431268874,'files/22/j4/i1bkheyyxx/cancelbutton.gif',1221),(92,'cuowu.jpg','2014-10-16 15:35:52',8,'customer',178,0,1413444200819,1413444200819,'files/j/8/i1bs6lbn1mr/noimage.png',2115),(93,'header-bg.jpg','2014-10-16 15:38:01',9,'customer',167,0,1413431268874,1413431268874,'files/22/j4/i1bkheyy934/Thumbs.db',11776),(94,'header-bg.jpg','2014-10-16 15:39:42',9,'customer',167,0,1413431268874,1413431268874,'files/22/j4/i1bkheyy4wk/handlers.js',6356),(95,'logo.gif','2014-10-16 15:39:44',9,'customer',167,0,1413431268874,1413431268874,'files/22/j4/i1bkheyyset/swfupload.js',36821),(96,'header-bg.jpg','2014-10-16 15:39:44',9,'customer',167,0,1413431268874,1413431268874,'files/22/j4/i1bkheyy25m/swfupload.queue.js',2794),(97,'cuowu.jpg','2014-10-16 15:45:13',9,'customer',178,0,1413431268874,1413431268874,'files/22/j4/i1bkheyy458/fileprogress.js',5372),(98,'cuowu.jpg','2014-10-16 15:45:13',9,'customer',178,0,1413431268874,1413431268874,'files/22/j4/i1bkheyy4wk/handlers.js',6356),(99,'cuowu.jpg','2014-10-16 15:45:15',9,'customer',178,0,1413431268874,1413431268874,'files/22/j4/i1bkheyyset/swfupload.js',36821),(100,'handlers.js','2014-10-16 15:45:50',9,'customer',179,1,1413431268874,1413431268874,'files/22/j4/i1bkheyy4wk/handlers.js',6356),(101,'swfupload.js','2014-10-16 15:45:52',9,'customer',179,1,1413431268874,1413431268874,'files/22/j4/i1bkheyyset/swfupload.js',36821),(102,'swfupload.queue.js','2014-10-16 15:45:52',9,'customer',179,1,1413431268874,1413431268874,'files/22/j4/i1bkheyy25m/swfupload.queue.js',2794),(103,'swfupload.swf','2014-10-16 15:45:53',9,'customer',179,1,1413431268874,1413431268874,'files/22/j4/i1bkheyy97f/swfupload.swf',11931),(104,'swfupload.queue.js','2014-10-16 15:47:42',9,'customer',179,1,1413431268874,1413431268874,'files/22/j4/i1bkheyy25m/swfupload.queue.js',2794),(105,'swfupload.queue.js','2014-10-16 15:49:35',9,'customer',179,1,1413431268874,1413431268874,'files/22/j4/i1bkheyybr/header-bg.jpg',423),(106,'header-bg.jpg','2014-10-16 15:49:36',9,'customer',179,1,1413431268874,1413431268874,'files/22/j4/i1bkheyyvf/TestImageNoText_65x29.png',1131),(107,'swfupload.queue.js','2014-10-16 16:23:38',9,'customer',179,1,1413431268874,1413431268874,'files/22/j4/i1bkheyybr/header-bg.jpg',423),(108,'swfupload.queue.js','2014-10-16 16:26:09',9,'customer',179,1,1413431268874,1413431268874,'files/22/j4/i1bkheyy8wc/logo.gif',11532),(109,'cuowu.jpg','2014-10-16 16:31:03',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyy7sf/cuowu.jpg',10095),(110,'demo.html','2014-10-16 16:31:04',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyy81a/demo.html',10414),(111,'demo.html','2014-10-16 16:32:38',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyy7ou/shanchu.jpg',9966),(112,'chenggong.jpg','2014-10-16 16:32:38',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyy7of/xiazai.jpg',9951),(113,'chenggong.jpg','2014-10-16 16:34:00',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyy81a/demo.html',10414),(114,'demo.html','2014-10-16 16:34:06',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyy7ou/shanchu.jpg',9966),(115,'shanchu.jpg','2014-10-16 16:34:07',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyy7of/xiazai.jpg',9951),(116,'cancelbutton.gif','2014-10-16 16:40:56',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyyxx/cancelbutton.gif',1221),(117,'header-bg.jpg','2014-10-16 16:40:56',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyybr/header-bg.jpg',423),(118,'TestImageNoText_65x29.png','2014-10-16 16:41:10',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyyvf/TestImageNoText_65x29.png',1131),(119,'Thumbs.db','2014-10-16 16:41:10',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyy934/Thumbs.db',11776),(120,'cancelbutton.gif','2014-10-16 16:42:02',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyyxx/cancelbutton.gif',1221),(121,'logo.gif','2014-10-16 16:42:12',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyy8wc/logo.gif',11532),(122,'TestImageNoText_65x29.png','2014-10-16 16:42:12',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyyvf/TestImageNoText_65x29.png',1131),(123,'Thumbs.db','2014-10-16 16:42:13',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyy934/Thumbs.db',11776),(124,'logo.gif','2014-10-16 16:44:10',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyy8wc/logo.gif',11532),(125,'TestImageNoText_65x29.png','2014-10-16 16:44:11',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyyvf/TestImageNoText_65x29.png',1131),(126,'Thumbs.db','2014-10-16 16:44:12',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyy934/Thumbs.db',11776),(127,'header-bg.jpg','2014-10-16 16:52:44',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyybr/header-bg.jpg',423),(128,'logo.gif','2014-10-16 16:52:45',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyy8wc/logo.gif',11532),(129,'TestImageNoText_65x29.png','2014-10-16 16:52:45',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyyvf/TestImageNoText_65x29.png',1131),(130,'header-bg.jpg','2014-10-16 16:58:15',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyybr/header-bg.jpg',423),(131,'header-bg.jpg','2014-10-16 16:59:33',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyybr/header-bg.jpg',423),(132,'header-bg.jpg','2014-10-16 16:59:57',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyybr/header-bg.jpg',423),(133,'cancelbutton.gif','2014-10-16 17:00:43',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyyxx/cancelbutton.gif',1221),(134,'cancelbutton.gif','2014-10-16 17:01:14',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyyxx/cancelbutton.gif',1221),(135,'cancelbutton.gif','2014-10-16 17:02:02',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyyxx/cancelbutton.gif',1221),(136,'新建文本文档.txt','2014-10-16 17:01:40',10,'contract',187,0,1413447654536,1413447654536,'files/10/f5/i1bu8m88sfv/新建文本文档.txt',36859),(137,'header-bg.jpg','2014-10-16 17:02:41',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyybr/header-bg.jpg',423),(138,'logo.gif','2014-10-16 17:03:05',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyy8wc/logo.gif',11532),(139,'text.html','2014-10-16 17:02:41',10,'contract',196,0,1413447654536,1413447654536,'files/10/f5/i1bu8m883r/text.html',135),(140,'cancelbutton.gif','2014-10-16 17:04:15',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyyxx/cancelbutton.gif',1221),(141,'新建文本文档.txt','2014-10-16 17:03:39',10,'workflow',83,0,1413447654536,1413447654536,'files/10/f5/i1bu8m88sfv/新建文本文档.txt',36859),(142,'cancelbutton.gif','2014-10-16 17:05:00',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyyxx/cancelbutton.gif',1221),(143,'cancelbutton.gif','2014-10-16 17:05:20',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyyxx/cancelbutton.gif',1221),(144,'cancelbutton.gif','2014-10-16 17:05:40',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyyxx/cancelbutton.gif',1221),(145,'cancelbutton.gif','2014-10-16 17:06:23',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyyxx/cancelbutton.gif',1221),(146,'cancelbutton.gif','2014-10-16 17:07:24',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyyxx/cancelbutton.gif',1221),(147,'cancelbutton.gif','2014-10-16 17:07:41',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyy8wc/logo.gif',11532),(148,'logo.gif','2014-10-16 17:07:42',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyyvf/TestImageNoText_65x29.png',1131),(149,'logo.gif','2014-10-16 17:10:05',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyyvf/TestImageNoText_65x29.png',1131),(150,'TestImageNoText_65x29.png','2014-10-16 17:10:06',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyy934/Thumbs.db',11776),(151,'TestImageNoText_65x29.png','2014-10-16 17:12:22',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyybr/header-bg.jpg',423),(152,'header-bg.jpg','2014-10-16 17:12:23',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyy8wc/logo.gif',11532),(153,'header-bg.jpg','2014-10-16 17:16:27',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyy8wc/logo.gif',11532),(154,'logo.gif','2014-10-16 17:16:40',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyy934/Thumbs.db',11776),(155,'logo.gif','2014-10-16 17:18:38',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyybr/header-bg.jpg',423),(156,'header-bg.jpg','2014-10-16 17:18:38',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyyvf/TestImageNoText_65x29.png',1131),(157,'TestImageNoText_65x29.png','2014-10-16 17:18:39',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyy934/Thumbs.db',11776),(158,'TestImageNoText_65x29.png','2014-10-16 17:24:25',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyy8wc/logo.gif',11532),(159,'logo.gif','2014-10-16 17:24:27',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyy934/Thumbs.db',11776),(160,'TestImageNoText_65x29.png','2014-10-16 17:27:30',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyyxx/cancelbutton.gif',1221),(161,'TestImageNoText_65x29.png','2014-10-16 17:27:30',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyybr/header-bg.jpg',423),(162,'logo.gif','2014-10-16 17:31:31',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyybr/header-bg.jpg',423),(163,'header-bg.jpg','2014-10-16 17:31:31',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyyvf/TestImageNoText_65x29.png',1131),(164,'header-bg.jpg','2014-10-16 17:35:17',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyy8wc/logo.gif',11532),(165,'031619456443.jpg','2014-10-16 17:33:54',8,'customer',183,0,1413451720982,1413451720982,'files/2a/5t/i1bwnrx225l4/031619456443.jpg',100552),(166,'logo.gif','2014-10-16 17:35:25',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyy934/Thumbs.db',11776),(167,'logo.gif','2014-10-16 17:37:12',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyyxx/cancelbutton.gif',1221),(168,'cancelbutton.gif','2014-10-16 17:37:13',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyybr/header-bg.jpg',423),(169,'header-bg.jpg','2014-10-16 17:37:14',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyyvf/TestImageNoText_65x29.png',1131),(170,'TestImageNoText_65x29.png','2014-10-16 17:37:30',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyy934/Thumbs.db',11776),(171,'TestImageNoText_65x29.png','2014-10-16 17:38:47',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyybr/header-bg.jpg',423),(172,'header-bg.jpg','2014-10-16 17:38:48',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyy8wc/logo.gif',11532),(173,'logo.gif','2014-10-16 17:38:49',9,'customer',181,1,1413431268874,1413453672782,'files/22/j4/i1bkheyy934/Thumbs.db',11776),(174,'files-1r-hd-i14q8ear7ou (2).jpg','2014-10-16 17:52:41',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyy7ou/files-2b-4d-i14bdp8n7ou.jpg',9966),(175,'files-2b-4d-i14bdp8n7ou.jpg','2014-10-16 17:52:41',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyy7ou/files-11-my-i14q8tsd7ou.jpg',9966),(176,'files-11-my-i14q8tsd7ou.jpg','2014-10-16 17:52:42',9,'customer',181,1,1413431268874,1413431268874,'files/22/j4/i1bkheyy7ou/files-11-my-i14q8tsd7ou (1).jpg',9966),(177,'logo.gif','2014-10-16 17:54:59',9,'customer',181,1,1413431268874,1413453673100,'files/22/j4/i1bkheyy7ou/files-1r-hd-i14q8ear7ou (1).jpg',9966),(178,'files-1r-hd-i14q8ear7ou (1).jpg','2014-10-16 17:54:59',9,'customer',181,1,1413431268874,1413453676388,'files/22/j4/i1bkheyy7ou/files-1r-hd-i14q8ear7ou (2).jpg',9966),(179,'files-1r-hd-i14q8ear7ou (2).jpg','2014-10-16 17:55:01',9,'customer',181,1,1413431268874,1413453678236,'files/22/j4/i1bkheyy7ou/files-2b-4d-i14bdp8n7ou.jpg',9966),(180,'files-2b-4d-i14bdp8n7ou.jpg','2014-10-16 17:55:01',9,'customer',181,1,1413431268874,1413454399847,'files/22/j4/i1bkheyy7ou/files-11-my-i14q8tsd7ou.jpg',9966),(181,'files-2b-4d-i14bdp8n7ou.jpg','2014-10-16 18:01:35',9,'customer',181,1,1413453695300,1413454085792,'files/n/qg/i1bxu3937ou/files-1r-hd-i14q8ear7ou (2).jpg',9966),(182,'files-1r-hd-i14q8ear7ou (2).jpg','2014-10-16 18:01:35',9,'customer',181,1,1413453695475,1413454083340,'files/6/qi/i1bxu3e67ou/files-11-my-i14q8tsd7ou.jpg',9966),(183,'files-11-my-i14q8tsd7ou.jpg','2014-10-16 18:01:35',9,'customer',181,1,1413453695857,1413454078351,'files/21/qj/i1bxu3it7ou/files-11-my-i14q8tsd7ou (1).jpg',9966),(184,'arrow_up.png','2014-10-16 18:06:50',2,'customer',182,1,1413454010311,1413454193311,'files/2b/2t/i1by0u9z282/arrow_up.png',2882),(185,'ban.html','2014-10-16 18:06:50',2,'customer',182,1,1413454010569,1413454190534,'files/6/2x/i1by0uiy56z/ban.html',6731),(186,'files-2b-4d-i14bdp8n7ou.jpg','2014-10-16 18:08:52',9,'customer',181,1,1413454132303,1413454160728,'files/k/7g/i1by3c9w7ou/files-1r-hd-i14q8ear7ou (2).jpg',9966),(187,'files-1r-hd-i14q8ear7ou (2).jpg','2014-10-16 18:08:52',9,'customer',181,1,1413454132875,1413454159139,'files/27/91/i1by3gpv7ou/files-11-my-i14q8tsd7ou.jpg',9966),(188,'files-11-my-i14q8tsd7ou.jpg','2014-10-16 18:08:53',9,'customer',181,1,1413454133799,1413454157475,'files/1o/96/i1by3h387ou/files-11-my-i14q8tsd7ou (1).jpg',9966),(189,'files-2b-4d-i14bdp8n7ou.jpg','2014-10-16 18:09:37',9,'customer',181,1,1413454177835,1413454398178,'files/x/lj/i1by4fel7ou/files-11-my-i14q8tsd7ou.jpg',9966),(190,'files-11-my-i14q8tsd7ou.jpg','2014-10-16 18:09:38',9,'customer',181,1,1413454178073,1413454396384,'files/2g/ln/i1by4fr87ou/files-11-my-i14q8tsd7ou (1).jpg',9966),(191,'files-11-my-i14q8tsd7ou (1).jpg','2014-10-16 18:09:38',9,'customer',181,1,1413454178540,1413454394752,'files/15/lq/i1by4fy97ou/files-11-my-i14q8tsd7ou (2).jpg',9966),(192,'ban.html','2014-10-16 18:10:36',2,'customer',182,1,1413454236070,1413454261340,'files/h/9x/i1by5oat56z/ban.html',6731),(193,'block.html','2014-10-16 18:10:36',2,'customer',182,1,1413454236535,1413454259495,'files/2l/a1/i1by5oo12gg/block.html',3184),(194,'ban.html','2014-10-16 18:11:37',2,'customer',182,1,1413454297959,1413455376629,'files/3/r7/i1by70a756z/ban.html',6731),(195,'block.html','2014-10-16 18:11:38',2,'customer',182,1,1413454298213,1413455374214,'files/p/r9/i1by70gd2gg/block.html',3184),(196,'1412749557248.xlsx','2014-10-16 18:18:05',9,'customer',181,1,1413454685977,1413454729483,'files/t/nv/i1byfbop53k/1412749557248.xlsx',6608),(197,'1412749557248.xlsx','2014-10-16 18:21:53',9,'customer',181,1,1413454913779,1413454948450,'files/1n/3c/i1byk66353k/1412749557248.xlsx',6608),(198,'1412749562430.xlsx','2014-10-16 18:21:53',9,'customer',181,1,1413454913957,1413454946742,'files/6/3v/i1byk7le53j/1412749562430.xlsx',6607),(199,'files-1r-hd-i14q8ear7ou.jpg','2014-10-16 18:21:54',9,'customer',181,1,1413454914345,1413454945003,'files/23/3w/i1byk7q37ou/files-1r-hd-i14q8ear7ou.jpg',9966),(200,'files-1r-hd-i14q8ear7ou (1).jpg','2014-10-16 18:21:54',9,'customer',181,1,1413454914829,1413454942323,'files/1m/41/i1byk83i7ou/files-1r-hd-i14q8ear7ou (1).jpg',9966),(201,'files-1r-hd-i14q8ear7ou (2).jpg','2014-10-16 18:21:55',9,'customer',181,1,1413454915229,1413454940388,'files/1q/45/i1byk8eq7ou/files-1r-hd-i14q8ear7ou (2).jpg',9966),(202,'1412749557248.xlsx','2014-10-16 18:25:57',9,'customer',181,0,1413455157652,1413455157652,'files/1u/fx/i1bypfg653k/1412749557248.xlsx',6608),(203,'1412749562430.xlsx','2014-10-16 18:25:57',9,'customer',181,0,1413455157828,1413455157828,'files/2b/g1/i1bypfrr53j/1412749562430.xlsx',6607),(204,'files-1r-hd-i14q8ear7ou.jpg','2014-10-16 18:25:58',9,'customer',181,0,1413455158209,1413455158209,'files/19/g3/i1bypfw97ou/files-1r-hd-i14q8ear7ou.jpg',9966),(205,'ban.html','2014-10-16 18:29:47',2,'customer',182,1,1413455387712,1413455512986,'files/1h/oc/i1byud51ux/arrow_down.png',1113),(206,'arrow_down.png','2014-10-16 18:32:00',2,'customer',182,1,1413455520269,1413455558054,'files/c/5m/i1byx7f8ux/arrow_down.png',1113),(207,'arrow_up.png','2014-10-16 18:32:00',2,'customer',182,1,1413455520446,1413455556034,'files/2a/5n/i1byx7jy282/arrow_up.png',2882),(208,'ban.html','2014-10-16 18:32:00',2,'customer',182,1,1413455520721,1413455554094,'files/1q/5q/i1byx7rq56z/ban.html',6731),(209,'block.html','2014-10-16 18:32:00',2,'customer',182,1,1413455520988,1413455551662,'files/w/5t/i1byx7z82gg/block.html',3184),(210,'arrow_down.png','2014-10-16 18:32:44',2,'customer',182,0,1413455564813,1413455564813,'files/q/hz/i1byy5rqux/arrow_down.png',1113),(211,'test.txt','2014-10-16 18:51:51',10,'customer',161,1,1413456711111,1413456924585,'files/27/32/i1bzmqav37/test.txt',115),(212,'hs_err_pid2528.log','2014-10-16 18:52:03',10,'customer',161,1,1413456723276,1413456904308,'files/1r/65/i1bzmyur2fqz/hs_err_pid2528.log',113723),(213,'listPage.js','2014-10-16 18:52:19',10,'customer',161,1,1413456739296,1413456952009,'files/2p/at/i1bznbudj3t/listPage.js',24761),(214,'abc.txt','2014-10-16 18:53:19',10,'customer',161,1,1413456799533,1413457149696,'files/2e/rm/i1bzomimhl/abc.txt',633),(215,'listPage改.js','2014-10-16 18:53:19',10,'customer',161,1,1413456799876,1413457157309,'files/7/ro/i1bzomlzjeo/listPage改.js',25152),(216,'abc.txt','2014-10-16 18:53:20',10,'customer',161,1,1413456800057,1413457147603,'files/k/0/i1bzomxghl/abc.txt',633),(217,'routes.py','2014-10-16 18:53:53',10,'customer',161,1,1413456833547,1413456989152,'files/5/9b/i1bzpcrl5lp/routes.py',7261),(218,'abc.txt','2014-10-16 18:59:01',10,'customer',161,1,1413457141968,1413457172222,'files/q/bn/i1bzvyqu4f/__init__.pyc',159),(219,'__init__.py','2014-10-16 18:59:55',10,'customer',161,1,1413457195085,1413457371402,'files/s/qe/i1bzx3pw0/__init__.py',0),(220,'databases.yaml','2014-10-16 18:59:55',10,'customer',161,0,1413457195323,1413457195323,'files/13/qg/i1bzx3vrmr/databases.yaml',819),(221,'oss_config.yaml','2014-10-16 18:59:55',10,'customer',161,0,1413457195531,1413457195531,'files/24/qi/i1bzx42ckc/oss_config.yaml',732),(222,'widgets.py','2014-10-16 18:59:55',10,'customer',161,0,1413457195676,1413457195676,'files/z/qk/i1bzx46r12l/widgets.py',1389),(223,'widgets.pyc','2014-10-16 19:00:17',10,'customer',161,0,1413457217452,1413457217452,'files/f/4u/i1bzxkzr1f6/widgets.pyc',1842),(224,'test.txt','2014-10-16 19:00:17',10,'customer',161,0,1413457217585,1413457217585,'files/1g/4v/i1bzxl3k37/test.txt',115),(225,'hs_err_pid2528.log','2014-10-16 19:00:18',10,'customer',161,0,1413457218224,1413457218225,'files/2e/4w/i1bzxl7a2fqz/hs_err_pid2528.log',113723),(226,'test.txt','2014-10-16 19:03:30',10,'contract',201,1,1413457410044,1413457424112,'files/6/2s/i1c01pli37/test.txt',115),(227,'hs_err_pid2528.log','2014-10-16 19:03:30',10,'contract',201,0,1413457410945,1413457410945,'files/2g/2t/i1c01pqk2fqz/hs_err_pid2528.log',113723);
/*!40000 ALTER TABLE `attachments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contract_cases`
--

DROP TABLE IF EXISTS `contract_cases`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contract_cases` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `contract_id` bigint(20) NOT NULL,
  `case_type` varchar(50) NOT NULL,
  `name` varchar(200) NOT NULL,
  `association_code` varchar(30) NOT NULL,
  `operator_id` bigint(20) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL DEFAULT '0',
  `created_at` bigint(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contract_cases`
--

LOCK TABLES `contract_cases` WRITE;
/*!40000 ALTER TABLE `contract_cases` DISABLE KEYS */;
INSERT INTO `contract_cases` VALUES (1,160,'patent','123456','123',5,0,1413255468050),(2,160,'patent','123456','456',5,0,1413255591121),(3,160,'patent','123456','789',5,0,1413255634419),(4,151,'1','fewjiof专利1','',5,0,1413255814253),(5,0,'1','fewjiof专利2','',5,0,1413256315017),(6,0,'10','fewjiof专利3','',5,0,1413256684794),(7,0,'1','专利1','',5,0,1413258877468),(8,0,'1','专利2','',5,0,1413258899163),(9,0,'1','专利1','',5,0,1413258941166),(10,0,'1','专利1','',5,0,1413258973855),(11,0,'1','专利1','',5,0,1413259032579),(12,154,'1','专利1','123',5,0,1413259231545),(13,154,'1','fewjiof专利2','456',5,1,1413259253237),(14,154,'1','fewjiof专利3','',5,1,1413259261244),(15,113,'1','33333','',5,1,1413269609578),(16,0,'7','44444','',5,0,1413269621065),(17,113,'7','顶顶顶顶','',5,1,1413269654743),(18,0,'6','呃呃呃','',5,0,1413269662309),(19,113,'10','123456','',5,1,1413269764512),(20,113,'10','3333344','',5,1,1413269822084),(21,113,'10','3333344','',5,1,1413269893592),(22,155,'patent','合同 1号专利','',1,0,1413284865642),(23,155,'patent','合同 专利2号','',1,0,1413284865642),(24,155,'patent','合同 专利3号','',1,0,1413284865642),(25,155,'patent','合同 专利4号','',1,0,1413285098832),(26,155,'patent','合同 专利5号','',1,0,1413285203166),(27,155,'patent','合同 专利6号','',1,0,1413285322547),(28,155,'patent','合同 专利7号','',1,0,1413285394037),(29,155,'patent','合同 专利7号','',1,0,1413286218246),(30,155,'patent','合同 专利8号','',1,0,1413286218246),(31,163,'patent','专利1','',5,1,1413351065811),(32,167,'patent','专利1','',5,1,1413361213341),(33,167,'patent','fewjiof专利2','',5,1,1413361213341),(34,166,'patent','专利1','',5,1,1413364017965),(35,168,'patent','sdfsdf','',13,0,1413369034695),(36,173,'patent','sdfsdf','',13,0,1413370640290),(37,174,'patent','sdfsdf','',13,0,1413371367513),(38,176,'patent','专利1','',5,0,1413372364516),(39,176,'trademark','商标1','',5,0,1413372364516),(40,177,'patent','阿萨德飞','',13,0,1413372351477),(41,176,'','','',5,0,1413428395598),(42,178,'trademark','客户商标注册','',10,0,1413432058961),(43,171,'patent','123','',8,0,1413445236917),(44,196,'copyright','添加版权','',10,1,1413447654536),(45,196,'patent','专利1','',5,1,1413454231109),(46,192,'patent','专利1','',5,1,1413454281864),(47,192,'patent','154879','',5,1,1413454307087),(48,202,'trademark','合同 商标测试作废','',1,1,1413456163143);
/*!40000 ALTER TABLE `contract_cases` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contract_dealers`
--

DROP TABLE IF EXISTS `contract_dealers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contract_dealers` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `dealer_id` bigint(20) DEFAULT NULL,
  `contract_id` varchar(30) COLLATE utf8mb4_bin DEFAULT NULL,
  `created_at` bigint(20) DEFAULT NULL,
  `operator_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=426 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contract_dealers`
--

LOCK TABLES `contract_dealers` WRITE;
/*!40000 ALTER TABLE `contract_dealers` DISABLE KEYS */;
INSERT INTO `contract_dealers` VALUES (38,2,'29',1409904187462,2),(39,1,'29',1409904187502,2),(40,2,'30',1409904297377,2),(41,1,'30',1409904297499,2),(69,2,'34',1409908646665,2),(70,1,'34',1409908646737,2),(71,2,'35',1409908945862,2),(72,1,'35',1409908945949,2),(73,2,'35',1409908946007,2),(74,2,'36',1409909064343,2),(75,1,'36',1409909064436,2),(76,2,'36',1409909064505,2),(77,2,'37',1409909130112,2),(78,1,'37',1409909130510,2),(105,1,'41',1410319366361,5),(112,5,'44',1410330716380,5),(113,2,'44',1410330716462,5),(118,5,'46',1410774900344,5),(119,5,'47',1410775378691,5),(120,5,'48',1410775670785,5),(121,5,'49',1410853471605,5),(122,5,'50',1410853932864,5),(123,5,'51',1410854487301,5),(124,5,'52',1410856420469,5),(125,5,'53',1410856588593,5),(126,5,'54',1410939602762,5),(127,5,'55',1410941531905,5),(128,5,'56',1410941773937,5),(129,5,'57',1410944466500,5),(130,5,'58',1410944654888,5),(131,5,'59',1410944703030,5),(132,5,'60',1410945054863,5),(133,5,'61',1410945249278,5),(136,5,'63',1411010680857,5),(145,5,'66',1411098029753,5),(146,5,'67',1411378875491,5),(147,5,'68',1411379239656,5),(150,5,'69',1411613616577,5),(151,5,'70',1411613863369,5),(153,2,'72',1412739666930,2),(154,9,'72',1412739667022,2),(155,2,'73',1412739985582,2),(156,2,'74',1412740052208,2),(157,2,'75',1412740116658,2),(158,5,'76',1412752643276,5),(159,5,'77',1412752764047,5),(160,5,'78',1412753006556,5),(161,5,'79',1412753074786,5),(162,5,'80',1412753274531,5),(163,5,'81',1412753293086,5),(164,5,'82',1412753488657,5),(165,5,'83',1412753670063,5),(166,5,'84',1412753704840,5),(167,5,'85',1412754144935,5),(168,5,'86',1412754246831,5),(169,5,'87',1412758029496,5),(170,5,'88',1412758368877,5),(171,5,'89',1412758430223,5),(172,2,'90',1412758876952,5),(174,2,'92',1412763250882,5),(175,5,'93',1412834538963,5),(176,5,'94',1412834612318,5),(177,5,'95',1412834662102,5),(178,5,'96',1412834758731,5),(179,5,'97',1412834830040,5),(180,5,'98',1412835035231,5),(181,5,'99',1412835137867,5),(182,5,'100',1412835182293,5),(183,2,'91',1412835467668,5),(184,5,'101',1412835513794,5),(185,5,'102',1412835550522,5),(186,5,'103',1412835740924,5),(187,5,'104',1412835880115,5),(188,5,'105',1412835929798,5),(189,5,'106',1412836080394,5),(190,5,'107',1412837058839,5),(191,2,'108',1412844650913,5),(195,2,'38',1412845550864,10),(196,1,'38',1412845550916,10),(197,1,'38',1412845550972,10),(198,2,'31',1412845569982,10),(199,2,'32',1412845596917,10),(200,1,'32',1412845597002,10),(201,1,'32',1412845597101,10),(202,5,'45',1412845609203,10),(203,5,'40',1412845625458,10),(204,2,'40',1412845625545,10),(205,1,'40',1412845625656,10),(206,2,'42',1412845647593,10),(207,1,'42',1412845647649,10),(208,2,'43',1412845658602,10),(209,1,'43',1412845658659,10),(210,2,'39',1412845673920,10),(211,1,'39',1412845673981,10),(212,2,'25',1412845694557,10),(213,1,'25',1412845694743,10),(214,5,'109',1412852662908,1),(215,5,'110',1412852718176,1),(217,12,'112',1412910223086,10),(222,12,'114',1412924471451,10),(225,12,'115',1412924796880,10),(228,12,'113',1412925214240,5),(229,10,'116',1412926305600,10),(230,12,'117',1412927285080,5),(231,12,'146',1412930066813,5),(232,12,'147',1412930127172,5),(250,5,'151',1413012875153,5),(251,10,'152',1413169260721,5),(252,8,'152',1413169260779,5),(265,2,'150',1413169655960,5),(266,1,'150',1413169656025,5),(267,9,'150',1413169656082,5),(268,5,'150',1413169656143,5),(269,6,'150',1413169656204,5),(270,3,'150',1413169656266,5),(271,6,'155',1413275775546,6),(272,6,'154',1413300509819,13),(273,6,'149',1413300509819,13),(274,1,'148',1413300509819,13),(275,2,'148',1413300509819,13),(276,3,'148',1413300509819,13),(277,5,'148',1413300509819,13),(278,6,'148',1413300509819,13),(279,9,'148',1413300509819,13),(297,1,'111',1413303428853,1),(298,2,'111',1413303428853,1),(299,6,'111',1413303428853,1),(300,1,'157',1413303428853,1),(301,6,'157',1413303428853,1),(302,5,'157',1413303428853,1),(307,2,'159',1413340220722,2),(308,5,'160',1413343047684,5),(309,5,'161',1413349980007,5),(310,5,'163',1413351065811,5),(311,1,'165',1413358117719,13),(312,5,'166',1413360935625,5),(313,5,'167',1413361189465,5),(314,13,'169',1413369645124,13),(315,13,'170',1413369645124,13),(317,2,'172',1413370528872,2),(319,5,'176',1413372286164,5),(323,10,'178',1413443725020,2),(324,13,'177',1413443725020,2),(325,5,'175',1413443725020,2),(326,13,'174',1413443725020,2),(327,6,'174',1413443725020,2),(328,2,'180',1413443725020,2),(329,6,'180',1413443725020,2),(330,2,'181',1413443725020,2),(331,1,'181',1413443725020,2),(332,9,'181',1413443725020,2),(338,2,'184',1413443224519,10),(340,2,'171',1413444813460,2),(344,2,'183',1413443224519,10),(359,5,'186',1413446389735,5),(363,5,'188',1413447089823,2),(364,5,'189',1413446690611,5),(365,5,'190',1413447232394,5),(366,5,'191',1413447232394,5),(368,5,'193',1413447372457,5),(372,2,'194',1413447516020,2),(374,2,'195',1413447613484,2),(375,2,'185',1413447613484,2),(395,5,'197',1413449558605,5),(414,5,'187',1413452903221,5),(415,2,'199',1413453168391,5),(416,5,'198',1413453183659,5),(420,5,'196',1413453282821,5),(422,5,'202',1413454246927,5),(423,2,'192',1413454263639,5),(425,5,'201',1413457444327,10);
/*!40000 ALTER TABLE `contract_dealers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contracts`
--

DROP TABLE IF EXISTS `contracts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contracts` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `num` varchar(30) CHARACTER SET utf8mb4 NOT NULL COMMENT '默认编号',
  `customer_id` bigint(20) NOT NULL COMMENT '客户编号',
  `name` varchar(100) COLLATE utf8mb4_bin NOT NULL COMMENT '合同名称',
  `sign_time` date NOT NULL COMMENT '签订时间',
  `amount` double(20,2) NOT NULL COMMENT '合同金额',
  `start_time` date NOT NULL COMMENT '合同起止时间',
  `end_time` date NOT NULL COMMENT '合同结束时间',
  `dealer_id` bigint(10) NOT NULL COMMENT '法务，处理人id',
  `organization_id` bigint(10) NOT NULL COMMENT '所属公司id',
  `project_num` bigint(20) NOT NULL COMMENT '项目数量',
  `payment_way` varchar(20) COLLATE utf8mb4_bin NOT NULL COMMENT '支付方式',
  `account_time` date DEFAULT NULL COMMENT '到款时间',
  `account_company` varchar(50) COLLATE utf8mb4_bin NOT NULL COMMENT '到款单位',
  `account_money` double(20,2) NOT NULL COMMENT '到款金额',
  `receipt` varchar(50) COLLATE utf8mb4_bin NOT NULL COMMENT '是否开发票',
  `state` tinyint(1) NOT NULL DEFAULT '0' COMMENT '状态 0:处理中 1:作废 2:完成',
  `markup` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '备注',
  `operator_id` bigint(20) DEFAULT NULL,
  `is_deleted` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `created_at` bigint(20) NOT NULL,
  `updated_at` bigint(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=203 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contracts`
--

LOCK TABLES `contracts` WRITE;
/*!40000 ALTER TABLE `contracts` DISABLE KEYS */;
INSERT INTO `contracts` VALUES (1,'20140905095347836309',150,'税金合同','2014-09-20',8000.00,'2014-09-03','2014-09-13',456,1,124312,'已付款','2014-09-18','中旬',600.00,'是',0,'',2,0,0,1409884215574),(2,'20140905095507012853',150,'456','2014-09-06',4456.00,'2014-09-10','2014-09-12',456,5,123,'分期付款','2014-09-13','11111111111',6865.00,'是',0,'',2,0,0,1409882107012),(3,'20140905105544388606',150,'测试合同','2014-09-18',15401430.00,'2014-09-20','2014-09-21',456,2,424,'分期付款','2014-09-21','23534',56457.00,'是',0,'',2,0,0,1409885744388),(4,'20140905105550961799',150,'测试合同','2014-09-18',15401430.00,'2014-09-20','2014-09-21',456,2,424,'分期付款','2014-09-21','23534',56457.00,'是',0,'',2,0,0,1409885750961),(5,'20140905105653802009',150,'测试合同','2014-09-18',15401430.00,'2014-09-20','2014-09-21',456,2,424,'分期付款','2014-09-21','23534',56457.00,'是',0,'',2,0,0,1409885813802),(6,'20140905105819852985',150,'测试合同','2014-09-18',15401430.00,'2014-09-20','2014-09-21',456,2,424,'分期付款','2014-09-21','23534',56457.00,'是',0,'',2,0,0,1409885899853),(7,'20140905105922284231',150,'测试合同','2014-09-18',15401430.00,'2014-09-20','2014-09-21',456,2,424,'分期付款','2014-09-21','23534',56457.00,'是',0,'',2,0,0,1409885962284),(8,'20140905111345074239',150,'测试合同','2014-09-11',123456.00,'2014-09-13','2014-09-28',456,1,3124,'分期付款','1980-11-15','4234',45235.00,'是',1,'xixihaha',2,0,0,1409886825074),(9,'20140905112557555851',150,'嘻嘻哈哈','2014-09-13',15401430.00,'2014-09-07','2014-09-06',456,6,111111111,'分期付款','2014-09-07','11111111111',4235.00,'是',1,'',2,0,0,1409887557555),(10,'20140905150706754101',150,'嘻嘻哈哈','2014-09-09',12131.00,'2014-09-07','2014-09-13',2,1,123,'分期付款','2014-09-28','123213',1243123412.00,'是',0,'',2,0,0,1409900826754),(11,'20140905150759980518',150,'嘻嘻哈哈','2014-09-09',12131.00,'2014-09-07','2014-09-13',2,1,123,'分期付款','2014-09-28','123213',1243123412.00,'是',0,'',2,0,0,1409900879980),(12,'20140905151800014514',150,'嘻嘻哈哈','2014-09-09',12131.00,'2014-09-07','2014-09-13',2,1,123,'分期付款','2014-09-28','123213',1243123412.00,'是',0,'',2,0,0,1409901480014),(13,'20140905151842036922',150,'嘻嘻哈哈','2014-09-13',123124.00,'2014-09-11','2014-09-13',2,1,5,'分期付款','2014-09-20','423423',5453.00,'是',0,'',2,0,0,1409901522036),(14,'20140905151941959414',150,'嘻嘻哈哈','2014-09-13',123124.00,'2014-09-11','2014-09-13',2,1,5,'分期付款','2014-09-20','423423',5453.00,'是',0,'',2,0,0,1409901581959),(15,'20140905152030258985',150,'嘻嘻哈哈','2014-09-13',123124.00,'2014-09-11','2014-09-13',2,1,5,'分期付款','2014-09-20','423423',5453.00,'是',0,'',2,0,0,1409901630259),(16,'20140905152558480282',150,'嘻嘻哈哈','2014-09-13',123124.00,'2014-09-11','2014-09-13',2,1,5,'分期付款','2014-09-20','423423',5453.00,'是',0,'',2,0,0,1409901958480),(17,'20140905152614433606',150,'嘻嘻哈哈','2014-09-13',123124.00,'2014-09-11','2014-09-13',2,1,5,'分期付款','2014-09-20','423423',5453.00,'是',0,'',2,0,0,1409901974433),(18,'20140905152746445915',150,'嘻嘻哈哈','2014-09-13',123124.00,'2014-09-11','2014-09-13',2,1,5,'分期付款','2014-09-20','423423',5453.00,'是',0,'',2,0,0,1409902066446),(19,'20140905152939794213',150,'嘻嘻哈哈','2014-09-13',123124.00,'2014-09-11','2014-09-13',2,1,5,'分期付款','2014-09-20','423423',5453.00,'是',0,'',2,0,0,1409902179794),(20,'20140905152958531176',150,'嘻嘻哈哈','2014-09-13',123124.00,'2014-09-11','2014-09-13',2,1,5,'分期付款','2014-09-20','423423',5453.00,'是',0,'',2,0,0,1409902198531),(21,'20140905153041541882',150,'嘻嘻哈哈','2014-09-13',123124.00,'2014-09-11','2014-09-13',2,1,5,'分期付款','2014-09-20','423423',5453.00,'是',0,'',2,0,0,1409902241541),(22,'20140905153141631383',150,'嘻嘻哈哈','2014-09-13',123124.00,'2014-09-11','2014-09-13',2,1,5,'分期付款','2014-09-20','423423',5453.00,'是',0,'',2,0,0,1409902301631),(23,'20140905153212775489',150,'嘻嘻哈哈','2014-09-13',123124.00,'2014-09-11','2014-09-13',2,1,5,'分期付款','2014-09-20','423423',5453.00,'是',0,'',2,0,0,1409902332775),(24,'20140905153522474755',150,'嘻嘻哈哈','2014-09-13',123124.00,'2014-09-11','2014-09-13',2,1,5,'分期付款','2014-09-20','423423',5453.00,'是',0,'',2,0,0,1409902522744),(25,'20140905153814649179',150,'葫芦娃','2014-09-05',12300000.00,'2014-09-04','2014-09-07',2,1,11,'已付款','2014-09-07','123444',1234.00,'是',0,'葫芦发的合同',10,0,0,1412845694934),(26,'20140905155653922901',150,'金刚葫芦娃','2014-09-12',100000.00,'2014-09-07','2014-09-14',2,1,123,'已付款','2014-09-03','312412',12412.00,'是',0,'',2,0,0,1409903814130),(27,'20140905160105695545',150,'金刚葫芦娃','2014-09-12',100000.00,'2014-09-07','2014-09-14',2,1,123,'已付款','2014-09-03','312412',12412.00,'是',0,'',2,0,0,1409904065858),(28,'20140905160137597396',150,'金刚葫芦娃','2014-09-12',100000.00,'2014-09-07','2014-09-14',2,1,123,'已付款','2014-09-03','312412',12412.00,'是',0,'',2,0,0,1409904097827),(29,'20140905160307406659',150,'金刚葫芦娃','2014-09-12',100000.00,'2014-09-07','2014-09-14',2,1,123,'已付款','2014-09-03','312412',12412.00,'是',0,'',2,0,0,1409904187557),(30,'20140905160457248523',150,'金刚葫芦娃','2014-09-12',100000.00,'2014-09-07','2014-09-14',2,1,123,'已付款','2014-09-03','312412',12412.00,'是',0,'',2,0,0,1409904297697),(31,'20140905161147122821',150,'大南瓜','2014-09-05',1546461.00,'2014-09-05','2014-09-13',2,1,15645,'已付款','2014-09-07','12456',326564.00,'是',0,'',10,0,0,1412845570038),(32,'20140905161412041166',150,'大南瓜','2014-09-05',1546461.00,'2014-09-05','2014-09-13',2,1,15645,'已付款','2014-09-07','12456',326564.00,'是',0,'',10,0,0,1412845597259),(33,'20140905162458560195',150,'大南瓜11','2014-09-05',1546461.00,'2014-09-06','2014-09-14',2,1,12344444,'已付款','2014-09-07','423423',5453.00,'是',0,'a mu mu',2,0,0,1409907896748),(34,'20140905171726597320',150,'大南瓜22','2014-09-05',12456.00,'2014-09-13','2014-09-21',2,1,15645,'已付款','2014-09-19','123',15646.00,'是',1,'ha ha ha',2,0,0,1409908646798),(35,'20140905172225791139',150,'大南瓜22','2014-09-05',123.00,'2014-09-06','2014-09-20',2,1,123,'分期付款','2014-09-28','123',1234.00,'是',0,'wu hah a',2,0,0,1409908946072),(36,'20140905172424204860',150,'大南瓜22','2014-09-05',123.00,'2014-09-06','2014-09-20',2,1,123,'分期付款','2014-09-28','123',1234.00,'是',0,'wu hah a',2,0,0,1409909064569),(37,'20140905172529975119',150,'大南瓜33','2014-09-12',123124.00,'2014-09-13','2014-09-28',2,1,456,'分期付款','2014-09-05','423423',5453.00,'是',0,'',2,0,0,1409909130669),(38,'20140905172924642009',150,'大南瓜44','2014-09-05',12456.00,'2014-09-08','2014-09-27',2,1,789456,'已付款','2014-09-10','789',156456.00,'是',0,'测试',10,0,0,1412845551027),(39,'20140909111719765690',150,'大南瓜55','2014-09-09',19000.00,'2014-09-10','2014-09-28',2,2,111111111,'已付款','2014-09-07','123456',1624.00,'是',0,'测试123467',10,0,0,1412845674037),(40,'20140909135009880095',150,'大南瓜66','2014-09-09',20000.00,'2014-09-11','2014-09-14',5,8,1654,'已付款','2014-09-13','19897',1234.00,'是',127,'嘻嘻哈哈1',10,0,0,1412845625785),(41,'20140909135206126942',150,'大南瓜66','2014-09-09',20000.00,'2014-09-11','2014-09-14',1,8,1654,'已付款','2014-09-13','19897',1234.00,'是',127,'嘻嘻哈哈12355',5,0,0,1410319366442),(42,'20140909151123023586',150,'测试合同嘻嘻哈哈','2014-09-10',15401430.00,'2014-09-03','2014-09-20',2,3,111111111,'已付款','2014-09-20','11111111111',123.00,'是',0,'',10,0,0,1412845647772),(43,'20140909161042363648',150,'测试合同嘻嘻哈哈','2014-09-11',123456.00,'2014-09-04','2014-09-20',2,4,111111111,'分期付款','2014-09-19','423423',1234.00,'否',0,'1111333',10,0,0,1412845658735),(44,'20140910143156312668',150,'大南瓜77','2014-09-10',123456.00,'2014-09-10','2014-09-21',5,8,123,'已付款','2014-09-12','423423',5453.00,'是',0,'',5,0,0,1410330716625),(45,'20140910144410440329',150,'大南瓜88','2014-09-03',1000000.45,'2014-09-10','2014-09-13',5,8,123,'已付款','2014-09-13','123',1234.00,'否',127,'',10,0,0,1412845609261),(46,'20140915175459769649',150,'123','2014-08-28',123124.00,'2014-09-05','2014-09-13',5,8,123,'分期付款','2014-09-24','123',5453.00,'是',0,'',5,0,0,1410774900205),(47,'20140915180257689089',150,'测试合同','2014-09-24',123456.00,'2014-09-13','2014-09-13',5,8,123,'分期付款','2014-09-13','123',1234.00,'是',0,'',5,0,0,1410775378594),(48,'20140915180750230175',150,'测试合同','2014-09-09',123456.00,'2014-09-17','2014-09-19',5,8,123,'已付款','2014-09-13','123',4235.00,'是',0,'',5,0,0,1410775670723),(49,'20140916154431327041',150,'测试合同','2014-08-27',123124.00,'2014-09-11','2014-09-07',5,8,111111111,'已付款','2014-09-12','123',123.00,'是',0,'',5,0,0,1410853471500),(50,'20140916155212575074',150,'123','2014-09-12',1989.00,'2014-09-03','2014-09-14',5,8,123,'已付款','2014-09-05','436456',123.00,'是',0,'',5,0,0,1410853932791),(51,'20140916160122582161',150,'测试合同嘻嘻哈哈','2014-09-05',1989.00,'2014-09-06','2014-09-19',5,8,123,'已付款','2014-08-30','423423',42342.00,'是',0,'',5,0,0,1410854487194),(52,'20140916163254276553',150,'测试合同','2014-09-04',15401430.00,'2014-09-06','2014-09-20',5,8,111111111,'分期付款','2014-09-13','1234',5453.00,'是',0,'',5,0,0,1410856420307),(53,'20140916163628333932',150,'嘻嘻哈哈','2014-09-05',123124.00,'2014-09-13','2014-09-05',5,8,111111111,'已付款','2014-09-26','423423',5453.00,'是',0,'',5,0,0,1410856588493),(54,'20140917154002429687',150,'测试合同','2014-09-06',1989.00,'2014-09-19','2014-09-28',5,8,123,'已付款','2014-09-19','123',5453.00,'是',0,'',5,0,0,1410939602639),(55,'20140917161211659340',150,'测试合同','2014-09-12',123124.00,'2014-09-13','2014-09-27',5,8,111111111,'已付款','2014-09-13','123',5453.00,'是',0,'',5,0,0,1410941531816),(56,'20140917161318809766',150,'测试合同','2014-09-11',1989.00,'2014-09-12','2014-09-21',5,8,111111111,'已付款','2014-09-04','423423',123.00,'是',0,'',5,0,0,1410941773831),(57,'20140917170106201771',150,'测试合同','2014-09-17',123124.00,'2014-09-17','2014-09-20',5,8,1,'已付款','2014-09-17','11111111111',1234.00,'是',90,'sdfsdf',5,0,0,1410944466360),(58,'20140917170226713049',150,'测试合同','2014-09-17',15401430.00,'2014-09-17','2014-09-17',5,8,123,'已付款','2014-09-17','11111111111',1234.00,'是',0,'',5,0,0,1410944654752),(59,'20140917170453461852',150,'嘻嘻哈哈','2014-09-17',15401430.00,'2014-09-12','2014-09-14',5,8,123456,'已付款','2014-09-17','436456',4235.00,'是',0,'',5,0,0,1410944702779),(60,'20140917171050318315',150,'测试合同','2014-09-17',123124.00,'2014-09-17','2014-09-17',5,8,123,'已付款','2014-09-05','423423',123.00,'是',0,'',5,0,0,1410945054731),(61,'20140917171404262685',150,'测试合同嘻嘻哈哈','2014-09-12',123456.00,'2014-09-17','2014-09-17',5,8,111111111,'已付款','2014-09-17','423423',5453.00,'是',90,'',5,0,0,1410945249200),(62,'20140918112349552343',150,'123','2014-09-11',123456.00,'2014-09-05','2014-09-21',5,8,123,'已付款','2014-09-06','11111111111',123.00,'是',0,'',5,0,0,1411010629552),(63,'20140918112440785151',150,'123','2014-09-03',1989.00,'2014-09-12','2014-09-28',5,8,123,'已付款','2014-09-05','423423',123.00,'是',0,'',5,0,0,1411010680785),(64,'20140918125219085000',150,'123','2014-08-27',123124.00,'2014-09-19','2014-09-21',-1,8,123,'已付款','2014-09-05','423423',1234.00,'是',0,'',5,0,0,1411015939259),(65,'20140918125336173075',150,'测试合同','2014-09-05',123124.00,'2014-09-12','2014-09-13',-1,8,123,'已付款','2014-09-05','123',5453.00,'是',0,'',5,0,0,1411016023228),(66,'20140918132237668282',150,'123','2014-09-05',123456.00,'2014-09-19','2014-09-14',5,8,123,'已付款','2014-09-03','423423',5453.00,'是',0,'',5,0,0,1411098029825),(67,'20140922174115420011',150,'213456','2014-09-12',123124.00,'2014-09-06','2014-09-14',5,8,123,'已付款','2014-09-06','423423',5453.00,'是',0,'',5,0,0,1411378875420),(68,'20140922174719570097',150,'1313131','2014-09-04',123456.00,'2014-09-12','2014-09-20',5,8,123,'已付款','2014-09-11','123',1234.00,'是',0,'',5,0,0,1411379239570),(69,'20140925105336506937',150,'测试-发明专利申请','2014-09-10',15000.00,'2014-09-11','2014-09-30',5,8,3,'已付款','2014-09-18','上海网易公司',150000.00,'是',0,'',5,0,0,1411613616626),(70,'20140925105743120781',150,'123','2014-09-06',123456.00,'2014-09-04','2014-09-21',5,8,123,'已付款','2014-09-12','423423',4235.00,'是',0,'',5,0,0,1411613863603),(71,'20141008112950150404',158,'客户,合同关联','2014-10-09',14444.00,'2014-10-08','2014-10-08',2,6,2,'未付款','2014-10-06','11111111',2222222.00,'是',0,'',2,0,0,1412738990150),(72,'20141008113341188154',150,'客户合同联合','2014-10-04',111.00,'2014-10-10','2014-10-03',2,1,111,'未付款','2014-10-10','11',111.00,'是',0,'',2,0,0,1412739667080),(73,'20141008114625511403',158,'11111','2014-10-17',11111.00,'2014-10-09','2014-10-11',2,6,111,'未付款','2014-12-06','11111',1111.00,'是',0,'',2,0,0,1412739985642),(74,'20141008114732104485',158,'11111','2014-10-17',11111.00,'2014-10-09','2014-10-11',2,6,111,'未付款','2014-10-08','11111',1111.00,'是',0,'',2,0,0,1412740052275),(75,'20141008114836576210',158,'11111','2014-10-17',1111.00,'2014-10-09','2014-10-02',2,6,111,'已付款','2014-10-08','1111',1111.00,'是',0,'',2,0,0,1412740116753),(76,'20141008151723198316',-1,'测试合同151','2014-11-13',1989.00,'2014-10-10','2014-10-12',5,-1,123,'已付款','2014-10-02','11111111111',123.00,'是',0,'',5,0,0,1412752643369),(77,'20141008151923909127',-1,'测试合同151','2014-11-13',1989.00,'2014-10-10','2014-10-12',5,-1,123,'已付款','2014-10-02','11111111111',123.00,'是',0,'',5,0,0,1412752764108),(78,'20141008152326480140',-1,'测试合同151','2014-11-13',1989.00,'2014-10-10','2014-10-12',5,-1,123,'已付款','2014-10-02','11111111111',123.00,'是',0,'',5,0,0,1412753006666),(79,'20141008152434711885',-1,'测试合同151','2014-11-13',1989.00,'2014-10-10','2014-10-12',5,-1,123,'已付款','2014-10-02','11111111111',123.00,'是',0,'',5,0,0,1412753074873),(80,'20141008152754456456',-1,'测试合同151','2014-11-13',1989.00,'2014-10-10','2014-10-12',5,-1,123,'已付款','2014-10-02','11111111111',123.00,'是',0,'',5,0,0,1412753274610),(81,'20141008152813021422',-1,'测试合同151','2014-11-13',1989.00,'2014-10-10','2014-10-12',5,-1,123,'已付款','2014-10-02','11111111111',123.00,'是',0,'',5,0,0,1412753293163),(82,'20141008153128574370',-1,'测试合同151','2014-11-13',1989.00,'2014-10-10','2014-10-12',5,-1,123,'已付款','2014-10-02','11111111111',123.00,'是',0,'',5,0,0,1412753488735),(83,'20141008153429975781',-1,'测试合同151','2014-11-13',1989.00,'2014-10-10','2014-10-12',5,-1,123,'已付款','2014-10-02','11111111111',123.00,'是',0,'',5,0,0,1412753670124),(84,'20141008153504765103',-1,'测试合同151','2014-11-13',1989.00,'2014-10-10','2014-10-12',5,-1,123,'已付款','2014-10-02','11111111111',123.00,'是',0,'',5,0,0,1412753704961),(85,'20141008154224874469',-1,'测试合同131','2014-10-09',123456.00,'2014-10-10','2014-09-20',5,-1,111111111,'已付款','2014-10-11','123',5453.00,'是',0,'',5,0,0,1412754145009),(86,'20141008154406748881',-1,'测试合同131','2014-10-09',123456.00,'2014-10-10','2014-09-20',5,-1,111111111,'已付款','2014-10-11','123',5453.00,'是',0,'',5,0,0,1412754246905),(87,'20141008164709419496',-1,'123','2014-10-02',1989.00,'2014-10-03','2014-10-18',5,-1,123,'未付款','2014-09-05','423423',123.00,'是',0,'',5,0,0,1412758029570),(88,'20141008165248830183',-1,'测试合同','2014-09-13',1989.00,'2014-10-03','2014-10-11',5,-1,123,'未付款','2014-10-11','423423',123.00,'是',0,'',5,0,0,1412758368937),(89,'20141008165350156745',-1,'测试合同','2014-09-13',1989.00,'2014-10-03','2014-10-11',5,-1,123,'未付款','2014-10-11','423423',123.00,'是',0,'',5,0,0,1412758430303),(90,'20141008170116885332',158,'123','2014-09-17',1989.00,'2014-10-10','2014-10-19',2,6,123,'已付款','2014-10-09','123',5453.00,'是',0,'',5,0,0,1412758877022),(91,'20141008181305845640',158,'测试合同','2014-10-04',123456.00,'2014-10-10','2014-10-17',2,6,123,'已付款','2014-10-16','123',1234.00,'是',0,'',5,0,0,1412835467723),(92,'20141008181410813407',158,'测试合同','2014-10-04',123456.00,'2014-10-10','2014-10-17',2,6,123,'已付款','2014-10-16','123',1234.00,'是',0,'',5,0,0,1412763250980),(93,'20141009140218862665',-1,'测试合同','2014-10-10',123456.00,'2014-10-11','2014-09-14',5,-1,123,'未付款','2014-10-11','436456',123.00,'是',0,'',5,0,0,1412834539062),(94,'20141009140332210675',-1,'测试合同','2014-10-10',123456.00,'2014-09-05','2014-10-04',5,-1,123,'已付款','2014-09-10','123',1234.00,'是',0,'',5,0,0,1412834612492),(95,'20141009140422031938',-1,'123','2014-10-25',1989.00,'2014-10-15','2014-10-19',5,-1,5,'已付款','2014-10-10','11111111111',1234.00,'是',0,'',5,0,0,1412834662171),(96,'20141009140558664973',-1,'123','2014-10-25',1989.00,'2014-10-15','2014-10-19',5,-1,5,'已付款','2014-10-10','11111111111',1234.00,'是',0,'',5,0,0,1412834758803),(97,'20141009140709958504',-1,'123','2014-10-25',1989.00,'2014-10-15','2014-10-19',5,-1,5,'已付款','2014-10-10','11111111111',1234.00,'是',0,'',5,0,0,1412834830122),(98,'20141009141035048887',-1,'123','2014-10-25',1989.00,'2014-10-15','2014-10-19',5,-1,5,'已付款','2014-10-10','11111111111',1234.00,'是',0,'',5,0,0,1412835035331),(99,'20141009141217796203',-1,'123','2014-10-25',1989.00,'2014-10-15','2014-10-19',5,-1,5,'已付款','2014-10-10','11111111111',1234.00,'是',0,'',5,0,0,1412835137945),(100,'20141009141302182478',-1,'123','2014-10-25',1989.00,'2014-10-15','2014-10-19',5,-1,5,'已付款','2014-10-10','11111111111',1234.00,'是',0,'',5,0,0,1412835182350),(101,'20141009141833624400',-1,'测试合同','2014-10-11',123124.00,'2014-10-17','2014-10-26',5,-1,123,'已付款','2014-09-27','423423',1234.00,'是',0,'',5,0,0,1412835513878),(102,'20141009141910421099',-1,'测试合同','2014-10-11',123124.00,'2014-10-17','2014-10-26',5,-1,123,'已付款','2014-09-27','423423',1234.00,'是',0,'',5,0,0,1412835550622),(103,'20141009142220846947',-1,'测试合同','2014-10-11',123124.00,'2014-10-17','2014-10-26',5,-1,123,'已付款','2014-09-27','423423',1234.00,'是',0,'',5,0,0,1412835740996),(104,'20141009142440039952',-1,'测试合同','2014-10-11',123124.00,'2014-10-11','2014-10-26',5,-1,123,'未付款','2014-09-07','11111111111',123456.00,'是',0,'',5,0,0,1412835880198),(105,'20141009142529727268',-1,'测试合同','2014-10-11',123124.00,'2014-10-11','2014-10-26',5,-1,123,'未付款','2014-09-07','11111111111',123456.00,'是',0,'',5,0,0,1412835929878),(106,'20141009142800340189',-1,'测试合同','2014-10-11',123124.00,'2014-10-11','2014-10-26',5,-1,123,'未付款','2014-09-07','11111111111',123456.00,'是',0,'',5,0,0,1412836080457),(107,'20141009144418787492',-1,'测试合同','2014-10-08',123124.00,'2014-10-04','2014-10-19',5,-1,123,'已付款','2014-10-25','11111111111',1234.00,'是',0,'',5,0,0,1412837058884),(108,'20141009165050781094',158,'嘻嘻哈哈','2014-10-09',1989.00,'2014-10-09','2015-10-09',2,6,111111111,'未付款','2014-10-09','423423',123.00,'是',0,'是test',5,0,0,1412844650990),(109,'20141009190422820380',159,'sdfsadf','2014-10-09',12.00,'2014-10-09','2014-10-09',5,6,11,'未付款','2014-10-09','alibaba',12.00,'是',0,'',1,0,0,1412852662980),(110,'20141009190518057492',157,'sdfsadf','2014-10-09',12.00,'2014-10-09','2014-10-09',5,6,11,'未付款','2014-10-09','alibaba',12.00,'是',0,'',1,0,0,1412852718237),(111,'20141009191105490188',156,'sdfsadf','2014-10-09',12.00,'2014-10-09','2014-10-17',1,6,11,'未付款','2014-10-09','alibaba',12.00,'是',0,'测试，感觉太操蛋了是短发是',1,0,0,1413303428853),(112,'20141010110343014178',160,'123','2014-10-09',5646.00,'2014-10-03','2014-10-19',12,1,4654,'已付款','2014-10-17','6456',64564.00,'是',0,'',10,0,0,1412910223179),(113,'20141010145413813399',160,'测试合同','2014-10-09',1989.00,'2014-10-17','2014-10-19',12,1,123,'已付款','2014-10-17','423423',1234.00,'是',0,'',5,0,0,1413270728490),(114,'20141010150111378319',160,'123','2014-10-11',5646.00,'2014-10-18','2014-10-18',12,1,11,'已付款','2014-10-17','6456',64564.00,'是',0,'',10,0,0,1412924471539),(115,'20141010150636823576',160,'123','2014-11-01',123.00,'2014-10-11','2014-10-18',12,1,132,'已付款','2014-10-17','6456',134.00,'是',1,'',10,0,0,1412924796944),(116,'20141010153145435167',160,'123','2014-10-10',123.00,'2014-11-01','2014-10-19',10,1,132,'未付款','2014-10-10','13',64564.00,'是',127,'213',10,1,0,1412994981180),(117,'20141010154804998526',160,'123456','2014-10-02',1989.00,'2014-10-11','2014-10-19',12,1,123,'未付款','2014-09-06','423423',1234.00,'是',0,'',5,1,0,1412994981136),(146,'20141010728',160,'123','2014-10-01',1989.00,'2014-10-18','2014-10-19',12,1,123,'未付款','2014-09-13','423423',5453.00,'是',0,'',5,1,0,1412994981057),(147,'20141010114',160,'123','2014-10-01',1989.00,'2014-10-18','2014-10-19',12,1,123,'未付款','2014-09-13','423423',5453.00,'是',0,'',5,1,0,1412993488340),(148,'20141011623',167,'测试合同','2014-10-02',123456.00,'2014-10-25','2014-10-26',1,6,123,'未付款','2014-10-09','423423',123.00,'是',0,'',13,0,0,1413300509819),(149,'20141011382',167,'123','2014-10-07',1989.00,'2014-10-24','2014-10-26',6,6,123,'未付款','2014-10-17','423423',123.00,'是',0,'',13,0,0,1413300509819),(150,'20141011962',167,'20140905095347836309','2014-10-10',13555134.00,'2014-10-11','2014-11-29',2,6,111333,'未付款','2014-10-11','asdgfg',12223.00,'是',0,'',5,1,0,1413172023609),(151,'20141011847',169,'测试合同','2014-10-11',1989.00,'2014-10-11','2014-10-31',5,6,123,'未付款','2014-10-11','123',5453.00,'是',123,'123',5,0,0,1413179418131),(152,'20141011820',169,'123','2014-10-11',5646.00,'2014-10-11','2014-10-31',10,6,132,'未付款','2014-10-17','13',64564.00,'是',0,'',5,0,0,1413179337499),(153,'20141011379',169,'123','2014-10-03',1989.00,'2014-10-02','2014-10-05',9,6,111111111,'未付款','2014-10-09','423423',0.00,'是',0,'',13,0,0,1413300509819),(154,'20141013892',169,'公司合同','2014-10-02',123456.00,'2014-10-04','2014-10-12',6,6,123,'未付款','2014-10-15','',0.00,'是',0,'',13,0,0,1413300509819),(155,'20141014684',173,'asdffffag','2014-10-17',13455.00,'2014-10-16','2014-10-17',10,1,2,'未付款','2014-10-10','',0.00,'是',0,'',6,0,0,1413275775546),(156,'20141015554',173,'sdfsadf','2014-10-09',12.00,'2014-10-13','2014-10-09',10,1,11,'未付款','2014-10-10','',0.00,'是',0,'sdf',1,0,1413303428853,1413303428853),(157,'20141015837',173,'胡伟测试','2014-10-09',12.00,'2014-10-15','2014-10-16',10,1,1221,'未付款','2014-10-10','',0.00,'是',0,'阿萨帝',1,0,1413303428853,1413303428853),(158,'20141015388',167,'胡伟10151','2014-10-14',1000.00,'2014-10-15','2014-10-16',2,6,12,'已付款','2014-10-15','的萨芬',1212.00,'是',0,'teste',2,0,1413337576169,1413340933137),(159,'20141015251',173,'测试上传文件','2014-10-09',1000.00,'2014-10-15','2014-10-16',2,1,11,'已付款','2014-10-15','11111',11111.00,'是',0,'',2,0,1413340220722,1413340220722),(160,'20141015798',173,'测试合同','2014-10-02',123456.00,'2014-10-19','2014-10-19',10,1,111111111,'已付款','2014-10-01','423423',1234.00,'是',0,'',5,0,1413343047684,1413343047684),(161,'20141015393',173,'新添加合同测试','2014-10-01',1989.00,'2014-10-02','2014-10-05',10,1,123,'已付款','2014-10-02','423423',123.00,'是',0,'',5,0,1413349980007,1413359357535),(162,'20141015955',173,'胡伟测试','2013-12-06',12.00,'2014-10-09','2014-12-12',10,1,10,'已付款','2014-10-10','阿萨德f',12.01,'是',1,'2',10,0,1413351268189,1413443224519),(163,'20141015633',173,'测试合同 案件','2014-10-02',1989.00,'2014-10-18','2014-10-12',10,1,123,'已付款','2014-10-09','423423',123.00,'是',0,'',5,0,1413351065811,1413353128146),(164,'20141015544',175,'易正清北京合同管理员测','2014-10-14',1000.00,'2014-10-14','2014-10-15',2,6,12,'已付款','1899-12-31','的萨芬',12.00,'是',0,'sdfsdf',13,0,1413358117719,1413369645124),(165,'20141015260',175,'胡伟10151','2014-10-14',1000.00,'2014-10-14','2014-10-16',2,6,12,'已付款','2014-10-15','的萨芬',12.00,'是',0,'是打发斯蒂芬',13,0,1413358117719,1413358117719),(166,'20141015234',175,'测试合同1122','2014-10-10',1989.00,'2014-10-04','2014-10-11',2,6,123,'已付款','2014-10-03','423423',1234.00,'是',0,'',5,0,1413360935625,1413364098837),(167,'20141015510',175,'测试合同1122','2014-10-10',1989.00,'2014-10-04','2014-10-11',2,6,123,'已付款','2014-10-03','423423',1234.00,'是',0,'',5,0,1413361189465,1413362611590),(168,'20141015650',174,'易正清北京合同管理员测','2014-10-15',1000.00,'2014-10-15','2014-10-15',2,6,2324243,'已付款','2014-10-15','的萨芬',12.00,'是',1,'sdfasdf',10,0,1413369034695,1413443224519),(169,'20141015956',176,'易正清北京合同管理员测','2014-10-15',234.00,'2014-10-15','2014-10-16',2,6,2324243,'已付款','2014-10-15','的萨芬',12.00,'是',0,'是短发是',13,0,1413369645124,1413369645124),(170,'20141015907',174,'胡伟10151','2014-10-15',234.00,'2014-10-15','2014-10-17',2,6,23,'已付款','2014-10-15','234234',2342.00,'是',0,'是打发斯蒂芬',13,0,1413369645124,1413369645124),(171,'20141015533',174,'测试保存后跳转','2014-10-03',1111.00,'2014-10-02','2014-10-09',2,6,1111,'已付款','2014-10-09','11',111.00,'是',0,'1111',2,0,1413370467188,1413444813460),(172,'20141015782',174,'测试保存后跳转','2014-10-03',1111.00,'2014-10-02','2014-10-09',2,6,1111,'已付款','2014-10-09','11',111.00,'是',0,'1111',2,0,1413370528872,1413370528872),(173,'20141015367',176,'易正清北京合同管理员测','2014-10-15',234.00,'2014-10-15','2014-10-15',2,6,11233,'已付款','2014-10-15','是打发斯蒂芬',234.00,'是',0,'撒地方223',13,0,1413370559009,1413370640290),(174,'20141015390',174,'易正清北京合同管理员测','2014-10-14',1000.00,'2014-10-15','2014-10-17',13,6,2324243,'已付款',NULL,'的萨芬',223.00,'是',1,'的算法',2,0,1413371367513,1413443725020),(175,'20141015833',174,'wl测试合同','2014-10-02',1989.00,'2014-10-12','2014-10-19',5,6,123,'未付款',NULL,'',0.00,'是',1,'',2,0,1413372177516,1413443725020),(176,'20141015553',174,'123','2014-10-02',1989.00,'2014-10-11','2014-10-19',2,6,123,'未付款',NULL,'',0.00,'是',0,'',5,0,1413372286164,1413372286164),(177,'20141015119',174,'易正清北京合同管理员测','2014-10-15',1000.00,'2014-10-15','2014-10-15',13,6,2324243,'已付款','2014-10-15','的萨芬',234.00,'是',1,'是打发斯蒂芬',2,0,1413372351477,1413443725020),(178,'20141016093',173,'123','2014-10-16',123.00,'2014-10-16','2014-10-30',10,1,132,'已付款',NULL,'',133.00,'是',1,'',2,0,1413432058961,1413443725020),(179,'20141016079',178,'测试用合同','2014-10-15',123.00,'2014-10-13','2014-10-17',8,4,123,'未付款','2014-10-17','123',213.00,'否',1,'qweqe',8,0,1413443364359,1413443364359),(180,'20141016092',178,'2222','2014-10-10',22222222.00,'2014-10-02','2014-10-01',8,4,111,'已付款','2014-10-08','1111',0.00,'是',1,'',2,0,1413443725020,1413443725020),(181,'20141016731',178,'123123123','2014-10-10',22222222.00,'2014-10-02','2014-10-01',8,4,111,'已付款','2014-10-08','1111',0.00,'是',1,'',2,0,1413443725020,1413443725020),(182,'20141016788',178,'测试用','2014-10-14',123.12,'2014-10-14','2014-10-16',8,4,1,'已付款','2014-10-25','123',123.00,'是',1,'2132123',8,0,1413444200819,1413444200819),(183,'20141016020',178,'eeeeeeeeeeeee','2014-10-09',1111.00,'2014-10-02','2014-10-11',2,4,11,'已付款','2014-10-06','11',0.00,'是',1,'',10,0,1413444191997,1413443224519),(184,'20141016960',167,'wwwwwwwwwwwww','2014-10-09',111.00,'2014-10-02','2014-10-09',2,6,111,'已付款','2014-10-10','11111111',0.00,'是',1,'',10,0,1413444588495,1413443224519),(185,'20141016508',178,'tttttttttttttt','2014-10-23',44444444.00,'2014-10-24','2014-10-16',2,4,4444,'已付款',NULL,'',1.00,'是',1,'',2,0,1413444588495,1413457461729),(186,'20141016098',178,'wlwlwlwlwl','2014-10-03',1989.00,'2014-10-04','2014-10-12',5,4,111111111,'已付款','2014-10-10','423423',123.00,'是',0,'',5,0,1413443863267,1413446389735),(187,'20141016406',167,'wl123456wl','2014-10-02',123124.00,'2014-10-03','2014-10-05',5,6,111111111,'未付款',NULL,'',0.00,'是',1,'',5,0,1413443863267,1413457952854),(188,'20141016025',181,'123','2014-10-10',1989.00,'2014-10-18','2014-10-19',5,6,123,'未付款',NULL,'',0.00,'是',0,'',2,0,1413446690611,1413447089823),(189,'20141016642',181,'123','2014-10-10',1989.00,'2014-10-18','2014-10-19',1,6,123,'未付款',NULL,'',0.00,'是',0,'',5,0,1413446690611,1413446690611),(190,'20141016203',181,'123','2014-10-10',1989.00,'2014-10-18','2014-10-19',1,6,123,'未付款',NULL,'',0.00,'是',0,'',5,0,1413447232394,1413447232394),(191,'20141016321',181,'123','2014-10-10',1989.00,'2014-10-18','2014-10-19',1,6,123,'未付款',NULL,'',0.00,'是',0,'',5,0,1413447232394,1413447232394),(192,'20141016799',181,'人人人人人人人人人人人人','2014-10-17',2222.00,'2014-10-03','2014-10-09',2,6,111,'未付款',NULL,'',0.00,'是',1,'',5,0,1413447250560,1413455994906),(193,'20141016643',181,'123','2014-10-10',1989.00,'2014-10-18','2014-10-19',1,6,123,'未付款',NULL,'',0.00,'是',2,'',5,0,1413447372457,1413458390131),(194,'20141016952',181,'柔柔弱弱','2014-10-02',2323.00,'2014-10-09','2014-10-01',2,6,22,'未付款',NULL,'',0.00,'是',1,'',2,0,1413447250560,1413458158804),(195,'20141016100',181,'5555','2014-10-04',2.00,'2014-10-12','2014-10-10',2,6,2,'未付款',NULL,'',0.00,'是',1,'',2,0,1413447516020,1413457973271),(196,'20141016524',181,'123456789','2014-10-09',1989.00,'2014-10-11','2014-10-12',5,6,123,'未付款',NULL,'',0.00,'是',1,'',5,0,1413448451757,1413456298406),(197,'20141016101',181,'1111111111111111111111111111111111','2014-10-03',1989.00,'2014-10-18','2014-10-19',5,6,123,'未付款',NULL,'',0.00,'是',0,'',5,1,1413448451757,1413447654536),(198,'20141016459',181,'11223345566778','2014-10-02',1989.00,'2014-10-11','2014-10-26',5,6,111111111,'未付款',NULL,'',0.00,'是',1,'',5,0,1413448451757,1413456011953),(199,'20141016505',181,'阿斯顿发生地方','2014-10-02',2222.00,'2014-10-02','2014-10-02',2,6,22,'未付款',NULL,'',0.00,'是',1,'1',5,0,1413447686496,1413455980969),(200,'20141016322',183,'千千万额','2014-10-21',123.00,'2014-10-18','2014-10-19',8,1,123,'未付款',NULL,'其外额',123.00,'否',1,'',8,1,1413450795233,1413457484109),(201,'20141016102',182,'wl111111111111111111111111','2014-10-10',123456.00,'2014-10-11','2014-10-12',5,6,123,'未付款',NULL,'',0.00,'是',1,'',10,0,1413453253102,1413457634072),(202,'20141016899',182,'wl5555555555555555555555555','2014-10-10',1989.00,'2014-09-19','2014-10-26',5,6,123,'未付款',NULL,'',0.00,'是',1,'',5,0,1413454204899,1413456190886);
/*!40000 ALTER TABLE `contracts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer_contacts`
--

DROP TABLE IF EXISTS `customer_contacts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer_contacts` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '联系人ID',
  `customer_id` bigint(20) NOT NULL COMMENT '客户编码',
  `name` varchar(50) COLLATE utf8mb4_bin NOT NULL COMMENT '姓名',
  `gender` varchar(3) COLLATE utf8mb4_bin NOT NULL COMMENT '性别',
  `position` varchar(50) COLLATE utf8mb4_bin NOT NULL,
  `office_phone` varchar(50) COLLATE utf8mb4_bin NOT NULL COMMENT '座机号',
  `mobile` varchar(50) COLLATE utf8mb4_bin NOT NULL COMMENT '手机号',
  `email` varchar(50) COLLATE utf8mb4_bin NOT NULL COMMENT '邮箱',
  `qq` varchar(50) COLLATE utf8mb4_bin NOT NULL,
  `address` varchar(100) COLLATE utf8mb4_bin NOT NULL COMMENT '地址',
  `markup` varchar(200) COLLATE utf8mb4_bin NOT NULL COMMENT '备注',
  `created_at` bigint(20) NOT NULL,
  `updated_at` bigint(20) NOT NULL,
  `operator_id` bigint(20) DEFAULT NULL,
  `is_deleted` bigint(20) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=264 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer_contacts`
--

LOCK TABLES `customer_contacts` WRITE;
/*!40000 ALTER TABLE `customer_contacts` DISABLE KEYS */;
INSERT INTO `customer_contacts` VALUES (136,150,'王者','男','经理','4515447','13522456859','876213774@163.com','856245885','北京市朝阳区28号','多个联系人之一',1411370311506,1411370311506,NULL,0),(137,150,'刘洋','女','主管','451256','13526595657','8458257@qq.com','879547','北京市朝阳区28号','aa',1411370311601,1411370311601,NULL,0),(143,152,'郑元','男','','','','8458257@qq.com','','北京胡同','',1411373200518,1411373200518,NULL,0),(145,153,'２３２３','男','','','','','','１２３１２３','',1411461509711,1411461509711,NULL,0),(146,151,'刘月','男','副经理','','','','','上海','',1411525091566,1411525091566,NULL,0),(147,151,'秦向','男','总经理','','','','','上海','',1411525091644,1411525091644,NULL,0),(156,154,'文件','男','','','','','','北京','',1411529155492,1411529155492,NULL,0),(158,155,'资料','男','','','','','','北京市朝阳区28号','',1411530535267,1411530535267,NULL,0),(164,157,'888','男','','','','','','1212','',1411531028423,1411531028423,NULL,0),(165,156,'请问请问','男','','','','','','去问去问','',1411531343834,1411531343834,NULL,0),(167,159,'嘻嘻哈哈','男','','','','','','12','',1411613784008,1411613784008,NULL,0),(170,158,'1111','男','','','','','','1111','',1412772775151,1412772775151,NULL,0),(172,160,'嘻嘻哈哈','女','打杂','123456','13522656589','123@89.com','111111','北京市朝阳区22号','备注',1412845482156,1412845482156,NULL,0),(174,162,'1111','男','','','','','','111','',1412937176103,1412937176103,NULL,0),(175,163,'1111','男','','','','','','111','',1412937205418,1412937205418,NULL,0),(176,163,'1111','男','','','','','','111','',1412937205508,1412937205508,NULL,0),(177,164,'222222222','女','','','','','','2222222','',1412937584207,1412937584207,NULL,0),(178,165,'222222222','女','','','','','','2222222','',1412937713428,1412937713428,NULL,0),(181,168,'sdasd','男','sadsad','asdasd','15330077113','sadasd@163.com','4546456','dasdas','sadasd',1413009793239,1413009793239,NULL,0),(189,170,'sdsad','男','asdas','asdasd','15330077113','sadasd@163.com','4454','sadsadsad','sadasd',1413184099177,1413184099177,NULL,0),(194,169,'sdsad','男','asdas','454564','15330077113','sadasd@163.com','4454','sadsadsad','sadasd',1413195846524,1413195846524,NULL,0),(205,171,'sdsad','男','asdas','454564','15330077113','sadasd@163.com','4454','sadsadsad','sadasd',1413255317970,1413255317970,NULL,0),(206,172,'测试联系人','女','终极测试','6325647','13526548547','333@123.com','','北京','1111111111',1413269656794,1413269656794,NULL,0),(208,173,'新建飞','男','阿斯顿发撒旦法','终极测试','13522656589','1201542697@163.com','123123','asdf','asdf',1413272951374,1413272951374,NULL,0),(212,175,'111','男','','','','','','北京上传文件','',1413360501439,1413360501439,NULL,0),(213,174,'111','男','','','','','','北京上传文件','',1413361068529,1413361068529,NULL,0),(215,176,'啊啊','男','','','','','','啊啊','',1413361068529,1413361068529,NULL,0),(219,178,'12312','男','qweqwe','qweqe','18623061722','','123123','12312312','',1413442206815,1413442206815,NULL,0),(225,179,'sdfsdf','男','','','','','','asdf asdf','',1413445318417,1413445318417,NULL,0),(231,167,'男人','男','','','','','','44444','',1413445769293,1413445769293,NULL,0),(235,180,'啊啊','男','','','','','','北京上d传文件 ','',1413445958659,1413445958659,NULL,0),(236,180,'多个','男','','','','','','啊','',1413445958659,1413445958659,NULL,0),(237,177,'测试人员','女','','1111','','','','北京','',1413445958659,1413445958659,NULL,0),(238,181,'34343','男','','','','','','北京上传文件','',1413446818743,1413446818743,NULL,0),(249,183,'123','男','','','','','','213其外额','',1413448884526,1413448884526,NULL,0),(254,184,'11111','女','','','','','','111111111','',1413448884526,1413448884526,NULL,0),(257,185,'阿斯顿','男','','','','','','撒旦法','',1413448884526,1413448884526,NULL,0),(262,182,'88','男','','','','735556911@qq.com','','111','',1413452890160,1413452890160,NULL,0),(263,161,'测试','男','','','','','','啊啊啊','',1413456858937,1413456858937,NULL,0);
/*!40000 ALTER TABLE `customer_contacts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer_dealers`
--

DROP TABLE IF EXISTS `customer_dealers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer_dealers` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `customer_id` bigint(20) DEFAULT NULL,
  `dealer_id` bigint(20) DEFAULT NULL,
  `operator_id` bigint(20) DEFAULT NULL,
  `created_at` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=359 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer_dealers`
--

LOCK TABLES `customer_dealers` WRITE;
/*!40000 ALTER TABLE `customer_dealers` DISABLE KEYS */;
INSERT INTO `customer_dealers` VALUES (144,150,2,2,1411370311203),(145,150,3,2,1411370311278),(146,150,5,2,1411370311336),(152,152,3,2,1411373200340),(154,153,2,2,1411461509490),(155,151,2,6,1411525091244),(156,151,6,6,1411525091299),(157,151,1,6,1411525091355),(166,154,2,2,1411529155259),(168,155,2,2,1411530535033),(174,157,5,5,1411531028236),(175,156,2,2,1411531343460),(177,159,5,5,1411613783531),(181,158,2,10,1412772774896),(183,160,12,10,1412845481955),(185,162,2,2,1412937175957),(186,163,2,2,1412937205219),(187,164,2,2,1412937584021),(188,165,2,2,1412937713272),(196,168,9,9,1413009793045),(204,170,9,9,1413184099035),(208,169,9,2,1413195846289),(264,171,9,9,1413255317970),(265,172,10,10,1413269656794),(267,173,10,2,1413272951374),(271,175,2,1,1413360501439),(272,174,2,2,1413361068529),(274,176,2,2,1413361068529),(282,178,8,8,1413442206815),(299,179,1,1,1413445318417),(321,167,2,2,1413445769293),(322,167,1,2,1413445769293),(323,167,9,2,1413445769293),(324,167,5,2,1413445769293),(325,167,6,2,1413445769293),(328,180,2,2,1413445958659),(329,180,6,2,1413445958659),(330,180,13,2,1413445958659),(331,180,5,2,1413445958659),(332,177,10,2,1413445958659),(333,181,1,1,1413446818743),(344,183,8,2,1413448884526),(349,184,2,2,1413448884526),(352,185,2,2,1413448884526),(357,182,2,10,1413452890160),(358,161,2,10,1413456858670);
/*!40000 ALTER TABLE `customer_dealers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customers` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '客户编码',
  `name` varchar(50) COLLATE utf8mb4_bin NOT NULL COMMENT '客户名称',
  `dealer_id` bigint(20) DEFAULT NULL COMMENT '法务 ，销售 ，处理人',
  `organization_id` bigint(20) NOT NULL COMMENT '所属公司',
  `contact_id` bigint(20) DEFAULT NULL COMMENT '客户默认联系人',
  `status` bigint(20) NOT NULL COMMENT '客户性质',
  `industry` bigint(20) NOT NULL COMMENT '客户行业',
  `entering_time` varchar(50) COLLATE utf8mb4_bin NOT NULL COMMENT '录入时间',
  `certificate_number` varchar(50) COLLATE utf8mb4_bin NOT NULL COMMENT '机构代码/身份证号',
  `address` varchar(100) COLLATE utf8mb4_bin NOT NULL COMMENT '客户地址',
  `zip_code` varchar(6) COLLATE utf8mb4_bin NOT NULL COMMENT '邮编',
  `markup` varchar(200) COLLATE utf8mb4_bin NOT NULL COMMENT '备注',
  `created_at` bigint(20) NOT NULL COMMENT '创建日期',
  `updated_at` bigint(20) NOT NULL COMMENT '更新事件',
  `operator_id` bigint(20) DEFAULT NULL,
  `is_deleted` bigint(255) DEFAULT '0' COMMENT '逻辑删除标记字段',
  `file` varchar(200) CHARACTER SET utf8mb4 DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=186 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES (150,'北京天阳',2,1,136,1,14,'2014-09-22 15:18','112123','北京市朝阳区28号','123456','多个法务 多个联系人',1411370311129,1412845738635,10,1,NULL),(151,'上海天力',2,1,146,2,1,'2014-09-22 15:20','78478AFASDF','上海','586514','多个法务',1411370451446,1411525091701,6,0,NULL),(152,'北京论证',3,1,143,1,21,'2014-09-22 16:06','123123WWWW','北京胡同','','所属公司，跟法务所属公司，是否要过滤啊？',1411373200266,1412845355743,10,1,NULL),(153,'北京论证１１１',2,6,145,1,13,'2014-09-23 16:37','','１２３１２３','','',1411461452322,1411461509783,2,0,NULL),(154,'上传文件',2,6,156,1,1,'2014-09-24 10:26','','北京市朝阳区28号','','',1411525603569,1411529155590,2,0,'16/ed/i0g40fzy7at.jpeg'),(155,'资料上传校验',2,6,158,2,1,'2014-09-24 11:48','','北京','','',1411530514680,1411530535379,2,0,'29/9m/i0g4u32x81o.jpg'),(156,'上传文件测试2',2,6,165,1,1,'2014-09-24 11:49','','去问去问','','',1411530576870,1411531343907,2,0,''),(157,'123',5,6,164,2,14,'2014-09-24 11:57','','1212','','',1411531028157,1411531028577,5,0,'1z/6g/i0g54k2v8z0.jpg'),(158,'上传多个文件',2,6,170,3,14,'2014-09-24 17:47','','1111','','',1411552062930,1412772775223,10,0,''),(159,'123',5,6,167,1,13,'2014-09-25 10:56','123344','1231','102104','',1411613783427,1411613784241,5,0,'r/n0/i0hiedrf1j.'),(160,'肯德基',12,1,172,6,10,'2014-10-09 17:04','','北京市朝阳区22号','123123','',1412845466044,1412845482217,10,0,''),(161,'上传多个文件测试',2,6,263,1,1,'2014-10-10 18:09','','啊啊啊','','',1412935756367,1413456859082,10,0,''),(162,'111',2,6,174,2,1,'2014-10-10 18:32','','111','','',1412937175888,1412937176204,2,0,''),(163,'111',2,6,175,2,1,'2014-10-10 18:33','','111','','',1412937205149,1412937205608,2,0,''),(164,'222222',2,6,177,4,13,'2014-10-10 18:39','','2222222','','',1412937583951,1412937584265,2,0,''),(165,'222222',2,6,178,4,13,'2014-10-10 18:41','','2222222','','',1412937713195,1412937713521,2,0,''),(167,'222222111',2,6,231,1,13,'2014-10-10 18:56','','4444','','',1412938603224,1413445769293,2,0,''),(168,'测试',9,6,181,4,13,'2014-10-11 14:43','464456','1111','','',1413009792953,1413009793365,9,0,''),(169,'测试1',9,6,194,1,14,'2014-10-11 14:48','','sadsadsad','','',1413010107961,1413195846589,9,0,''),(170,'测试2',9,6,189,2,13,'2014-10-13 15:08','','sadsadsad','','',1413184098763,1413184099262,9,0,''),(171,'测试3',9,2,205,3,14,'2014-10-14 14:27','464456','1111','','',1413255317970,1413255317970,9,0,''),(172,'易清',10,1,206,1,16,'2014-10-14 14:57','123134213','北京市朝阳区','123456','客户新加内容',1413269656794,1413269656794,10,0,''),(173,'京港酒店',10,1,208,1,15,'2014-10-14 16:45','GT-89374213','111','123123','',1413276154759,1413272951374,10,0,''),(174,'测试上传文件',2,6,213,2,13,'2014-10-15 14:49','','北京上传文件','','',1413355669196,1413361068529,2,0,''),(175,'测试上传文件',2,6,212,2,13,'2014-10-15 14:50','','北京上传文件','','',1413355781262,1413360501439,2,0,''),(176,'客户测试',2,6,215,1,1,'2014-10-15 17:34','','啊啊','','',1413361068529,1413361068529,2,0,''),(177,'易清',10,1,237,1,16,'2014-10-16 14:21','123134213','北京','','',1413432058961,1413445958659,2,0,''),(178,'测试客户',8,4,219,1,17,'2014-10-16 15:00','sdaasdasd','12312312','123123','adsdd',1413442206815,1413447892547,8,1,''),(179,'测试上传文件test',1,6,225,1,1,'2014-10-16 15:43','234234','北京上传文件','310052','asdfsf',1413445318417,1413445318417,1,0,''),(180,'测试保存',2,6,235,1,1,'2014-10-16 15:53','','北京上d传文件','','',1413445958659,1413445958659,2,0,''),(181,'测试上传文件23',1,6,238,1,1,'2014-10-16 16:07','234234','wangshang road 699#','310052','sdfsdf',1413446818743,1413446818743,1,0,''),(182,'222222111',2,6,262,4,13,'2014-10-16 16:56','','111','','',1413448884526,1413452890160,10,0,''),(183,'测试客户123',8,1,249,4,13,'2014-10-16 17:24','阿斯顿','完全额前万恶123 企鹅企鹅2','123123','123',1413450795233,1413448884526,2,0,''),(184,'1111111111111',2,6,254,2,13,'2014-10-16 17:35','','111111111','','',1413448884526,1413448884526,2,0,''),(185,'测试联系人新建，地址为客户地址',2,6,257,1,13,'2014-10-16 17:39','','撒旦法','','',1413448884526,1413448884526,2,0,'');
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `departments`
--

DROP TABLE IF EXISTS `departments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `departments` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `parent_id` bigint(20) DEFAULT NULL,
  `organization_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departments`
--

LOCK TABLES `departments` WRITE;
/*!40000 ALTER TABLE `departments` DISABLE KEYS */;
INSERT INTO `departments` VALUES (1,'易清总公司',NULL,1),(2,'易清北京分公司',1,2),(3,'易清重庆分公司',1,3),(4,'易清上海分公司',1,4),(5,'易正达总公司',NULL,5),(6,'易正达北京分公司',5,6),(7,'易正达深圳分公司',5,7),(8,'易正达上海分公司',5,8),(9,'易正达重庆分公司',5,9),(10,'董事会',5,5),(11,'编辑部',5,5),(12,'客服部',5,5),(13,'专利部',5,5),(14,'商标版权部',5,5),(15,'总裁办',5,5),(16,'人力资源部',5,5),(17,'人力资源部',6,6),(18,'人力资源部',7,7),(19,'人力资源部',8,8),(20,'人力资源部',9,9),(21,'客服部',6,6),(22,'客服部',7,7),(23,'客服部',8,8),(24,'客服部',9,9),(25,'培训部',6,6),(26,'培训部',7,7),(27,'培训部',8,8),(28,'培训部',9,9),(29,'法务一部',6,6),(30,'法务一部',7,7),(31,'法务一部',8,8),(32,'法务一部',9,9),(33,'法务二部',6,6),(34,'法务二部',7,7),(35,'法务二部',8,8),(36,'法务二部',9,9),(37,'法务三部',6,6),(38,'法务三部',7,7),(39,'法务三部',8,8),(40,'法务三部',9,9),(41,'财务结算中心',5,5),(42,'财务结算中心',6,6),(43,'财务结算中心',7,7),(44,'财务结算中心',8,8),(45,'财务结算中心',9,9);
/*!40000 ALTER TABLE `departments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `options`
--

DROP TABLE IF EXISTS `options`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `options` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `opt_value` varchar(20) COLLATE utf8mb4_bin NOT NULL,
  `opt_title` varchar(100) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `opt_type` varchar(20) COLLATE utf8mb4_bin NOT NULL,
  `opt_selected` bigint(20) NOT NULL,
  `opt_order` bigint(20) DEFAULT NULL COMMENT '排序，序号越小越靠前',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `options`
--

LOCK TABLES `options` WRITE;
/*!40000 ALTER TABLE `options` DISABLE KEYS */;
INSERT INTO `options` VALUES (1,'1','普通客户','CUS_STATUS',1,0),(2,'2','VIP客户','CUS_STATUS',0,0),(3,'3','未成单客户','CUS_STATUS',0,0),(4,'4','战略客户','CUS_STATUS',0,0),(5,'5','其他客户','CUS_STATUS',0,0),(6,'1','农林牧渔','INDUSTRY',0,0),(7,'2','医药卫生','INDUSTRY',0,0),(8,'3','建筑建材','INDUSTRY',0,0),(9,'4','冶金矿产','INDUSTRY',0,0),(10,'5','石油化工','INDUSTRY',0,0),(11,'6','水利水电','INDUSTRY',0,0),(12,'7','交通运输','INDUSTRY',0,0),(13,'8','信息产业','INDUSTRY',0,0),(14,'9','机械机电','INDUSTRY',0,0),(15,'10','轻工食品','INDUSTRY',0,0),(16,'11','服装纺织','INDUSTRY',0,0),(17,'12','专业服务','INDUSTRY',0,0),(18,'13','安全防护','INDUSTRY',0,0),(19,'14','环保绿化','INDUSTRY',0,0),(20,'15','旅游休闲','INDUSTRY',0,0),(21,'16','办公文教','INDUSTRY',0,0),(22,'17','电子电工','INDUSTRY',0,0),(23,'18','家居用品','INDUSTRY',0,0),(24,'19','物资','INDUSTRY',0,0),(25,'20','包装','INDUSTRY',0,0),(26,'21','体育','INDUSTRY',0,0),(27,'22','其他','INDUSTRY',0,0),(28,'6','沉睡客户','CUS_STATUS',0,0),(29,'patent','专利','CON_TYPE',0,10),(30,'trademark','商标','CON_TYPE',0,9),(31,'copyright','版权','CON_TYPE',0,8),(32,'project','项目','CON_TYPE',0,7),(33,'law','法律','CON_TYPE',0,6),(34,'appreciation','增值','CON_TYPE',0,5),(35,'trainning','培训','CON_TYPE',0,4),(36,'planing','策划','CON_TYPE',0,3),(37,'propertyright','产权运用','CON_TYPE',0,2),(38,'trusteeship','知识产权托管','CON_TYPE',0,1),(39,'other','其他','CON_TYPE',0,0),(40,'patent_order','专利下单','WFL_TYPE',0,0),(41,'trademark_order','商标下单','WFL_TYPE',0,1),(42,'copyright_order','版权下单','WFL_TYPE',0,2),(43,'0','处理中','CON_STATE',0,0),(44,'1','作废','CON_STATE',0,1),(45,'2','完成','CON_STATE',0,2);
/*!40000 ALTER TABLE `options` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `organizations`
--

DROP TABLE IF EXISTS `organizations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `organizations` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT '',
  `description` varchar(50) DEFAULT '',
  `is_deleted` tinyint(1) DEFAULT '0',
  `updated_at` bigint(20) NOT NULL,
  `created_at` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_orgs_name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `organizations`
--

LOCK TABLES `organizations` WRITE;
/*!40000 ALTER TABLE `organizations` DISABLE KEYS */;
INSERT INTO `organizations` VALUES (1,'易清总公司','',0,1409033149000,1409033149000),(2,'易清北京分公司','',0,1409033149000,1409033149000),(3,'易清重庆分公司','',0,1409033149000,1409033149000),(4,'易清上海分公司','',0,1409033149000,1409033149000),(5,'易正达总公司','',0,1409033149000,1409033149000),(6,'易正达北京分公司','',0,1409033149000,1409033149000),(7,'易正达深圳分公司','',0,1409033149000,1409033149000),(8,'易正达上海分公司','',0,1409033149000,1409033149000),(9,'易正达重庆分公司','',0,1409033149000,1409033149000);
/*!40000 ALTER TABLE `organizations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `permissions`
--

DROP TABLE IF EXISTS `permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `permissions` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` varchar(255) NOT NULL,
  `permission_type` varchar(20) NOT NULL,
  `category` varchar(30) NOT NULL,
  `order_num` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_perms_name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `permissions`
--

LOCK TABLES `permissions` WRITE;
/*!40000 ALTER TABLE `permissions` DISABLE KEYS */;
INSERT INTO `permissions` VALUES (1,'/admin/permissions','角色权限','module','admin',1),(2,'/admin/user_roles','角色分配','module','admin',2),(3,'/human/staffs','雇员管理','module','human',1),(4,'/customer/search','客户查询','module','customer',1),(5,'/customer/search/all','查询所有客户','func','customer',2),(6,'/customer/search/org','查询本公司客户','func','customer',3),(7,'/customer/search/sub','查询下属客户','func','customer',4),(8,'/customer/search/self','查询自己的客户','func','customer',5),(9,'/customer/edit','修改客户','module','customer',8),(10,'/customer/add','添加客户','module','customer',6),(11,'/customer/delete','删除客户','module','customer',7),(12,'/customer/view','查看客户详情','func','customer',9),(13,'/customer/import','导入客户','func','customer',10),(14,'/customer/export','导出客户','func','customer',11),(15,'/customer/email','给客户发送邮件','func','customer',12),(16,'/contract/search','合同查询','func','contract',1),(17,'/contract/search/all','查询所有合同','func','contract',2),(18,'/contract/search/org','查询本公司合同','func','contract',3),(19,'/contract/search/sub','查询下属合同','func','contract',4),(20,'/contract/search/self','查询自己的合同','func','contract',5),(22,'/contract/edit','修改合同','func','contract',8),(24,'/contract/add','添加合同','func','contract',6),(25,'/contract/delete','删除合同','func','contract',7),(26,'/contract/view','查看合同详情','func','contract',9),(27,'/contract/export','导出合同','func','contract',10),(28,'/admin/workflow_state','工作流状态管理','module','admin',4),(29,'/workflow/search','工作流查询','module','workflow',1),(30,'/workflow/search/all','查询所有的工作流','func','workflow',2),(31,'/workflow/search/org','查询本公司的工作流','func','workflow',3),(32,'/workflow/search/sub','查询下属的工作流','func','workflow',4),(35,'/workflow/search/self','查询自己的工作流','func','workflow',5),(36,'/admin','系统管理','main_module','admin',0),(37,'/admin/config','配置管理','module','admin',3),(38,'/customer','客户管理','main_module','customer',0),(39,'/human','人事系统','main_module','human',0),(40,'/human/salary','薪资管理','module','human',2),(41,'/human/performance','绩效管理','module','human',3),(42,'/workflow','工作流','main_module','workflow',0),(43,'/contract','合同管理','main_module','contract',0),(45,'/workflow/data_upload','资料上传','func','workflow',6);
/*!40000 ALTER TABLE `permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profile_basics`
--

DROP TABLE IF EXISTS `profile_basics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `profile_basics` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) NOT NULL,
  `mobile` varchar(50) DEFAULT '',
  `gender` varchar(3) DEFAULT '',
  `office_phone` varchar(50) DEFAULT '',
  `office_city` varchar(50) DEFAULT '',
  `organization_id` bigint(20) NOT NULL,
  `department` varchar(50) DEFAULT '',
  `position` varchar(50) DEFAULT '',
  `grade` varchar(50) DEFAULT '',
  `hometown` varchar(50) DEFAULT '',
  `birthday` date DEFAULT NULL,
  `entry_day` date DEFAULT NULL,
  `conversion_day` date DEFAULT NULL,
  `qq` varchar(50) DEFAULT '',
  `address` varchar(100) DEFAULT '',
  `urgent_mobile` varchar(100) DEFAULT '',
  `ethnic` varchar(10) DEFAULT '',
  `household` varchar(50) DEFAULT '',
  `household_character` varchar(10) DEFAULT '',
  `signature` varchar(50) DEFAULT '',
  `updated_at` bigint(20) NOT NULL,
  `created_at` bigint(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profile_basics`
--

LOCK TABLES `profile_basics` WRITE;
/*!40000 ALTER TABLE `profile_basics` DISABLE KEYS */;
INSERT INTO `profile_basics` VALUES (1,1,'18042400707','男','18042400707','北京',6,'29','副总裁','无','文化街道3#901','1979-07-07','2014-06-19','2014-06-19','3314672','安苑北里10栋406','18657121775','汉','重庆万州','外埠城镇','',1412844546220,1408811924648),(2,2,'18611434363','男','','北京',6,'29','WEB前端','无','辽宁丹东','1989-09-29','2014-08-07','2014-08-07','876213774','北京市天通苑半截塔村','13644566321','汉','辽宁丹东','外部农业','',1411454586375,1408955567861),(3,3,'13552122614','女','','北京',6,'29','软件工程师','无','湖南','2014-08-28','2013-08-16','2013-11-16','1599685149','北京','13552122614','汉','湖南','外部农业','',1411123262074,1409205597450),(5,5,'13651014301','男','','北京',6,'29','python开发工程师','L1','北京市延庆县永宁镇阜民街','1989-12-09','2014-09-01','2014-12-01','374401830','北京市昌平区半截塔村','15810293050','汉','北京市延庆县永宁镇阜民街','本市城镇','',1412844529866,1410256964928),(6,6,'18910912335','男','010-6542636','北京',6,'29','软件工程师','无','景德镇','2009-09-03','2014-09-09','2014-12-09','851909956','景德镇','15842306519','汉','江西','外部农业','',1413359276577,1411006088606),(7,7,'13979850145','男','','65465',2,'2','331654','334165','景德镇','2014-09-11','2014-09-19','2014-09-13','8519666544666444','北京','13843215365','11123','江西','外埠城镇','',1411010383369,1411010383369),(8,8,'18630617227','男','','北京',1,'1','python','L1','河北','2014-09-03','2014-09-22','2014-09-26','812708519','天通苑','13522658475','汉','河北','外埠城镇','',1411664816065,1411664816065),(9,9,'15330077113','男','','北京',6,'29','web前端','L1','山西','2014-09-25','2014-09-25','2014-11-25','471412740','北京','15330077113','汉','山西','外埠城镇','',1411956766226,1411640409987),(10,10,'15801325602','女','','北京',1,'1','无','L1','湖北','2014-09-01','2014-09-25','2014-09-25','735556911','北京','18611434363','汉','湖北','外埠城镇','',1411641308428,1411640856864),(11,11,'13522659568','男','','北京',1,'1','北京','北京','北京','2014-09-03','2014-08-28','2014-09-04','253625666','北京','13522659586','汉','北京','本市城镇','',1411711357926,1411711357926),(12,12,'13612345678','女','','北京',1,'1','111','111','北京','2014-10-08','2014-10-09','2014-10-09','876213774','北京','13622492375','汉','北京','本市城镇','',1412733170906,1412733170906),(13,13,'18042400707','男','','北京',6,'29','哈哈','呵呵','北京','2014-10-14','2014-10-14','2014-10-14','3314672','wangshang road 699#','18657128771','汉族','梦幻高','外埠城镇','',1413297432532,1413296430857),(14,14,'18042400707','男','18042400707','hangzhou',5,'14','哈哈','呵呵','重庆万州','2014-10-16','2014-10-16','2014-10-16','3314672','安苑北里10栋406','18657121775','汉族','梦幻高','外埠城镇','',1413446818743,1413446818743);
/*!40000 ALTER TABLE `profile_basics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role_permissions`
--

DROP TABLE IF EXISTS `role_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `role_permissions` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `role_name` varchar(50) NOT NULL,
  `permission_name` varchar(100) NOT NULL,
  `created_at` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_ropers_rname_pname` (`role_name`,`permission_name`),
  KEY `idx_ropers_rname` (`role_name`)
) ENGINE=InnoDB AUTO_INCREMENT=948 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role_permissions`
--

LOCK TABLES `role_permissions` WRITE;
/*!40000 ALTER TABLE `role_permissions` DISABLE KEYS */;
INSERT INTO `role_permissions` VALUES (41,'human','/human/staffs',1410428401343),(628,'custom_service','/customer',1413015450174),(629,'custom_service','/customer/search',1413015450235),(630,'custom_service','/customer/search/sub',1413015450290),(631,'custom_service','/customer/add',1413015450346),(632,'custom_service','/customer/edit',1413015450422),(633,'custom_service','/customer/export',1413015450599),(634,'custom_service','/customer/email',1413015450774),(635,'custom_service','/workflow',1413015450863),(636,'custom_service','/workflow/search',1413015450918),(637,'custom_service','/workflow/search/org',1413015450974),(638,'custom_service','/workflow/search/self',1413015451030),(647,'sub_ceo','/customer/search',1413016391493),(648,'sub_ceo','/workflow',1413016391647),(649,'sub_ceo','/workflow/search',1413016391782),(650,'sub_ceo','/workflow/search/org',1413016391936),(651,'sub_ceo','/contract/search',1413016391995),(652,'sub_ceo','/contract/search/sub',1413016392104),(653,'sub_ceo','/contract/add',1413016392257),(654,'sub_ceo','/contract/edit',1413016392347),(655,'sub_ceo','/contract/view',1413016392437),(778,'legal_sales','/customer/search',1413345376451),(779,'legal_sales','/customer/search/self',1413345376451),(780,'legal_sales','/customer/add',1413345376451),(781,'legal_sales','/customer/edit',1413345376451),(782,'legal_sales','/workflow',1413345376451),(783,'legal_sales','/workflow/search',1413345376451),(784,'legal_sales','/workflow/search/self',1413345376451),(785,'legal_sales','/contract/search',1413345376451),(786,'legal_sales','/contract/search/self',1413345376451),(787,'legal_sales','/contract/add',1413345376451),(788,'legal_sales','/contract/view',1413345376451),(789,'legal_sales','/contract/export',1413345376451),(843,'contract_manager','/customer',1413352744447),(844,'contract_manager','/customer/search',1413352744447),(845,'contract_manager','/customer/search/org',1413352744447),(846,'contract_manager','/customer/view',1413352744447),(847,'contract_manager','/workflow',1413352744447),(848,'contract_manager','/workflow/search',1413352744447),(849,'contract_manager','/workflow/search/org',1413352744447),(850,'contract_manager','/workflow/search/sub',1413352744447),(851,'contract_manager','/workflow/search/self',1413352744447),(852,'contract_manager','/contract',1413352744447),(853,'contract_manager','/contract/search',1413352744447),(854,'contract_manager','/contract/search/org',1413352744447),(855,'contract_manager','/contract/add',1413352744447),(856,'contract_manager','/contract/delete',1413352744447),(857,'contract_manager','/contract/edit',1413352744447),(858,'contract_manager','/contract/view',1413352744447),(859,'contract_manager','/contract/export',1413352744447),(860,'contract_manager','/contract/edit_canceled',1413352744447),(919,'legal_sales_director','/admin',1413459582274),(920,'legal_sales_director','/admin/permissions',1413459582368),(921,'legal_sales_director','/admin/user_roles',1413459582467),(922,'legal_sales_director','/admin/config',1413459582530),(923,'legal_sales_director','/admin/workflow_state',1413459582618),(924,'legal_sales_director','/customer',1413459582686),(925,'legal_sales_director','/customer/search',1413459582752),(926,'legal_sales_director','/customer/search/sub',1413459582819),(927,'legal_sales_director','/customer/search/self',1413459582989),(928,'legal_sales_director','/customer/add',1413459583086),(929,'legal_sales_director','/customer/edit',1413459583192),(930,'legal_sales_director','/customer/view',1413459583264),(931,'legal_sales_director','/customer/import',1413459583363),(932,'legal_sales_director','/customer/export',1413459583422),(933,'legal_sales_director','/customer/email',1413459583486),(934,'legal_sales_director','/human',1413459583545),(935,'legal_sales_director','/human/staffs',1413459583635),(936,'legal_sales_director','/workflow',1413459583708),(937,'legal_sales_director','/workflow/search',1413459583808),(938,'legal_sales_director','/workflow/search/sub',1413459583908),(939,'legal_sales_director','/workflow/search/self',1413459584008),(940,'legal_sales_director','/contract',1413459584151),(941,'legal_sales_director','/contract/search',1413459584286),(942,'legal_sales_director','/contract/search/all',1413459584374),(943,'legal_sales_director','/contract/search/sub',1413459584431),(944,'legal_sales_director','/contract/search/self',1413459584497),(945,'legal_sales_director','/contract/edit',1413459584553),(946,'legal_sales_director','/contract/view',1413459584614),(947,'legal_sales_director','/contract/export',1413459584686);
/*!40000 ALTER TABLE `role_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roles` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `description` varchar(255) NOT NULL,
  `updated_at` bigint(20) NOT NULL,
  `created_at` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_roles_name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'admin','系统管理员',1408811924634,1408376245698),(2,'human','人事管理员',1408811924634,1408376245698),(3,'legal_sales','法务',1408811924634,1408376245698),(4,'legal_sales_director','法务主任',1408811924634,1408376245698),(5,'custom_service','子公司客服',0,0),(6,'contract_manager','合同管理员',0,0),(7,'sub_ceo','子公司老总',0,0),(8,'patent_register_staff','专利立案人员',0,0),(9,'trademark_register_staff','商标立案人员',0,0),(10,'copyright_register_staff','版权立案人员',0,0);
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `state_roles`
--

DROP TABLE IF EXISTS `state_roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `state_roles` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `state_id` bigint(20) NOT NULL,
  `role_id` bigint(20) NOT NULL,
  `created_at` bigint(20) NOT NULL,
  `updated_at` bigint(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `state_roles`
--

LOCK TABLES `state_roles` WRITE;
/*!40000 ALTER TABLE `state_roles` DISABLE KEYS */;
/*!40000 ALTER TABLE `state_roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test`
--

DROP TABLE IF EXISTS `test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `test` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) COLLATE utf8mb4_bin NOT NULL,
  `type` varchar(45) COLLATE utf8mb4_bin NOT NULL,
  `age` varchar(45) COLLATE utf8mb4_bin NOT NULL,
  `created_at` bigint(20) NOT NULL,
  `updated_at` bigint(20) NOT NULL,
  `operator_id` bigint(20) NOT NULL,
  `is_deleted` bigint(20) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test`
--

LOCK TABLES `test` WRITE;
/*!40000 ALTER TABLE `test` DISABLE KEYS */;
/*!40000 ALTER TABLE `test` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_roles`
--

DROP TABLE IF EXISTS `user_roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_roles` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) NOT NULL,
  `role_id` bigint(20) NOT NULL,
  `created_at` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_userroles_uid_rid` (`user_id`,`role_id`)
) ENGINE=InnoDB AUTO_INCREMENT=213 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_roles`
--

LOCK TABLES `user_roles` WRITE;
/*!40000 ALTER TABLE `user_roles` DISABLE KEYS */;
INSERT INTO `user_roles` VALUES (83,9,1,1411970745022),(91,3,4,1412057804335),(120,12,5,1412822409197),(123,1,1,1412852602142),(124,1,5,1412852602224),(128,2,1,1413006391408),(184,13,6,1413296430857),(195,5,6,1413343047684),(196,5,5,1413343047684),(197,5,4,1413343047684),(198,5,8,1413343047684),(205,6,1,1413357328994),(206,6,4,1413357328994),(207,14,10,1413446818743),(208,8,1,1413450795233),(209,10,1,1413454362711),(210,10,6,1413454362774),(211,10,5,1413454362844),(212,10,8,1413454362909);
/*!40000 ALTER TABLE `user_roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `account` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  `hashed_password` varchar(32) NOT NULL,
  `salt` varchar(5) NOT NULL,
  `avatar` varchar(500) NOT NULL,
  `is_locked` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `ip_address` varchar(40) NOT NULL,
  `last_login_at` datetime NOT NULL,
  `updated_at` bigint(20) NOT NULL,
  `created_at` bigint(20) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_user_account` (`account`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'huwei@eking.mobi','胡伟','cc5295069d7eb98bdd82bb4bcb9bba6a','dGLo5','/home/wangjing/devtools/python/workspaces/inc-eking-web/public/img/avatar-default.gif',0,'127.0.0.1','2014-10-14 22:20:48',1413296430857,1408376245698,0),(2,'wangshubin@eking.mobi','王淑彬','7f06cbde4dd348e56eaea555aad02f0b','06h1d','d/kx/i0dmu7rl7at.jpeg',0,'127.0.0.1','2014-10-15 10:11:59',1413339106634,1408955567806,0),(3,'wangjing@eking.mobi','王静','02df80024198edadcbd7110aaa0efa7c','3au04','2g/ce/hzds3xsg2g6t.jpg',1,'127.0.0.1','2014-08-28 13:55:22',1412845275276,1409205322467,1),(5,'wanglei@eking.mobi','王磊','7db3474bd12e4d29be790f43acb54742','y9zKJ','2c/8d/i0ep5kawans.jpg',0,'127.0.0.1','2014-10-15 10:44:01',1413341033935,1411382546023,0),(6,'lishijun@eking.mobi','李士俊','49322bf04a95a862990b54aa95caee6d','lJNYw','19/o5/i0900t1dfmo7.jpg',0,'127.0.0.1','2014-09-18 10:02:31',1413359276577,1411005751755,0),(7,'132232@qq.com','215','f69a6c07905dc54c7f888815341433da','COj5x','',0,'','2014-09-18 11:19:43',1411467458140,1411010383312,1),(8,'yanglu@eking.mobi','杨璐','d18c740c9b6048c9aa6d69e5548fac66','Cl2AL','',0,'127.0.0.1','2014-10-16 18:28:54',1413455334832,1411664528731,0),(9,'shaozhenxing@eking.mobi','邵振兴','95a60cd3dbf839699041f4eb3c514101','qVw9t','',0,'127.0.0.1','2014-10-16 16:30:34',1413431268874,1411640409899,0),(10,'wenjia@eking.mobi','闻佳','b0978c4e0a6ffbb7c86b5f3fff4377aa','R948t','images/1p/gd/i1bkycltl4u.jpg',0,'127.0.0.1','2014-10-16 16:32:48',1413447654536,1411640856799,0),(11,'876213774@163.com','测试账号','b5e7e626d09a5a2535b78dbd2cf8fa09','705qY','',0,'','2014-09-26 14:02:37',1412822366015,1411711357801,1),(12,'876213774@qq.com','测试账号1','19e31ae20a5641c82705bcc4192beeae','1gzud','',0,'127.0.0.1','2014-10-09 10:01:49',1412820109794,1412733170839,0),(13,'test1@eking.mobi','test1','a9538c9884e7bed93355b4726eebd641','n0wOU','',0,'127.0.0.1','2014-10-14 22:40:08',1413297432532,1413296430857,0),(14,'test2@eking.mobi','版权立案人员1','bb21afc285e2cb5dbb7edb84adb7cca9','BJT6U','',0,'','2014-10-16 16:12:00',1413446818743,1413446818743,0);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `workflow_actions`
--

DROP TABLE IF EXISTS `workflow_actions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `workflow_actions` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `workflow_id` bigint(20) NOT NULL COMMENT '工作流id',
  `remark` varchar(255) COLLATE utf8mb4_bin NOT NULL COMMENT '备注',
  `action` varchar(50) COLLATE utf8mb4_bin NOT NULL COMMENT '处理的行为，直接可以用中文。比如：同意、驳回',
  `next_user_id` bigint(20) NOT NULL COMMENT '下一个处理人',
  `created_at` bigint(20) NOT NULL COMMENT '创建时间',
  `operator_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=92 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='工作流处理行为表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `workflow_actions`
--

LOCK TABLES `workflow_actions` WRITE;
/*!40000 ALTER TABLE `workflow_actions` DISABLE KEYS */;
INSERT INTO `workflow_actions` VALUES (80,70,'sdafasdf','通过',1,1413287009791,1),(81,70,'司法斯蒂芬','通过',5,1413287009791,1),(82,71,'','通过',5,1413351065811,5),(83,71,'11','驳回',5,1413351910508,5),(84,71,'','通过',5,1413351910508,5),(85,71,'','驳回',5,1413351910508,5),(86,80,'似懂非懂','通过',1,1413372351477,13),(87,81,'','通过',5,1413432058961,10),(88,83,'','通过',12,1413447654536,10),(89,77,'TEST','通过',5,1413450795233,8),(90,86,'好饿','通过',10,1413454375984,5),(91,86,'','驳回',5,1413454310540,10);
/*!40000 ALTER TABLE `workflow_actions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `workflow_stacks`
--

DROP TABLE IF EXISTS `workflow_stacks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `workflow_stacks` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `workflow_id` bigint(20) NOT NULL,
  `workflow_action_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `created_at` bigint(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=152 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `workflow_stacks`
--

LOCK TABLES `workflow_stacks` WRITE;
/*!40000 ALTER TABLE `workflow_stacks` DISABLE KEYS */;
INSERT INTO `workflow_stacks` VALUES (120,65,0,1,1413284865642),(121,66,0,1,1413284865642),(122,67,0,1,1413284865642),(123,68,0,1,1413285394037),(124,69,0,1,1413286218246),(125,70,0,1,1413286218246),(126,70,80,1,1413287009791),(127,70,81,5,1413287009791),(129,71,82,5,1413351065811),(131,72,0,5,1413361213341),(132,73,0,5,1413361213341),(133,74,0,5,1413364017965),(134,75,0,13,1413369034695),(135,76,0,13,1413370640290),(136,77,0,13,1413371367513),(137,78,0,5,1413372364516),(138,79,0,5,1413372364516),(139,80,0,13,1413372351477),(140,80,86,1,1413372351477),(141,81,0,10,1413432058961),(142,81,87,5,1413432058961),(143,82,0,8,1413445236917),(144,83,0,10,1413447654536),(145,83,88,12,1413447654536),(146,77,89,5,1413450795233),(147,84,0,5,1413454231393),(148,85,0,5,1413454282029),(149,86,0,5,1413454307382),(151,87,0,1,1413456163441);
/*!40000 ALTER TABLE `workflow_stacks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `workflow_states`
--

DROP TABLE IF EXISTS `workflow_states`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `workflow_states` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `workflow_type` varchar(50) CHARACTER SET utf8mb4 NOT NULL,
  `name` varchar(50) COLLATE utf8mb4_bin NOT NULL,
  `state` varchar(50) COLLATE utf8mb4_bin NOT NULL,
  `action_rules` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `stack_rules` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `role_rules` varchar(255) CHARACTER SET utf8mb4 NOT NULL,
  `is_finished` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `workflow_states`
--

LOCK TABLES `workflow_states` WRITE;
/*!40000 ALTER TABLE `workflow_states` DISABLE KEYS */;
INSERT INTO `workflow_states` VALUES (10,'patent_order','专利合同登记','patent_order_contract_registration','{\'通过\':\'patent_order_data_upload\'}','{\'patent_order_data_upload\':1}','{\'patent_order_data_upload\':\'custom_service\'}',0),(11,'patent_order','专利资料上传','patent_order_data_upload','{\'通过\':\'patent_order_register\',\'驳回\':\'patent_order_contract_registration\'}','{\'patent_order_register\':1,\'patent_order_contract_registration\':0}','{\'patent_order_register\':\'patent_register_staff\',\'patent_order_contract_registration\':\'contract_manager\'}',0),(12,'patent_order','专利立案','patent_order_register','{\'完成\':\'patent_order_archive\',\'驳回\':\'patent_order_data_upload\'}','{\'patent_order_archive\':1,\'patent_order_data_upload\':0}','{\'patent_order_archive\':\'\',\'patent_order_data_upload\':\'custom_service\'}',0),(13,'patent_order','专利归档','patent_order_archive','{\'驳回\':\'patent_order_register\'}','{\'patent_order_register\':0}','',1),(22,'trademark_order','商标合同登记','trademark_order_contract_registration','{\'通过\':\'trademark_order_data_upload\'}','{\'trademark_order_data_upload\':1}','{\'trademark_order_data_upload\':\'custom_service\'}',0),(24,'trademark_order','商标资料上传','trademark_order_data_upload','{\'通过\':\'trademark_order_register\',\'驳回\':\'trademark_order_contract_registration\'}','{\'trademark_order_register\':1,\'trademark_order_contract_registration\':0}','{\'trademark_order_register\':\'trademark_register_staff\',\'trademark_order_contract_registration\':\'contract_manager\'}',0),(25,'trademark_order','商标立案','trademark_order_register','{\'完成\':\'trademark_order_archive\',\'驳回\':\'trademark_order_data_upload\'}','{\'trademark_order_archive\':1,\'trademark_order_data_upload\':0}','{\'trademark_order_archive\':\'\',\'trademark_order_data_upload\':\'custom_service\'}',0),(26,'trademark_order','商标归档','trademark_order_archive','{\'驳回\':\'trademark_order_register\'}','{\'trademark_order_register\':0}','',1),(27,'copyright_order','版权合同登记','copyright_order_contract_registration','{\'通过\':\'copyright_order_data_upload\'}','{\'copyright_order_data_upload\':1}','{\'copyright_order_data_upload\':\'custom_service\'}',0),(28,'copyright_order','版权资料上传','copyright_order_data_upload','{\'通过\':\'copyright_order_register\',\'驳回\':\'copyright_order_contract_registration\'}','{\'copyright_order_register\':1,\'copyright_order_contract_registration\':0}','{\'copyright_order_register\':\'copyright_register_staff\',\'copyright_order_contract_registration\':\'contract_manager\'}',0),(29,'copyright_order','版权立案','copyright_order_register','{\'完成\':\'copyright_order_archive\',\'驳回\':\'copyright_order_data_upload\'}','{\'copyright_order_archive\':1,\'copyright_order_data_upload\':0}','{\'copyright_order_archive\':\'\',\'copyright_order_data_upload\':\'custom_service\'}',0),(30,'copyright_order','版权归档','copyright_order_archive','{\'驳回\':\'copyright_order_register\'}','{\'copyright_order_register\':0}','',1);
/*!40000 ALTER TABLE `workflow_states` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `workflows`
--

DROP TABLE IF EXISTS `workflows`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `workflows` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(200) COLLATE utf8mb4_bin NOT NULL,
  `type` varchar(20) CHARACTER SET utf8mb4 NOT NULL COMMENT '工作流当前节点',
  `state` varchar(50) COLLATE utf8mb4_bin NOT NULL COMMENT '描述',
  `organization_id` bigint(20) NOT NULL,
  `rid` varchar(30) COLLATE utf8mb4_bin NOT NULL,
  `relation_entity_id` varchar(30) COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `current_user_id` bigint(20) NOT NULL,
  `owner_user_id` bigint(20) NOT NULL,
  `is_finished` tinyint(1) NOT NULL DEFAULT '0',
  `is_canceled` tinyint(1) NOT NULL DEFAULT '0',
  `is_deleted` tinyint(1) NOT NULL,
  `created_at` bigint(20) NOT NULL,
  `updated_at` bigint(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=88 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `workflows`
--

LOCK TABLES `workflows` WRITE;
/*!40000 ALTER TABLE `workflows` DISABLE KEYS */;
INSERT INTO `workflows` VALUES (65,'合同 1号专利','patent_order','',6,'155','22',1,1,0,0,0,1413284865642,1413284865642),(66,'合同 专利2号','patent_order','',1,'155','23',1,1,0,0,0,1413284865642,1413284865642),(67,'合同 专利3号','patent_order','',1,'155','24',1,1,0,0,0,1413284865642,1413284865642),(68,'合同 专利9号','patent_order','patent_order_contract_registration',6,'155','28',1,1,0,0,0,1413285394037,1413285394037),(69,'合同 专利7号','patent_order','patent_order_contract_registration',6,'155','29',1,1,0,0,0,1413286218246,1413286218246),(70,'合同 专利8号','patent_order','patent_order_register',6,'155','30',5,1,0,0,0,1413286218246,1413287009791),(71,'专利1','patent_order','patent_order_contract_registration',6,'163','31',6,5,0,1,0,1413351065811,1413353128146),(72,'专利1','patent_order','patent_order_contract_registration',6,'167','32',5,5,0,1,0,1413361213341,1413362611590),(73,'fewjiof专利2','patent_order','patent_order_contract_registration',6,'167','33',5,5,0,1,0,1413361213341,1413362611590),(74,'专利1','patent_order','patent_order_contract_registration',6,'166','34',5,5,0,1,0,1413364017965,1413364098837),(75,'sdfsdf','patent_order','patent_order_contract_registration',6,'168','35',13,13,0,0,0,1413369034695,1413369034695),(76,'sdfsdf','patent_order','patent_order_contract_registration',6,'173','36',13,13,0,0,0,1413370640290,1413370640290),(77,'sdfsdf','patent_order','patent_order_data_upload',6,'174','37',5,13,0,0,0,1413371367513,1413450795233),(78,'专利1','patent_order','patent_order_contract_registration',6,'176','38',5,5,0,0,0,1413372364516,1413372364516),(79,'商标1','trademark_order','trademark_order_contract_registration',6,'176','39',5,5,0,0,0,1413372364516,1413372364516),(80,'阿萨德飞','patent_order','patent_order_data_upload',6,'177','40',1,13,0,0,0,1413372351477,1413372351477),(81,'客户商标注册','trademark_order','trademark_order_data_upload',1,'178','42',5,10,0,0,0,1413432058961,1413432058961),(82,'123','patent_order','patent_order_contract_registration',1,'171','43',8,8,0,0,0,1413445236917,1413445236917),(83,'添加版权','copyright_order','copyright_order_data_upload',1,'196','44',12,10,0,1,0,1413447654536,1413456298636),(84,'专利1','patent_order','patent_order_contract_registration',6,'196','45',5,5,0,1,0,1413454231325,1413456298700),(85,'专利1','patent_order','patent_order_contract_registration',6,'192','46',5,5,0,1,0,1413454281958,1413455995162),(86,'154879','patent_order','patent_order_contract_registration',6,'192','47',5,5,0,1,0,1413454307234,1413455995225),(87,'合同 商标测试作废','trademark_order','trademark_order_contract_registration',6,'202','48',1,1,0,1,0,1413456163342,1413456191101);
/*!40000 ALTER TABLE `workflows` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-10-16 19:44:06
