#Crea un programa que permita ingresar numeros del 0 al 100 y muestre por pantalla el numero entero ingresado a letras

unidades = { 0:" ", 1:"uno", 2:"dos", 3:"tres", 4:"cuatro", 5: "cinco", 6:"seis", 7:"siete", 8:"ocho", 9:"nueve"}
decenas = {1: "dieci", 2:"veinte", 3: "treinta", 4:"cuarenta", 5:"cincuenta", 6:"sesenta", 7:"setenta", 8:"ochenta", 9:"noventa"}
otros = {0:"cero", 10: "diez",11: "once", 12:"doce", 13: "trece", 14: "catorce", 15:"quince", 100 :"cien"}


#primero verificar cuantas cifras tiene
def verificarCifras(numero):
    num_cifras = 0
    verificar_num = numero

    while verificar_num > 0:
        verificar_num = verificar_num//10
        num_cifras += 1
    
    return num_cifras


def convertir(num_cifras, numero):
    lista_num = []
    #si el numero tiene solo una cifra entonces solo se llama a decenas
    if num_cifras == 1:
        decena_letra = unidades.get(numero)
        print(decena_letra)
    #si tiene dos cifras entonces
    else:
        #estos numeros no se pueden combinar asi que le damos trato especial
        if numero in otros.keys(): 
            excentrico = otros.get(numero)
            print(excentrico)
        #si se puede combinar entonces
        else:
            nuevo = str(numero) #paso el numero a una cadena para poderlo iterar ya que los enteros no son iterables

            for cifras in nuevo:
                lista_num.append(int(cifras)) #ya que se va iterando lo guardo en una lista pero ya como entero

            print(numero)
            uni = decenas.get(lista_num[0]) #medinate esos enteros guardo el valor del diccionario correspondiente a esa llave
            dec = unidades.get(lista_num[1])
            #si unidad es cero entonces solo imprime la decena

            if lista_num[1] > 0: #si la unidad es mayor que cero se le agrega el "y" a la cadena
                print(uni+" y "+dec)
            else: #sino solo se imprime la decena
                print(uni + dec)


#pedir el numero y verificar que sea del 0 al 100
def principal():
    try:
        numero = int(input("Digita numero: "))
        if numero >= 0 and numero<=100:
            cifras = verificarCifras(numero)
            convertir(cifras, numero)
        else:
            print("Solo numeros del 0 al 100")
    except ValueError:
        print("Ingresa solo numeros")
        print("--------------------")


#aqui iniciamos el programa
while True:
    print("------------------------------")
    iniciar = input("Convertir un numero? (s/n): ")
    
    if iniciar == 's':
        principal()
    else:
        break


