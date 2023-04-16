USE builddeploydashboard;

CREATE TABLE IF NOT EXISTS auth_users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(150) NOT NULL UNIQUE,
    password VARCHAR(128) NOT NULL ,
    email VARCHAR(150) NOT NULL UNIQUE,
    role varchar(50) NULL 
);