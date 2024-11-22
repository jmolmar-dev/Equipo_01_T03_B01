class Videojuego:
    """Clase que representa un videojuego con sus propiedades y métodos relacionados."""

    def __init__(self, titulo, genero, plataforma, desarrollador, fechaLanzamiento, sinopsis):
        """Constructor de la clase Videojuego."""
        # Atributos privados que representan las propiedades del videojuego
        self._titulo = titulo
        self._genero = genero
        self._plataforma = plataforma
        self._desarrollador = desarrollador
        self._fechaLanzamiento = fechaLanzamiento
        self._sinopsis = sinopsis

    # Getters
    def get_titulo(self):
        """Devuelve el título del videojuego."""
        return self._titulo

    def get_genero(self):
        """Devuelve el género del videojuego."""
        return self._genero

    def get_plataforma(self):
        """Devuelve la plataforma del videojuego."""
        return self._plataforma

    def get_desarrollador(self):
        """Devuelve el desarrollador del videojuego."""
        return self._desarrollador

    def get_fechaLanzamiento(self):
        """Devuelve la fecha de lanzamiento del videojuego."""
        return self._fechaLanzamiento

    def get_sinopsis(self):
        """Devuelve la sinopsis del videojuego."""
        return self._sinopsis

    # Setters
    def set_titulo(self, titulo):
        """Establece un nuevo título para el videojuego."""
        self._titulo = titulo

    def set_genero(self, genero):
        """Establece un nuevo género para el videojuego."""
        self._genero = genero

    def set_plataforma(self, plataforma):
        """Establece una nueva plataforma para el videojuego."""
        self._plataforma = plataforma

    def set_desarrollador(self, desarrollador):
        """Establece un nuevo desarrollador para el videojuego."""
        self._desarrollador = desarrollador

    def set_fechaLanzamiento(self, fechaLanzamiento):
        """Establece una nueva fecha de lanzamiento para el videojuego."""
        self._fechaLanzamiento = fechaLanzamiento

    def set_sinopsis(self, sinopsis):
        """Establece una nueva sinopsis para el videojuego."""
        self._sinopsis = sinopsis

    # Métodos especiales
    def __str__(self):
        """Devuelve una representación en cadena para mostrar la información del videojuego."""
        return (f"Título: {self._titulo}, Género: {self._genero}, Plataforma: {self._plataforma}, "
                f"Desarrollador: {self._desarrollador}, Fecha de Lanzamiento: {
                    self._fechaLanzamiento}, "
                f"Sinopsis: {self._sinopsis}")

    def __repr__(self):
        """Devuelve una representación oficial y detallada de la instancia de Videojuego."""
        return (f"Videojuego({self._titulo!r}, {self._genero!r}, {self._plataforma!r}, "
                f"{self._desarrollador!r}, {self._fechaLanzamiento!r}, {self._sinopsis!r})")
