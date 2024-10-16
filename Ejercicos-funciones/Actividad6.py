"""
Escribe un programa que solicite al usuario ingresar el día, el mes y el año de
una fecha. Luego, verifica si la fecha es válida o no. Considera los diferentes
casos, como los días de cada mes y si el año es bisiesto. Muestra un mensaje
indicando si la fecha es válida o no.
"""
# Función para verificar si un año es bisiesto
def es_bisiesto(año):
    # Un año es bisiesto si es divisible entre 4 y (no divisible entre 100 o divisible entre 400)
    return año % 4 == 0 or año % 400 == 0

# Función para verificar si una fecha es válida
def verificar_fecha(dia, mes, ano):
    # Diccionario que define la cantidad de días en cada mes
    dias_por_mes = {
        1: 31,  # Enero
        2: 29 if es_bisiesto(ano) else 28,  # Febrero, dependiendo si es año bisiesto
        3: 31,  # Marzo
        4: 30,  # Abril
        5: 31,  # Mayo
        6: 30,  # Junio
        7: 31,  # Julio
        8: 31,  # Agosto
        9: 30,  # Septiembre
        10: 31,  # Octubre
        11: 30,  # Noviembre
        12: 31   # Diciembre
    }

    # Verifica si el mes está entre 1 y 12
    if mes < 1 or mes > 12:
        return False

    # Verifica si el día es válido para el mes dado
    if dia < 1 or dia > dias_por_mes[mes]:
        return False

    # Si el día y mes son válidos, la fecha es válida
    return True

# Función principal para solicitar la fecha al usuario
def ingresar_fecha():
    # Solicitar al usuario día, mes y año
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    año = int(input("Ingrese el año: "))

    # Verificar si la fecha es válida
    if verificar_fecha(dia, mes, año):
        print("La fecha ingresada es válida.")
    else:
        print("La fecha ingresada es inválida.")

# Ejecuta la función principal
if __name__ == '__main__':
    ingresar_fecha()
