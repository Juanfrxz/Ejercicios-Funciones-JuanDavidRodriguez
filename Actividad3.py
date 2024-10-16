"""
Escribe un programa que solicite al
usuario ingresar su calificación en un
examen y determine si ha aprobado o
no. Si la calificación es igual o mayor a
60, muestra el mensaje "Has aprobado".
De lo contrario, muestra el mensaje "Has
reprobado".
"""
# Función para evaluar si un estudiante aprueba o reprueba según su calificación
def calificacion():
    # Se solicita al usuario que ingrese una calificación, convirtiéndola a tipo float
    calf = float(input("Ingrese su calificación: ")) 
    
    # Se evalúa si la calificación es mayor o igual a 60
    if calf >= 60:
        # Si la condición es verdadera, el estudiante aprueba
        print("Has aprobado")
    else:
        # Si la condición es falsa, el estudiante reprueba
        print("Has reprobado")

if __name__ == '__main__':
    # Llama a la función calificación para iniciar la evaluación
    calificacion()
