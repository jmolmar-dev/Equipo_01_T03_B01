from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Slot
from views.qt.qt_login_equipo_1 import Ui_Login_Equipo_1
from views.registro_window import VentanaRegistro
from controllers.usuario_controller import UsuarioController
from views.busqueda_window import BusquedaWindow


class VentanaLogin(QMainWindow):
    def __init__(self, parent=None):
        """Constructor que configura la ventana de inicio de sesión y sus componentes."""
        super().__init__(parent)
        self.ui = Ui_Login_Equipo_1()
        self.ui.setupUi(self)

        self.ui.button_crear_cuenta.clicked.connect(self.abrir_ventana_registro)
        self.ui.button_login_2.clicked.connect(self.iniciar_sesion)
        self.ventana_registro = None
        self.gestor_usuarios = UsuarioController()
        self.ventana_busqueda = None

    @Slot()
    def abrir_ventana_registro(self):
        """Método que se ejecuta al hacer clic en 'Crear Cuenta'."""
        try:
            self.hide()
            if self.ventana_registro is None:
                self.ventana_registro = VentanaRegistro(parent=self)
            self.ventana_registro.show()
        except Exception as e:
            print(f"Error al abrir la ventana de registro: {e}")

    @Slot()
    def iniciar_sesion(self):
        """Método que se ejecuta al hacer clic en 'Login'."""
        try:
            username = self.ui.campo_usuario.text()
            password = self.ui.campo_password.text()
            usuario = self.gestor_usuarios.verify_user_by_name(username, password)
            if usuario is not None:
                print(f"Bienvenido {usuario.nombre_usuario}")
                self.abrir_ventana_busqueda()
            else:
                print("Credenciales no válidas")
        except Exception as e:
            print(f"Error al iniciar sesión: {e}")

    @Slot()
    def abrir_ventana_busqueda(self):
        """Método que se ejecuta después de iniciar sesión con éxito."""
        try:
            self.hide()
            if self.ventana_busqueda is None:
                self.ventana_busqueda = BusquedaWindow(self)
            self.ventana_busqueda.show()
        except Exception as e:
            print(f"Error al abrir la ventana de búsqueda: {e}")
