import mysql.connector
from mysql.connector import Error


class Conexion():
    def crear_conexion():
        try:
            conexion = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='juego'
            )
            if conexion.is_connected():
                print("Conexión exitosa a la base de datos")
                return conexion
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None

    def cerrar_conexion(conexion):
        if conexion and conexion.is_connected():
            conexion.close()
            print("Conexión cerrada exitosamente")

