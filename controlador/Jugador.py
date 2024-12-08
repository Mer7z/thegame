from modelo.Conexion import Conexion

class Jugador():
    def __init__(self, id = None, nombre = "", clave = "", puntaje = 0):
        self.id = id
        self.nombre = nombre
        self.clave = clave
        self.puntaje = puntaje

    def obtener_usurio(self, id):
        con = Conexion.crear_conexion()
        if not con:
            return
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM jugador WHERE id={id}")
        datos = cursor.fetchone()
        self.id = datos[0]
        self.nombre = datos[1]
        self.clave = datos[2]
        self.puntaje = datos[3]
        Conexion.cerrar_conexion(con)
        return self


    def iniciar_sesion(self, nombre, clave):
        con = Conexion.crear_conexion()
        if not con:
            return
        cursor = con.cursor()
        cursor.execute("SELECT * FROM jugador WHERE usuario=%s", (nombre,))
        datosjugador = cursor.fetchone()
        sesionIniciada = False
        error = ""
        if datosjugador:
            if datosjugador[2] == clave:
                print("Inició sección correctamente")
                self.obtener_usurio(datosjugador[0])
                sesionIniciada = True
            else:
                error = "Nombre o contraseña incorrectos"
        else:
            error = "El usuario no existe"
        Conexion.cerrar_conexion(con)
        if sesionIniciada:
            return self
        else:
            raise Exception(error)
        
    def registrar_jugador(self, nombre, clave):
        con = Conexion.crear_conexion()
        if not con:
            return
        cursor = con.cursor()
        cursor.execute("SELECT id FROM jugador WHERE usuario=%s", (nombre,))
        obtenido = cursor.fetchone()
        if obtenido:
            Conexion.cerrar_conexion(con)
            raise Exception("El usuario ya existe")
        
        cursor.execute("INSERT INTO jugador (usuario, clave) VALUES (%s, %s)", (nombre, clave,))
        con.commit()
        cursor.execute("SELECT id FROM jugador WHERE usuario=%s", (nombre,))
        jugador = cursor.fetchone()
        print(jugador)

        Conexion.cerrar_conexion(con)
        if jugador:
            return self.obtener_usurio(jugador[0])
        