"""
Crea un rpograma que solicite al usuario un numero entero positivo
y luego imprima los numeros desde ese numero hasta 1 utilizando
bucle while
"""
# Se inicializa la variable num con un valor de 1
num = 1

# Función que solicita al usuario un número entero positivo y cuenta hacia atrás hasta 1
def num_user():
    # Se solicita al usuario que ingrese un número entero positivo
    numeroUsuario = int(input("Ingrese un número entero positivo: "))
    
    # Se ejecuta el bucle mientras el número ingresado sea mayor o igual a 1
    while numeroUsuario >= num:
        # Imprime el número actual
        print(numeroUsuario)
        # Resta 1 al número actual en cada iteración para contar hacia atrás
        numeroUsuario -= 1

if __name__ == '__main__':
# Llama a la función para iniciar el proceso
    num_user()
