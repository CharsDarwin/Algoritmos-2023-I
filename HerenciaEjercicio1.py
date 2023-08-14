class Persona:
    tipoEspecie = ""
    nombreCientifico = ""

    dni = ""
    apellidos = ""
    nombre = ""
    nacionalidad = ""
    edad= ""
    anio = ""
    # 

    def _init_(self, dni, apellidos, nombre, nacionalidad,edad,anio):
        self.dni = dni
        self.apellidos = apellidos
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.edad=edad
        self.anio = anio
        

    def _cambiarNombre(self, nuevoNombre):
        self.nombre = nuevoNombre

    def _cambiarApellido(self, nuevoApellido):
        self.apellidos = nuevoApellido

    def _DatosAlumnos(self):
        print(
            f"Dni= {self.dni=} apellidos {self.apellido =} nombre {self.nombre=} nacionalidad {self.nacionalidad=} edad{self.edad=}anio{self.anio=}"
        )


class Alumnos(Persona):
    edad = ""
    anio = ""

    def _init_(self, dni, apellidos, nombre, nacionalidad, edad, anio):
        super()._init_(dni, apellidos, nombre, nacionalidad)

        self.edad = edad
        self.anio = anio

    def _anioiEstudio(self, anio):
        return 2023 - anio
    
    def _DatosAlumnos(self):
        print(f"Dni= {self.dni} apellidos {self.apellidos } nombre {self.nombre} nacionalidad {self.nacionalidad} edad{self.edad} anio de ingreso{self.anio}")


alumnos1 = Alumnos('48088259', "Apellido 1", " Nombre 1", "Nacionalidad 1", '17', '1999')

alumnos2 = Alumnos('45897654', "Apellido 2", " Nombre 2", "Nacionalidad 2", "5", '2000')
alumnos3 = Alumnos('84565487', "Apellido 2", " Nombre 3", "Nacionalidad 3", '4', '2001')
alumnos4 = Alumnos('45789654', "Apellido 2", " Nombre 4", "Nacionalidad 4", '15', '2002')
alumnos5 = Alumnos('15446878', "Apellido 2", " Nombre 4", "Nacionalidad 4", '2', '2003')

alumnos1._DatosAlumnos()