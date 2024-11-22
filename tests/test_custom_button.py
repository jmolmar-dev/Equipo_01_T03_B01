import pytest
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPalette

from views.custom_button import CustomButton

# ===== Fixture para manejar QApplication =====


@pytest.fixture(scope="module", autouse=True)
def qt_app():
    """
    Crea una instancia global de QApplication para usar en las pruebas.
    Esta instancia es necesaria para que los widgets de Qt funcionen correctamente.
    """
    app = QApplication.instance() or QApplication(
        [])  # Reutiliza o crea QApplication
    yield app
    app.quit()  # Finaliza la aplicación después de las pruebas

# ===== PRUEBAS PARA CustomButton =====


def test_custom_button_creation():
    """
    Verifica que el botón personalizado se crea con las propiedades correctas.
    - El texto es correcto.
    - El botón es visible después de crearlo.
    """
    button = CustomButton(text="Probar")
    button.show()
    assert button.text() == "Probar"  # Comprueba el texto del botón
    assert button.isVisible() is True  # Verifica que el botón esté visible


def test_custom_button_hover_event(qtbot):
    """
    Valida que el color del botón cambia correctamente al pasar el mouse sobre él.
    """
    button = CustomButton()
    qtbot.addWidget(button)  # Añade el botón al entorno de pruebas de Qt
    button.show()
    # Espera a que el botón esté completamente renderizado
    qtbot.waitExposed(button)
    qtbot.mouseMove(button)  # Simula mover el cursor sobre el botón
    qtbot.wait(100)  # Pequeña espera para procesar el evento de hover
    # Verifica que el color del fondo coincide con hover_color
    assert button.palette().color(button.backgroundRole()) == QColor(button.hover_color)


def test_custom_button_initial_style(qtbot):
    """
    Verifica que el botón personalizado se inicializa con los estilos correctos.
    - Color de fondo inicial: blanco.
    - Color del texto inicial: negro.
    """
    button = CustomButton(
        text="Prueba",
        bg_color="#FFFFFF",  # Fondo blanco
        font_color="#000000"  # Texto negro
    )
    qtbot.addWidget(button)
    button.show()

    # Verifica el color de fondo inicial
    background_color = button.palette().color(button.backgroundRole())
    assert background_color == QColor("#FFFFFF"), (
        f"Color de fondo esperado: #FFFFFF, pero se obtuvo: {
            background_color.name()}"
    )

    # Verifica el color del texto inicial
    text_color = button.palette().color(QPalette.ColorRole.ButtonText)
    assert text_color == QColor("#000000"), (
        f"Color de texto esperado: #000000, pero se obtuvo: {
            text_color.name()}"
    )
