# Clase Categoria
class Categoria:
    # Atributos de la clase Categoria
    codigo_categoria = ''  # Código de la categoría
    categoria = ''         # Nombre de la categoría

    # Constructor de la clase Categoria
    def __init__(self, codigo_categoria, categoria):
        # Inicializa los atributos de la clase Categoria
        self.codigo_categoria = codigo_categoria  # Asigna el código de la categoría
        self.categoria = categoria                # Asigna el nombre de la categoría

    # Método getter para obtener el código de la categoría
    def get_codigo_categoria(self):
        return self.codigo_categoria

    # Método setter para establecer el código de la categoría
    def set_codigo_categoria(self, codigo_categoria):
        self.codigo_categoria = codigo_categoria

    # Método getter para obtener el nombre de la categoría
    def get_categoria(self):
        return self.categoria

    # Método setter para establecer el nombre de la categoría
    def set_categoria(self, categoria):
        self.categoria = categoria

    # Método para imprimir los datos de la categoría
    def imprimir(self):
        return f'Datos de la categoría: {self.codigo_categoria}, {self.categoria}'
