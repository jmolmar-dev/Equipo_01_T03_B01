from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_ventana_busqueda(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(589, 427)
        MainWindow.setStyleSheet(u"background-color: rgb(5, 13, 32);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.boton_volver = QPushButton(self.centralwidget)
        self.boton_volver.setObjectName(u"boton_volver")
        self.boton_volver.setMinimumSize(QSize(131, 51))
        self.boton_volver.setMaximumSize(QSize(131, 51))
        self.boton_volver.setStyleSheet(u"background-color: rgb(26, 103, 248);")

        self.horizontalLayout_2.addWidget(self.boton_volver)


        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(571, 71))
        self.widget.setMaximumSize(QSize(571, 71))
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(51, 41))
        self.label.setMaximumSize(QSize(51, 41))
        self.label.setPixmap(QPixmap(u"icons/search_icon.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(311, 21))
        self.lineEdit.setMaximumSize(QSize(311, 21))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(51, 41))
        self.label_2.setMaximumSize(QSize(51, 41))
        self.label_2.setPixmap(QPixmap(u"icons/trash_icon.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_2)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabla_usuarios = QTableWidget(self.centralwidget)
        if (self.tabla_usuarios.columnCount() < 3):
            self.tabla_usuarios.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla_usuarios.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_usuarios.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla_usuarios.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tabla_usuarios.setObjectName(u"tabla_usuarios")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabla_usuarios.sizePolicy().hasHeightForWidth())
        self.tabla_usuarios.setSizePolicy(sizePolicy)
        self.tabla_usuarios.setMinimumSize(QSize(301, 191))
        self.tabla_usuarios.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tabla_usuarios.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tabla_usuarios.setColumnCount(3)
        self.tabla_usuarios.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_usuarios.horizontalHeader().setDefaultSectionSize(180)
        self.tabla_usuarios.horizontalHeader().setStretchLastSection(False)
        self.tabla_usuarios.verticalHeader().setCascadingSectionResizes(False)
        self.tabla_usuarios.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout.addWidget(self.tabla_usuarios)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 589, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.boton_volver.setText(QCoreApplication.translate("MainWindow", u"Volver", None))
        self.label.setText("")
        self.label_2.setText("")
        ___qtablewidgetitem = self.tabla_usuarios.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Correo", None));
        ___qtablewidgetitem1 = self.tabla_usuarios.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Usuario", None));
        ___qtablewidgetitem2 = self.tabla_usuarios.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Password", None));
    # retranslateUi