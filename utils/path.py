import os

#1 --> Obtendremos la ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#2 --> Rutas de nuestros directorios principales
UTILS_DIR = os.path.join(BASE_DIR, 'utils')
VIEWS_DIR = os.path.join(BASE_DIR, 'views')
ICONS_DIR = os.path.join(BASE_DIR, 'icons')
MODELS_DIR = os.path.join(BASE_DIR, 'models')
CONTROLLERS_DIR = os.path.join(BASE_DIR, 'controllers')

#3 --> Rutas especificas a archivos de utils_button (Colores y al propio archivo)
UTILS_COLORES_PATH = os.path.join(UTILS_DIR, 'colores.py')
UTILS_RUTAS_PATH = os.path.join(UTILS_DIR, 'path.py')

#4 --> Rutas especificas a archivos de views_button
CUSTOM_QPUSHBUTTON_PATH = os.path.join(VIEWS_DIR, 'custom_button.py')
CUSTOM_QSEARCHBAR_PATH = os.path.join(VIEWS_DIR, 'custom_search_bar.py')

#5 --> Ruta al archivo main_button.py en la raiz del proyecto
MAIN_PATH = os.path.join(BASE_DIR, 'main_button.py')

# 6 --> Rutas específicas a los íconos, usando rutas completas desde el directorio "icons"
SEARCH_ICON_PATH = os.path.join(os.path.dirname(BASE_DIR), 'icons', 'search_icon.png')
TRASH_ICON_PATH = os.path.join(os.path.dirname(BASE_DIR), 'icons', 'trash_icon.png')





