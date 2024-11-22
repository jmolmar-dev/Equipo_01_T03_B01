#Importaciones de módulos necesarios de PySide6
#QtCore, QtGui y QtWidgets incluyen componentes esenciales de Qt como layouts, colores, ...
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Slot)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QWidget)



#Clase para la interfaz de la ventana de Login
class Ui_Login_Equipo_1(object):
    #Metodo que nos configurara la interfaz de usuario para la ventana de Login
    def setupUi(self, Login_Equipo_1):
        #Configuracion basica de nuestra ventana principal de Login: se configura el nombre del objeto si no ha sido establecido
        if not Login_Equipo_1.objectName():
            Login_Equipo_1.setObjectName("Login_Equipo_1")
        Login_Equipo_1.resize(480, 620)
        Login_Equipo_1.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        Login_Equipo_1.setAutoFillBackground(False)
        
        #Color de fondo y fuente establecidos dentro de nuestra ventana de Login
        Login_Equipo_1.setStyleSheet("background-color: rgb(5, 13, 33);\n""font: 10pt \"Arial\";")
        Login_Equipo_1.setTabShape(QTabWidget.TabShape.Rounded)
        
        
        #Definicion de las acciones dentro de la barra de menu (Salir, Guardar, ....)
        self.actionpepe = QAction(Login_Equipo_1)
        self.actionpepe.setObjectName("actionpepe")
        self.actionSalir = QAction(Login_Equipo_1)
        self.actionSalir.setObjectName("actionSalir")
        self.actionGuardar = QAction(Login_Equipo_1)
        self.actionGuardar.setObjectName("actionGuardar")
        self.actionGuardar_Como = QAction(Login_Equipo_1)
        self.actionGuardar_Como.setObjectName("actionGuardar_Como")
        self.actionEditar = QAction(Login_Equipo_1)
        self.actionEditar.setObjectName("actionEditar")
        self.actionDeshacer = QAction(Login_Equipo_1)
        self.actionDeshacer.setObjectName("actionDeshacer")
        self.actionReahacer = QAction(Login_Equipo_1)
        self.actionReahacer.setObjectName("actionReahacer")
        self.actionCortar = QAction(Login_Equipo_1)
        self.actionCortar.setObjectName("actionCortar")
        self.actionCopiar = QAction(Login_Equipo_1)
        self.actionCopiar.setObjectName("actionCopiar")
        self.actionZoom_in = QAction(Login_Equipo_1)
        self.actionZoom_in.setObjectName("actionZoom_in")
        self.actionZoom_out = QAction(Login_Equipo_1)
        self.actionZoom_out.setObjectName("actionZoom_out")
        self.actionDocumentacion = QAction(Login_Equipo_1)
        self.actionDocumentacion.setObjectName("actionDocumentacion")
        self.actionAbout = QAction(Login_Equipo_1)
        self.actionAbout.setObjectName("actionAbout")
        self.actionDocumentacion_2 = QAction(Login_Equipo_1)
        self.actionDocumentacion_2.setObjectName("actionDocumentacion_2")
        self.actionAbout_2 = QAction(Login_Equipo_1)
        self.actionAbout_2.setObjectName("actionAbout_2")
        self.actionPegar = QAction(Login_Equipo_1)
        self.actionPegar.setObjectName("actionPegar")
        
        #Creacion y configuracion del widget centrar y layout
        self.centralwidget = QWidget(Login_Equipo_1)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.layout2 = QHBoxLayout()
        self.layout2.setSpacing(6)
        self.layout2.setObjectName("layout2")
        self.layout2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        
        #Creacion del QLabel para mostrar texto ¿No tiene una cuenta?
        self.info = QLabel(self.centralwidget)
        self.info.setObjectName("info")
        self.info.setMinimumSize(QSize(158, 30))
        self.info.setMaximumSize(QSize(158, 30))
        self.info.setStyleSheet("color: rgb(201, 213, 238);")

        #Incluye el label info al layout horizontal layout2
        self.layout2.addWidget(self.info)

        #Creacion y configuracion del boton de Crear Cuenta
        self.button_crear_cuenta = QPushButton(self.centralwidget)
        self.button_crear_cuenta.setObjectName("button_login_1")
        self.button_crear_cuenta.setMinimumSize(QSize(157, 23))
        self.button_crear_cuenta.setMaximumSize(QSize(157, 23))
        self.button_crear_cuenta.setStyleSheet("background-color: rgb(26, 103, 248);")

        #Añade el botón "Crear Cuenta" al layout horizontal layout2 con alineación vertical al centro
        self.layout2.addWidget(self.button_crear_cuenta, 0, Qt.AlignmentFlag.AlignVCenter)

        #Añade el layout `layout2` al grid layout principal
        self.gridLayout.addLayout(self.layout2, 2, 0, 1, 1)

        #Creacion y configuracion del boton Login
        self.button_login_2 = QPushButton(self.centralwidget)
        self.button_login_2.setObjectName("button_login_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_login_2.sizePolicy().hasHeightForWidth())
        self.button_login_2.setSizePolicy(sizePolicy)
        self.button_login_2.setMinimumSize(QSize(460, 51))
        #Configuracion de fuente y estilo dentro del boton de Login
        font = QFont()
        font.setFamilies(["Arial"])
        font.setPointSize(10)
        self.button_login_2.setFont(font)
        self.button_login_2.setStyleSheet("background-color: rgb(26, 103, 248);\n""")
        
        #Añadimos el botón de Login al grid layout 
        self.gridLayout.addWidget(self.button_login_2, 3, 0, 1, 1)

        #Creación y configuración del título principal en la ventana de Login
        self.titulo_main = QLabel(self.centralwidget)
        self.titulo_main.setObjectName("titulo_main")
        self.titulo_main.setMinimumSize(QSize(67, 160))
        self.titulo_main.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.titulo_main.setStyleSheet("color: rgb(201, 213, 238);\n"" font-size:20pt;\n""")
        self.titulo_main.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #Incluimos el titulo principal dentro del grid layout
        self.gridLayout.addWidget(self.titulo_main, 0, 0, 1, 1)

        #Configuración de layout1 como un QFormLayout para los campos de usuario y contraseña
        self.layout1 = QFormLayout()
        self.layout1.setObjectName("layout1")
        self.layout1.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.layout1.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout1.setHorizontalSpacing(20)
        self.layout1.setVerticalSpacing(20)
        
        #Creacion y configuracion del Label Usuario
        self.titulo_usuario = QLabel(self.centralwidget)
        self.titulo_usuario.setObjectName("titulo_usuario")
        self.titulo_usuario.setMinimumSize(QSize(121, 51))
        self.titulo_usuario.setMaximumSize(QSize(121, 51))
        self.titulo_usuario.setFont(font)
        self.titulo_usuario.setAutoFillBackground(False)
        self.titulo_usuario.setStyleSheet("color: rgb(201, 213, 238);")

        #Incluimos el Label Usuario dentro del layout1
        self.layout1.setWidget(0, QFormLayout.ItemRole.LabelRole, self.titulo_usuario)

        #Creacion y configuracion del campo de entrada de texto para el nombre de usuario
        self.campo_usuario = QLineEdit(self.centralwidget)
        self.campo_usuario.setObjectName("campo_usuario")
        self.campo_usuario.setMinimumSize(QSize(161, 51))
        self.campo_usuario.setMaximumSize(QSize(161, 51))
        self.campo_usuario.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.campo_usuario.setStyleSheet("background-color: rgb(255, 255, 255);")

        #Incluimos el campo de usuario al layout1
        self.layout1.setWidget(0, QFormLayout.ItemRole.FieldRole, self.campo_usuario)

        #Creacion y configuracion del label Contraseña
        self.titulo_password = QLabel(self.centralwidget)
        self.titulo_password.setObjectName("titulo_password")
        self.titulo_password.setMinimumSize(QSize(121, 51))
        self.titulo_password.setMaximumSize(QSize(121, 51))
        self.titulo_password.setFont(font)
        self.titulo_password.setAutoFillBackground(False)
        self.titulo_password.setStyleSheet("color: rgb(201, 213, 238);")

        #Incluimos el label de contraseña dentro del layout1
        self.layout1.setWidget(1, QFormLayout.ItemRole.LabelRole, self.titulo_password)

        #Creacion y configuracion del campo de entrada de texto para la Contraseña
        self.campo_password = QLineEdit(self.centralwidget)
        self.campo_password.setObjectName("campo_password")
        self.campo_password.setMinimumSize(QSize(161, 51))
        self.campo_password.setMaximumSize(QSize(161, 51))
        self.campo_password.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.campo_password.setStyleSheet("background-color: rgb(255, 255, 255);\n""")
        self.campo_password.setEchoMode(QLineEdit.EchoMode.Password)

        #Incluimos el campo de la Contraseña dentro del layout1
        self.layout1.setWidget(1, QFormLayout.ItemRole.FieldRole, self.campo_password)

        #Se incluye el layout1 dentro del grid layout
        self.gridLayout.addLayout(self.layout1, 1, 0, 1, 1)

        #Finalizamos configurando el layout central y estableciendo tanto el menu como el status bar
        Login_Equipo_1.setCentralWidget(self.centralwidget)
        self.titulo_main.raise_()
        self.button_login_2.raise_()
        self.menubar = QMenuBar(Login_Equipo_1)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 480, 33))
        self.menubar.setStyleSheet("color: rgb(201, 213, 238);")
        self.menuEditar = QMenu(self.menubar)
        self.menuEditar.setObjectName("menuEditar")
        self.menuEditar.setStyleSheet("color: rgb(201, 213, 238);")
        self.menuVista = QMenu(self.menubar)
        self.menuVista.setObjectName("menuVista")
        self.menuVista.setStyleSheet("color: rgb(201, 213, 238);")
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuArchivo.setStyleSheet("color: rgb(201, 213, 238);")
        self.menuAyuda = QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        self.menuAyuda.setStyleSheet("color: rgb(201, 213, 238);")
        Login_Equipo_1.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Login_Equipo_1)
        self.statusbar.setObjectName("statusbar")
        Login_Equipo_1.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuEditar.menuAction())
        self.menubar.addAction(self.menuVista.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.menuEditar.addAction(self.actionDeshacer)
        self.menuEditar.addSeparator()
        self.menuEditar.addAction(self.actionReahacer)
        self.menuEditar.addSeparator()
        self.menuEditar.addAction(self.actionCortar)
        self.menuEditar.addSeparator()
        self.menuEditar.addAction(self.actionCopiar)
        self.menuEditar.addSeparator()
        self.menuEditar.addAction(self.actionPegar)
        self.menuVista.addAction(self.actionZoom_in)
        self.menuVista.addSeparator()
        self.menuVista.addAction(self.actionZoom_out)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionSalir)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionGuardar_Como)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionEditar)
        self.menuAyuda.addAction(self.actionDocumentacion_2)
        self.menuAyuda.addSeparator()
        self.menuAyuda.addAction(self.actionAbout_2)

        #Metodo para establecer texto en cada uno de los elementos de la UI
        self.retranslateUi(Login_Equipo_1)

        #Metodo que nos contecta las señales y los slots en la interfaz
        QMetaObject.connectSlotsByName(Login_Equipo_1)
    
    #Metodo pata traducir y asignar texto a cada componente de la interfaz
    def retranslateUi(self, Login_Equipo_1):
          #Traduccion basica de los textos de la UI
        Login_Equipo_1.setWindowTitle(QCoreApplication.translate("Login_Equipo_1", "Login_Equipo_1", None))
        self.actionpepe.setText(QCoreApplication.translate("Login_Equipo_1", "pepe", None))
        self.actionSalir.setText(QCoreApplication.translate("Login_Equipo_1", "Abrir", None))
        self.actionGuardar.setText(QCoreApplication.translate("Login_Equipo_1", "Guardar", None))
        self.actionGuardar_Como.setText(QCoreApplication.translate("Login_Equipo_1", "Guardar Como", None))
        self.actionEditar.setText(QCoreApplication.translate("Login_Equipo_1", "Salir", None))
        self.actionDeshacer.setText(QCoreApplication.translate("Login_Equipo_1", "Deshacer", None))
        self.actionReahacer.setText(QCoreApplication.translate("Login_Equipo_1", "Reahacer", None))
        self.actionCortar.setText(QCoreApplication.translate("Login_Equipo_1", "Cortar", None))
        self.actionCopiar.setText(QCoreApplication.translate("Login_Equipo_1", "Copiar", None))
        self.actionZoom_in.setText(QCoreApplication.translate("Login_Equipo_1", "Zoom in", None))
        self.actionZoom_out.setText(QCoreApplication.translate("Login_Equipo_1", "Zoom out", None))
        self.actionDocumentacion.setText(QCoreApplication.translate("Login_Equipo_1", "Documentacion", None))
        self.actionAbout.setText(QCoreApplication.translate("Login_Equipo_1", "About", None))
        self.actionDocumentacion_2.setText(QCoreApplication.translate("Login_Equipo_1", "Documentacion", None))
        self.actionAbout_2.setText(QCoreApplication.translate("Login_Equipo_1", "About", None))
        self.actionPegar.setText(QCoreApplication.translate("Login_Equipo_1", "Pegar", None))
        self.info.setText(QCoreApplication.translate("Login_Equipo_1", "\u00bfNo tiene una cuenta?", None))
        self.button_crear_cuenta.setText(QCoreApplication.translate("Login_Equipo_1", "Crear Cuenta", None))
        self.button_login_2.setText(QCoreApplication.translate("Login_Equipo_1", "Login", None))
        self.titulo_main.setText(QCoreApplication.translate("Login_Equipo_1", "Login", None))
        self.titulo_usuario.setText(QCoreApplication.translate("Login_Equipo_1", "Usuario", None))
        self.campo_usuario.setText(QCoreApplication.translate("Login_Equipo_1", "lorenzo29", None))
        self.titulo_password.setText(QCoreApplication.translate("Login_Equipo_1", "Contrase\u00f1a", None))
        self.campo_password.setText(QCoreApplication.translate("Login_Equipo_1", "duhfhuhdufh", None))
        self.menuEditar.setTitle(QCoreApplication.translate("Login_Equipo_1", "Editar", None))
        self.menuVista.setTitle(QCoreApplication.translate("Login_Equipo_1", "Vista", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("Login_Equipo_1", "Archivo", None))
        self.menuAyuda.setTitle(QCoreApplication.translate("Login_Equipo_1", "Ayuda", None))
    
