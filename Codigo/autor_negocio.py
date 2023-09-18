import pandas as pd
from openpyxl import Workbook
from autor import Autor

#editar eliminar guardar del main autor
class AutorNegocio():
    listado_autores=[]
    registros_autores = 'listado_autores.xlsx'

    def __init__(self):
        self.listado_autor=[]

    def obtener_autores(self):
        
        df = pd.read_excel(self.registros_autores)
        listado_autor = []
        for index, row in df.iterrows():
            autor = Autor(row['Nombre'], row['Apellido Paterno'], row['Apellido Materno'], row['Fecha de Nacimiento'], row['Codigo del Autor'], row['Pais'], row['Editorial'])
            listado_autor.append(autor)
        return listado_autor

    def registrar_autores(self,nombre, apellido_paterno, apellido_materno, fecha_nacimiento, codigo_autor, pais, editorial):
        
        print(f'{nombre}, {apellido_paterno}, {apellido_materno}, {fecha_nacimiento}, {codigo_autor}, {pais}, {editorial}')
        self.listado_autor = self.obtener_autores()
        autor = Autor(nombre, apellido_paterno, apellido_materno, fecha_nacimiento, codigo_autor, pais, editorial)
        self.listado_autor.append(autor)
        
        print(f'se agrego un autor : {len(self.listado_autor)}')

    def guardar_autores(self):
        
        print(f'listado de autores es: {len(self.listado_autor)}')
        if len(self.listado_autor) > 0:
            data =[]
            for autor in self.listado_autor:
                data.append([autor.nombre, autor.apellido_paterno, autor.apellido_materno, autor.fecha_nacimiento, autor.codigo_autor, autor.pais, autor.editorial])
            columnas = ['Nombre', 'Apellido Paterno', 'Apellido Materno', 'Fecha de Nacimiento', 'Codigo del Autor', 'Pais', 'Editorial']
            df = pd.DataFrame(data, columns=columnas)
            df.to_excel(self.registros_autores, index=False, engine='openpyxl')
            return f'se registro correctamento los datos del autor'
        else:
            return f'se genero un erro al registrar el autor'

    def editar_autor(self,_indice, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, codigo_autor, pais, editorial):
        
        df = pd.read_excel(self.registros_autores)
        df.loc[_indice, 'Nombre'] = nombre
        df.loc[_indice, 'Apellido Paterno'] = apellido_paterno
        df.loc[_indice, 'Apellido Materno'] = apellido_materno
        df.loc[_indice, 'Fecha de Nacimiento'] = fecha_nacimiento
        df.loc[_indice, 'Codigo del Autor'] = codigo_autor
        df.loc[_indice, 'Pais'] = pais
        df.loc[_indice, 'Editorial'] = editorial
        df.to_excel(self.registros_autores, index=False, engine='openpyxl')
        
        return f'actualización correcta'

    def eliminar_autor(self, _indice):
        try:
            
            # Leer el archivo Excel y cargar los datos en un DataFrame
            df = pd.read_excel(self.registros_autores)
            
            # Verificar si el índice está dentro del rango válido
            if 0 <= _indice < len(df):
                # Eliminar el docente en el índice especificado
                # inplace=True, los cambios se aplican directamente al DataFrame original
                df.drop(_indice, inplace=True)
                
                # Guardar los cambios en el archivo Excel
                df.to_excel(self.registros_autores, index=False, engine='openpyxl')
                
                return f'Curso en el índice {_indice + 1} eliminado correctamente.'
            else:
                return 'Índice de curso fuera de rango, no se pudo eliminar.'
            
        except FileNotFoundError:
            return 'Archivo de registros de cursos no encontrado.'
