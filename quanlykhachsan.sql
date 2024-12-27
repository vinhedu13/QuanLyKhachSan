-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: quanlykhachsan
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
-- Table structure for table `baocaodoanhthu`
--

DROP TABLE IF EXISTS `baocaodoanhthu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `baocaodoanhthu` (
  `id` int NOT NULL AUTO_INCREMENT,
  `doanhThu` double NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `baocaodoanhthu_ibfk_1` FOREIGN KEY (`id`) REFERENCES `baocaothongke` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `baocaodoanhthu`
--

LOCK TABLES `baocaodoanhthu` WRITE;
/*!40000 ALTER TABLE `baocaodoanhthu` DISABLE KEYS */;
/*!40000 ALTER TABLE `baocaodoanhthu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `baocaotansuatsudung`
--

DROP TABLE IF EXISTS `baocaotansuatsudung`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `baocaotansuatsudung` (
  `id` int NOT NULL,
  `soLuotThue` int NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `baocaotansuatsudung_ibfk_1` FOREIGN KEY (`id`) REFERENCES `baocaothongke` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `baocaotansuatsudung`
--

LOCK TABLES `baocaotansuatsudung` WRITE;
/*!40000 ALTER TABLE `baocaotansuatsudung` DISABLE KEYS */;
/*!40000 ALTER TABLE `baocaotansuatsudung` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `baocaothongke`
--

DROP TABLE IF EXISTS `baocaothongke`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `baocaothongke` (
  `thoiGianTao` datetime NOT NULL,
  `trangThai` tinyint(1) NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `baocaothongke`
--

LOCK TABLES `baocaothongke` WRITE;
/*!40000 ALTER TABLE `baocaothongke` DISABLE KEYS */;
/*!40000 ALTER TABLE `baocaothongke` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `baocaothongke_hoadon`
--

DROP TABLE IF EXISTS `baocaothongke_hoadon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `baocaothongke_hoadon` (
  `idBaoCaoThongKe` int NOT NULL,
  `idHoaDon` int NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `idBaoCaoThongKe` (`idBaoCaoThongKe`),
  KEY `idHoaDon` (`idHoaDon`),
  CONSTRAINT `baocaothongke_hoadon_ibfk_1` FOREIGN KEY (`idBaoCaoThongKe`) REFERENCES `baocaothongke` (`id`),
  CONSTRAINT `baocaothongke_hoadon_ibfk_2` FOREIGN KEY (`idHoaDon`) REFERENCES `hoadon` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `baocaothongke_hoadon`
--

LOCK TABLES `baocaothongke_hoadon` WRITE;
/*!40000 ALTER TABLE `baocaothongke_hoadon` DISABLE KEYS */;
/*!40000 ALTER TABLE `baocaothongke_hoadon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hoadon`
--

DROP TABLE IF EXISTS `hoadon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hoadon` (
  `tongTien` double NOT NULL,
  `trangThai` tinyint(1) NOT NULL,
  `idPhieu` int NOT NULL,
  `thoiGianTao` datetime NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idPhieu` (`idPhieu`),
  CONSTRAINT `hoadon_ibfk_1` FOREIGN KEY (`idPhieu`) REFERENCES `phieu` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hoadon`
--

LOCK TABLES `hoadon` WRITE;
/*!40000 ALTER TABLE `hoadon` DISABLE KEYS */;
INSERT INTO `hoadon` VALUES (2000000,1,1,'2024-12-10 21:14:36',1),(4000000,0,2,'2024-12-10 21:14:36',2),(1000000,1,42,'2024-12-13 19:36:59',4),(500000,1,43,'2024-12-14 18:12:24',5),(1000000,1,44,'2024-12-14 20:36:26',6),(500000,1,46,'2024-12-17 16:12:59',7),(500000,1,47,'2024-12-17 16:16:07',8),(500000,1,48,'2024-12-17 16:49:01',9),(500000,1,49,'2024-12-17 16:52:25',10),(500000,1,50,'2024-12-20 19:10:28',11),(500000,1,867338584,'2024-12-22 18:36:10',12),(500000,1,889269925,'2024-12-23 00:41:44',13),(500000,1,940504737,'2024-12-23 14:56:21',14),(500000,1,940632772,'2024-12-23 14:57:23',15),(500000,1,39472648,'2024-12-24 18:24:56',16),(500000,1,222504701,'2024-12-26 21:15:16',17),(500000,1,222829605,'2024-12-26 21:20:42',18),(500000,1,249650665,'2024-12-27 04:47:46',19);
/*!40000 ALTER TABLE `hoadon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `khachhang`
--

DROP TABLE IF EXISTS `khachhang`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `khachhang` (
  `tenKhachHang` varchar(50) DEFAULT NULL,
  `hoKhachHang` varchar(50) DEFAULT NULL,
  `gioiTinh` enum('Nam','Nữ') DEFAULT NULL,
  `cccd` varchar(12) DEFAULT NULL,
  `sdt` varchar(15) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `diaChi` varchar(200) DEFAULT NULL,
  `idLoaiKhach` int DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `idLoaiKhach` (`idLoaiKhach`),
  CONSTRAINT `khachhang_ibfk_1` FOREIGN KEY (`idLoaiKhach`) REFERENCES `loaikhach` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=154542138 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `khachhang`
--

LOCK TABLES `khachhang` WRITE;
/*!40000 ALTER TABLE `khachhang` DISABLE KEYS */;
INSERT INTO `khachhang` VALUES ('Nguyễn Văn','A','Nam','123456789012','0987654321','vinh13052004@gmail.com','Hà Nội',1,1),('Trần Thị','B','Nữ','234567890123','0978645321','ttb@example.com','TP.HCM',1,2),('Lê Văn','C','Nam','345678901234','0967534210','lvc@example.com','USA',2,3),('a',NULL,NULL,'1',NULL,NULL,NULL,NULL,154542123),('b',NULL,NULL,'2',NULL,NULL,NULL,NULL,154542124),('a',NULL,NULL,'1',NULL,NULL,NULL,NULL,154542125),('Lê Quang Vinh',NULL,NULL,NULL,NULL,NULL,NULL,NULL,154542128),('nhanvien',NULL,NULL,NULL,NULL,NULL,NULL,NULL,154542129),('ATOI',NULL,NULL,NULL,NULL,'atoi@gmail.com',NULL,NULL,154542130),('ádasdasd',NULL,NULL,'1111111',NULL,NULL,NULL,NULL,154542131),('aaaaaaaaaa',NULL,NULL,'11111',NULL,NULL,NULL,1,154542132),('bbbbbbbb',NULL,NULL,'22222',NULL,NULL,NULL,2,154542133),('asimaruoi',NULL,NULL,'123',NULL,NULL,NULL,1,154542135),('COPHIEUDAT',NULL,NULL,'123',NULL,NULL,NULL,1,154542136),('COPHIEUDAT',NULL,NULL,'321',NULL,NULL,NULL,1,154542137);
/*!40000 ALTER TABLE `khachhang` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loaikhach`
--

DROP TABLE IF EXISTS `loaikhach`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loaikhach` (
  `tenLoaiKhach` varchar(50) NOT NULL,
  `heSo` double NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loaikhach`
--

LOCK TABLES `loaikhach` WRITE;
/*!40000 ALTER TABLE `loaikhach` DISABLE KEYS */;
INSERT INTO `loaikhach` VALUES ('Nội Địa',1,1),('Nước ngoài',1.5,2);
/*!40000 ALTER TABLE `loaikhach` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loaiphieu`
--

DROP TABLE IF EXISTS `loaiphieu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loaiphieu` (
  `tenLoaiPhieu` varchar(50) NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loaiphieu`
--

LOCK TABLES `loaiphieu` WRITE;
/*!40000 ALTER TABLE `loaiphieu` DISABLE KEYS */;
INSERT INTO `loaiphieu` VALUES ('Phiếu thuê phòng',1),('Phiếu đặt phòng',2);
/*!40000 ALTER TABLE `loaiphieu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loaiphong`
--

DROP TABLE IF EXISTS `loaiphong`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loaiphong` (
  `tenLoaiPhong` varchar(50) NOT NULL,
  `donGia` double NOT NULL,
  `soLuong` int NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  `dienTich` double DEFAULT NULL,
  `moTa` varchar(100) DEFAULT NULL,
  `luongKhachToiDa` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loaiphong`
--

LOCK TABLES `loaiphong` WRITE;
/*!40000 ALTER TABLE `loaiphong` DISABLE KEYS */;
INSERT INTO `loaiphong` VALUES ('Phòng đơn',500000,3,1,19,NULL,1),('Phòng đôi',800000,1,2,30,NULL,2),('Phòng VIP',1500000,1,3,45,NULL,3);
/*!40000 ALTER TABLE `loaiphong` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loaitaikhoan`
--

DROP TABLE IF EXISTS `loaitaikhoan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loaitaikhoan` (
  `tenLoaiTaiKhoan` varchar(50) NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loaitaikhoan`
--

LOCK TABLES `loaitaikhoan` WRITE;
/*!40000 ALTER TABLE `loaitaikhoan` DISABLE KEYS */;
INSERT INTO `loaitaikhoan` VALUES ('Admin',1),('Khách hàng',2),('Nhân viên',3);
/*!40000 ALTER TABLE `loaitaikhoan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phieu`
--

DROP TABLE IF EXISTS `phieu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `phieu` (
  `loaiPhieu` int NOT NULL,
  `thoiGianTao` datetime NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `loaiPhieu` (`loaiPhieu`),
  CONSTRAINT `phieu_ibfk_1` FOREIGN KEY (`loaiPhieu`) REFERENCES `loaiphieu` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=940632773 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phieu`
--

LOCK TABLES `phieu` WRITE;
/*!40000 ALTER TABLE `phieu` DISABLE KEYS */;
INSERT INTO `phieu` VALUES (1,'2024-12-10 21:10:28',1),(2,'2024-12-10 21:10:28',2),(2,'2024-12-13 18:51:04',37),(2,'2024-12-13 18:54:47',38),(2,'2024-12-13 18:55:28',39),(2,'2024-12-13 19:18:09',40),(2,'2024-12-13 19:20:21',41),(2,'2024-12-13 19:36:17',42),(2,'2024-12-14 18:12:05',43),(2,'2024-12-14 20:36:01',44),(2,'2024-12-17 16:12:37',45),(2,'2024-12-17 16:12:37',46),(2,'2024-12-17 16:15:56',47),(2,'2024-12-17 16:42:04',48),(2,'2024-12-17 16:52:14',49),(2,'2024-12-20 19:10:04',50),(2,'2024-12-24 18:24:56',39472648),(1,'2024-12-25 16:38:09',119489064),(1,'2024-12-25 16:40:54',119654401),(1,'2024-12-26 21:00:49',221623192),(1,'2024-12-26 21:10:18',222206555),(1,'2024-12-26 21:15:16',222504701),(1,'2024-12-26 21:20:42',222829605),(1,'2024-12-27 04:39:08',249116891),(1,'2024-12-27 04:43:30',249386538),(1,'2024-12-27 04:47:46',249650665),(1,'2024-12-27 04:50:25',249824961),(2,'2024-12-22 18:36:10',867338584),(1,'2024-12-23 00:37:55',889036374),(1,'2024-12-23 00:41:44',889269925),(2,'2024-12-23 14:56:21',940504737),(1,'2024-12-23 14:57:23',940632772);
/*!40000 ALTER TABLE `phieu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phieudatphong`
--

DROP TABLE IF EXISTS `phieudatphong`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `phieudatphong` (
  `id` int NOT NULL AUTO_INCREMENT,
  `idKhachHang` int NOT NULL,
  `idLoaiPhong` int NOT NULL,
  `soLuong` int NOT NULL,
  `trangThai` enum('Đã nhận phòng','Chưa nhận phòng','Đã hủy') DEFAULT NULL,
  `ngayNhanPhong` datetime DEFAULT NULL,
  `ngayTraPhong` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idKhachHang` (`idKhachHang`),
  KEY `idLoaiPhong` (`idLoaiPhong`),
  CONSTRAINT `phieudatphong_ibfk_1` FOREIGN KEY (`id`) REFERENCES `phieu` (`id`),
  CONSTRAINT `phieudatphong_ibfk_2` FOREIGN KEY (`idKhachHang`) REFERENCES `khachhang` (`id`),
  CONSTRAINT `phieudatphong_ibfk_3` FOREIGN KEY (`idLoaiPhong`) REFERENCES `loaiphong` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=940504738 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phieudatphong`
--

LOCK TABLES `phieudatphong` WRITE;
/*!40000 ALTER TABLE `phieudatphong` DISABLE KEYS */;
INSERT INTO `phieudatphong` VALUES (42,1,1,2,'Đã nhận phòng','2024-12-01 14:00:00','2024-12-05 12:00:00'),(50,1,1,1,'Chưa nhận phòng','2024-12-20 14:00:00','2024-12-21 12:00:00'),(39472648,154542130,1,1,'Chưa nhận phòng','2024-12-31 14:00:00','2025-01-01 12:00:00'),(867338584,1,1,1,'Chưa nhận phòng','2024-12-22 14:00:00','2024-12-23 12:00:00'),(940504737,1,1,1,'Đã nhận phòng','2024-12-23 14:00:00','2024-12-25 12:00:00');
/*!40000 ALTER TABLE `phieudatphong` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phieuthuephong`
--

DROP TABLE IF EXISTS `phieuthuephong`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `phieuthuephong` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ngayNhanPhong` datetime NOT NULL,
  `ngayTraPhong` datetime NOT NULL,
  `idPhieuDatPhong` int DEFAULT NULL,
  `trangThai` enum('Đang sử dụng','Đã trả phòng') DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idPhieuDatPhong` (`idPhieuDatPhong`),
  CONSTRAINT `phieuthuephong_ibfk_1` FOREIGN KEY (`id`) REFERENCES `phieu` (`id`),
  CONSTRAINT `phieuthuephong_ibfk_2` FOREIGN KEY (`idPhieuDatPhong`) REFERENCES `phieudatphong` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=940632773 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phieuthuephong`
--

LOCK TABLES `phieuthuephong` WRITE;
/*!40000 ALTER TABLE `phieuthuephong` DISABLE KEYS */;
INSERT INTO `phieuthuephong` VALUES (1,'2024-12-01 14:00:00','2024-12-05 12:00:00',NULL,NULL),(119489064,'2024-12-25 16:38:09','2024-12-25 12:00:00',940504737,NULL),(222829605,'2024-12-26 21:20:42','2024-12-28 21:20:00',NULL,NULL),(249650665,'2024-12-27 04:47:46','2024-12-29 04:47:00',NULL,NULL),(249824961,'2024-12-27 04:50:25','2024-12-05 12:00:00',42,NULL),(889269925,'2024-12-23 00:41:44','2024-12-23 00:40:00',NULL,NULL),(940632772,'2024-12-23 14:57:23','2024-12-24 14:57:00',NULL,NULL);
/*!40000 ALTER TABLE `phieuthuephong` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phieuthuephong_phong`
--

DROP TABLE IF EXISTS `phieuthuephong_phong`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `phieuthuephong_phong` (
  `idPhong` int NOT NULL,
  `idPhieuThuePhong` int NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `idPhong` (`idPhong`),
  KEY `idPhieuThuePhong` (`idPhieuThuePhong`),
  CONSTRAINT `phieuthuephong_phong_ibfk_1` FOREIGN KEY (`idPhong`) REFERENCES `phong` (`id`),
  CONSTRAINT `phieuthuephong_phong_ibfk_2` FOREIGN KEY (`idPhieuThuePhong`) REFERENCES `phieuthuephong` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phieuthuephong_phong`
--

LOCK TABLES `phieuthuephong_phong` WRITE;
/*!40000 ALTER TABLE `phieuthuephong_phong` DISABLE KEYS */;
INSERT INTO `phieuthuephong_phong` VALUES (201,1,2),(101,889269925,3),(102,889269925,4),(101,940632772,5),(101,119489064,6),(101,222829605,9),(102,222829605,10),(103,249650665,11),(101,249824961,12),(102,249824961,13);
/*!40000 ALTER TABLE `phieuthuephong_phong` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phieuthuephong_phong_khachhang`
--

DROP TABLE IF EXISTS `phieuthuephong_phong_khachhang`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `phieuthuephong_phong_khachhang` (
  `id` int NOT NULL AUTO_INCREMENT,
  `idKhachHang` int NOT NULL,
  `idPhieuThuePhong_Phong` int NOT NULL,
  `trangThai` enum('Đã nhận phòng','Đã trả phòng') NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fkidKhachHang_idx` (`idKhachHang`),
  KEY `fkidPhieuThuePhong_Phong_idx` (`idPhieuThuePhong_Phong`),
  CONSTRAINT `fkidKhachHang` FOREIGN KEY (`idKhachHang`) REFERENCES `khachhang` (`id`),
  CONSTRAINT `fkidPhieuThuePhong_Phong` FOREIGN KEY (`idPhieuThuePhong_Phong`) REFERENCES `phieuthuephong_phong` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phieuthuephong_phong_khachhang`
--

LOCK TABLES `phieuthuephong_phong_khachhang` WRITE;
/*!40000 ALTER TABLE `phieuthuephong_phong_khachhang` DISABLE KEYS */;
INSERT INTO `phieuthuephong_phong_khachhang` VALUES (1,154542123,3,'Đã nhận phòng'),(2,154542124,4,'Đã nhận phòng'),(3,154542125,5,'Đã nhận phòng'),(4,154542131,6,'Đã nhận phòng'),(5,154542132,9,'Đã nhận phòng'),(6,154542133,10,'Đã nhận phòng'),(7,2,2,'Đã nhận phòng'),(8,154542135,11,'Đã nhận phòng'),(9,154542136,12,'Đã nhận phòng'),(10,154542137,13,'Đã nhận phòng');
/*!40000 ALTER TABLE `phieuthuephong_phong_khachhang` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phong`
--

DROP TABLE IF EXISTS `phong`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `phong` (
  `tenPhong` varchar(50) NOT NULL,
  `idLoaiPhong` int NOT NULL,
  `idTinhTrangPhong` int NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `idLoaiPhong` (`idLoaiPhong`),
  KEY `idTinhTrangPhong` (`idTinhTrangPhong`),
  CONSTRAINT `phong_ibfk_1` FOREIGN KEY (`idLoaiPhong`) REFERENCES `loaiphong` (`id`),
  CONSTRAINT `phong_ibfk_2` FOREIGN KEY (`idTinhTrangPhong`) REFERENCES `tinhtrangphong` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=302 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phong`
--

LOCK TABLES `phong` WRITE;
/*!40000 ALTER TABLE `phong` DISABLE KEYS */;
INSERT INTO `phong` VALUES ('101',1,1,101),('102',1,2,102),('103',1,1,103),('201',2,1,201),('301',3,3,301);
/*!40000 ALTER TABLE `phong` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `taikhoan`
--

DROP TABLE IF EXISTS `taikhoan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `taikhoan` (
  `ten` varchar(50) NOT NULL,
  `matKhau` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `thoiGianTao` datetime NOT NULL,
  `idLoaiTaiKhoan` int NOT NULL,
  `idKhachHang` int NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idKhachHang` (`idKhachHang`),
  KEY `idLoaiTaiKhoan` (`idLoaiTaiKhoan`),
  CONSTRAINT `taikhoan_ibfk_1` FOREIGN KEY (`idLoaiTaiKhoan`) REFERENCES `loaitaikhoan` (`id`),
  CONSTRAINT `taikhoan_ibfk_2` FOREIGN KEY (`idKhachHang`) REFERENCES `khachhang` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `taikhoan`
--

LOCK TABLES `taikhoan` WRITE;
/*!40000 ALTER TABLE `taikhoan` DISABLE KEYS */;
/*!40000 ALTER TABLE `taikhoan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tinhtrangphong`
--

DROP TABLE IF EXISTS `tinhtrangphong`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tinhtrangphong` (
  `tenTinhTrangPhong` varchar(50) DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tinhtrangphong`
--

LOCK TABLES `tinhtrangphong` WRITE;
/*!40000 ALTER TABLE `tinhtrangphong` DISABLE KEYS */;
INSERT INTO `tinhtrangphong` VALUES ('Trống',1),('Đang thuê',2),('Đang bảo trì',3);
/*!40000 ALTER TABLE `tinhtrangphong` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tylephuthu`
--

DROP TABLE IF EXISTS `tylephuthu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tylephuthu` (
  `tyLe` double NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tylephuthu`
--

LOCK TABLES `tylephuthu` WRITE;
/*!40000 ALTER TABLE `tylephuthu` DISABLE KEYS */;
/*!40000 ALTER TABLE `tylephuthu` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-27  5:10:09
