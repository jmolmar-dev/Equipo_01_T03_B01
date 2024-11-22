# Archivo: 02_WIDGETS_AVANZADOS\utils_customTable\estilos.py

# Colores definidos para uso general en la aplicación en modo oscuro
DARK_BACKGROUND = "#1E1E1E"     # Color de fondo oscuro principal
DARK_GREY = "#2E2E2E"           # Gris oscuro para elementos secundarios
SOFT_WHITE = "#D9D9D9"          # Blanco suave para el texto
ACCENT_BLUE = "#4A90E2"         # Azul acento para elementos interactivos
DARK_GREEN = "#1B5E20"          # Verde oscuro para estados positivos
ACCENT_ORANGE = "#FF8C42"       # Naranja acento para resaltar elementos
DEEP_RED = "#D32F2F"            # Rojo profundo para alertas o errores
SOFT_YELLOW = "#FFEB3B"         # Amarillo suave para avisos
PURPLE_ACCENT = "#673AB7"       # Púrpura acento para detalles visuales
ICON_COLOR = ACCENT_BLUE        # Color de los iconos para resaltar
BORDER_COLOR = ACCENT_BLUE      # Color de bordes para separar elementos
SHADOW_COLOR = "#121212"        # Color de la sombra para dar profundidad
PASTEL_YELLOW = "#FFF5CC"       # Amarillo pastel suave para celdas seleccionadas
HEADER_BLUE = "#3A7BBF"         # Azul elegante para encabezados

# Estilo para el campo de texto
ESTILO_CAMPO_TEXTO = f"""
    color: {SOFT_WHITE};  /* Color del texto */
    background-color: {DARK_BACKGROUND};  /* Color de fondo */
    border: 1px solid {BORDER_COLOR};  /* Borde del campo */
    border-radius: 5px;  /* Bordes redondeados */
    padding: 5px;  /* Espaciado interno */
"""

# Estilo para la tabla personalizada
ESTILO_TABLA = f"""
    QTableView {{
        background-color: {DARK_BACKGROUND};  /* Color de fondo de la tabla */
        color: {SOFT_WHITE};  /* Color del texto */
        gridline-color: {BORDER_COLOR};  /* Color de las líneas de la cuadrícula */
        /* border: 1px solid {BORDER_COLOR}; */  /* Borde opcional */
        selection-color: {DARK_BACKGROUND};  /* Color del texto en la celda seleccionada */
    }}
    
    QHeaderView::section {{
        background-color: {HEADER_BLUE};  /* Color de fondo del encabezado */
        color: {SOFT_WHITE};  /* Color del texto del encabezado */
        padding: 5px;  /* Espaciado interno en las secciones del encabezado */
        border: 1px solid {BORDER_COLOR};  /* Borde de las secciones del encabezado */
    }}
    
    QTableCornerButton::section {{
        background-color: {HEADER_BLUE};  /* Color de fondo del botón de la esquina */
        border: 1px solid {BORDER_COLOR};  /* Borde del botón de la esquina */
    }}

    QTableView::item:selected {{
        background-color: {PASTEL_YELLOW};  /* Color de fondo para celdas seleccionadas */
        color: {DARK_BACKGROUND};  /* Color del texto en la celda seleccionada */
    }}
"""

