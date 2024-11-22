import psycopg #Importatemos la biblioteca psycopg --> Nos permitira trabajar con PostgreSQL desde Python
from models import db #Importar el modulo db con la finalidad la conexion de la base de datos
from models.usuario import Usuario #Importamos la clase Usuario para poder obtener los datos del mismo

class CRUDUsuario:
    """
    Clase que implementa operaciones CRUD para la tabla 'usuarios' en la base de datos
    """
    def insertar_usuario (self,email,nombre_usuario,password):
        
        """
        Metodo para insertar un nuevo usuario dentro de la BBDD
        
        :param email: Correo electrónico del nuevo usuario, el cual será nuestra clase Primaria
        :param nombre_usuario: Nombre de usuario con el que insertaremos dentro de la BBDD
        :param nueva_password: Contraseña para el nuevo usuario que insertaremos dentro del BBDD
        
        """
        # Se establece la consulta SQL para insertar el nuevo usuario dentro de la BBDD
        query = """
        INSERT INTO usuarios (email, nombre_usuario, password)
        VALUES (%s,%s,%s) 
        """
        
        # Conectamos la BBDD utilizando la funcion db_conectar()
        conexion = db.connect_db()
        if conexion is None: #Verificaremos de que la conexion exista antes de poder continuar
            return False
        
        try:
            #Mediante un cursor, ejecutaremos la consulta con los parametros, y mediante el commit confirmaremos que se han realizado los cambios
            with conexion.cursor() as cursor:
                cursor.execute(query, (email,nombre_usuario,password)) 
                conexion.commit()
                return True
        #Ante cualquier tipo de error, sera controlado por una excepcion
        except Exception as error: 
                print(f"Error al insertar el usuario --> {error}")  
        finally:
            #Finalmente, cerraremos la conexion
            db.close_connection(conexion) 
            
    def seleccionar_usuario (self,email):
        """
        Metodo para obtener un usuario de la BBDD a traves de su email (clave primaria)
        
        :param email: Correo Electrónico del usuario que se desea obtener
        :return: devolvemos una instancia de la clase Usuario si la encontramos, en caso contrario, retornamos None
        """
        #Definimos la consulta mediante la cual vamos a obtener a un usuario a partir de su email
        query = "SELECT email,nombre_usuario, password FROM usuarios WHERE email = %s"
        #Posteriormente, nos volvemos a conectar a la BBDD, verificando una vez mas que la conexion existe
        conexion = db.connect_db()
        if conexion is None:
            return None
        
        try:
            #Ejecutar la consulta SQL mediante un cursor
            with conexion.cursor() as cursor:
                cursor.execute(query, (email,))
                resultado = cursor.fetchone() #Obtenemos el primer resultado
                if resultado is not None:
                    return Usuario(*resultado) #Obtenemos la tupla 'resultado' , pasando cada valor por separado (email, ...) a la clase Usuario
                return None
        except Exception as error: #Controlamos mediante la excepcion cualquier tipo de error y finalmente cerramos la conexion en el finally
            print(f"Error al obtener el usuario --> {error}")
            return None
        finally:
            db.close_connection(conexion)
        
    def actualizar_usuario (self,email,nuevo_nombre_usuario = None, nueva_password = None):
        """
        Metodo que nos actualiza un usuario en la base de datos, cambiando el email y de forma opcional el nombre y la password
        
        :param email: Correo electronico del usuario que deseamos actualizar
        :param nuevo_nombre_usuario: Nuevo nombre de usuario que deseamos establecer (opcional)
        :param nueva_password: Nueva contraseña del usuario que deseamos establecer (opcional)
        
        """
        
        #Definimos la consulta SQL para actualizar un usuario por su email
        query = "UPDATE usuarios SET nombre_usuario = %s, password = %s WHERE email = %s"
        #Nos conectamos a la BBDD usando la funcion correspondiente para ello
        conexion = db.connect_db()
        if conexion is None:
            return False
        try:
            #Volvemos a ejecurtar la consulta mediante un cursos, efectuandola mediante el commit
            with conexion.cursor() as cursor:
                cursor.execute(query,(nuevo_nombre_usuario,nueva_password,email))
                conexion.commit()
                return True
        except Exception as error: #Se controla cualquier error con las excepciones, y volvemos a cerrar la conexion en el finally
            print(f"Error al actualizar el usuario --> {error}")
        finally:
            db.close_connection(conexion)
            
    def eliminar_usuario(self,email):
        """
        Metodo para eliminar un usuario de la BBDD
        
        :param email: Correo Electrónico del usuario a eliminar
        :return: True en el caso de que el usuario sea eliminado correctamente, y False en caso contrario
        
        """
        #Definimos la consulta SQL para eliminar un usuario por su email
        query = "DELETE FROM usuarios WHERE email = %s"
        #Conectamos la BBDD usando la funcion correspondiente
        conexion = db.connect_db()
        #Verificamos que la conexion existe antes de continuar
        if conexion is None:
            return False
        
        try:
            #Ejecutamos la consulta SQL mediante un cursor, efectuandola con un commit y controlando los errores con una Excepcion. Finalmente,
            # la cerramos en el finally
            with conexion.cursor() as cursor:
                cursor.execute(query, (email,))
                conexion.commit()
                return True
        except Exception as error:
            print(f"Error al eliminar un usuario --> {error}")
            return False
        finally:
            db.close_connection(conexion)
            
    def lista_usuarios(self):
        """
        Metodo con el que mostraremos una lista de todos los usuarios presentes dentro de la BBDD
        
        :return: Lista de instancias de Usuario, o una lista vacía en caso de errror
        """
        
        #Definir la consulta SQL para poder obtener todas las instancias de usuario
        query = "SELECT email, nombre_usuario, password FROM usuarios"
        #Nos conectamos posteriormente a nuestra BBDD mediante el metodo correspondiente
        conexion = db.connect_db()
        if conexion is None:
            return [] #En caso de fallar la conexion, devolveremos una lista vacia
        
        try:
            #Ejecutamos la consulta mediante un cursor, retornando una lista de usuarios, o bien una lista vacia en caso de no encontrarlos
            #Cualquier error sera controlado mediante una excepcion, y volvemos a cerrar la conexion dentro del finally
            with conexion.cursor() as cursor:
                conexion.execute(query)
                resultados = cursor.fetchall()
                if resultados:
                    return [Usuario(*row) for row in resultados]
                return []
        except Exception as error:
            print (f"Error al mostrar la lista de usuarios --> {error}")
            return []
        finally:
            db.close_connection()
            
            
    def seleccionar_usuario_por_nombre(self, nombre_usuario):
        """
        Método para obtener un usuario de la BBDD a través de su nombre de usuario.

        :param nombre_usuario: Nombre de usuario del usuario que se desea obtener.
        :return: Devolvemos una instancia de la clase Usuario si la encontramos, en caso contrario, retornamos None.
        """
        # Consulta SQL para buscar el usuario por nombre de usuario
        query = "SELECT email, nombre_usuario, password FROM usuarios WHERE nombre_usuario = %s"
        
        # Conectar a la base de datos
        conexion = db.connect_db()
        if conexion is None:
            return None
        
        try:
            # Ejecutar la consulta SQL
            with conexion.cursor() as cursor:
                cursor.execute(query, (nombre_usuario,))
                resultado = cursor.fetchone()  # Obtener el primer resultado
                if resultado is not None:
                    return Usuario(*resultado)  # Crear y retornar una instancia de Usuario
                return None
        except Exception as error:
            print(f"Error al obtener el usuario por nombre de usuario --> {error}")
            return None
        finally:
            db.close_connection(conexion)
                    