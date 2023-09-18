# Importamos la clase Persona para que Autor herede de ella
from persona import Persona

# Definición de la clase Autor que hereda de Persona
class Autor(Persona):
    # Variables de instancia específicas de la clase Autor
    codigo_autor = ''
    pais = ''
    editorial = ''

    # Constructor de la clase Autor
    def __init__(self, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, codigo_autor, pais, editorial):
        # Llama al constructor de la clase base (Persona) para inicializar los atributos comunes
        super().__init__(nombre, apellido_paterno, apellido_materno, fecha_nacimiento)
        
        # Inicializa los atributos específicos de Autor
        self.codigo_autor = codigo_autor
        self.pais = pais
        self.editorial = editorial

    # Métodos getter para obtener los valores de los atributos específicos de Autor
    def get_codigo_autor(self):
        return self.codigo_autor

    def get_pais(self):
        return self.pais

    def get_editorial(self):
        return self.editorial

    # Métodos setter para actualizar los valores de los atributos específicos de Autor
    def set_codigo_autor(self, codigo_autor):
        self.codigo_autor = codigo_autor

    def set_pais(self, pais):
        self.pais = pais

    def set_editorial(self, editorial):
        self.editorial = editorial

    # Método para imprimir los datos del autor
    def imprimir(self):
        # Llama al método imprimir de la clase base (Persona) para obtener los datos comunes
        per_data = super().imprimir()
        # Devuelve una cadena formateada con los datos específicos del autor
        return f'Datos del autor: {per_data=}, {self.codigo_autor=}, {self.pais=}, {self.editorial=}'
