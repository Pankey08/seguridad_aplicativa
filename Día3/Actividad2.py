#calculadora en python jiji

def Bienvenida():
    print("Bienvenido a la calculadora de python\nElige cualquiera de las siguientes opciones")
    print("1- Suma\n2- Resta\n3-Multiplicacion\n4- Division\n5- salir")

def Suma(eNum1, eNum2):
    return eNum1 + eNum2

def Resta(eNum1, eNum2):
    return eNum1 - eNum2

def Multiplicacion(eNum1, eNum2):
    return eNum1 * eNum2

def Division(eNum1, eNum2):
    return eNum1 / eNum2

def calculadora():

    Bienvenida()

    eOpcion = input("por favor ingresa una opcion: ")
    eNum1 = input("ingresa el primer valor: ")
    eNum2 = input("ingresa el segundo valor: ")

    if int(eOpcion) == 1:
        print("El resultado es:", Suma(int(eNum1), int(eNum2)))
    elif int(eOpcion) == 2:
        print("El resultado es:", Resta(int(eNum1), int(eNum2)))
    elif int(eOpcion) == 3:
        print("El resultado es:", Multiplicacion(int(eNum1), int(eNum2)))
    elif int(eOpcion) == 4:
        print("El resultado es:", Division(float(eNum1), float(eNum2)))
    elif int(eOpcion) == 5:
        print("MUchas gracias por usarme, hasta pronto :)")
    else:
            print("elige una de las opciones señaladas")

calculadora()
