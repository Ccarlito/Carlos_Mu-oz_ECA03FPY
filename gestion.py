from modulos.construccion import constrc_menu, sol_ans, ver_pint, sol_buscar, buscar, agregar, eliminar, sol_eliminar, exportar
from modulos.data import ruta_c, ruta_j, menu
'''
Pinturas Acrílicas Mandarina.
Este algoritmo realiza la gestion del inventario de productos.
--PARAMS--
inventario = archivo json
pintura = {"CODIGO": 380560, "NOMBRE": 'color', "TIPO": 'Acrilico o latex', "VALOR": int, "STOCK": int}
'''
while True:
    constrc_menu(menu)
    ans = sol_ans()
    if ans == '1':
        ver_pint(ruta_j)
    elif ans == '2':
        buscar(sol_buscar(), ruta_j)
    elif ans == '3':
        agregar(ruta_j)
    elif ans == '4':
        eliminar(sol_eliminar(), ruta_j)
    elif ans == '5':
        exportar(ruta_j, ruta_c)
    else:
        print('Coloque una opcion valida')
