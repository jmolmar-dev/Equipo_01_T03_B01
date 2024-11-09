#Clase usuario: 
class Usuario:
    def __init__ (self,email, nombre_usuario, password):
        """
        Definimos el constructor de la clase Usuario
        
        :param email: el correo electronico que tendra cada usuario
        :param nombre_usuario: el nombre que poseera el usuario
        :param password: contraseña que poseera nuestro usuario
        """
        #Almacenamos los atributos privados de la clase
        self.email = email
        self.nombre_usuario = nombre_usuario
        self.password = password
        
    #Getters de la clase
    @property
    def get_email(self):
        """
        Getter para obtener el email del usuario
        :return: Correo electrónico del usuario
        """
        return self.email #Devuelve el email almacenado
    
    @property
    def get_nombre_usuario(self):
        """
        Getter para obtener el nombre del usuario
        :return: Nombre del usuario
        """
        
        return self.nombre_usuario
    
    @property
    def get_password(self):
        """
        Getter para obtener la contraseña del usuario
        :return: Contraseña del usuario
        """
        
        return self.password
    
    #Setters de la clase
    @property
    def set_email(self, nuevo_email):
        """
        Setter con el que le establecemos un nuevo valor al email
        :param nuevo_email: Nuevo correo electronico
        """
        self.email = nuevo_email
        
    @property
    def set_nombre_usuario(self,nombre_usuario_nuevo):
        """
        Setter con el que le establecemos el nuevo valor al nombre de usuario
        :param nombre_usuario_nuevo: Nuevo nombre de usuario 
        """
        self.nombre_usuario = nombre_usuario_nuevo
        
    @property
    def set_password (self, password_nueva):
        """
        Setter con el que le establecemos el nuevo valor a la contraseña
        :param password_nueva: Nueva contraseña para el usuario
        """
        
        self.password = password_nueva
        
    #Metodo mediante el cual representaremos al usuario como una cadena -- Metodo toString()
    def __str__(self):
        """
        Representacion en cadena de texto de una instancia de nuestra Clase Usuario
        """
        
        return f"Usuario: {self.get_nombre_usuario}, Email: {self.get_email}"
    
    #Metodo con el que cambiaremos la contraseña de un Usuario
    def modificarPassword(self, password_nueva):
        """
        Método para cambiar la contraseña del usuario
        """
        self.password = password_nueva