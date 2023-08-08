#LIBRERIAS IMPORTADAS

import datetime
import random
import time

# FUNCIONES SECUNDARIAS 

#Esta funcion se encargar de tomar un valor entero, convertirlo a una cadena y una vez convertido calcular la cantidad de digitos que posee. La misma rertorna este ultimo valor. 
def cantidad_cifras(numero):      
    conversion_numero = str(numero) #conversion de entero a cadena 
    cantidad_cifras = len(conversion_numero) #lee la longitud de la cadena 
    return cantidad_cifras #retorna la cantidad de digitos

#Esta funcion se encarga de imprimir en la consola un ticket con informacion sobre la apuesta (de quienila o quini 6, se utiliza en ambas), toma una serie de parametros. 
def crear_ticket(dni, dinero_apostado, fecha_hora, numero_comprobante, numero_apuesta): 
    print("\n--- Ticket Comprobante ---") #Realiza un salto de linea e imprime el encabezado del ticket
    print("Quiniela: 'LA FORTUNA'") #imprime el nombre de la quiniela
    print("Fecha y hora:", fecha_hora.strftime("%Y-%m-%d %H:%M")) #imprime la fecha y hora de la apuesta 
    print("Número de comprobante:", numero_comprobante) #imprime el numero de comprobante 
    print("DNI del cliente:", dni) #imprime el DNI del apostador
    print("Numero apostado:", numero_apuesta) #imprime el numero apostado por el cliente
    print("Cifra apostada: $" + str(dinero_apostado)) #imprime el dinero apostado por el cliente y lo concatena con el signo "$"
    print("--------------------------\n")

#Esta funcion se encarga de almacenar una apuesta (de quiniela o quini 6, se utiliza en ambos) en un fichero. Cada apuesta se almacena en una misma linea 
def almacenar(nombre_archivo,dni, dinero_apostado, fecha_hora, numero_comprobante, numero_apuesta): 
     with open(nombre_archivo, "a") as archivo: #abre el fichero especifico de "nombre_archivo" como modo apertura y lo asocia a la variable "archivo"
        archivo.write(f"{fecha_hora},{numero_comprobante},{dni},{dinero_apostado},{numero_apuesta}\n") #Se encarga de escribir en una unica linea del fichero toda la informacion relevante sobre la apuesta, los valores se separan uno a los otros por comas y cuando se termina de escribir una linea se produce un salto de linea. 

#Esta funcion se encarga de cargar la información de las apuestas desde un fichero y luego almacenar esa información en una lista en forma de diccionarios.
def cargar(nombre_archivo): 
    apuestas = [] #se crea una lista vacia para almacenar las apuestas
    with open(nombre_archivo, "r") as archivo: #abre el fichero especifico de "nombre_archivo" en modo lectura y lo asocia a la variable "archivo"
        for linea in archivo: #se itera cada linea del archivo, cada iteracion contendra una linea del archivo
            apuesta_unica = linea.strip().split(",") #divide mediante comas la linea en partes y almacena los resultados en una lista llamada apuesta_unica. Con el método .strip() se eliminan los espacios en blanco del inicio y final de la línea.
            apuesta = { #crea un diccionario que almacenara la informacion de la apuesta en diferentes campos, estos valores se obtienen de la lista "apuesta_unica" y mediante corchetes se indica la posicion de cada valor almcenado.  
                "fecha_hora": apuesta_unica[0],
                "numero_comprobante": apuesta_unica[1],
                "dni": apuesta_unica[2],
                "cantidad_dinero": apuesta_unica[3],
                "numero_apostado": int(apuesta_unica[4])
            }
            apuestas.append(apuesta) #agrega en la lista "apuestas" el diccionario "apuesta" 
    return apuestas #retorna la lista de diccionarios "apuestas"

