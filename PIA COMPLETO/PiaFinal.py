import pickle
import datetime
import re

# Representación de datos
carreras = {
    'LTI': 'LICENCIADO EN TECNOLOGÍA DE LA INFORMACIÓN',
    'LA': 'LICENCIADO EN ADMINISTRACIÓN',
    'CP': 'CONTADOR PÚBLICO',
    'LNI': 'LICENCIADO EN NEGOCIOS INTERNACIONALES',
    'LGRS': 'LICENCIADO EN GESTIÓN DE RESPONSABILIDAD SOCIAL'
}

auditorios = {
    'A': ['Gumersindo Cantú Hinojosa', 1000],
    'B': ['Víctor Gómez', 200],
    'C': ['Casas Alatriste', 150]
}

conferencias = {
    1: ['04/11/2023 15:00', 'Inteligencia Artificial en los Negocios', 'Dr. Alvaro Francisco Salazar', 'A', []],
    2: ['05/11/2023 09:00', 'Uso de la nube para gestión de procesos', 'Dr. Manuel Leos', 'B', []],
    3: ['05/11/2023 14:00', 'Industria 4.0 retos y oportunidades', 'Dra. Monica Hernández', 'C', []],
    4: ['05/11/2023 19:00', 'Machine Learning for a better world', 'Dr. Janick Jameson', 'C', []],
    5: ['06/11/2023 15:00', 'Retos de la Banca Electrónica en México', 'Ing. Clara Benavides', 'A', []]
}

# Clases
class Alumno:
    def __init__(self, matricula, nombre, apellido1, apellido2, fecha_nacimiento, carrera):
        self.matricula = matricula
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.fecha_nacimiento = fecha_nacimiento
        self.carrera = carrera

    def __str__(self):
        return f"{self.matricula}: {self.nombre} {self.apellido1} {self.apellido2}, nacido el {self.fecha_nacimiento}, carrera: {self.carrera}"

class Auditorio:
    def __init__(self, letra, nombre, capacidad):
        self.letra = letra
        self.nombre = nombre
        self.capacidad = capacidad

    def __str__(self):
        return f"{self.letra}: {self.nombre}, con capacidad de {self.capacidad} asistentes."

class Evento:
    def __init__(self, nombre, fecha, presentador, auditorio, asistencias):
        self.nombre = nombre
        self.fecha = fecha
        self.presentador = presentador
        self.auditorio = auditorio
        self.asistencias = asistencias

    def obtener_listado_asistencia(self):
        return self.asistencias

    def __str__(self):
        return f"{self.fecha} - {self.nombre} - {self.presentador} - Auditorio {self.auditorio} ({len(self.asistencias)} asistentes)."

class Asistencia:
    def __init__(self, matricula, alumno, evento, fecha_asistencia):
        self.matricula = matricula
        self.alumno = alumno
        self.evento = evento
        self.fecha_asistencia = fecha_asistencia

