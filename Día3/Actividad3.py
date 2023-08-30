#de la siguiente lista realizar las funciones que obtengan lo siguiente
#obtner el promedio
#la cantidad de reprobados

Lista = [8, 9, 10, 6, 6, 7, 8, 9, 5, 6, 7, 6, 8, 8, 9, 9, 5, 6, 7, 9, 10, 7, 8, 9, 9]

def Promedio(Lista):
    
    eContador = 0
    ePromedio = 0
    for ePromedio in Lista:
        eContador += ePromedio
    resultado = eContador / len(Lista)
    print(resultado)
    

def Reprobados(Lista):

    eTotalReprobados = 0
    eContador = 1
    for eTotalReprobados in Lista:
        if eTotalReprobados == 5:
            eContador +=1
    print("total de reprobados:",eContador - 1 )

Reprobados(Lista)

Promedio(Lista)