#Esta funcion se encarga de comprobar si el numero ganador ingresado coincide con algun numero apostado que se encuentre dentro de la la lista "apuestas"
def comprobar_apuesta(numero_ganador, apuestas):
    obtener_ganadores = [] #se crea una lista vacia para almacenar los ganadores
    for apuesta in apuestas: #se itera en cada diccionario dentro de la lista "apuestas"
        if numero_ganador == apuesta["numero_apostado"]: #se comprueba si el numero ganador ingresado por el usuario coincide con el numero apostado en el presente diccionario
            obtener_ganadores.append(apuesta) #si se encuentra se agrega la apuesta ganadora a la lista "ganadores"
    return obtener_ganadores #se retorna la lista con las apuestas ganadoras 

# FUNCIONES PRINCIPALES

#Esta funcion se encarga de tomar apuestas de la quiniela, almacenarlas en un fichero y mostrar un ticket en consola con los detalles de la apuesta. 
def quiniela():
    print("Has seleccionado la opcion 'QUINIELA'")
    
    while True: 
        dni = input("Ingrese su DNI: ") #pide al usuario su DNI
        if(cantidad_cifras(dni) == 8): #comprobar si el DNI ingresado contiene 8 cifras, para esto se utiliza la funcion "cantidad_cifras" donde se le pasa el DNI ingresado para determinar la cantidad de cifras del mismo
            break #si el DNI posee 8 cifras sale del bucle
        else: #si el DNI no posee 8 cifras se indica que se ingrese nuevamente un DNI 
            print("El DNI ingresado no es valido, recuerde que debe poseer 8 digitos") 
            dni = input("Ingrese nuevamente su DNI: ")

    cifra = int(input("Ingrese el numero de cifras del numero que desea apostar (2,3 o 4): ")) #pide al usuario que ingrese la cantidad de cifras del numero que desea apostar
    while(cifra < 2) or (cifra > 4 ): #se crea un while que se ejecuta siempre que la cifra ingresada no esté en el rango válido. 
       cifra = int(input("La cifra ingresada es incorrecta, por favor ingrese '2' , '3'  o '4' ): ")) #si la cifra no coincide con las soliciradas se muestra este mensaje y se solicita ingresar nuevamente la cantidad de cifras
    
    numero_apuesta = int(input(f"Ingrese un numero de {cifra} cifras para apostar: ")) #pide al usuario que ingrese el numero que desea apostar que coincida con las cifras elegida previamente 
    cifras_usadas = cantidad_cifras(numero_apuesta) #se utiliza la funcion "cantidad_cifras" para almacenar en la variable "cifras_usadas" la cantidad de cifras que posee el numero de apuesta 
    while(cifras_usadas != cifra): #se crea un bucle while que se ejecuta siempre que la cantidad de cifras de la apuesta no coincida con la cifra elegida previamente
        numero_apuesta = int(input("El numero ingresado no concuerda con la cantidad de cifras elegida, intentelo nuevamente: ")) #si la cantidad de cifras no coincide de muestra este mensaje y se solicita ingresar nuevamente un numero de apuesta
        cifras_usadas = cantidad_cifras(numero_apuesta) #se calcula nuevamente la cantidad de cifras del numero de apuesta
    
    dinero_apostado = int(input("Ingrese la cifra que desea apostar: ")) #se solicita al usuario que ingrese la cantidad de dinero que desea apostar

    fecha_hora = datetime.datetime.now() #se almacena en una variable la fecha y hora actual, para eso se utiliza el medulo presente
    numero_comprobante = random.randint(10000,99999) #se almacena en una variable un numero aleatorio en el rango de 10000 a 99999, este numero lo genera el modulo "random" 

    nombre_archivo = "quiniela.txt" #se almacena en una variable el nombre del fichero donde se almacenaran las apuestas de la quiniela

    almacenar(nombre_archivo, dni, dinero_apostado, fecha_hora, numero_comprobante, numero_apuesta) #se llama a la funcion "almacenar" para almacenar la informacion de la apuesta
    
    crear_ticket(dni, dinero_apostado, fecha_hora, numero_comprobante, numero_apuesta) #se llama a la funcion "crear_ticket" para crear el ticket con la informacion de la apuesta y mostrarlo en consola. 

