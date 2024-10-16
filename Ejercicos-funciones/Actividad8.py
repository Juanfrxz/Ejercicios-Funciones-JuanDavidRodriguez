"""
Escribe un programa que solicite al usuario
ingresar un número y luego muestre la tabla
de multiplicar de ese número del 1 al 10
"""

# Función para mostrar la tabla de multiplicar de un número
def tabla_multiplicar():
    # Solicita al usuario ingresar un número
    numero = int(input("Ingrese un número: "))
    
    # Recorre los números del 1 al 10 para generar la tabla de multiplicar
    for i in range(1, 11):
        # Imprime la multiplicación del número por el valor actual de i
        print(f"{numero} x {i} = {numero * i}")

# Ejecuta la función
if __name__ == '__main__':
    tabla_multiplicar()
