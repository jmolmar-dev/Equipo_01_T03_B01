

from models.crud_usuario import CRUDUsuario  # Importar el CRUD que gestiona las operaciones de la base de datos

from models.usuario import Usuario



# Importar la clase Usuario para manipular objetos de tipo Usuario


class UsuarioController:
    """
    Controlador para las interacciones entre las vistas y el modelo usuario.
    """

    def __init__(self):
        # Instancia del CRUD para realizar operaciones con la base de datos
        self.user_crud = CRUDUsuario()
    # __init__

    def register_user(self, email, username, password, verified_password):
        """
        Método para registrar un nuevo usuario en la base de datos.

        :param email: Correo electrónico del nuevo usuario.
        :param username: Nombre de usuario.
        :param password: Contraseña del usuario.
        :param verified_password: Verificación de la contraseña.
        :return: Un objeto Usuario si se registra con exitos, None en caso contrario.
        """
        
        if password != verified_password:  # Si no coinciden contraseñas, salir de función.
            print("Las contraseñas no coinciden.")  
            return None  

       
        usuario_existente = self.user_crud.seleccionar_usuario(email) #Si ya existe el usario, salir de función.
        if usuario_existente is not None: 
            print(f"Ya hay un usuario con el correo: {email}")  
            return None  

       
        if self.user_crud.insertar_usuario(email, username, password): 
            print("Usuario creado exitosamente.")  
           
            return Usuario(email, username, password)  
        else:
            print("Error al crear el usuario.") 
            return None  
   
   
    def verify_user_by_name(self, username, password):
        """
        Método para verificar si un usuario existe en la base de datos y si sus credenciales son correctas.

        :param username: Nombre de usuario.
        :param password: Contraseña del usuario.
        :return: Un objeto Usuario si las credenciales son correctas, o None si son incorrectas.
        """
        # Usamos el nuevo método `seleccionar_usuario_por_nombre` en lugar de `seleccionar_usuario`
        usuario = self.user_crud.seleccionar_usuario_por_nombre(username)  
        if usuario is not None and usuario.get_password == password:  
            print("Usuario verificado.")  
            return usuario 
        else:
            print("Credenciales incorrectas.")  
            return None  
