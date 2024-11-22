import pytest
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor

from views.custom_tableview import CustomTableView

# ===== Fixture para manejar QApplication =====


@pytest.fixture(scope="module", autouse=True)
def qt_app():
    """
    Crea una instancia de QApplication para las pruebas de widgets de Qt.
    """
    app = QApplication.instance() or QApplication([])
    yield app
    app.quit()

# ===== PRUEBAS PARA CustomTableView =====


def test_table_view_creation():
    """
    Verifica que la tabla personalizada se crea correctamente:
    - No tiene filas iniciales.
    - Tiene 6 columnas por defecto.
    """
    table = CustomTableView()
    assert table.model().rowCount() == 0  # La tabla está vacía inicialmente
    assert table.model().columnCount() == 6  # Hay 6 columnas configuradas


def test_table_view_add_data():
    """
    Comprueba que los datos se pueden cargar correctamente en la tabla.
    """
    table = CustomTableView()

    # Clase mock para simular un videojuego
    class MockVideojuego:
        def get_titulo(self): return "Título"
        def get_genero(self): return "Acción"
        def get_plataforma(self): return "PC"
        def get_desarrollador(self): return "Desarrollador X"
        def get_fechaLanzamiento(self): return "2024-01-01"
        def get_sinopsis(self): return "Descripción del juego."

    videojuegos = [MockVideojuego()]
    table.cargar_videojuegos_en_tabla(
        videojuegos)  # Carga los datos en la tabla
    assert table.model().rowCount() == 1  # Hay una fila cargada
    # Verifica que el título del videojuego se muestra correctamente en la tabla
    assert table.model().data(table.model().index(0, 0)) == "Título"


def test_table_view_filter():
    """
    Comprueba que el filtro de búsqueda funciona correctamente:
    - Muestra las filas que coinciden con el texto.
    - Oculta las filas que no coinciden.
    """
    table = CustomTableView()

    # Clase mock para simular un videojuego
    class MockVideojuego:
        def get_titulo(self): return "Título"
        def get_genero(self): return "Acción"
        def get_plataforma(self): return "PC"
        def get_desarrollador(self): return "Desarrollador X"
        def get_fechaLanzamiento(self): return "2024-01-01"
        def get_sinopsis(self): return "Descripción del juego."

    videojuegos = [MockVideojuego()]
    # Carga un videojuego de prueba
    table.cargar_videojuegos_en_tabla(videojuegos)

    # Filtra por un texto que coincide
    table.filtrar_tabla("Título")
    assert table.model().rowCount() == 1  # La fila sigue visible

    # Filtra por un texto que no coincide
    table.filtrar_tabla("Inexistente")
    assert table.model().rowCount() == 0  # No hay filas visibles
