class Libro:
    codigo_libro = ''
    titulo = ''
    anio = 0

    def __init__(self, codigo_libro, titulo, anio):
        self.codigo_libro = codigo_libro
        self.titulo = titulo
        self.anio = anio
        self.autor = None
        self.categoria = None

    def get_codigo_libro(self):
        return self.codigo_libro
    
    def set_codigo_libro(self, codigo_libro):
        self.codigo_libro = codigo_libro

    def get_titulo(self):
        return self.titulo

    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_anio(self):
        return self.anio

    def set_anio(self, anio):
        self.anio = anio

    def asignar_autor(self, autor):
        self.autor = autor

    def mostrar_autor(self):
        return self.autor

    def asignar_categoria(self, categoria):
        self.categoria = categoria

    def mostrar_categoria(self):
        return self.categoria

    def mostrar_libro(self):
        return f'{self.codigo_libro=} {self.titulo=}, {self.anio=}, \n{self.mostrar_autor().imprimir()}, \n{self.mostrar_categoria().imprimir()} '
