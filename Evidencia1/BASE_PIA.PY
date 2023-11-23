# Declaraciones generales
import re

def elegir_letra(prompt:str='Dame una letra: ',
                 opciones_validas:str='12345'):
        while True:
            opcion=input(prompt)
            opcion=opcion.upper()
            if (opcion==''):
                print('Error en captura. Opción no se puede omitir. Inténtelo de nuevo')
                continue
            if not bool(re.match(f'^[{opciones_validas}]$',opcion)):
                print('Error en captura. Opción no reconocida. Inténtelo de nuevo')
                continue
            # Si todo fue bien, se sale.
            break
        return opcion
def mostrar_menu(
    opciones:dict,
    titulo:str='OPCIONES DISPONIBLES'):

    print(titulo)
    opciones_validas=''
    for k,v in opciones.items():
        print(f'[{k}] {v}')
        opciones_validas=f'{opciones_validas}{k}'

    opc=elegir_letra('Qué opción deseas?: ', opciones_validas)
    return opc
# Programa principal

opciones_menu_principal={
    'A':'Registrar un asistente',
    'B':'Registrar asistente a un evento',
    'C':'Registrar asistencia al evento',
    'D':'Ver eventos del alumno',
    'E':'Listado de asistencia',
    'X':'Salir\n'
}

opciones_menu_asistentes={
    'A':'Registrar un asistente',
    'B':'Registrar asistente a un evento',
    'X':'Salir\n'
}

while True:
    opcion_elegida=mostrar_menu(opciones_menu_principal, '\n** MENÚ PRINCIPAL\n')
    match opcion_elegida:
        case 'A':
            while True:
                opcion_elegida_asistente=mostrar_menu(opciones_menu_asistentes, '\n** MENÚ ASISTENTES\n')
                match opcion_elegida_asistente:
                    case 'X':
                        break
                    case _:
                        print('Opción no reconocida.')
                        continue
        case 'X':
            print('Gracias por usar el sistema.')
            break
        case _:
            print('Opción no reconocida.')
            continue

# Representación de auditorios en un diccionario.
auditorios={
    'A': ['Gumersindo Cantú Hinojosa', 1000],
    'B': ['Víctor Gómez', 200],
    'C': ['Casas Alatriste', 150]
}
from IPython.core.excolors import exception_colors
conferencias={
    1:['04/11/2023 15:00','Inteligencia Artificial en los Negocios',
       'Dr. Alvaro Francisco Salazar', 'A', 0],
    2:['05/11/2023 09:00','Uso de la nube para gestión de procesos',
       'Dr. Manuel Leos','B',0],
    3:['05/11/2023 14:00','Industria 4.0 retos y oportunidades',
       'Dra. Monica Hernández','C',20],
    4:['05/11/2023 19:00','Machine Learning for a better world',
       'Dr. Janick Jameson','C',0],
    5:['06/11/2023 15:00','Retos de la Banca Electrónica en México',
       'Ing. Clara Benavides','A',0]
}

conferencia=0
while True:
    _conferencia=input('A qué conferencia deseas inscribirte?: ')
    # Validar que no se omita
    if (_conferencia==''):
        print('Error. Se debe especificar una conferencia válida. Intenta de nuevo')
        continue
    # Validar que sea entero.
    try:
        conferencia=int(_conferencia)
    except:
        print('Error.Debe ser entero. Intenta de nuevo')
        continue
    # Validar que la conferencia exista
    if not (conferencia in conferencias):
        print('Error. Esa conferencia no existe. Intenta de nuevo')
        continue
    # Si capturé una conferencia existente, que la despliegue.
    break

print('Encontré.')

def info_disponibilidad(conferencia_deseada:int):
    datos_conferencia=conferencias.get(conferencia_deseada,'')
    print(f'Conferencia: {datos_conferencia[1]}')
    print(f'Expositor: {datos_conferencia[2]}')
    print(f'Fecha: {datos_conferencia[0]}')
    nombre_auditorio=auditorios.get(datos_conferencia[3],'')[0]
    capacidad_auditorio=auditorios.get(datos_conferencia[3],'')[1]
    lugares_disponibles=capacidad_auditorio-datos_conferencia[4]
    print(f'Auditorio: {nombre_auditorio}')
    print(f'Lugares disponibles: {lugares_disponibles:,}')
    return lugares_disponibles

disponibilidad=info_disponibilidad(conferencia)

def inscribir(conferencia_destino:int,cant:int=0):
    conferencias[conferencia_destino][4]+=cant

nuevos_asistentes=5
disponibilidad=disponibilidad=info_disponibilidad(conferencia)

if (disponibilidad>=nuevos_asistentes):
    inscribir(conferencia,nuevos_asistentes)

disponibilidad=info_disponibilidad(conferencia)

carreras={
    'LTI':'LICENCIADO EN TECNOLOGÍA DE LA INFORMACIÓN',
    'LA':'LICENCIADO EN ADMINISTRACIÓN',
    'CP':'CONTADOR PÚBLICO',
    'LNI':'LICENCIADO EN NEGOCIOS INTERNACIONALES',
    'LGRS':'LICENCIADO EN GESTIÓN DE RESPONSABILIDAD SOCIAL'
}