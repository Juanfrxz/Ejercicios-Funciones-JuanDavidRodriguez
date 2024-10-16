"""
Escribe un programa que solicite al usuario ingresar el día, el mes y el año de
una fecha. Luego, verifica si la fecha es válida o no. Considera los diferentes
casos, como los días de cada mes y si el año es bisiesto. Muestra un mensaje
indicando si la fecha es válida o no.
"""
def fecha():
    dd_user = int(input("Ingrese el día: "))
    mm_user = int(input("Ingrese el mes: "))
    aa_user = int(input("Ingrese el año: "))
    if mm_user == 4 or mm_user == 6 or mm_user == 9 or mm_user == 11:
        if dd_user <= 30:
            if aa_user <= 2024:
                print("La fecha es válida.")
            else:
                print("La fecha no es válida.")
        else:
            print("La fecha no es válida.")        
    if mm_user == 1 or mm_user == 3 or mm_user == 5 or mm_user == 7 or mm_user == mm_user == 8 or mm_user == 10 or mm_user == 12:
        if dd_user <= 31:
            if aa_user <= 2024:
                print("La fecha es válida.")
            else:
                print("La fecha no es válida.")
        else:
            print("La fecha no es válida")        
    if mm_user == 2:
        if dd_user <= 29:
            if aa_user % 4 == 0 or aa_user % 400 == 0:
                print("La fecha es válida.")
            else:
                print("La fecha no es válida.")
        else:
            print("La fecha no es válida.")


if __name__ == '__main__':
    fecha()
