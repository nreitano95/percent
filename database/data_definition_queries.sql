
--
-- Table structure for table `UsersTest`
--

DROP TABLE IF EXISTS `UsersTest`;

CREATE TABLE `UsersTest` (
  `id` int(11) NOT NULL AUTO_INCREMENT UNIQUE,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Employees`
--

LOCK TABLES `UsersTest` WRITE;
INSERT INTO `UsersTest` (`first_name`, `last_name`) 
VALUES ('Michael', 'Scott'),
        ('Dwight', 'Schrute'),
        ('Jim', 'Halpert'),
        ('Andrew', 'Bernard'),
        ('Stanley', 'Hudson'),
        ('Phyllis', 'Vance'),
        ('Creed', 'Bratton'),
        ('Kevin', 'Malone'),
        ('Angela', 'Schrute');      
UNLOCK TABLES;

