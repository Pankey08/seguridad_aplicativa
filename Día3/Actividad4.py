#del siguiente diccionario realizar las funciones siguientes
#obtener el promedio
#los que tienen la mayor calificacion y los de menor calificacion

Diccionario = {

    "Juan":8,
    "Giselle": 9,
    "Damian": 5,
    "Ricardo": 6,
    "Yaotzin": 6,
    "Erick": 7,
    "Mario":8,
    "Edgar ":9,
    "Fernanada": 5,
    "Daniel": 6,
    "Jesus": 7,
    "Damian": 8,
    "Yemahina": 6,
    "Eduardo": 9,
    "Bryan": 9,
    "Mariano": 10,
    "Alberto":8
}

def Promedio(pDiccionario):
    ePromedio = 0
    eContador = 0
    for eContador in Diccionario:
        ePromedio += int(Diccionario[eContador])

    print("El promedio es:", ePromedio / len(Diccionario))

def CalificacionMasAlta(pDiccionario):

    print("\nLas personas con la calificacion más alta son:")
    for eContador in Diccionario:
        if int(Diccionario[eContador] == 10):
            print(eContador, end=(", "))
        
def CalificacionMasBaja(pDiccionario):
    
    print("\nLas personas con la calificacion más baja son:")
    for eContador in Diccionario:
        if int(Diccionario[eContador] <= 5):
            print(eContador, end=", ")
            

Promedio(Diccionario)
CalificacionMasAlta(Diccionario)
CalificacionMasBaja(Diccionario)
