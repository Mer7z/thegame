from vista.Login import Login
from controlador.Jugador import Jugador
from vista.Tips import add_tooltip

class Registro(Login):

    def iniciarSesion(self, event):
        if self.nombre and self.clave:
            try:
                mijugador = Jugador().registrar_jugador(self.nombre, self.clave)
                if mijugador:
                    self.root.setJugador(mijugador)
                    self.ventana.destroy()
                else:
                    self.lblErr.config(text="Error en la base de datos. Verifique la conexión")
            except Exception as e:
                self.lblErr.config(text=e)
        else:
            self.lblErr.config(text="Campos faltantes.\nDebes ingresar un nombre y contraseña.")

    def __init__(self, root):
        super().__init__(root)
        self.ventana.title("Registrarse")
        self.lblTitulo.config(text="Registro")
        self.btnLogin.config(text="Registrarse",bg="gray30", fg="white")
        add_tooltip(self.btnLogin, "Haz clic aquí para terminar el registro e iniciar sesión.")
