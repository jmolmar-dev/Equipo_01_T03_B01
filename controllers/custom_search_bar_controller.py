from PySide6.QtCore import QObject, Slot #Importamos QObject para poder usar nuestra clase base y Slot para definir metodos como tales
from PySide6.QtGui import QMouseEvent #Importa QMouseEvent para manera los eventos de los clics
from views.custom_search_bar import  CustomSearchBar #Se importara la vista CustomSearchBar

class CustomSearchBarController(QObject):
    """Controlador con el que podremos gestionar la funcionalidad y eventos de la barra de busqueda personalizada"""

    def __init__(self, search_bar: CustomSearchBar, callback_func):
        """Inicializa el controlador para gestionar la barra de busqueda"""
        super().__init__()# LLamamos al constructor de la clase Padre (QObject)
        self.search_bar = search_bar
        self.callback_func = callback_func

        #CONFIGURACION DE SEÑALES Y EVENTOS
        self.conectar_sennales_eventos()


    def conectar_sennales_eventos (self):
        """Conectaremos las señales y los eventos dentro de la barra de busqueda"""
        self.search_bar.campo_texto.textChanged.connect(self.emitir_busqueda)
        self.search_bar.campo_texto.returnPressed.connect(self.emitir_busqueda)
        self.search_bar.icono_busqueda.mousePressEvent = self.icono_click

        #Conectamos el evento de click al metodo de limpieza
        self.search_bar.icono_busqueda.mousePressEvent = self.icono_click
        self.search_bar.icono_papelera.mousePressEvent =self.limpiar_campo_texto

        self.search_bar.shortcut_buscar.activated.connect(self.emitir_busqueda)
        self.search_bar.shortcut_enfocar.activated.connect(self.search_bar.campo_texto.setFocus)
        self.search_bar.shortcut_borrar.activated.connect(self.limpiar_campo_texto_atajo)

    @Slot()
    def emitir_busqueda (self):
        """Emitimos la señal de busqueda en tiempo real si hay texto en el campo de busqueda"""
        texto = self.search_bar.campo_texto.text()
        self.callback_func(texto)
        print(f"Emitido desde el controlador --> {texto}")

    def icono_click (self, event):
        """Manejador de eventos de clic en el icono de busqueda"""
        self.emitir_busqueda()
        print ("Se ha hecho click en el icono de Busqueda")

    def limpiar_campo_texto (self, event):
        """Limpia el texto del campo de busqueda cuando se hace clic en el icono de la papelera"""
        self.search_bar.campo_texto.clear()

    def limpiar_campo_texto_atajo(self):
        self.search_bar.campo_texto.clear()
        print("Campo de busqueda de texto limpiado mediante un atajo de teclado")

