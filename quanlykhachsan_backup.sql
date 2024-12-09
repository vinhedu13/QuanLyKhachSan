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
-- Current Database: `quanlykhachsan`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `quanlykhachsan` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `quanlykhachsan`;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hoadon`
--

LOCK TABLES `hoadon` WRITE;
/*!40000 ALTER TABLE `hoadon` DISABLE KEYS */;
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
  `gioiTinh` enum('Nam','Nß╗»') DEFAULT NULL,
  `cccd` varchar(12) DEFAULT NULL,
  `sdt` varchar(15) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `diaChi` varchar(200) DEFAULT NULL,
  `idLoaiKhach` int DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `idLoaiKhach` (`idLoaiKhach`),
  CONSTRAINT `khachhang_ibfk_1` FOREIGN KEY (`idLoaiKhach`) REFERENCES `loaikhach` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `khachhang`
--

LOCK TABLES `khachhang` WRITE;
/*!40000 ALTER TABLE `khachhang` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loaikhach`
--

LOCK TABLES `loaikhach` WRITE;
/*!40000 ALTER TABLE `loaikhach` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loaiphieu`
--

LOCK TABLES `loaiphieu` WRITE;
/*!40000 ALTER TABLE `loaiphieu` DISABLE KEYS */;
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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loaiphong`
--

LOCK TABLES `loaiphong` WRITE;
/*!40000 ALTER TABLE `loaiphong` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loaitaikhoan`
--

LOCK TABLES `loaitaikhoan` WRITE;
/*!40000 ALTER TABLE `loaitaikhoan` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phieu`
--

LOCK TABLES `phieu` WRITE;
/*!40000 ALTER TABLE `phieu` DISABLE KEYS */;
/*!40000 ALTER TABLE `phieu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phieu_khachhang`
--

DROP TABLE IF EXISTS `phieu_khachhang`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `phieu_khachhang` (
  `idKhachHang` int NOT NULL,
  `idPhieu` int NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `idKhachHang` (`idKhachHang`),
  KEY `idPhieu` (`idPhieu`),
  CONSTRAINT `phieu_khachhang_ibfk_1` FOREIGN KEY (`idKhachHang`) REFERENCES `khachhang` (`id`),
  CONSTRAINT `phieu_khachhang_ibfk_2` FOREIGN KEY (`idPhieu`) REFERENCES `phieuthuephong` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phieu_khachhang`
--

LOCK TABLES `phieu_khachhang` WRITE;
/*!40000 ALTER TABLE `phieu_khachhang` DISABLE KEYS */;
/*!40000 ALTER TABLE `phieu_khachhang` ENABLE KEYS */;
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
  PRIMARY KEY (`id`),
  KEY `idKhachHang` (`idKhachHang`),
  KEY `idLoaiPhong` (`idLoaiPhong`),
  CONSTRAINT `phieudatphong_ibfk_1` FOREIGN KEY (`id`) REFERENCES `phieu` (`id`),
  CONSTRAINT `phieudatphong_ibfk_2` FOREIGN KEY (`idKhachHang`) REFERENCES `khachhang` (`id`),
  CONSTRAINT `phieudatphong_ibfk_3` FOREIGN KEY (`idLoaiPhong`) REFERENCES `loaiphong` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phieudatphong`
--

LOCK TABLES `phieudatphong` WRITE;
/*!40000 ALTER TABLE `phieudatphong` DISABLE KEYS */;
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
  `trangThai` enum('─É├ú nhß║¡n ph├▓ng','Ch╞░a nhß║¡n ph├▓ng','─É├ú hß╗ºy','Qu├í hß║ín nhß║¡n') NOT NULL,
  `idPhieuDatPhong` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idPhieuDatPhong` (`idPhieuDatPhong`),
  CONSTRAINT `phieuthuephong_ibfk_1` FOREIGN KEY (`id`) REFERENCES `phieu` (`id`),
  CONSTRAINT `phieuthuephong_ibfk_2` FOREIGN KEY (`idPhieuDatPhong`) REFERENCES `phieudatphong` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phieuthuephong`
--

LOCK TABLES `phieuthuephong` WRITE;
/*!40000 ALTER TABLE `phieuthuephong` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phieuthuephong_phong`
--

LOCK TABLES `phieuthuephong_phong` WRITE;
/*!40000 ALTER TABLE `phieuthuephong_phong` DISABLE KEYS */;
/*!40000 ALTER TABLE `phieuthuephong_phong` ENABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phong`
--

LOCK TABLES `phong` WRITE;
/*!40000 ALTER TABLE `phong` DISABLE KEYS */;
/*!40000 ALTER TABLE `phong` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quydinhphong`
--

DROP TABLE IF EXISTS `quydinhphong`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quydinhphong` (
  `soKhachToiDa` int NOT NULL,
  `dieuKien` varchar(200) DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quydinhphong`
--

LOCK TABLES `quydinhphong` WRITE;
/*!40000 ALTER TABLE `quydinhphong` DISABLE KEYS */;
/*!40000 ALTER TABLE `quydinhphong` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `taikhoan`
--

DROP TABLE IF EXISTS `taikhoan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `taikhoan` (
  `tenDangNhap` varchar(50) NOT NULL,
  `matKhau` varchar(50) NOT NULL,
  `sdt` varchar(15) NOT NULL,
  `email` varchar(100) NOT NULL,
  `thoiGianTao` datetime NOT NULL,
  `idLoaiTaiKhoan` int NOT NULL,
  `idKhachHang` int NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idKhachHang` (`idKhachHang`),
  KEY `idLoaiTaiKhoan` (`idLoaiTaiKhoan`),
  CONSTRAINT `taikhoan_ibfk_1` FOREIGN KEY (`idLoaiTaiKhoan`) REFERENCES `loaitaikhoan` (`id`),
  CONSTRAINT `taikhoan_ibfk_2` FOREIGN KEY (`idKhachHang`) REFERENCES `khachhang` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tinhtrangphong`
--

LOCK TABLES `tinhtrangphong` WRITE;
/*!40000 ALTER TABLE `tinhtrangphong` DISABLE KEYS */;
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

-- Dump completed on 2024-12-09 18:46:28
