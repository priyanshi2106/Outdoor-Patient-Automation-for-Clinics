-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 10, 2019 at 01:41 PM
-- Server version: 10.1.31-MariaDB
-- PHP Version: 7.2.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `opd`
--

-- --------------------------------------------------------

--
-- Table structure for table `appointment`
--

CREATE TABLE `appointment` (
  `appointmentid` int(11) NOT NULL,
  `pid` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `previoushistory` varchar(500) NOT NULL,
  `doctorid` int(11) NOT NULL,
  `date` date NOT NULL,
  `slotid` int(11) NOT NULL,
  `amount` float NOT NULL,
  `typeofbooking` varchar(200) NOT NULL,
  `paymentrecieved` float NOT NULL,
  `token` int(11) NOT NULL,
  `status` varchar(200) NOT NULL,
  `diagnosis` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `appointment`
--

INSERT INTO `appointment` (`appointmentid`, `pid`, `name`, `previoushistory`, `doctorid`, `date`, `slotid`, `amount`, `typeofbooking`, `paymentrecieved`, `token`, `status`, `diagnosis`) VALUES
(1, 3, 'saumya', 'iljhhul\n', 2, '2019-07-09', 4, 1000, 'Walkin', 100, 0, 'pending', '');

-- --------------------------------------------------------

--
-- Table structure for table `doctors`
--

CREATE TABLE `doctors` (
  `doctorid` int(11) NOT NULL,
  `email` varchar(200) NOT NULL,
  `name` varchar(200) NOT NULL,
  `mobile` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `doctors`
--

INSERT INTO `doctors` (`doctorid`, `email`, `name`, `mobile`) VALUES
(1, 'priya', 'priya11@gmail.com', '9878672400'),
(2, 'karan', 'karan@gmail.com', '9658742136');

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

CREATE TABLE `patient` (
  `pid` int(11) NOT NULL,
  `pname` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `mobile` varchar(100) NOT NULL,
  `spousename` varchar(200) NOT NULL,
  `fathername` varchar(200) NOT NULL,
  `dob` date NOT NULL,
  `age` int(11) NOT NULL,
  `knownproblems` varchar(200) NOT NULL,
  `knownallergies` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`pid`, `pname`, `email`, `mobile`, `spousename`, `fathername`, `dob`, `age`, `knownproblems`, `knownallergies`) VALUES
(1, 'kartik', 'kartik@gmail.com', '6987532641', 'kritika', 'karan', '2083-07-19', 36, 'headache,cough,fever\n', 'none\n'),
(3, 'saumya', 'saumyahasija@gmail.com', '8654793521', 'none', 'shami', '2000-11-15', 20, 'constipation\n', 'none\n'),
(4, 'kiara', 'kiara@gmail.com', '9865423104', 'none', 'rajesh', '2019-07-10', 20, 'headache\n', 'none\n');

-- --------------------------------------------------------

--
-- Table structure for table `slot`
--

CREATE TABLE `slot` (
  `slotid` int(11) NOT NULL,
  `slotdetail` varchar(200) NOT NULL,
  `maxcapacity` int(11) NOT NULL,
  `monday` varchar(200) NOT NULL,
  `tuesday` varchar(200) NOT NULL,
  `wednesday` varchar(200) NOT NULL,
  `thursday` varchar(200) NOT NULL,
  `friday` varchar(200) NOT NULL,
  `saturday` varchar(200) NOT NULL,
  `sunday` varchar(200) NOT NULL,
  `doctorid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `slot`
--

INSERT INTO `slot` (`slotid`, `slotdetail`, `maxcapacity`, `monday`, `tuesday`, `wednesday`, `thursday`, `friday`, `saturday`, `sunday`, `doctorid`) VALUES
(3, '5:00pm-8:00pm\n', 6, 'no', 'no', 'no', 'no', 'no', 'no', 'no', 1),
(4, '11:30am-1:00pm\n', 7, 'no', 'no', 'no', 'no', 'no', 'no', 'no', 2),
(6, '9:00am to 10:30pm\n', 7, 'yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 2);

-- --------------------------------------------------------

--
-- Table structure for table `slots`
--

CREATE TABLE `slots` (
  `slotid` int(11) NOT NULL,
  `slotdetail` varchar(200) NOT NULL,
  `monday` varchar(200) NOT NULL,
  `tuesday` varchar(200) NOT NULL,
  `wednesday` varchar(200) NOT NULL,
  `thursday` varchar(200) NOT NULL,
  `friday` varchar(200) NOT NULL,
  `saturday` varchar(200) NOT NULL,
  `sunday` varchar(200) NOT NULL,
  `doctorid` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

CREATE TABLE `staff` (
  `staff_id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `mobile` varchar(100) NOT NULL,
  `password` varchar(200) NOT NULL,
  `designation` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `staff`
--

INSERT INTO `staff` (`staff_id`, `name`, `email`, `mobile`, `password`, `designation`) VALUES
(3, 'ankita', 'ankitas@gmail.com', '9652315748', 'anku12345', 'gynaecologist'),
(4, 'upadhi', 'upadhi@gmail.com', '5684237156', 'upadhi12345', 'cadiologist'),
(5, 'sanjana', 'sanjana@gmail.com', '7658421359', 'sanjana87465', 'doctor'),
(6, 'sahil', 'sahil@gmail.com', '8752103147', 'sahiltata321', 'receptionist'),
(7, 'manish', 'manish@gmail.com', '8647953214', 'mani123', 'nurse');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `appointment`
--
ALTER TABLE `appointment`
  ADD PRIMARY KEY (`appointmentid`),
  ADD KEY `pid` (`pid`),
  ADD KEY `doctorid` (`doctorid`),
  ADD KEY `slotid` (`slotid`);

--
-- Indexes for table `doctors`
--
ALTER TABLE `doctors`
  ADD PRIMARY KEY (`doctorid`);

--
-- Indexes for table `patient`
--
ALTER TABLE `patient`
  ADD PRIMARY KEY (`pid`);

--
-- Indexes for table `slot`
--
ALTER TABLE `slot`
  ADD PRIMARY KEY (`slotid`),
  ADD KEY `doctorid` (`doctorid`);

--
-- Indexes for table `staff`
--
ALTER TABLE `staff`
  ADD PRIMARY KEY (`staff_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `appointment`
--
ALTER TABLE `appointment`
  MODIFY `appointmentid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `doctors`
--
ALTER TABLE `doctors`
  MODIFY `doctorid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `patient`
--
ALTER TABLE `patient`
  MODIFY `pid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `slot`
--
ALTER TABLE `slot`
  MODIFY `slotid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `staff`
--
ALTER TABLE `staff`
  MODIFY `staff_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `appointment`
--
ALTER TABLE `appointment`
  ADD CONSTRAINT `appointment_ibfk_1` FOREIGN KEY (`pid`) REFERENCES `patient` (`pid`),
  ADD CONSTRAINT `appointment_ibfk_2` FOREIGN KEY (`doctorid`) REFERENCES `doctors` (`doctorid`),
  ADD CONSTRAINT `appointment_ibfk_3` FOREIGN KEY (`slotid`) REFERENCES `slot` (`slotid`);

--
-- Constraints for table `slot`
--
ALTER TABLE `slot`
  ADD CONSTRAINT `slot_ibfk_1` FOREIGN KEY (`doctorid`) REFERENCES `doctors` (`doctorid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