##Esta funcion se encarga de tomar apuestas del quini 6, almacenarlas en un fichero y mostrar un ticket en consola con los detalles de la apuesta. 
def quiniela_tradicional(): 
    print("Has seleccionado la opcion 'QUINI 6'")

    while True: 
        dni = input("Ingrese su DNI: ") #pide al usuario su DNI
        if(cantidad_cifras(dni) == 8): #comprobar si el DNI ingresado contiene 8 cifras, para esto se utiliza la funcion "cantidad_cifras" donde se le pasa el DNI ingresado para determinar la cantidad de cifras del mismo
            break #si el DNI posee 8 cifras sale del bucle
        else: #si el DNI no posee 8 cifras se indica que se ingrese nuevamente un DNI 
            print("El DNI ingresado no es valido, recuerde que debe poseer 8 digitos") 
            dni = input("Ingrese nuevamente su DNI: ")

    print("Debe ingresar el numero que desea apostar") #indica al usuario que debe ingresar el numero que desea apostar 
    print("Presione (1) si desea ingresar el numero manualmente") #indica al usuario que debe presionar el 1 si desea ingresar el numero manuelamente
    print("Presione (2) si deseas que el numero se genere automaticamente") #indica al usuario que debe ingresar el 2 si desea que el numero se genere automaticamente 
    opcion = int(input("Ingrese una opción: ")) #indica al usuario que ingrese la opcion que desea
    while opcion not in (1,2): #se crea un bucle que se ejecutara simpre que la opcion no sea ni 1 ni 2 
        print("Opcion no valida, debe ingresar 1 o 2") #indica al usuario que la opcion no es valida 
        opcion = int(input("Ingrese nuevamente una opción: ")) #indica al usuario que ingrese nuevamente una opcion
    
    if (opcion == 1): #si el usuario ingreso la opcion 1 se ingresa el valor manualmente
        print("Seleccionaste la opcion (1), ahora debes ingresar el numero manualmente") 
        numero_apuesta = "" #se crea una cadena vacia 
        for i in range (6): #se crea un bucle para ingresar 6 numeros 
            numero = int(input("Ingrese un numero entre 00 y 45:")) #indica al usuario que ingrese un numero dentro del rango
            while(numero < 0 or numero > 45): #se crea un bucle while que se ejecutara siempre que el numero ingresado este fuera del rango
                numero = int(input("El numero debe ser entre 00 y 45, vuelva a intentarlo: ")) #indica al usuario que ingrese nuevamete el numero
            numero_apuesta += str(numero).zfill(2) #coloca el número a la lista "numero_apuesta" y lo rellena con ceros a la izquierda si es necesario, esto mediante "zfill", tambien se convierte el entero a string
    elif (opcion == 2): #si el usuario ingreso la opcion 1 se genera el valor automaticamente
        print("Seleccionaste la opcion (2), el numero se generara automaticamente")
        print("Espere por favor")
        print("...")
        numero_apuesta = "" #se crea una cadena vacia 
        for i in range (6): 
            numero = random.randint(0,45) #se genera un numero aleatorio entre 0 y 45
            numero_apuesta += str(numero).zfill(2) ##coloca el número a la lista "numero_apuesta" y lo rellena con ceros a la izquierda si es necesario, esto mediante "zfill", tambien se convierte el entero a string. 
        time.sleep(2) #se pausa el programa por 2 segundos
        print("El numero se ha generado correctamente") 

    dinero_apostado = int(input("Ingrese la cifra de dinero que desea apostar: ")) #se solicita al usuario que ingrese la cantidad de dinero que desea apostar 

    fecha_hora = datetime.datetime.now() #se almacena en una variable la fecha y hora actual, para eso se utiliza el medulo presente
    numero_comprobante = random.randint(10000,99999) #se almacena en una variable un numero aleatorio en el rango de 10000 a 99999, este numero lo genera el modulo "random" 

    nombre_archivo = "quiniela_tradicional.txt" #se almacena en una variable el nombre del fichero donde se almacenaran las apuestas de la quiniela
    
    almacenar(nombre_archivo, dni, dinero_apostado, fecha_hora, numero_comprobante, numero_apuesta) #se llama a la funcion "almacenar" para almacenar la informacion de la apuesta
    
    crear_ticket(dni, dinero_apostado, fecha_hora, numero_comprobante, numero_apuesta) #se llama a la funcion "crear_ticket" para crear el ticket con la informacion de la apuesta y mostrarlo en consola. 
    
