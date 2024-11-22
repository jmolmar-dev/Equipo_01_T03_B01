from models.videojuego import Videojuego
import models.db as database


class VideojuegoController:
    """Controlador que gestiona la carga y obtención de videojuegos desde la base de datos."""

    def __init__(self):
        """Inicializa el controlador cargando los videojuegos desde la base de datos."""
        self.videojuegos = self.cargar_videojuegos()

    def cargar_videojuegos(self):
        """
        Carga una lista de objetos Videojuego desde la base de datos.
        """
        videojuegos = []
        query = "SELECT titulo, genero, plataforma, desarrollador, fechaLanzamiento, sinopsis FROM videojuegos"

        try:
            conn = database.connect_db()
            if conn is not None:
                with conn.cursor() as cursor:
                    cursor.execute(query)
                    results = cursor.fetchall()
                    for row in results:

                        videojuegos.append(Videojuego(*row))
                conn.close()
            else:
                print("No se pudo conectar a la base de datos.")
        except Exception as error:
            print(f"Error al cargar videojuegos: {error}")

        return videojuegos

    def obtener_videojuegos(self):
        """
        Devuelve la lista de videojuegos cargados desde la base de datos.
        Retorna:
            Una lista de objetos Videojuego.
        """
        return self.videojuegos

    def agregar_videojuego(self, videojuego):
        """
        Agrega un nuevo videojuego a la base de datos.
        Argumentos:
            videojuego (Videojuego): Objeto Videojuego a insertar.
        """
        query = """
            INSERT INTO videojuegos (titulo, genero, plataforma, desarrollador, fechaLanzamiento, sinopsis)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (titulo) DO NOTHING;
        """
        try:
            conn = database.connect_db()
            if conn is not None:
                with conn.cursor() as cursor:
                    cursor.execute(query, (
                        videojuego.titulo, videojuego.genero, videojuego.plataforma,
                        videojuego.desarrollador, videojuego.fechaLanzamiento, videojuego.sinopsis
                    ))
                    conn.commit()
                    print(f"Videojuego '{videojuego.titulo}' agregado a la base de datos.")
                conn.close()
            else:
                print("No se pudo conectar a la base de datos para agregar el videojuego.")
        except Exception as error:
            print(f"Error al agregar el videojuego a la base de datos: {error}")
