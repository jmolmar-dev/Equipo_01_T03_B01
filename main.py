# Realizamos las importaciones necesarias tanto de sys como de PySide6
import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow


# Importamos las clases de las interfaces de usuario creadas y que queramos mostrar
from views.login_window import VentanaLogin
from views.registro_window import VentanaRegistro
#Importamos la inicializacion de la BBDD para poder trabajar con ella
from models import inicializacion_db as init_db

# Configuración y ejecución de la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)
    init_db.init_db()
    login_window = VentanaLogin()
    login_window.show()
    sys.exit(app.exec())
