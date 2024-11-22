from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Signal
from utils.colores import *


class CustomButton(QPushButton):
    def __init__(
        self,
        text="Volver",
        font_family="Arial",
        font_size=14,
        font_color=BLACK,
        bg_color=ORIGINAL_BUTTON,
        hover_color=YELLOW_ORANGE,
        pressed_color=GRIS_INTERFAZ,
        border_radius=5,
        parent=None,
    ):
        super().__init__(text, parent)

        # Asignación de colores
        self.bg_color = QColor(bg_color)
        self.hover_color = QColor(hover_color)
        self.pressed_color = QColor(pressed_color)
        self.text_color = QColor(font_color)

        # Configuración de la fuente y estilo
        self.setFontProperties(font_family, font_size)
        self.setStyleSheet(self.generateStyleSheet(self.bg_color, border_radius))

        # Auto-fill para asegurarnos que los colores se apliquen correctamente
        self.setAutoFillBackground(True)

    def setFontProperties(self, family, size):
        """Configura las propiedades de la fuente del botón."""
        font = self.font()
        font.setFamily(family)
        font.setPointSize(size)
        self.setFont(font)

    def generateStyleSheet(self, bg_color, border_radius):
        """Genera la hoja de estilo basada en los colores actuales."""
        return f"""
            QPushButton {{
                background-color: {bg_color.name()};
                color: {self.text_color.name()};
                border-radius: {border_radius}px;
            }}
        """

    def updateStyleSheet(self, bg_color):
        """Actualiza la hoja de estilo con el color de fondo especificado."""
        self.setStyleSheet(self.generateStyleSheet(bg_color, 5))

    ######### EVENTOS #########
    def enterEvent(self, event):
        """Se ejecuta al pasar el ratón sobre el botón."""
        self.updateStyleSheet(self.hover_color)
        super().enterEvent(event)

    def leaveEvent(self, event):
        """Se ejecuta al sacar el ratón del botón."""
        self.updateStyleSheet(self.bg_color)
        super().leaveEvent(event)

    def mousePressEvent(self, event):
        """Se ejecuta al presionar el botón."""
        print("Botón presionado")  # Depuración
        self.updateStyleSheet(self.pressed_color)
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        """Se ejecuta al soltar el botón."""
        # Determina si el ratón sigue sobre el botón para aplicar hover o fondo normal
        if self.underMouse():
            self.updateStyleSheet(self.hover_color)
        else:
            self.updateStyleSheet(self.bg_color)
        super().mouseReleaseEvent(event)  # Asegura la emisión de la señal `clicked`
