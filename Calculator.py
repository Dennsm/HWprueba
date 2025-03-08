#Proyecto Calculadora

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b
#Multiplicar
def multiplicar(a, b):
    return a * b
#Dividir
def dividir(a, b):
    if b == 0:
        print("No se puede dividir por 0")
        return
    
    return a/b

def salir():
    print("Salio")

print("Calculador 1.0")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Salir")
opt = input("Introduzca una opción válida: ")

if int(opt) >= 1 and int(opt) <= 5:
    
    if opt == "5":
        salir()
    else:
        a = float(input ("Introduzca el número a: "))
        b = float(input ("Introduzca el número b: "))
    
        if opt == "1":
            print("La suma es: ", sumar(a, b))
            
        elif opt == "2":
            print("La resta es: ", restar(a, b))
        elif opt == "3":
            print("La multiplicación es: ", multiplicar(a, b))
        elif opt =="4":
            print("La división es: ", dividir(a, b))
        
else:
    print("No es una opcion válida! ")
