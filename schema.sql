DROP DATABASE IF EXISTS parsons;
CREATE DATABASE parsons;
USE parsons;

DROP TABLE IF EXISTS user;
CREATE TABLE user (
    id          int             PRIMARY KEY,
    username    varchar(100),
    password    varchar(100)
);