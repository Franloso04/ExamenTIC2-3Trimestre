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
    asignaturas.remove(borrar)
#fin 4
#Ejercicio 5
def numAle():
    numale = []
    numNotas = int(input("¿Cuantas notas tienes?"))
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

    for i in numAle:
        total = total + i
        contador = contador + 1
    
    media = total / contador
    
    return media

    
    


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
        print("si")
    if opc==4:
        print ("si")

    if opc==5:
        print("SALIENDO...")
        break
    opc=mostrarmenu()
