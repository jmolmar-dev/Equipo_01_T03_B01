# Importamos QMainWindow para construir la ventana principal de la aplicación
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Slot
from views.qt.qt_registro_equipo_1 import Ui_ventana_registro 
from controllers.usuario_controller import UsuarioController


class VentanaRegistro(QMainWindow):
    def __init__(self, parent = None):
        """
        Constructor de la clase VentanaRegistro.

        :param ventana_padre: Referencia a la ventana de login que actúa como ventana principal.
        """
        
        super().__init__(parent)
        # Inicializa la ventana QMainWindow
        # Crea una instancia de la interfaz gráfica de la ventana de registro
        self.ui = Ui_ventana_registro()
        # Configura la interfaz gráfica llamando al método setupUi
        self.ui.setupUi(self)

        # Conecta el botón "Iniciar sesión" para que al pulsarlo vuelva a la ventana de login
        self.ui.boton_login.clicked.connect(self.mostrar_ventana_login)

        # Conecta el botón "Registrar Cuenta" al método que se encarga de la creación de un usuario nuevo
        self.ui.boton_crear_cuenta.clicked.connect(self.procesar_registro_usuario)

        # Crea un controlador para manejar las operaciones relacionadas con el usuario en la base de datos
        # Este controlador realiza tareas de validación y creación en el modelo de usuario y la base de datos
        self.controlador_usuario = UsuarioController()

    

    @Slot()
    def mostrar_ventana_login(self):
        """
        Método que se ejecuta al hacer clic en 'Iniciar sesión'.
        Oculta esta ventana de registro y muestra la ventana de login.
        """
    # Oculta la ventana de registro --> ventana actual donde nos situamos
        self.hide()

    # Si existe una ventana padre, la utiliza para abrir la ventana de login
        if self.parent() is not None:  # Verifica que haya una ventana padre
            # Crea una nueva instancia de la ventana de login
            ventana_login = self.parent()  # Suponiendo que la ventana de login es la ventana padre
            ventana_login.show()  # Muestra la ventana de login


    @Slot()
    def procesar_registro_usuario(self):
        """
        Método para gestionar el registro de un usuario nuevo.
        Comprueba que las contraseñas coincidan y delega la creación al controlador.
        """
        # Obtiene los datos introducidos en los campos de texto
        correo = self.ui.email_valor.text()
        nombre_usuario = self.ui.usuario_valor.text()
        contrasena = self.ui.password_valor.text()
        contrasena_confirmacion = self.ui.password_confirmada_valor.text()

        # Verifica que las contraseñas coincidan
        if contrasena != contrasena_confirmacion:  # Compara ambas contraseñas
            # Muestra un mensaje de error si las contraseñas no coinciden
            print("Las contraseñas no coinciden")
            return  # Sale del método si las contraseñas no son iguales

        # Intenta registrar al nuevo usuario utilizando el controlador
        if self.controlador_usuario.register_user(correo, nombre_usuario, contrasena, contrasena_confirmacion):
            # El controlador verifica si el usuario ya existe y, de no ser así, lo guarda en la base de datos
            # Muestra un mensaje de éxito en la consola si el registro fue exitoso
            print("Usuario registrado con éxito")
        else:
            # Si ocurre algún problema (usuario ya existente o error en la base de datos), se muestra un mensaje aquí
            print("Error al registrar el usuario")  


