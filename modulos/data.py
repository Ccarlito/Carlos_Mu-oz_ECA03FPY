from pathlib import Path

home = Path(__file__).parent.parent

ruta_c = Path(home/'mandarina.csv')
ruta_j = Path(home/'base.json')

menu = ['Ver listado de pinturas', 'Buscar pinturas', 'Agregar pinturas', 'Eliminar pinturas', 'Exportar pinturas']

pintura_base = {"CODIGO": 380560, "NOMBRE": 'negro', "TIPO": 'latex', "VALOR": 6990, "STOCK": 5}