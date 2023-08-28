from persona import Persona

class Docente(Persona):
    codigo_docente = ''
    facultad = ''
    
    def __init__(self, nombre, ap_paterno, ap_materno, dni, codigo, facultad):
        super().__init__(nombre, ap_paterno, ap_materno, dni)
        self.codigo_docente = codigo
        self.facultad = facultad

    def get_codigo(self):
        return self.codigo_docente

    def set_codigo(self, codigo):
        self.codigo_docente = codigo

    def get_facultad(self):
        return self.facultad

    def set_facultad(self, facultad):
        self.facultad = facultad

    def imprimir(self):
        apellidos = self.ap_materno + ' ' + self.ap_paterno
        nombres = self.nombre
        codigo = self.codigo_docente
        dni = self.dni
        facultad = self.facultad
        return f"{apellidos.ljust(24)}{nombres.ljust(24)}{dni.ljust(24)}{codigo.ljust(24)}{facultad}\n"










