-- Script to prepare MySQL server for the project
-- Create project testing database with the name: hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create a new user named: hbnb_test with all privileges on the db hbnb_test_db
-- Set the password: hbnb_test_pwd if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant SELECT privilege for the user hbnb_test on the db performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
-- Grant all privileges to the new user on hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
