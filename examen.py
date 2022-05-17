import random


# ----  Ejercicios ---- 

#Ejercicio 1
def mostrarmenu():
    print("---MENU---")
    print("1-Guardar Asignatura")
    print("2-Borrar asignatura")
    print("3-Ver nota media")
    print("4-Ver todas las asignaturas")
    print("5-Salir")
    bandera=True
    while bandera==True:
        try:
           seleccion=int(input("Dime tu opccion:"))
           bandera=False 
           return seleccion
        except:
            print("Dime una opcion valida del 1-5 bobo ")
            bandera=True 




#Fin ejercicio 1
#Ejercicio 3
def guardaasignatura(asignaturas):
    asignatura =(input("Dime el nombre de la asignatura que quieres introducir "))
    asignaturas.append(asignatura)
    return asignaturas
# Fin Ejercicio3

#Ejercicio 4
def borrarasig(asignaturas):
    borrar=input("Que asignatura quieres borrar")
    try:
        asignaturas.remove(borrar)
        return True
    except:
        return False 


#fin 4
#Ejercicio 5
def numAle():
    numale = []
    numNotas = int(input("¿Cuantas asignaturas tienes y te hago la media ?"))
    num = 0

    for i in range(0, numNotas):
        num = random.randint(0, 10)
        numale.append(num)
   
    return numale
#Finejercicio5

#Ejercicio 6
def calcmedia():
    numale = numAle()
    total = 0
    contador = 0

    for i in numale:
        total = total + i
        contador = contador + 1
    
    media = total / contador
    print(media)
    return media
#fin ej 6
#ejercicio 7
def verlista(asignaturas):
    print(" *********** Asignaturas matriculadas **************")
    contador = 0

    for i in asignaturas:
        contador = contador + 1
    
    for i in range(0, contador):
        print(i+1, "-", asignaturas[i])
    print("*********** Fin asignaturas matriculadas **************")
  
#fi ejercico 7

#Ejercicio 8


    


#Fin ejercicio 8
    
    


# ---- Programa principal -----

#Ejercicio 2


asignaturas=[]
opc=mostrarmenu()



while (opc>0) and (opc<6):
    if opc==1:
        guardaasignatura(asignaturas)

    if opc==2:
        borrarasig(asignaturas)

    if opc==3:
       calcmedia()
    if opc==4:
        verlista(asignaturas)

    if opc==5:
        print("SALIENDO...")
        break
    opc=mostrarmenu()
