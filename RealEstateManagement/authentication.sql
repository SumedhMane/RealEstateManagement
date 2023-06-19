create database studentregistration;

use studentregistration;

CREATE TABLE Login
(user int auto_increment key not null,
UserName varchar(100),
PassWord varchar(100))

CREATE TABLE Login
(User int NOT NULL AUTO_INCREMENT PRIMARY KEY,
Username varchar(100),
Password varchar(100)
);

insert into Login values(1,"Sumedh","mane@123");

INSERT INTO Login (Username,Password)
VALUES ("Devesh","Narkhede@543");

INSERT INTO Login (Username,Password)
VALUES ("Rahu;","nagalang@3");

INSERT INTO Login (Username,Password)
VALUES ("rajkumar","Nadsa2");

INSERT INTO Login (Username,Password)
VALUES ("Lalit","patil@832");

INSERT INTO Login (Username,Password)
VALUES ("Pushkraj","chd@12");

INSERT INTO Login (Username,Password)
VALUES ("Vinay","naguu@131");

INSERT INTO Login (Username,Password)
VALUES ("Yash","hedb@84");

INSERT INTO Login (Username,Password)
VALUES ("Jitesh","jiyv@766");

INSERT INTO Login (Username,Password)
VALUES ("Akshay","gabjm@722");

select * from login;
