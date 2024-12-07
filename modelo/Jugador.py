from db.Conexion import Conexion

class Jugador():
    def __init__(self, id = None, nombre = "", clave = "", puntaje = 0):
        self.id = id
        self.nombre = nombre
        self.clave = clave
        self.puntaje = puntaje

    def obtener_usurio(self, id):
        con = Conexion.crear_conexion()
        if con:
            cursor = con.cursor()
            cursor.execute(f"SELECT * FROM jugador WHERE id={id}")
            datos = cursor.fetchone()
            self.id = datos[0]
            self.nombre = datos[1]
            self.clave = datos[2]
            self.puntaje = datos[3]