import psycopg # Necesitaremos importar el módulo 'psycopg' --> nos proporciona la biblioteca de PostgreSQL para trabajar con Python

def connect_db():
    """
    Nos conectaremos con la BBDD PostGreSQL, y posteriormente vamos a devolver la conexion.
    :return: Objeto de conexión a la base de datos, o None en caso de suceder cualquier error en el proceso
    """
    
    try:
        #Vamos a intentar crear una conexión con nuestra BBDD en funcion de los datos obtenidos
        conexion = psycopg.connect(
            dbname = "eq_01_gamevault_db", #Nombre de nuestra base de datos
            user = "admin",  #Usuario para acceder a la base de datos
            password = "0000",  #Contraseña para poder acceder a la base de datos
            host = "localhost",  #Dirección del servidor
            port = "5432"
        )
        return conexion
    except Exception as error:
        #Si durante el proceso de conexion se produce algun error, lo controlaremos mediante esta excepcion, informando mediante un mensaje
        print(f"Error al conectar con la BBDD --> {error}")
        return None
    
def close_connection(conexion):
    """
    Metodo que nos cerrar la conexion con la BBDD PostgreSQL.
    :param conexion: la conexion a la BBDD que queremos cerrar
    """
    #Lo primero sera comprobar si la conexion existe
    if conexion is not None:
        try:
            #Cerraremos la conexion, y en el caso de que ocurrar cualquier tipo de error, sera controlado mediante la expecion
            conexion.close()
        except Exception as error:
            print(f"Error al cerrar nuestra conexion con la BBDD --> {error}")
            
