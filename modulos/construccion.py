import json
import csv

def constrc_menu(lista):
    '''
    Recibe un iterable de tipo lista y los ordna enumerandolos segun su indice
    --PARAMS--
    lista = debe ser un iterable de tipo lista
    '''
    for ind, opt in enumerate(lista):
        print(f'{ind + 1}. {opt}')


def sol_ans():
    '''
    Solicita una respuesta y la retorna al ambiente global
    --PARAMS--
    no params
    '''
    rsp = input('¿Que quieres hacer?\n')
    return rsp


def ver_pint(archivo):
    '''
    Recibe un arhivo para comprobar existencia y contenido, lo crea si no esta creado, lo abre en modo lectura y lo carga.
    '''
    if not archivo.exists():
        archivo.touch()
    if archivo.stat().st_size == 0:
        print('El archivo esta vacio¡\n')
        json_f = []
        cod = 380560
    else:
        with open(archivo, 'r') as stream:
            json_f = json.load(stream)
            cod = []
            for elemento in json_f:
                print(elemento)


def sol_buscar():
    '''
    Solicita el codigo o nombre de una pintura en el archivo y la retorna al ambiente global.
    '''
    resp = input('Ingresa el codigo o nombre de la pintura que buscas')
    return resp


def buscar(dato, archivo):
    '''
    Recibe un dato y un archivo, comprueba el contenido y la existencia del archivo,
    utiliza el dato para encontrar una coincidencia en el archivo previamente cargado.
    '''
    if not archivo.exists():
        archivo.touch()
    if archivo.stat().st_size == 0:
        print('El archivo esta vacio, no hay pinturas¡\n')
        json_f = []
        cod = 380560
    else:
        with open(archivo, 'r') as stream:
            json_f = json.load(stream)
            cod = []
            for elemento in json_f:
                if str(elemento["CODIGO"]) == dato or dato in elemento["NOMBRE"]:
                    print(f'CODIGO: {elemento["CODIGO"]}')
                    print(f'NOMBRE: {elemento["NOMBRE"]}')


def agregar(archivo):
    '''
    
    '''
    if not archivo.exists():
        archivo.touch()
    if archivo.stat().st_size == 0:
        json_f = []
        cod = 380560
    else:
        with open(archivo, 'r') as stream:
            json_f = json.load(stream)
            cod = []
            for elemento in json_f:
                cod.append(elemento["CODIGO"])
            cod = max(cod) + 1
        while True:
            nom = input('Ingresa el color de la nueva pintura\n')
            if nom.isnumeric():
                print('Solo se permiten caracteres alphabeticos')
            else:
                break
        while True:
            tipo = input('Ingresa el tipo de pintura: (Acrílico o Látex)\n')
            if tipo in ['Acrilico'] or tipo in ['Latex']:
                break
            else:
                print('Error: coloque una opcion valida')
        while True:
            valor = input('Ingresa el valor de la pintura:\n')
            valor = int(valor)
            if type(valor) == int:
                break
            else:
                print('Error: coloque una opción valida')
        while True:
            stock = input('Ingresa el stock de la pintura:\n')
            stock = int(stock)
            if type(stock) == int:
                break
            else:
                print('Error: coloque una opción valida')
        data = {"CODIGO": cod,
                "NOMBRE": nom,
                "TIPO": tipo,
                "VALOR": valor,
                "STOCK": stock}
        json_f.append(data)
        with open(archivo, 'w') as stream:
            json.dump(json_f, stream)
            print('La pintura se ha añadido con exito¡')

        
def sol_eliminar():
    '''
    Solicita una respuesta para luego iterar con ella en otra funcion
    '''
    reesp = input('Ingresa el codigo de la pintura que quieres eliminar')
    return reesp


def eliminar(dato, archivo):
    if not archivo.exists():
        archivo.touch()
    if archivo.stat().st_size == 0:
        print('El archivo esta vacio¡\n')
        json_f = []
        cod = 380560
    else:
        with open(archivo, 'r') as stream:
            json_f = json.load(stream)
            cod = []
            for elemento in json_f:
                if str(elemento["CODIGO"]) == dato:
                    json_f.remove(elemento)
        with open(archivo, 'w') as stream:
            json.dump(json_f, stream)
            print('La pintura se ha borrado con exito')


def exportar(archivo, rutac):
    if not archivo.exists():
        archivo.touch()
    if not rutac.exists():
        rutac.touch()
    else:
        rutac.unlink()
        rutac.touch()
    with open(archivo, 'r') as stream:
        json_f = json.load(stream)
        for elemento in json_f:
            line = [elemento["CODIGO"],
                    elemento["NOMBRE"],
                    elemento["TIPO"],
                    elemento["VALOR"],
                    elemento["STOCK"]]
            with open(rutac, 'w', newline='') as cfile:
                writer = csv.writer(cfile)
                writer.writerow(line)
