from PySide6.QtWidgets import QTableView, QHeaderView
from PySide6.QtCore import Qt, QSortFilterProxyModel
from PySide6.QtGui import QStandardItemModel, QStandardItem
from datetime import datetime
import utils.estilos as estilos


class CustomTableView(QTableView):

    def __init__(self, estilo=None, parent=None):
        """Constructor de la clase CustomTableView."""
        super().__init__(parent)

        # CONFIGURACIÓN DE COMPONENTES
        self._configurar_datos_tabla()
        self._configurar_filtro_datos()
        self._configurar_cabeceras()

        # ESTILOS
        if estilo is not None:
            self.setStyleSheet(estilo)

    def _configurar_datos_tabla(self):
        """Configura la estructura de los datos de la tabla."""
        # Crea un modelo de datos con 6 columnas
        self.datos_tabla = QStandardItemModel(0, 6)
        # Establece los nombres de las cabeceras de las columnas
        self.datos_tabla.setHorizontalHeaderLabels(
            ["Título", "Género", "Plataforma", "Desarrollador",
                "Fecha de Lanzamiento", "Sinopsis"]
        )

    def _configurar_filtro_datos(self):
        """Configura el filtro de datos para la búsqueda y filtrado."""
        self.filtro_datos = QSortFilterProxyModel()
        self.filtro_datos.setSourceModel(self.datos_tabla)
        self.filtro_datos.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.filtro_datos.setFilterKeyColumn(-1)
        self.setModel(self.filtro_datos)

    def _configurar_cabeceras(self):
        """Configura las cabeceras de la tabla."""
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.horizontalHeader().setStretchLastSection(True)
        for i in range(6):
            self.horizontalHeader().setSectionResizeMode(
                i, QHeaderView.ResizeToContents if i in [
                    0, 1, 2, 3, 4] else QHeaderView.Stretch
            )

    def cargar_videojuegos_en_tabla(self, videojuegos):
        """Carga una lista de objetos Videojuego en la tabla.

        Args:
            videojuegos (list): Lista de objetos Videojuego a cargar en la tabla.
        """
        # Limpia cualquier fila existente en la tabla
        self.datos_tabla.setRowCount(0)
        # Itera sobre la lista de videojuegos y agrega cada uno como una fila en la tabla
        for videojuego in videojuegos:
            # Obtener la fecha de lanzamiento y convertirla a cadena con formato 'YYYY-MM-DD'
            fecha_lanzamiento = videojuego.get_fechaLanzamiento()
            if isinstance(fecha_lanzamiento, datetime):
                fecha_str = fecha_lanzamiento.strftime('%Y-%m-%d')
            else:
                fecha_str = str(fecha_lanzamiento)  # En caso de que no sea datetime, convertimos a string directamente

            fila = [
                # Columna de título
                QStandardItem(videojuego.get_titulo()),
                # Columna de género
                QStandardItem(videojuego.get_genero()),
                # Columna de plataforma
                QStandardItem(videojuego.get_plataforma()),
                # Columna de desarrollador
                QStandardItem(videojuego.get_desarrollador()),
                # Columna de fecha de lanzamiento
                QStandardItem(fecha_str),  # Usamos la fecha convertida a string
                # Columna de sinopsis
                QStandardItem(videojuego.get_sinopsis())
            ]
            # Alinea el texto al centro para ciertas columnas
            for i, item in enumerate(fila):
                if i in [0, 1, 2, 3, 4]:
                    item.setTextAlignment(Qt.AlignCenter)
            # Agrega la fila al modelo de datos
            self.datos_tabla.appendRow(fila)

    def filtrar_tabla(self, texto):
        """Aplica un filtro al modelo de datos para mostrar solo las filas que coincidan con el texto.

        Args:
            texto (str): Texto de búsqueda.
        """
        self.filtro_datos.setFilterFixedString(texto.strip())
