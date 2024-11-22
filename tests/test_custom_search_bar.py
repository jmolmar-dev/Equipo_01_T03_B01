import pytest
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from views.custom_search_bar import CustomSearchBar

# ===== Fixture para manejar QApplication =====


@pytest.fixture(scope="module", autouse=True)
def qt_app():
    """
    Crea una instancia global de QApplication para los widgets de Qt.
    """
    app = QApplication.instance() or QApplication([])
    yield app
    app.quit()

# ===== PRUEBAS PARA CustomSearchBar =====


def test_search_bar_creation():
    """
    Verifica que la barra de búsqueda se crea correctamente:
    - Tiene un placeholder en el campo de texto.
    - Los iconos de búsqueda y papelera están configurados.
    """
    search_bar = CustomSearchBar()
    # El placeholder no está vacío
    assert search_bar.campo_texto.placeholderText() != ""
    # El icono de búsqueda está configurado
    assert search_bar.icono_busqueda.pixmap() is not None
    # El icono de papelera está configurado
    assert search_bar.icono_papelera.pixmap() is not None


def test_search_bar_placeholder():
    """
    Comprueba que el texto del placeholder (marcador de posición) es correcto.
    """
    search_bar = CustomSearchBar()
    expected_placeholder = (
        "Búsqueda por código de producto o nombre o descripción o precio o stock o número de ventas"
    )
    assert search_bar.campo_texto.placeholderText() == expected_placeholder


def test_search_bar_keyboard_shortcuts():
    """
    Verifica que los atajos de teclado están configurados correctamente:
    - Ctrl+F para buscar.
    - Ctrl+E para enfocar.
    - Ctrl+Q para borrar.
    """
    search_bar = CustomSearchBar()
    assert search_bar.shortcut_buscar.key().toString() == "Ctrl+F"
    assert search_bar.shortcut_enfocar.key().toString() == "Ctrl+E"
    assert search_bar.shortcut_borrar.key().toString() == "Ctrl+Q"
