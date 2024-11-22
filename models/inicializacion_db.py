import models.db as database


# Función para crear las tablas requeridas en la base de datos
def create_tables():
    """
    Si la tabla usuario no existe, la crea.
    """
    # Comandos SQL para crear las tablas si no existen (IF NOT EXISTS)

    commands = (
        """
        CREATE TABLE IF NOT EXISTS usuarios (
            email VARCHAR(255) PRIMARY KEY,  
            nombre_usuario VARCHAR(255) NOT NULL, 
            password VARCHAR(255) NOT NULL  
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS videojuegos(
            titulo VARCHAR(255) PRIMARY KEY,
            genero VARCHAR(255) NOT NULL,
            plataforma VARCHAR(255) NOT NULL,
            desarrollador VARCHAR(255) NOT NULL,
            fechaLanzamiento DATE NOT NULL,
            sinopsis VARCHAR(255) NOT NULL
        );
        """
    )

    try:
        # Creamos la conexion.
        connection = database.connect_db()
        # Verificar si la conexión se realizó correctamente
        if connection is not None:
            with connection.cursor() as cursor:
                for command in commands:
                    cursor.execute(command)
                connection.commit()
                print("Tablas Correctas")
            connection.close()
        else:
            print("Error de conexión con la base de datos")
    except Exception as error:  # Capturar cualquier excepción que ocurra
        # Mostrar un mensaje de error si ocurre alguna excepción
        print(f"Error al crear las tablas: {error}")


# Función para insertar datos de ejemplo en la tabla 'usuarios'
def insert_data():
    """
    Se insertan datos de ejemplo en las tablas 'usuarios' y 'videojuegos' y se utiliza 'ON CONFLICT' para evitar errores.
    """
    # Datos a insertar en la tabla usuarios
    user_inserts = (
        ('test1@gmail.com', 'usuario_test1', 'password1'),
        ('test2@outlook.com', 'usuario_test2', 'password2'),
        ('pperezperez97@iescarrillo.es', 'pp', '12345')
    )

    user_insert_query = """
        INSERT INTO usuarios (email, nombre_usuario, password)
        VALUES (%s, %s, %s)
        ON CONFLICT (email) DO NOTHING;
        """

    # Datos a insertar en la tabla videojuegos
    game_inserts = (
        ('Castlevania: Symphony of the Night', 'Metroidvania', 'Emulador', 'Konami', '1997-03-20',
         'Help Alucard defeat his father Dracula'),
        ('The Legend of Zelda: Ocarina of Time', 'Adventure', 'Nintendo 64', 'Nintendo', '1998-11-21',
         'Link embarks on a quest to stop Ganondorf.'),
        ('Minecraft', 'Sandbox', 'Multi-platform', 'Mojang', '2009-05-17',
         'A game about placing blocks and going on adventures.')
    )

    game_insert_query = """
        INSERT INTO videojuegos (titulo, genero, plataforma, desarrollador, fechaLanzamiento, sinopsis)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT (titulo) DO NOTHING;
        """

    try:
        conn = database.connect_db()

        if conn is not None:
            with conn.cursor() as cursor:
                # Insertar usuarios
                for user in user_inserts:
                    cursor.execute(user_insert_query, user)
                # Insertar videojuegos
                for game in game_inserts:
                    cursor.execute(game_insert_query, game)
                conn.commit()
                print("Datos insertados correctamente.")
            conn.close()
        else:
            print("No se pudo conectar a la base de datos.")
    except Exception as error:
        print(f"Error al insertar datos: {error}")


# Función para inicializar la base de datos, creando tablas e insertando datos de ejemplo
def init_db():
    """
    Inicializar la base de datos llamando a las funciones de creación de tablas e inserción de datos.
    """
    create_tables()
    insert_data()
