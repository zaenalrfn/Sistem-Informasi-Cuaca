-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 15, 2024 at 03:38 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `uas_alpro_semt1`
--

-- --------------------------------------------------------

--
-- Table structure for table `cuaca`
--

CREATE TABLE `cuaca` (
  `id_cuaca` int(11) NOT NULL,
  `lokasi` varchar(225) DEFAULT NULL,
  `waktu` datetime DEFAULT NULL,
  `suhu` int(11) DEFAULT NULL,
  `kondisi` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `cuaca`
--

INSERT INTO `cuaca` (`id_cuaca`, `lokasi`, `waktu`, `suhu`, `kondisi`) VALUES
(14, 'Jepara', '2024-01-15 20:41:42', 31, 'normal'),
(15, 'Yogyakarta', '2024-01-15 20:42:00', 36, 'panas'),
(20, 'Dieng', '2024-01-15 20:43:19', 21, 'dingin'),
(21, 'Semarang', '2024-01-15 21:22:21', 40, 'panas');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cuaca`
--
ALTER TABLE `cuaca`
  ADD PRIMARY KEY (`id_cuaca`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cuaca`
--
ALTER TABLE `cuaca`
  MODIFY `id_cuaca` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
