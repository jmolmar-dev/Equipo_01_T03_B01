import sys  # Importa el módulo sys para operaciones del sistema
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Slot
from views.qt.qt_login_equipo_1 import Ui_Login_Equipo_1
from views.registro_window import VentanaRegistro
from controllers.usuario_controller import UsuarioController


class VentanaLogin(QMainWindow):
    """
    Clase que representa la ventana de inicio de sesión.
    """

    def __init__(self, parent=None):
        """
        Constructor que configura la ventana de inicio de sesión y sus componentes.
        """
        try:
            super().__init__(parent)
            self.ui = Ui_Login_Equipo_1()
            self.ui.setupUi(self)
            self.ui.button_crear_cuenta.clicked.connect(self.abrir_ventana_registro)
            self.ui.button_login_2.clicked.connect(self.iniciar_sesion)
            self.ventana_registro = None
            self.gestor_usuarios = UsuarioController()
        except Exception as e:
            print(f"Error al inicializar la ventana de login: {e}")

    @Slot()
    def abrir_ventana_registro(self):
        """
        Método que se ejecuta al hacer clic en 'Crear Cuenta'.
        """
        try:
            #Ocultamos la ventana de login
            self.hide()
            #Si no existe la ventana de registro, la creamos mediante una instancia padre
            if self.ventana_registro is None:
                self.ventana_registro = VentanaRegistro(parent=self)
            #Mostrmoas la ventana de registro y controlamos cualquier error con la excepcion
            self.ventana_registro.show()
        except Exception as e:
            print(f"Error al abrir la ventana de registro: {e}")

    
    @Slot()
    def iniciar_sesion(self):
        """
        Método que se ejecuta al hacer clic en 'Login'.
        """
        try:
            # Obtener el email y la contraseña desde la interfaz
            username = self.ui.campo_usuario.text()  # Campo donde se ingresa el email
            password = self.ui.campo_password.text()  # Campo donde se ingresa la contraseña

            # Llamar al método verify_user para verificar las credenciales
            usuario = self.gestor_usuarios.verify_user_by_name(username, password)

            if usuario is not None:
                print(f"Bienvenido {usuario.nombre_usuario}")  # Muestra el mensaje de bienvenida
            else:
                print("Credenciales no válidas")  # Mensaje de error si las credenciales son incorrectas
        except Exception as e:
            print(f"Error al iniciar sesión: {e}")  # Captura y muestra cualquier error que ocurra

    