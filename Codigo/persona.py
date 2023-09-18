class Persona:
    # Variables de clase compartidas por todas las instancias de la clase
    codigo_persona = ""
    nombre = ""
    apellido_paterno = ""
    apellido_materno = ""
    fecha_nacimiento = ""

    # Constructor de la clase
    def __init__(self, nombre, apellido_paterno, apellido_materno, fecha_nacimiento):
        # Inicializa las variables de instancia con los valores proporcionados
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.fecha_nacimiento = fecha_nacimiento

    # Métodos getter para obtener los valores de las variables de instancia
    def get_nombre(self):
        return self.nombre

    def get_apellido_paterno(self):
        return self.apellido_paterno

    def get_apellido_materno(self):
        return self.apellido_materno

    def get_fecha_nacimiento(self):
        return self.fecha_nacimiento

    # Métodos setter para actualizar los valores de las variables de instancia
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_apellido_paterno(self, apellido_paterno):
        self.apellido_paterno = apellido_paterno

    def set_apellido_materno(self, apellido_materno):
        self.apellido_materno = apellido_materno

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento

    # Método para imprimir los datos de la persona
    def imprimir(self):
        # Concatena los apellidos en una sola cadena
        apellidos = self.apellido_paterno + ' ' + self.apellido_materno
        # Devuelve una cadena formateada con los datos de la persona
        return f'{self.nombre=}, {apellidos=}, {self.fecha_nacimiento=}'
