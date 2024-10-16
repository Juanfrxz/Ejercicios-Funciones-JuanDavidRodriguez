"""
Escribe un rpograma que solicite al ususario ingresar su edad y luego
determine si es mayor de edad o no utilizando una declaracion if.
si la edad es mayor "eres mayor de edad", de lo contrario, muestra el mensaje 
"eres menor de edad"
"""

# Función para determinar si el usuario es mayor o menor de edad
def edadUsuario():
    # Solicita al usuario que ingrese su edad y la convierte en un número entero
    edad = int(input("Ingresa tu edad: "))
    
    # Condición para verificar si la edad es menor que 18
    if edad < 18:
        # Si la edad es menor a 18, el usuario es menor de edad
        print("Usted es menor de edad")
    else:
        # Si la edad es mayor o igual a 18, el usuario es mayor de edad
        print("Usted es mayor de edad")


if __name__ == '__main__':
    # Llama a la función edadUsuario para evaluar la edad del usuario
    edadUsuario()
