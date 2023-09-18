import pandas as pd
import openpyxl
from tabulate import tabulate

class LibroNegocio:
    # Atributos de la clase
    listado_libros = []
    registros_libros = 'listado_libros.xlsx'

    # Constructor de la clase
    def __init__(self):
        self.listado_libros = []

    # Método para obtener libros desde un archivo Excel y crear objetos Libro
    def obtener_libros(self):
        try:
            # Lee los datos del archivo Excel en un DataFrame
            df = pd.read_excel(self.registros_libros)

            # Inicializa una lista para almacenar objetos Libro
            lista_libros = []

            # Itera a través de las filas del DataFrame y crea objetos Libro
            for index, row in df.iterrows():
                libro = Libro(row['Codigo del Libro'], row['Titulo'], row['Año'])
                codigo_autor = row['Codigo del Autor']
                codigo_categoria = row['Codigo de la Categoria']

                # Asigna autor y categoría a los libros
                for autor in lista_autores:
                    if codigo_autor == autor.get_codigo_autor():
                        libro.asignar_autor(autor)

                for categoria in lista_categorias:
                    if codigo_categoria == categoria.get_codigo_categoria():
                        libro.asignar_categoria(categoria)

                lista_libros.append(libro)

            # Asigna la lista de libros al atributo de la clase
            self.listado_libros = lista_libros

            return lista_libros

        except FileNotFoundError:
            print('Archivo de registros de libros no encontrado.')
            return []

    # Método para registrar un nuevo libro
    def registrar_libros(self, codigo_libro, titulo, anio, codigo_autor, codigo_categoria):
        try:
            # Obtiene la lista actual de libros
            lista_libros = self.obtener_libros()

            # Crea un nuevo objeto Libro
            libro = Libro(codigo_libro, titulo, anio)

            # Asigna autor y categoría al libro
            for autor in lista_autores:
                if autor.get_codigo_autor() == codigo_autor:
                    libro.asignar_autor(autor)

            for categoria in lista_categorias:
                if categoria.get_codigo_categoria() == codigo_categoria:
                    libro.asignar_categoria(categoria)

            # Agrega el nuevo libro a la lista
            lista_libros.append(libro)

            # Guarda la lista actualizada en el archivo Excel
            self.guardar_libros(lista_libros)

            print('Libro registrado correctamente.')

        except Exception as e:
            print(f'Error al registrar el libro: {str(e)}')

    # Método para guardar libros en un archivo Excel
    def guardar_libros(self, lista_libros):
        try:
            if len(lista_libros) > 0:
                data = []

                for libro in lista_libros:
                    # Crea una cadena con el nombre del autor y categoría
                    nombre_autor = f"{libro.mostrar_autor().nombre}, {libro.mostrar_autor().apellido_paterno} {libro.mostrar_autor().apellido_materno}"
                    data.append([libro.get_codigo_libro(), libro.get_titulo(), libro.get_anio(), libro.mostrar_autor().get_codigo_autor(), nombre_autor, libro.mostrar_categoria().get_codigo_categoria(), libro.mostrar_categoria().get_categoria()])

                columnas = ['Codigo del Libro', 'Titulo', 'Año', 'Codigo del Autor', 'Nombre del Autor', 'Codigo de la Categoria', 'Categoria']
                df = pd.DataFrame(data, columns=columnas)

                # Guarda los datos en el archivo Excel
                df.to_excel(self.registros_libros, index=False, engine='openpyxl')

        except Exception as e:
            print(f'Error al guardar libros: {str(e)}')

    # Método para editar un libro
    def editar_libros(self, _indice, codigo_libro, titulo, anio, codigo_autor, codigo_categoria):
        try:
            # Obtiene la lista actual de libros
            lista_libros = self.obtener_libros()

            # Verifica si el índice está dentro del rango válido
            if 0 <= _indice < len(lista_libros):
                # Actualiza los valores del libro en la lista
                lista_libros[_indice].set_codigo_libro(codigo_libro)
                lista_libros[_indice].set_titulo(titulo)
                lista_libros[_indice].set_anio(anio)

                # Busca y asigna autor y categoría al libro
                for autor in lista_autores:
                    if autor.get_codigo_autor() == codigo_autor:
                        lista_libros[_indice].asignar_autor(autor)

                for categoria in lista_categorias:
                    if categoria.get_codigo_categoria() == codigo_categoria:
                        lista_libros[_indice].asignar_categoria(categoria)

                # Guarda la lista actualizada en el archivo Excel
                self.guardar_libros(lista_libros)

                return f'Libro en el índice {_indice + 1} actualizado correctamente.'
            else:
                return 'Índice de libro fuera de rango, no se pudo actualizar.'

        except Exception as e:
            return f'Error al editar el libro: {str(e)}'

    # Método para eliminar un libro
    def eliminar_libros(self, _indice):
        try:
            # Obtiene la lista actual de libros
            lista_libros = self.obtener_libros()

            # Verifica si el índice está dentro del rango válido
            if 0 <= _indice < len(lista_libros):
                # Elimina el libro en el índice especificado
                lista_libros.pop(_indice)

                # Guarda la lista actualizada en el archivo Excel
                self.guardar_libros(lista_libros)

                return f'Libro en el índice {_indice + 1} eliminado correctamente.'
            else:
                return 'Índice de libro fuera de rango, no se pudo eliminar.'

        except Exception as e:
            return f'Error al eliminar el libro: {str(e)}'
