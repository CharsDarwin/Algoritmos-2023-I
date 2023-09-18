import pandas as pd
import openpyxl
from openpyxl import Workbook
from tabulate import tabulate

class CategoriaNegocio:
    # Atributos de la clase
    listado_categoria = []
    registros_categorias = 'listado_categorias.xlsx'

    # Constructor de la clase
    def __init__(self):
        self.listado_categoria = []

    # Método para obtener categorías desde un archivo Excel y crear objetos Categoría
    def obtener_categorias(self):
        try:
            # Lee los datos del archivo Excel en un DataFrame
            df = pd.read_excel(self.registros_categorias)

            # Inicializa una lista para almacenar objetos Categoría
            lista_categorias = []

            # Itera a través de las filas del DataFrame y crea objetos Categoría
            for index, row in df.iterrows():
                categoria = Categoria(row['Codigo de la Categoria'], row['Categoria'])
                lista_categorias.append(categoria)

            # Asigna la lista de categorías al atributo de la clase
            self.listado_categoria = lista_categorias

            return lista_categorias

        except FileNotFoundError:
            print('Archivo de registros de categorías no encontrado.')
            return []

    # Método para registrar una nueva categoría
    def registrar_categorias(self, codigo_categoria, categoria):
        try:
            # Obtiene la lista actual de categorías
            lista_categorias = self.obtener_categorias()

            # Crea un nuevo objeto Categoría
            nueva_categoria = Categoria(codigo_categoria, categoria)

            # Agrega la nueva categoría a la lista
            lista_categorias.append(nueva_categoria)

            # Guarda la lista actualizada en el archivo Excel
            self.guardar_categorias(lista_categorias)

            print('Categoría registrada correctamente.')

        except Exception as e:
            print(f'Error al registrar la categoría: {str(e)}')

    # Método para guardar categorías en un archivo Excel
    def guardar_categorias(self, lista_categorias):
        try:
            if len(lista_categorias) > 0:
                data = []

                for categoria in lista_categorias:
                    data.append([categoria.get_codigo_categoria(), categoria.get_categoria()])

                columnas = ['Codigo de la Categoria', 'Categoria']
                df = pd.DataFrame(data, columns=columnas)

                # Guarda los datos en el archivo Excel
                df.to_excel(self.registros_categorias, index=False, engine='openpyxl')

        except Exception as e:
            print(f'Error al guardar categorías: {str(e)}')

    # Método para editar una categoría
    def editar_categorias(self, _indice, codigo_categoria, categoria):
        try:
            # Obtiene la lista actual de categorías
            lista_categorias = self.obtener_categorias()

            # Verifica si el índice está dentro del rango válido
            if 0 <= _indice < len(lista_categorias):
                # Actualiza los valores de la categoría en la lista
                lista_categorias[_indice].set_codigo_categoria(codigo_categoria)
                lista_categorias[_indice].set_categoria(categoria)

                # Guarda la lista actualizada en el archivo Excel
                self.guardar_categorias(lista_categorias)

                return f'Categoría en el índice {_indice + 1} actualizada correctamente.'
            else:
                return 'Índice de categoría fuera de rango, no se pudo actualizar.'

        except Exception as e:
            return f'Error al editar la categoría: {str(e)}'

    # Método para eliminar una categoría
    def eliminar_categoria(self, _indice):
        try:
            # Obtiene la lista actual de categorías
            lista_categorias = self.obtener_categorias()

            # Verifica si el índice está dentro del rango válido
            if 0 <= _indice < len(lista_categorias):
                # Elimina la categoría en el índice especificado
                lista_categorias.pop(_indice)

                # Guarda la lista actualizada en el archivo Excel
                self.guardar_categorias(lista_categorias)

                return f'Categoría en el índice {_indice + 1} eliminada correctamente.'
            else:
                return 'Índice de categoría fuera de rango, no se pudo eliminar.'

        except Exception as e:
            return f'Error al eliminar la categoría: {str(e)}'
