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
    Se insertan 3 usuarios de ejemplo y se utiliza 'ON CONFLICT' para evitar que siguientes llamadas a esta función provoquen errores.
    """
    # datos a insertar
    inserts = (
        ('test1@gmail.com', 'usuario_test1', 'password1'),
        ('test2@outlook.com', 'usuario_test2', 'password2'),
        ('pperezperez97@iescarrillo.es', 'pp', '12345')
    )
    
    # Definición consulta
    insert_query = """
        INSERT INTO usuarios (email, nombre_usuario, password)
        VALUES (%s, %s, %s)
        ON CONFLICT (email) DO NOTHING;
        """  
    
    try:
        
        conn = database.connect_db()
        
        if conn is not None:  
            with conn.cursor() as cursor:  
                
                for user in inserts: #Nombrando user a cada miembro de inserts, lo recorremos
                    cursor.execute(insert_query, user)  # Ejecutamos la consulta de inserción para cada usuario.
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
