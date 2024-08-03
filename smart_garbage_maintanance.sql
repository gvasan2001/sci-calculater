-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Aug 03, 2024 at 07:33 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `smart_garbage_maintanance`
--

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `id` int(10) NOT NULL auto_increment,
  `name` varchar(50) NOT NULL,
  `fname` varchar(50) NOT NULL,
  `age` varchar(4) NOT NULL,
  `number` varchar(12) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `mailid` varchar(30) NOT NULL,
  `address` varchar(100) NOT NULL,
  `role` varchar(20) NOT NULL,
  `work_area` varchar(20) NOT NULL,
  `uname` varchar(20) NOT NULL,
  `pass` varchar(20) NOT NULL,
  `status` varchar(10) NOT NULL,
  KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `employee`
--


-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `id` int(10) NOT NULL auto_increment,
  `name` varchar(20) NOT NULL,
  `area` varchar(20) NOT NULL,
  `report` varchar(100) NOT NULL,
  `type` varchar(10) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `feedback`
--


-- --------------------------------------------------------

--
-- Table structure for table `user_register`
--

CREATE TABLE `user_register` (
  `id` int(10) NOT NULL auto_increment,
  `name` varchar(30) NOT NULL,
  `number` varchar(20) NOT NULL,
  `email` varchar(20) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `address` varchar(100) NOT NULL,
  `area` varchar(20) NOT NULL,
  `pincode` varchar(8) NOT NULL,
  `uname` varchar(10) NOT NULL,
  `pass` varchar(10) NOT NULL,
  `status` varchar(5) NOT NULL,
  KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `user_register`
--

