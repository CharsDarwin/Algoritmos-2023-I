# Clase Persona
class Persona:
    def __init__(self, cod_persona, nombre_apellido_paterno, apellido_materno, fecha_nacimiento):
        self.cod_persona = cod_persona
        self.nombre_apellido_paterno = nombre_apellido_paterno
        self.apellido_materno = apellido_materno
        self.fecha_nacimiento = fecha_nacimiento

# Clase Autor hereda de Persona
class Autor(Persona):
    def __init__(self, cod_persona, nombre_apellido_paterno, apellido_materno, fecha_nacimiento, codigo_autor, pais, editorial):
        super().__init__(cod_persona, nombre_apellido_paterno, apellido_materno, fecha_nacimiento)
        self.codigo_autor = codigo_autor
        self.pais = pais
        self.editorial = editorial

# Clase Categoria
class Categoria:
    def __init__(self, codigo_categoria, categoria):
        self.codigo_categoria = codigo_categoria
        self.categoria = categoria

# Clase Libro
class Libro:
    def __init__(self, codigo_libro, titulo, año, turno, autor, categoria):
        self.codigo_libro = codigo_libro
        self.titulo = titulo
        self.año = año
        self.turno = turno
        self.autor = autor  # Asociación simple con Autor
        self.categoria = categoria  # Asociación simple con Categoria

# Clase de Negocio para el mantenimiento
class MantenimientoLibros:
    def __init__(self):
        self.libros = []
        self.autores = []
        self.categorias = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def agregar_autor(self, autor):
        self.autores.append(autor)

    def agregar_categoria(self, categoria):
        self.categorias.append(categoria)

    def generar_reporte(self, nombre_archivo):
        try:
            with open(nombre_archivo, "w") as archivo:
                archivo.write("Reporte de Libros:\n")
                for libro in self.libros:
                    archivo.write(f"Código: {libro.codigo_libro}\n")
                    archivo.write(f"Título: {libro.titulo}\n")
                    archivo.write(f"Año: {libro.año}\n")
                    archivo.write(f"Turno: {libro.turno}\n")
                    archivo.write(f"Autor: {libro.autor.nombre_apellido_paterno} {libro.autor.apellido_materno}\n")
                    archivo.write(f"Categoría: {libro.categoria.categoria}\n")
                    archivo.write("\n")
            print(f"Reporte generado en {nombre_archivo}")
        except Exception as e:
            print(f"Error al generar el reporte: {str(e)}")

    def guardar_datos(self, archivo_libros, archivo_autores, archivo_categorias):
        try:
            with open(archivo_libros, "w") as archivo:
                for libro in self.libros:
                    archivo.write(f"{libro.codigo_libro},{libro.titulo},{libro.año},{libro.turno}\n")
            with open(archivo_autores, "w") as archivo:
                for autor in self.autores:
                    archivo.write(f"{autor.codigo_autor},{autor.nombre_apellido_paterno},{autor.apellido_materno}\n")
            with open(archivo_categorias, "w") as archivo:
                for categoria in self.categorias:
                    archivo.write(f"{categoria.codigo_categoria},{categoria.categoria}\n")
            print("Datos guardados exitosamente.")
        except Exception as e:
            print(f"Error al guardar los datos: {str(e)}")

# Ejemplo de uso:
if __name__ == "__main__":
    mantenimiento = MantenimientoLibros()
    autor1 = Autor(1, "Nombre Autor", "Apellido Autor", "01/01/1980", "AUT1", "País Autor", "Editorial Autor")
    categoria1 = Categoria("CAT1", "Ciencia Ficción")
    libro1 = Libro("LIB1", "Libro 1", 2023, "Mañana", autor1, categoria1)

    mantenimiento.agregar_autor(autor1)
    mantenimiento.agregar_categoria(categoria1)
    mantenimiento.agregar_libro(libro1)

    # Generar un reporte y guardar los datos
    mantenimiento.generar_reporte("reporte_libros.txt")
    mantenimiento.guardar_datos("datos_libros.csv", "datos_autores.csv", "datos_categorias.csv")