#Esta funcion permite al usuario verificar si gano la quiniela o el quini 6 ingresando el numero ganador
def comprobar_ganador(): 
    print("Has seleccionado la opcion 'COMPROBAR APUESTA'")
    print("Presione (1) si desea verificar si gano la Quiniela") #indica al usuario que ingrese 1 si desea verificar la quiniela
    print("Presione (2) si desea verificar si gano el Quini 6") #indica al usuario que ingrese 2 si desea verificar el quini 6
    print("Ingrese una opcion:") #indica al usuario que ingrese una de estas dos opciones
    opcion = int(input()) #se almacena en una varible la opcion elegida 
    while opcion not in (1,2): #se crea un bucle while que se ejecutara siempre que la opcion elegida no sea ni 1 ni 2 
        print("Opcion no valida, debe ingresar 1 o 2") #si la opcion no es 1 ni 2 se indica al usuario que la opcion ingresada es invalida
        opcion = int(input("Ingrese nuevamente una opción: ")) #se indica al usuario que ingrese nuevamente una opcion
    
    if(opcion == 1): #si la opcion seleccionada es 1 se indica al usuario que ingrese el numero ganador entre 2 y 4 cifras
        numero_ganador = int(input("Ingrese el numero ganador, recuerde que puede tener 2, 3 o 4 cifras: ")) 
        conversion_numero = str(numero_ganador) #se convierte el numero ganador a cadena, esto para determinar la cantidad de digitos que posee
        cantidad_cifras = len(conversion_numero) #se determina la longitud del numero ganador
        while (cantidad_cifras < 2) or (cantidad_cifras > 4): #se crea un bucle while que se ejecutara siempre que la cantidad de cifras del numero ganador sean menores a 2 o mayores a 4
            print("El numero ganador ingresado no es valido") #si el numero es menor a 2 o mayor a 4 se muestre este mensaje
            numero_ganador = int(input("Ingrese nuevamente el numero ganador: ")) #se indica al usuario que ingre un nuevo numero 
        
        nombre_archivo = "quiniela.txt" #se almacena el nombre del fichero donde se almacenan las apuestas de la quiniela

        try:
            obtener_ganadores = comprobar_apuesta(numero_ganador, cargar(nombre_archivo)) #se llama a la funcion "comprobar_apuesta" y se le pasa como parametro el numero ganador y la funcion "cargar()" junto con el nombre del archivo indicado para obtener las apuestas de la quiniela almacenadas en el fichero "quiniela". El resultado de llamar a la funcion "comprobar_apuesta" se almacena en una lista "obtener_ganadores" que poseera la/las apuesta/as ganadora/as. 

            if not obtener_ganadores: #si no se encontraron apuestas ganadoras, es decir que "obtener_ganadores" esta vacio, se presenta el siguiente mensaje. 
                print("No se encontro ningun ganador")
            else: #si se encontraron ganadores se itera en la lista "obtener_ganadores" y se muestra cada ganador en consola. 
                print("El/los ganadores son:")
                for ganador in obtener_ganadores:
                    print(f"Fecha y hora: {ganador['fecha_hora']}, Comprobante: {ganador['numero_comprobante']}, DNI: {ganador['dni']}, Cifra apostada: ${ganador['cantidad_dinero']}, Numero apostado: {ganador['numero_apostado']}")
        except FileNotFoundError:
            print("No se han encontrado apuestas")
    elif(opcion == 2): #si la opcion es 2 indica al usuario que ingrese el numero ganador
        numero_ganador = int(input("Ingrese el numero ganador: "))
        conversion_numero = str(numero_ganador) #se convierte el numero ganador a cadena, esto para determinar la cantidad de digitos que posee
        cantidad_cifras = len(conversion_numero)  #se determina la longitud del numero ganador
        while (cantidad_cifras != 12): #se crea un bucle for que se ejecutara siempre que la cantidad de cifras del numero ganador sea diferente a 12
            print("El numero ganador ingresado no es valido") #se muestra un mensaje de numero no valido
            numero_ganador = int(int(input("Ingrese nuevamente el numero ganador: "))) #se pide al usuario que ingrese un numero nuevamente

        nombre_archivo = "quiniela_tradicional.txt" ##se almacena el nombre del fichero donde se almacenan las apuestas del quini 6

        try: 
            obtener_ganadores = comprobar_apuesta(numero_ganador, cargar(nombre_archivo)) #se llama a la funcion "comprobar_apuesta" y se le pasa como parametro el numero ganador y la funcion "cargar()" junto con el nombre del archivo indicado para obtener las apuestas del quini 6 almacenadas en el fichero "quiniela_tradicional". El resultado de llamar a la funcion "comprobar_apuesta" se almacena en una lista "obtener_ganadores" que poseera la/las apuesta/as ganadora/as. 

            if not obtener_ganadores: #si no se encontraron apuestas ganadoras, es decir que "obtener_ganadores" esta vacio, se presenta el siguiente mensaje. 
                print("No se encontro ningun ganador") 
            else: #si se encontraron ganadores se itera en la lista "obtener_ganadores" y se muestra cada ganador en consola. 
                print("El/los ganadores son:")
                for ganador in obtener_ganadores:
                    print(f"Fecha y hora: {ganador['fecha_hora']}, Comprobante: {ganador['numero_comprobante']}, DNI: {ganador['dni']}, Cifra apostada: ${ganador['cantidad_dinero']}, Numero apostado: {ganador['numero_apostado']}")
        except FileNotFoundError: 
            print("No se han encontrado apuestas")
