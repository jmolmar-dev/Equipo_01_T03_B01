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
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QWidget)

#Clase para la interfaz de la ventana de registro
class Ui_ventana_registro(object):
    #Metodo que nos configurara la interfaz de usuario para la ventana de registro
    def setupUi(self, ventana_registro):
        #Configuracion basica de nuestra ventana principal de registro: se configura el nombre del objeto si no ha sido establecido
        if not ventana_registro.objectName():
            ventana_registro.setObjectName("ventana_registro")
        ventana_registro.resize(480, 630)
        ventana_registro.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        ventana_registro.setAutoFillBackground(False)
        
        #Color de fondo y fuente establecidos dentro de la ventana de registro
        ventana_registro.setStyleSheet("background-color: rgb(5, 13, 33);\n""font: 10pt \"Arial\";")
        ventana_registro.setTabShape(QTabWidget.TabShape.Rounded)
        
        #Definicion de las acciones de la barra de menú (Abrir, Guardar, Salir, etc)
        self.actionAbrir = QAction(ventana_registro)
        self.actionAbrir.setObjectName("actionAbrir")
        self.actionGuardar = QAction(ventana_registro)
        self.actionGuardar.setObjectName("actionGuardar")
        self.actionGuardar_Como = QAction(ventana_registro)
        self.actionGuardar_Como.setObjectName("actionGuardar_Como")
        self.actionSalir = QAction(ventana_registro)
        self.actionSalir.setObjectName("actionSalir")
        self.actionDeshacer = QAction(ventana_registro)
        self.actionDeshacer.setObjectName("actionDeshacer")
        self.actionRehacer = QAction(ventana_registro)
        self.actionRehacer.setObjectName("actionRehacer")
        self.actionCortar = QAction(ventana_registro)
        self.actionCortar.setObjectName("actionCortar")
        self.actionCopiar = QAction(ventana_registro)
        self.actionCopiar.setObjectName("actionCopiar")
        self.actionPegar = QAction(ventana_registro)
        self.actionPegar.setObjectName("actionPegar")
        self.actionZoom_in = QAction(ventana_registro)
        self.actionZoom_in.setObjectName("actionZoom_in")
        self.actionZoom_out = QAction(ventana_registro)
        self.actionZoom_out.setObjectName("actionZoom_out")
        self.actionDocumentacion = QAction(ventana_registro)
        self.actionDocumentacion.setObjectName("actionDocumentacion")
        self.actionAbout = QAction(ventana_registro)
        self.actionAbout.setObjectName("actionAbout")
        
        #Configuramos nuestro widget central
        self.centralwidget = QWidget(ventana_registro)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        
        #Configuracion de tamaño, fuente y estilo dentro del boton Crear Cuenta
        self.boton_crear_cuenta = QPushButton(self.centralwidget)
        self.boton_crear_cuenta.setObjectName("boton_crear_cuenta")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton_crear_cuenta.sizePolicy().hasHeightForWidth())
        self.boton_crear_cuenta.setSizePolicy(sizePolicy)
        self.boton_crear_cuenta.setMinimumSize(QSize(460, 51))
        font = QFont()
        font.setFamilies(["Arial"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.boton_crear_cuenta.setFont(font)
        self.boton_crear_cuenta.setStyleSheet("background-color: rgb(26, 103, 248);")
        
        #Incluimos el boton dentro del GridLayout
        self.gridLayout.addWidget(self.boton_crear_cuenta, 3, 0, 1, 1)

        #Layour horizontal para el mensaje y el botón de Login
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        #Configuración de etiqueta de texto alternativo (¿Ya tiene una cuenta?)
        self.label_info_2 = QLabel(self.centralwidget)
        self.label_info_2.setObjectName("label_info_2")
        self.label_info_2.setMinimumSize(QSize(133, 30))
        self.label_info_2.setMaximumSize(QSize(133, 30))
        self.label_info_2.setStyleSheet("color: rgb(201, 213, 238);")
        self.horizontalLayout.addWidget(self.label_info_2)

        #Configuracion del boton de Login
        self.boton_login = QPushButton(self.centralwidget)
        self.boton_login.setObjectName("boton_login")
        self.boton_login.setMinimumSize(QSize(132, 23))
        self.boton_login.setMaximumSize(QSize(132, 23))
        self.boton_login.setStyleSheet("background-color: rgb(26, 103, 248);")

        #Configuramos el layout horizontal y lo incluimos posteriormente dentro del principal
        self.horizontalLayout.addWidget(self.boton_login, 0, Qt.AlignmentFlag.AlignVCenter)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        #Configuracion de formulario de registro con etiquetas y campos de entrada (email, usuario, ...)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.formLayout.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(20)
        self.label_campo_email = QLabel(self.centralwidget)
        self.label_campo_email.setObjectName("label_campo_email")
        self.label_campo_email.setMinimumSize(QSize(121, 51))
        self.label_campo_email.setMaximumSize(QSize(121, 51))
        self.label_campo_email.setFont(font)
        self.label_campo_email.setAutoFillBackground(False)
        self.label_campo_email.setStyleSheet("color: rgb(201, 213, 238);")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_campo_email)

        self.email_valor = QLineEdit(self.centralwidget)
        self.email_valor.setObjectName("email_valor")
        self.email_valor.setMinimumSize(QSize(161, 51))
        self.email_valor.setMaximumSize(QSize(161, 51))
        self.email_valor.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.email_valor.setStyleSheet("background-color: rgb(255, 255, 255);\n""")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.email_valor)

        #Etiqueta y campo del usuario
        self.label_campo_usuario = QLabel(self.centralwidget)
        self.label_campo_usuario.setObjectName("label_campo_usuario")
        self.label_campo_usuario.setMinimumSize(QSize(121, 51))
        self.label_campo_usuario.setMaximumSize(QSize(121, 51))
        self.label_campo_usuario.setFont(font)
        self.label_campo_usuario.setAutoFillBackground(False)
        self.label_campo_usuario.setStyleSheet("color: rgb(201, 213, 238);")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_campo_usuario)

        self.usuario_valor = QLineEdit(self.centralwidget)
        self.usuario_valor.setObjectName("usuario_valor")
        self.usuario_valor.setMinimumSize(QSize(161, 51))
        self.usuario_valor.setMaximumSize(QSize(161, 51))
        self.usuario_valor.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.usuario_valor.setStyleSheet("background-color: rgb(255, 255, 255);\n""")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.usuario_valor)

        #Etiqueta y campo para la contraseña
        self.label_campo_password_registro = QLabel(self.centralwidget)
        self.label_campo_password_registro.setObjectName("label_campo_password_registro")
        self.label_campo_password_registro.setMinimumSize(QSize(121, 51))
        self.label_campo_password_registro.setMaximumSize(QSize(121, 51))
        self.label_campo_password_registro.setFont(font)
        self.label_campo_password_registro.setAutoFillBackground(False)
        self.label_campo_password_registro.setStyleSheet("color: rgb(201, 213, 238);")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_campo_password_registro)

        self.password_valor = QLineEdit(self.centralwidget)
        self.password_valor.setObjectName("password_valor")
        self.password_valor.setMinimumSize(QSize(161, 51))
        self.password_valor.setMaximumSize(QSize(161, 51))
        self.password_valor.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.password_valor.setStyleSheet("background-color: rgb(255, 255, 255);\n""")
        self.password_valor.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.password_valor)

        self.label_confirmar_password = QLabel(self.centralwidget)
        self.label_confirmar_password.setObjectName("label_confirmar_password")
        self.label_confirmar_password.setFont(font)
        self.label_confirmar_password.setAutoFillBackground(False)
        self.label_confirmar_password.setStyleSheet("color: rgb(201, 213, 238);")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_confirmar_password)

        self.password_confirmada_valor = QLineEdit(self.centralwidget)
        self.password_confirmada_valor.setObjectName("password_confirmada_valor")
        self.password_confirmada_valor.setMinimumSize(QSize(161, 51))
        self.password_confirmada_valor.setMaximumSize(QSize(161, 51))
        self.password_confirmada_valor.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.password_confirmada_valor.setStyleSheet("background-color: rgb(255, 255, 255);\n""")
        self.password_confirmada_valor.setEchoMode(QLineEdit.EchoMode.Password)

        #Terminamos de configurar el formulario y lo añadimos dentro de Layout principal
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.password_confirmada_valor)
        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 1)

        self.label_titulo = QLabel(self.centralwidget)
        self.label_titulo.setObjectName("label_titulo")
        sizePolicy.setHeightForWidth(self.label_titulo.sizePolicy().hasHeightForWidth())
        self.label_titulo.setSizePolicy(sizePolicy)
        self.label_titulo.setMinimumSize(QSize(67, 160))
        self.label_titulo.setStyleSheet("color: rgb(201, 213, 238);\n""font-size:20pt;")
        self.label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_titulo, 0, 0, 1, 1)
        #Finalizamos la configuracion del Widget Central
        ventana_registro.setCentralWidget(self.centralwidget)
        #Configuracion de la barra de menu y de la barra de estado
        self.menubar = QMenuBar(ventana_registro)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 480, 33))
        self.menubar.setStyleSheet("color: rgb(201, 213, 238);")
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuArchivo.setStyleSheet("color: rgb(201, 213, 238);")
        self.menuEditar = QMenu(self.menubar)
        self.menuEditar.setObjectName("menuEditar")
        self.menuEditar.setStyleSheet("color: rgb(201, 213, 238);")
        self.menuVista = QMenu(self.menubar)
        self.menuVista.setObjectName("menuVista")
        self.menuVista.setStyleSheet("color: rgb(201, 213, 238);")
        self.menuAyuda = QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        self.menuAyuda.setStyleSheet("color: rgb(201, 213, 238);")
        ventana_registro.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ventana_registro)
        self.statusbar.setObjectName("statusbar")
        ventana_registro.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuEditar.menuAction())
        self.menubar.addAction(self.menuVista.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionGuardar_Como)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionSalir)
        self.menuEditar.addAction(self.actionDeshacer)
        self.menuEditar.addSeparator()
        self.menuEditar.addAction(self.actionRehacer)
        self.menuEditar.addSeparator()
        self.menuEditar.addAction(self.actionCortar)
        self.menuEditar.addSeparator()
        self.menuEditar.addAction(self.actionCopiar)
        self.menuEditar.addSeparator()
        self.menuEditar.addAction(self.actionPegar)
        self.menuVista.addAction(self.actionZoom_in)
        self.menuVista.addSeparator()
        self.menuVista.addAction(self.actionZoom_out)
        self.menuAyuda.addAction(self.actionDocumentacion)
        self.menuAyuda.addSeparator()
        self.menuAyuda.addAction(self.actionAbout)
        
        #Metodo para establecer texto en cada uno de los elementos de la UI
        self.retranslateUi(ventana_registro)
        
        #Metodo que nos contecta las señales y los slots en la interfaz
        QMetaObject.connectSlotsByName(ventana_registro)
        
        
    
    #Metodo pata traducir y asignar texto a cada componente de la interfaz
    def retranslateUi(self, ventana_registro):
        ventana_registro.setWindowTitle(QCoreApplication.translate("ventana_registro", "Registro_Equipo_1", None))
        self.actionAbrir.setText(QCoreApplication.translate("ventana_registro", "Abrir", None))
        self.actionGuardar.setText(QCoreApplication.translate("ventana_registro", "Guardar", None))
        self.actionGuardar_Como.setText(QCoreApplication.translate("ventana_registro", "Guardar Como", None))
        self.actionSalir.setText(QCoreApplication.translate("ventana_registro", "Salir", None))
        self.actionDeshacer.setText(QCoreApplication.translate("ventana_registro", "Deshacer", None))
        self.actionRehacer.setText(QCoreApplication.translate("ventana_registro", "Rehacer", None))
        self.actionCortar.setText(QCoreApplication.translate("ventana_registro", "Cortar", None))
        self.actionCopiar.setText(QCoreApplication.translate("ventana_registro", "Copiar", None))
        self.actionPegar.setText(QCoreApplication.translate("ventana_registro", "Pegar", None))
        self.actionZoom_in.setText(QCoreApplication.translate("ventana_registro", "Zoom in", None))
        self.actionZoom_out.setText(QCoreApplication.translate("ventana_registro", "Zoom out", None))
        self.actionDocumentacion.setText(QCoreApplication.translate("ventana_registro", "Documentacion", None))
        self.actionAbout.setText(QCoreApplication.translate("ventana_registro", "About", None))
        self.boton_crear_cuenta.setText(QCoreApplication.translate("ventana_registro", "Crear Cuenta", None))
        self.label_info_2.setText(QCoreApplication.translate("ventana_registro", "\u00bfYa tiene una cuenta?", None))
        self.boton_login.setText(QCoreApplication.translate("ventana_registro", "Login", None))
        self.label_campo_email.setText(QCoreApplication.translate("ventana_registro", "Email", None))
        self.email_valor.setText(QCoreApplication.translate("ventana_registro", "lorenzo29@gmail.com", None))
        self.label_campo_usuario.setText(QCoreApplication.translate("ventana_registro", "Usuario", None))
        self.usuario_valor.setText(QCoreApplication.translate("ventana_registro", "lorenzo29", None))
        self.label_campo_password_registro.setText(QCoreApplication.translate("ventana_registro", "Contrase\u00f1a", None))
        self.password_valor.setText(QCoreApplication.translate("ventana_registro", "duhfhuhdufh", None))
        self.label_confirmar_password.setText(QCoreApplication.translate("ventana_registro", "Confirmar Contrase\u00f1a", None))
        self.password_confirmada_valor.setText(QCoreApplication.translate("ventana_registro", "duhfhuhdufh", None))
        self.label_titulo.setText(QCoreApplication.translate("ventana_registro", "Registro", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("ventana_registro", "Archivo", None))
        self.menuEditar.setTitle(QCoreApplication.translate("ventana_registro", "Editar", None))
        self.menuVista.setTitle(QCoreApplication.translate("ventana_registro", "Vista", None))
        self.menuAyuda.setTitle(QCoreApplication.translate("ventana_registro", "Ayuda", None))
    

