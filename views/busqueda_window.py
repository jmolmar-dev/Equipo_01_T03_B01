from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Slot
from views.qt.qt_busqueda_equipo_1 import Ui_ventana_busqueda  # Vista para la ventana de búsqueda
from controllers.usuario_controller import UsuarioController  # Controlador para gestionar usuarios
from views.login_window import VentanaLogin  # Vista para la ventana de login
from PySide6.QtWidgets import QApplication

class VentanaBusqueda(QMainWindow):
    def __init__(self, parent=None):
        """
        Constructor de la clase VentanaBusqueda
        """
        try:
            # Inicialización de la ventana principal
            super().__init__(parent)
            
            # Configuración de la interfaz de usuario usando el archivo Ui generado por Qt Designer
            self.ui = Ui_ventana_busqueda()
            self.ui.setupUi(self)  # Configura la interfaz
            
            # Conectar los botones o eventos a sus respectivos métodos
            self.ui.boton_volver.clicked.connect(self.volver_a_login)  # Conectar el botón volver
            self.gestor_usuarios = UsuarioController()  # Instancia el controlador para manejar usuarios
            
        except Exception as e:
            print(f"Error al inicializar la ventana de búsqueda: {e}")

    @Slot()
    def volver_a_login(self):
        """
        Método que se ejecuta al hacer clic en el botón 'Volver' para regresar a la ventana de login.
        """
        try:
            # Ocultar la ventana de búsqueda
            self.hide()
            
            # Crear una instancia de la ventana de login (si no la tienes ya creada)
            self.ventana_login = VentanaLogin(parent=self)
            
            # Mostrar la ventana de login
            self.ventana_login.show()
        
        except Exception as e:
            print(f"Error al volver a la ventana de login: {e}")