# Acciones
class Acciones:
    @staticmethod
    def _cargar_datos(filename):
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            return []

    @staticmethod
    def _guardar_datos(datos, filename):
        with open(filename, 'wb') as file:
            pickle.dump(datos, file)

    @staticmethod
    def guardar_datos(datos, filename):
        try:
            datos_guardados = Acciones._cargar_datos(filename)
            datos_guardados.append(datos)
            Acciones._guardar_datos(datos_guardados, filename)
        except Exception as e:
            print(f"Error al guardar datos: {e}")

    @staticmethod
    def leer_datos(filename):
        try:
            return Acciones._cargar_datos(filename)
        except Exception as e:
            print(f"Error al leer datos: {e}")
            return []

    @staticmethod
    def mostrar_menu(opciones, mensaje):
        while True:
            print(mensaje)
            for key, value in opciones.items():
                print(f"[{key}] {value}")

            opcion_elegida = input("Qué deseas hacer?: ").upper()
            if opcion_elegida in opciones:
                return opcion_elegida
            else:
                print("Opción no válida. Intente de nuevo.")

    @staticmethod
    def validar_fecha_nacimiento(fecha_nacimiento):
        # Expresión regular para el formato YYYY-MM-DD
        patron = re.compile(r'\d{4}-\d{2}-\d{2}')
        return bool(patron.match(fecha_nacimiento))

    @staticmethod
    def validar_carrera(carrera):
        carreras_validas = ['LTI', 'LA', 'CP', 'LNI', 'LGRS']
        return carrera in carreras_validas

    @staticmethod
    def registrar_asistente():
        while True:
            _matricula = input("Ingrese la matrícula del asistente: ")
            # Validación para asegurar que la matrícula tenga al menos 7 caracteres
            while len(_matricula) < 7:
                print("Error: La matrícula debe tener al menos 7 caracteres. Intente de nuevo.")
                _matricula = input("Ingrese la matrícula del asistente: ")

            try:
                matricula = int(_matricula)
            except ValueError:
                print("Error: La matrícula debe ser un número. Intente de nuevo.")
                continue

            nombre = input("Ingrese el nombre del asistente: ")
            # Validación para asegurar que el nombre no contenga números
            while any(char.isdigit() for char in nombre):
                print("Error: El nombre no debe contener números. Intente de nuevo.")
                nombre = input("Ingrese el nombre del asistente: ")

            apellido1 = input("Ingrese el primer apellido del asistente: ")
            # Validación para asegurar que el primer apellido no contenga números
            while any(char.isdigit() for char in apellido1):
                print("Error: El primer apellido no debe contener números. Intente de nuevo.")
                apellido1 = input("Ingrese el primer apellido del asistente: ")

            apellido2 = input("Ingrese el segundo apellido del asistente: ")
            # Validación para asegurar que el segundo apellido no contenga números
            while any(char.isdigit() for char in apellido2):
                print("Error: El segundo apellido no debe contener números. Intente de nuevo.")
                apellido2 = input("Ingrese el segundo apellido del asistente: ")

            # Validación de la fecha de nacimiento
            while True:
                fecha_nacimiento = input("Ingrese la fecha de nacimiento del asistente (YYYY-MM-DD): ")
                if Acciones.validar_fecha_nacimiento(fecha_nacimiento):
                    break
                else:
                    print("Error: El formato de la fecha de nacimiento no es válido. Intente de nuevo.")

            # Validación de la carrera dentro de un bucle hasta que se ingrese una opción válida
            carrera = input("Ingrese la carrera del asistente (LTI, LA, CP, LNI, LGRS): ").upper()
            while not Acciones.validar_carrera(carrera):
                print("ERROR. Ingresa una de estas opciones específicas (LTI, LA, CP, LNI, LGRS), intente de nuevo.")
                carrera = input("Ingrese la carrera del asistente (LTI, LA, CP, LNI, LGRS): ").upper()

            return Alumno(matricula, nombre, apellido1, apellido2, fecha_nacimiento, carreras[carrera])

    @staticmethod
    def validar_fecha_nacimiento(fecha_nacimiento):
        # Expresión regular para el formato YYYY-MM-DD
        patron = re.compile(r'\d{4}-\d{2}-\d{2}')
        return bool(patron.match(fecha_nacimiento))

    @staticmethod
    def registrar_asistente_a_evento(matricula, evento_id):
        try:
            eventos = Acciones._cargar_datos('eventos.pkl')
            alumnos = Acciones._cargar_datos('alumnos.pkl')

            evento_encontrado = None
            alumno_encontrado = None

            for evento in eventos:
                if evento_id in conferencias and evento.nombre == conferencias[evento_id][1]:
                    evento_encontrado = evento
                    break

            for alumno in alumnos:
                if alumno.matricula == matricula:
                    alumno_encontrado = alumno
                    break

            if evento_encontrado and alumno_encontrado:
                fecha_actual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
                nueva_asistencia = Asistencia(matricula, alumno_encontrado, evento_encontrado, fecha_actual)
                evento_encontrado.asistencias.append(nueva_asistencia)
                Acciones._guardar_datos(eventos, 'eventos.pkl')
        except Exception as e:
            print(f"Error al registrar asistente a evento: {e}")

    @staticmethod
    def eventos_registrados_para_asistente(matricula, evento_id):
        try:
            eventos = Acciones._cargar_datos('eventos.pkl')
            alumno_eventos = []

            for evento in eventos:
                for asistencia in evento.asistencias:
                    if asistencia.matricula == matricula:
                        print(f"Comparando eventos - Matrícula: {matricula}, Evento Matrícula: {asistencia.matricula}")
                        alumno_eventos.append(evento)

            return alumno_eventos
        except Exception as e:
            print(f"Error al obtener eventos registrados para el asistente: {e}")
            return []


