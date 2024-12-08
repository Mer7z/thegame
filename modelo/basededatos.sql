CREATE DATABASE IF NOT EXISTS juego;

USE juego;

DROP TABLE IF EXISTS jugador;
CREATE TABLE jugador(id int auto_increment primary key, usuario varchar(40) unique, clave varchar(100), puntaje int default 0);

INSERT INTO jugador (usuario, clave) VALUES ("Rex", "123456");