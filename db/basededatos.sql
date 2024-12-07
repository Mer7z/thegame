CREATE DATABASE IF NOT EXISTS juego;

USE juego;

DROP TABLE IF EXISTS jugador;
CREATE TABLE jugador(id int auto_increment primary key, nombre varchar(40), clave varchar(100), puntaje int default 0);

INSERT INTO jugador (nombre, clave) VALUES ("Rex", "123456");