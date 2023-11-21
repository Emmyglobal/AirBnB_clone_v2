-- Script to prepare MySQL server for the project
-- Create project development database with the name: hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create a new user named: hbnb_dev with all privileges on the db hbnb_dev_db
-- Set the password: hbnb_dev_pwd if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant all privileges to the new user on hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
-- Grant the SELECT privilege for the user hbnb_dev in the db performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
