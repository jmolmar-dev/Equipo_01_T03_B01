from PySide6.QtWidgets import QWidget, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt, QSize, Slot, Signal
from PySide6.QtGui import QPixmap, QCursor, QKeySequence, QShortcut, QIcon

import utils.path as path
import utils.colores as color
import utils.etiquetas as etiqueta

class CustomSearchBar(QWidget):
    def __init__(self, estilo=None, parent=None):
        """Constructor de la clase CustomSearchBar."""
        # Llama al constructor de la clase base QWidget con el parámetro parent
        super().__init__(parent)

        # Llamamos a los métodos para configurar los elementos
        self.configurar_icono_busqueda()
        self.configuracion_campo_texto()
        self.configuracion_icono_papelera()
        self.configuracion_atajos()
        self.configuracion_layouts()
        self.configurar_orden_tabulaciones()

    def configurar_icono_busqueda(self):
        """Configurar el QLabel del icono de búsqueda"""
        self.icono_busqueda = QLabel()  # Crearemos un QLabel para el icono de búsqueda
        pixmap = QPixmap(path.SEARCH_ICON_PATH)

        if not pixmap.isNull():
            pixmap = pixmap.scaled(24, 24, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            self.icono_busqueda.setPixmap(pixmap)
        else:
            print("Error, no hemos podido cargar el icono de búsqueda")

        self.icono_busqueda.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.icono_busqueda.setFixedSize(QSize(30, 30))
        self.icono_busqueda.setStyleSheet("background-color: transparent;")
        self.icono_busqueda.setCursor(QCursor(Qt.PointingHandCursor))

    def configuracion_campo_texto(self):
        """Configura el QLineEdit del campo de texto"""
        self.campo_texto = QLineEdit()
        self.campo_texto.setPlaceholderText(etiqueta.PLACEHOLDER_CAMPO_BUSQUEDA)
        self.campo_texto.setToolTip(etiqueta.TOOLTIP_CAMPO_BUSQUEDA)
        self.campo_texto.setMinimumWidth(200)
        self.campo_texto.setMaximumWidth(450)

    def configuracion_icono_papelera(self):
        """Configuración del QLabel del icono de la papelera"""
        self.icono_papelera = QLabel()  # Crearemos el QLabel para el icono de la papelera
        pixmap = QPixmap(path.TRASH_ICON_PATH)

        if not pixmap.isNull():
            pixmap = pixmap.scaled(24, 24, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)  # Escala el pixmap
            self.icono_papelera.setPixmap(pixmap)
        else:
            print("Error: no se pudo cargar el icono de la papelera")

        self.icono_papelera.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.icono_papelera.setFixedSize(QSize(30, 30))
        self.icono_papelera.setStyleSheet("background-color: transparent;")
        self.icono_papelera.setCursor(QCursor(Qt.PointingHandCursor))

    def configuracion_atajos(self):
        """Configuración de los atajos de teclado"""
        self.shortcut_buscar = QShortcut(QKeySequence("Ctrl+F"), self)
        self.shortcut_enfocar = QShortcut(QKeySequence("Ctrl+E"), self)
        self.shortcut_borrar = QShortcut(QKeySequence("Ctrl+Q"), self)

    def configuracion_layouts(self):
        """Configuración de los layouts de la interfaz"""

        # Configuración del layout horizontal
        horizontal_layout = QHBoxLayout()
        horizontal_layout.addWidget(self.icono_busqueda)
        horizontal_layout.addWidget(self.campo_texto)
        horizontal_layout.addWidget(self.icono_papelera)
        horizontal_layout.setSpacing(5)
        horizontal_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)

        # Configuración del layout vertical
        vertical_layout = QVBoxLayout()
        vertical_layout.addLayout(horizontal_layout)
        vertical_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)
        vertical_layout.setContentsMargins(20, 20, 20, 20)

        self.setLayout(vertical_layout)

    def configurar_orden_tabulaciones(self):
        """Configurar el orden de tabulación de los widgets en la vista"""
        self.setTabOrder(self.icono_busqueda, self.campo_texto)
        self.setTabOrder(self.campo_texto, self.icono_papelera)
