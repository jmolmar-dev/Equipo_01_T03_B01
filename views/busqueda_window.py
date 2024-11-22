from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton
from PySide6.QtCore import Slot
from views.custom_search_bar import CustomSearchBar



from Custom_Search_Bar.controllers.custom_search_bar_controller import CustomSearchBarController
from customButton.views.custom_button import CustomButton
from customTableView.views.custom_tableview import CustomTableView
from customTableView.controllers.custom_tableview_controller import CustomTableViewController
import utils.etiquetas as etiquetas
import utils.estilos as estilos


class BusquedaWindow(QMainWindow):
    def __init__(self, ventana_login=None):
        """Constructor de la clase BusquedaWindow"""
        super().__init__()
        self.ventana_login = ventana_login  # Guardamos la referencia a la ventana de login
        print(f"ventana_login recibido: {self.ventana_login}")

        self.configurar_ventana()
        self.creacion_widgets()
        self.inicializar_controladores()
        self.configurar_layouts()

    def configurar_ventana(self):
        """Configuramos las propiedades de la Ventana Principal"""
        self.setWindowTitle(etiquetas.TITULO_VENTANA_PRINCIPAL)
        self.resize(800, 600)

    def creacion_widgets(self):
        """Creamos los widgets de la ventana principal"""
        print("Creando widgets...")
        self.search_bar = CustomSearchBar(estilos.ESTILO_CAMPO_TEXTO)
        self.tabla = CustomTableView(estilos.ESTILO_TABLA)
        self.button = CustomButton(text="Volver a Login")
        self.button.clicked.connect(self.volver_a_login)
        print("Botón conectado al slot volver_a_login")

    def inicializar_controladores(self):
        """Inicializamos los controladores de los widgets de la ventana principal"""
        self.table_controller = CustomTableViewController(self.tabla)
        self.search_controller = CustomSearchBarController(self.search_bar, self.tabla.filtrar_tabla)

    def configurar_layouts(self):
        """Configura el layout principal de la ventana"""
        layout_principal = QVBoxLayout()
        layout_principal.addWidget(self.search_bar)
        layout_principal.addWidget(self.tabla)
        layout_principal.addWidget(self.button)

        widget = QWidget()
        widget.setLayout(layout_principal)
        self.setCentralWidget(widget)

    @Slot()
    def volver_a_login(self):
        """Método que se ejecuta al hacer clic en 'Volver a Login'"""
        print("Botón 'Volver a Login' presionado")  # Depuración
        try:
            self.hide()  # Ocultamos la ventana de búsqueda
            if self.ventana_login is not None:
                self.ventana_login.show()  # Mostramos la ventana de login
            else:
                print("Referencia a ventana_login no válida")  # Depuración
        except Exception as e:
            print(f"Error al volver a la ventana de login: {e}")