#Esta funcion se encarga de calcular de ambas quinielas la cantidad de total de dinero recaudado, la retencion y ganancia neta. 

def arqueo_caja():
    print("Has seleccionado la opcion 'ARQUEO DE CAJA'")

    try:
        apuestas_quiniela = cargar("quiniela.txt") #carga las apuestas almacenadas en el archivo "quiniela"
        apuestas_quini = cargar("quiniela_tradicional.txt") #Carga las apuestas almacenadas en el archivo "quiniela_tradicional"

        total_quiniela = 0 #iniciliza una variable en 0 para almacenar la cantidad de dinero de las apuestas de la quiniela
        total_quini = 0 #iniciliza una variable en 0 para almacenar la cantidad de dinero de las apuestas del quini 6
       
        #se itera en la lista "apuestas_quiniela" para poder obtener la cantidad de dinero de cada apuesta y sumular a la variable "total_quiniela"
        for apuesta in apuestas_quiniela: 
            total_quiniela += int(apuesta["cantidad_dinero"])

        #se itera en la lista "apuestas_quini" para poder obtener la cantidad de dinero de cada apuesta y sumular a la variable "total_quini"
        for apuesta in apuestas_quini:
            total_quini += int(apuesta["cantidad_dinero"])

        total= (total_quiniela + total_quini) #se suma el total del dinero de ambas quinielas 

        retencion = round(0.47 * total, 2) #calcula la retencion y la redondea 
        ganancia_neta = total - retencion #calcula la ganancia neta

        #Se muestran los calculos en consola
        print("La retencion es:", retencion) 
        print("La recaudacion total es: ", total)
        print("La ganacia neta para el quinelero es: ", ganancia_neta) 
    except FileNotFoundError:
        print("No se han encontrado apuestas, por lo tanto no se pueden obtener los calculos correspondientes")

# MENU 

print("-----------------------")
print("*Quiniela 'LA FORTUNA'*")
print("-----------------------")

while True: 
    print("------------------------------")
    print("|Ingrese la opcion que desea:|")
    print("------------------------------")
    print("1. Quiniela")
    print("2. Quini 6")
    print("3. Comprobar apuesta")
    print("4. Arqueo de caja")
    print("5. Salir")
    opcion = int(input()) 
    
    if (opcion == 1):
        quiniela()
    elif (opcion == 2):
        quiniela_tradicional()
    elif(opcion == 3):
        comprobar_ganador()
    elif(opcion == 4):
        arqueo_caja()
    elif(opcion == 5):
        print("Saliendo del sistema")
        break 
