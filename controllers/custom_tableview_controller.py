# Importa QObject para crear la clase base y Slot para definir funciones como slots
from PySide6.QtCore import QObject, Slot
# Importa el controlador de videojuegos
from customTableView.controllers.videojuego_controller import VideojuegoController
from customTableView.models.videojuego import Videojuego


class CustomTableViewController(QObject):
    """Controlador para gestionar la vista de tabla de videojuegos."""

    def __init__(self, table_view):
        """Inicializa el controlador para la vista de tabla."""
        super().__init__()
        self.table_view = table_view
        self.videojuego_controller = VideojuegoController()

        # Configura señales y eventos
        self._conectar_signals_y_eventos()

        # Cargar videojuegos en la tabla al inicializar
        self.cargar_datos()

    def _conectar_signals_y_eventos(self):
        """Conecta las señales y eventos de la tabla."""
        self.table_view.clicked.connect(self.mostrar_detalle_videojuego)

    @Slot()
    def mostrar_detalle_videojuego(self, index):
        """Muestra detalles del videojuego seleccionado."""
        datos_tabla = index.model().sourceModel()

        titulo = datos_tabla.item(index.row(), 0).text()
        genero = datos_tabla.item(index.row(), 1).text()
        plataforma = datos_tabla.item(index.row(), 2).text()
        desarrollador = datos_tabla.item(index.row(), 3).text()
        fecha_lanzamiento = datos_tabla.item(index.row(), 4).text()
        sinopsis = datos_tabla.item(index.row(), 5).text()

        videojuego = Videojuego(
            titulo, genero, plataforma, desarrollador, fecha_lanzamiento, sinopsis)
        print(f"Videojuego seleccionado: {videojuego}")

    def cargar_datos(self):
        """Carga videojuegos en la tabla."""
        videojuegos = self.videojuego_controller.obtener_videojuegos()
        self.table_view.cargar_videojuegos_en_tabla(videojuegos)
