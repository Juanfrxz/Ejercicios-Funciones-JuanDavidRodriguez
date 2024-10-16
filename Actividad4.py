"""
Crea un programa que solicite al
usuario ingresar una contraseña y
verifique si cumple con los siguientes
requisitos: debe tener al menos 8
caracteres y contener al menos un
número. Si la contraseña cumple con
los requisitos, muestra el
mensaje"Contraseña válida". De lo
contrario, muestra el mensaje
"Contraseña inválida".
"""

# Función simple para verificar si la contraseña es válida
def verificar_contraseña():
    # Solicita al usuario ingresar una contraseña
    contraseña = input("Ingrese una contraseña: ")
    
    # Verificar si la contraseña tiene al menos 8 caracteres
    tiene_ocho_caracteres = len(contraseña) >= 8
    
    # Verificar si la contraseña tiene al menos un número
    tiene_numero = False
    for i in contraseña:
        if i.isdigit():
            tiene_numero = True
            break  # Salir del bucle cuando encuentre un numero
    
    # Verifica si ambos requisitos se cumplen
    if tiene_ocho_caracteres and tiene_numero:
        print("Contraseña válida")
    else:
        print("Contraseña inválida")

if __name__ == '__main__':
# Ejecuta la función
    verificar_contraseña()