if __name__ == '__main__':
    acciones = Acciones()

    opciones_menu_principal = {
        'A': 'Registrar un asistente',
        'B': 'Registrar asistente a un evento',
        'C': 'Registrar asistencia al evento',
        'D': 'Ver eventos del alumno',
        'E': 'Listado de asistencia',
        'X': 'Salir\n'
    }

    opciones_menu_asistentes = {
        'A': 'Registrar un asistente',
        'B': 'Registrar asistente a un evento',
        'X': 'Salir\n'
    }

    asistente_registrado = False  # Variable para rastrear si se ha registrado un asistente

    while True:
        opcion_elegida = Acciones.mostrar_menu(opciones_menu_principal, '\n** MENÚ PRINCIPAL\n')
        if opcion_elegida == 'X':
            print("Saliendo del programa.")
            break
        elif opcion_elegida == 'A':
            while True:
                opcion_elegida_asistente = Acciones.mostrar_menu(opciones_menu_asistentes, '\n** MENÚ ASISTENTES\n')
                if opcion_elegida_asistente == 'A':
                    nuevo_asistente = acciones.registrar_asistente()
                    if nuevo_asistente:
                        Acciones.guardar_datos(nuevo_asistente, 'alumnos.pkl')
                        asistente_registrado = True  # Se ha registrado un asistente
                        print("Asistente registrado exitosamente.")
                    break
                elif opcion_elegida_asistente == 'B':
                    if not asistente_registrado:
                        print("Error: Debes registrar un asistente primero.")
                        break
                    matricula = input("Ingrese la matrícula del asistente: ")
                    try:
                        matricula = int(matricula)
                        while len(str(matricula)) < 7:
                            print("Error: La matrícula debe tener al menos 7 caracteres. Intente de nuevo.")
                            matricula = input("Ingrese la matrícula del asistente: ")

                        matricula = int(matricula)
                    except ValueError:
                        print("Error: La matrícula debe ser un número. Intente de nuevo.")
                        continue
                    
                    # Obtener evento_id
                    print("\nConferencias disponibles:")
                    for key, value in conferencias.items():
                        fecha_hora, nombre, presentador, auditorio, asistentes_registrados = value
                        print(f"[{key}] {fecha_hora} - {nombre} ({presentador}) - Auditorio {auditorio} ({len(asistentes_registrados)} asistentes registrados)")

                    evento_id = input("Ingrese el número de la conferencia a la que desea registrar asistencia: ")
                    try:
                        evento_id = int(evento_id)
                        if evento_id in conferencias:
                            acciones.registrar_asistente_a_evento(matricula, evento_id)
                            print("Asistente registrado a conferencia exitosamente.")
                        else:
                            print("Error: El número de conferencia ingresado no es válido.")
                    except ValueError:
                        print("Error: Ingrese un número válido para la conferencia.")
                    
                    break
                elif opcion_elegida_asistente == 'X':
                    break
                else:
                    print("Opción no válida en el menú de asistentes. Intente de nuevo.")

        elif opcion_elegida == 'B':
            if not asistente_registrado:
                print("Error: Debes registrar un asistente primero.")
            else:
                matricula = input("Ingrese la matrícula del asistente: ")
                try:
                    matricula = int(matricula)
                except ValueError:
                    print("Error: La matrícula debe ser un número. Intente de nuevo.")
                    continue
        
                    # Obtener evento_id
            print("\nConferencias disponibles:")
            for key, value in conferencias.items():
                fecha_hora, nombre, presentador, auditorio, asistentes_registrados = value
                print(f"[{key}] {fecha_hora} - {nombre} ({presentador}) - Auditorio {auditorio} ({len(asistentes_registrados)} asistentes registrados)")

            evento_id = input("Ingrese el número de la conferencia a la que desea registrar asistencia: ")
            try:
                evento_id = int(evento_id)
                if evento_id in conferencias:
                    acciones.registrar_asistente_a_evento(matricula, evento_id)
                    print("Asistente registrado a conferencia exitosamente.")
                else:
                    print("Error: El número de conferencia ingresado no es válido.")
            except ValueError:
                print("Error: Ingrese un número válido para la conferencia.")

                acciones.registrar_asistente_a_evento(matricula, evento_id)
                print("Asistente registrado a conferencia exitosamente.")

        elif opcion_elegida == 'C':
            if not asistente_registrado:
                print("Error: Debes registrar un asistente primero.")
            else:
                matricula = input("Ingrese la matrícula del asistente: ")
                try:
                    matricula = int(matricula)
                except ValueError:
                    print("Error: La matrícula debe ser un número. Intente de nuevo.")
                    continue

                # Obtener evento_id
                print("\nConferencias disponibles:")
                for key, value in conferencias.items():
                    fecha_hora, nombre, presentador, auditorio, asistentes_registrados = value
                    print(f"[{key}] {fecha_hora} - {nombre} ({presentador}) - Auditorio {auditorio} ({len(asistentes_registrados)} asistentes registrados)")

                evento_id = input("Ingrese el número de la conferencia a la que desea registrar asistencia: ")
                try:
                    evento_id = int(evento_id)
                    if evento_id in conferencias:
                        acciones.registrar_asistente_a_evento(matricula, evento_id)
                        print("Asistente registrado a conferencia exitosamente.")
                        
                        # Aquí llamamos a eventos_registrados_para_asistente con ambos argumentos
                        eventos_registrados = acciones.eventos_registrados_para_asistente(matricula, evento_id)
                        if not eventos_registrados:
                            print("Error: El asistente no está registrado para ningún evento. Registre al asistente en un evento antes de marcar asistencia.")
                            continue
                    else:
                        print("Error: El número de conferencia ingresado no es válido.")
                except ValueError:
                    print("Error: Ingrese un número válido para la conferencia.")


        elif opcion_elegida == 'D':
            if not asistente_registrado:
                print("Error: Debes registrar un asistente primero.")
            else:
                matricula = input("Ingrese la matrícula del asistente: ")
                try:
                    matricula = int(matricula)
                except ValueError:
                    print("Error: La matrícula debe ser un número. Intente de nuevo.")
                    continue

                eventos_registrados = acciones.eventos_registrados_para_asistente(matricula, evento_id)
                if not eventos_registrados:
                    print("El asistente no está registrado para ningún evento.")
                else:
                    print("\nEventos registrados para el asistente:")
                    for evento in eventos_registrados:
                        print(evento)
                        
        elif opcion_elegida == 'E':
            eventos = acciones.leer_datos('eventos.pkl')
            if not eventos:
                print("No hay eventos registrados.")
            else:
                for evento in eventos:
                    print(evento)
                    
        else:
            print("Opción no válida. Intente de nuevo.")

