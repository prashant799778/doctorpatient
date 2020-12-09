



CREATE TABLE `doctorMaster` (
`id` int(10) NOT NULL AUTO_INCREMENT,
`userID` varchar(255) DEFAULT NULL,
`name` varchar(255) DEFAULT NULL,
`email` varchar(255) DEFAULT NULL,
`qualification` varchar(255) DEFAULT NULL,
`password` varchar(255) DEFAULT NULL,
`age` varchar(255) DEFAULT NULL,
`speciality` varchar(255) DEFAULT NULL,
`experience` varchar(255) DEFAULT NULL,
`previously` varchar(255) DEFAULT NULL,
`status` int(1) NOT NULL DEFAULT '0',
`usercreate` varchar(255) DEFAULT NULL,
`DateCreate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
`UserUpdate` varchar(255) DEFAULT NULL,
`DateUpdate` datetime DEFAULT NULL,
PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;



--------------






CREATE TABLE `patientMaster` (
`id` int(10) NOT NULL AUTO_INCREMENT,
`userID` varchar(255) DEFAULT NULL,
`name` varchar(255) DEFAULT NULL,
`email` varchar(255) DEFAULT NULL,
`phoneNumber` varchar(255) DEFAULT NULL,
`password` varchar(255) DEFAULT NULL,
`age` varchar(255) DEFAULT NULL,
`gender` varchar(255) DEFAULT NULL,
`dob` varchar(255) DEFAULT NULL,
`address` varchar(255) DEFAULT NULL,
`pincode` varchar(255) DEFAULT NULL,
`first` varchar(255) DEFAULT NULL,
`healthIssue` varchar(255) DEFAULT NULL,
`status` int(1) NOT NULL DEFAULT '0',
`usercreate` varchar(255) DEFAULT NULL,
`DateCreate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
`UserUpdate` varchar(255) DEFAULT NULL,
`DateUpdate` datetime DEFAULT NULL,
PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;



CREATE TABLE `qualificationMaster` (
`id` int(10) NOT NULL AUTO_INCREMENT,
`qualification` varchar(255) DEFAULT NULL,
`status` int(1) NOT NULL DEFAULT '0',
`usercreate` varchar(255) DEFAULT NULL,
`DateCreate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
`UserUpdate` varchar(255) DEFAULT NULL,
`DateUpdate` datetime DEFAULT NULL,
PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

