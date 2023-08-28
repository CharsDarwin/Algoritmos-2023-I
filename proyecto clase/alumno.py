from persona import Persona
from curso import Curso

class Alumno(Persona):
    codigo = ""
    facultad = ""
    año_ingreso = 0
    Curso = []

    def __init__(
        self, nombre, ap_paterno, ap_materno, dni, codigo, facultad, año_ingreso
    ):
        super().__init__(nombre, ap_paterno, ap_materno, dni)
        self.codigo = codigo
        self.facultad = facultad
        self.año_ingreso = año_ingreso

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codigo):
        self.codigo = codigo

    def get_facultad(self):
        return self.facultad

    def set_facultad(self, facultad):
        self.facultad = facultad

    def get_anio_ingreso(self):
        return self.año_ingreso

    def set_anio_ingreso(self, anio):
        self.año_ingreso = anio

    def agregar_curso(self, curso):
        self.Curso.append(curso)

    def remover_curso(self, curso_eliminar):
        for curso in self.Curso:
            if curso_eliminar.get_codigo() == curso.get_codigo():
                self.Curso.remove(curso)
            else:
                print("No se encuentra registrado el curso a eliminar")

        if curso_eliminar in self.Curso:
            self.Curso.remove(curso_eliminar)

# funcion que muestra los cursos asignados a cada estudiante
    def mostrar_cursos_asignados(self):
        cursos_asignados = set(curso.get_nombre() for curso in self.Curso)
        print(f"Cursos asignados a {self.get_nombre()}:")
        for curso in cursos_asignados:
            print(curso)
        print("\n")


    def imprimir(self): 
        apellidos = self.ap_materno + ' ' + self.ap_paterno
        nombres = self.nombre
        codigo = self.codigo
        dni = self.dni
        facultad = self.facultad
        año = str(self.año_ingreso)
        return f"{apellidos.ljust(24)}{nombres.ljust(24)}{dni.ljust(20)}{codigo.ljust(20)}{facultad.ljust(40)}{año.ljust(20)}\n"




