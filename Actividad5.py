"""
Crea un programa que pida al usuario ingresar el nombre de un país y luego
determine en qué continente se encuentra.Utiliza estructuras condicionales para
asociar cada país con su respectivo continente y muestra un mensaje con el
continente correspondiente.
"""
# Función para determinar en qué continente está un país
def paisesContinente():
    # Definición de continentes 
    Adn = 'América del Norte'
    Ads = 'América del Sur'
    As = 'Asia'
    Af = 'África'
    Eu = 'Europa'
    Oc = 'Oceanía'
    # Solicita al usuario que ingrese un país
    pais = input('Ingrese su país por favor: ').lower()  # Convierte la entrada a minúsculas para comparar correctamente
    
    # Verificación del país ingresado y su continente
    if pais == 'colombia':
        print(f'Colombia se encuentra en el continente de {Ads}.')
    elif pais == 'canada':
        print(f'Canadá se encuentra en el continente de {Adn}.')
    elif pais == 'mongolia':
        print(f'Mongolia se encuentra en el continente de {As}.')
    elif pais == 'egipto':
        print(f'Egipto se encuentra en el continente de {Af}.')
    elif pais == 'alemania':
        print(f'Alemania se encuentra en el continente de {Eu}.')
    elif pais == 'nueva zelanda':
        print(f'Nueva Zelanda se encuentra en el continente de {Oc}.')
    else:
        # Si el país no está en la base de datos, se notifica al usuario
        print(f'Su país ({pais}) no está en nuestra base de datos.')

# Este bloque asegura que el código solo se ejecute cuando el archivo se ejecute directamente

if __name__ == '__main__':
    paisesContinente()  # Llama a la función para iniciar la interacción con el usuario
