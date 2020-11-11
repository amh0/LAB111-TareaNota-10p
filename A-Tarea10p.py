
# usuario = admin
# password = tareaLab-amh0

# [OPCIONAL]: la funcion de encriptacion NO es inyectiva porque el password 
# - 'MAPA' se encripta a 'HuLv' entonces en este caso 'A' se encriptó a 'u' y 'v' , 
# - 'TAPA' se encripta a 'PvMw' 'A' se encripta a 'v' y 'w'
# entonces un mismo elemento puede encriptarse a elementos diferentes
# dependiendo de los demas componentes del password
# Ya que la funcion de encriptacion NO es inyectiva entonces NO es biyectiva

####################### Inicio de Sesion ##################################
def encrypt(password):
    conjunto = 'abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWYZ0123456789 .,-'
    encryptPassword = ''
    despl = -5
    for elemento in password:
        posicion = conjunto.find(elemento)
        if posicion%2 == 0:
            despl -= 1
        nuevaPosicion = posicion + despl 
        encryptPassword += conjunto[nuevaPosicion]
    return encryptPassword 

def inicioSesion(verificacion):
    while verificacion != True:
        print('╔═════════════════════════════════════════╗')
        print('║            Inicio de Sesion             ║')
        print('╠═════════════════════════════════════════╣')
        print('║       Ingrese usuario y contraseña      ║')
        print('╚═════════════════════════════════════════╝')

        usuario = input('\tUsuario: ')
        password = input('\tContraseña: ')
        password = encrypt(password)
        if usuario == usuarioA and password == passwordA:
            verificacion = True
            print('\t*Sesion iniciada*')
        else:
            print('\t*Datos incorrectos*\n')
    return verificacion
#######################################################################
################## Funciones auxiliares ###################
def divisionAux(a,b):
    cociente = int(a*(b**-1))
    resto = a-(cociente*b)
    return cociente,resto

def hexEquiv(dec):
    if dec > 9:
        if dec == 10:
            dec = 'A'
        elif dec == 11:
            dec = 'B'
        elif dec == 12:
            dec = 'C'
        elif dec == 13:
            dec = 'D'
        elif dec == 14:
            dec = 'E'
        elif dec == 15:
            dec = 'F'
    return dec

##############################################################
################# Funciones principales ######################
def menu():
    opcion = 1
    while opcion != 5:
        print('\n╔═════════════════════════════════════════╗')
        print('║                 MENU                    ║')
        print('╠═════════════════════════════════════════╣')
        print('║\t1. Division de dos numeros        ║')
        print('║\t2. Divisores                      ║')
        print('║\t3. Numeros Capicua                ║')
        print('║\t4. Cambio de base                 ║')
        print('║\t5. Salir                          ║')
        print('╚═════════════════════════════════════════╝')
        opcion = int(input('\tElija una opcion: '))
        if opcion == 1:
            print('\t*Usted eligio la operacion 1*\n')
            division()
        elif opcion == 2:
            print('\t*Usted eligio la operacion 2*\n')
            divisores()
        elif opcion == 3:
            print('\t*Usted eligio la operacion 3*\n')
            capicua()
        elif opcion == 4:
            print('\t*Usted eligio la operacion 4*\n')
            cambioDeBase()
        elif opcion == 5:
            print('\t*Usted eligio salir del programa*\n')
            print('╔═════════════════════════════════════════╗')
            print('║\t     Fin del programa             ║')
            print('╚═════════════════════════════════════════╝')

def division():
    print('╔═════════════════════════════════════════╗')
    print('║\t1. Division de 2 Numeros: a/b     ║')
    print('╚═════════════════════════════════════════╝')

    a = int(input('\tIngrese a (dividendo): ')) 
    b = int(input('\tIngrese b (divisor)  : ')) 
    nuevoA, nuevoB = a, b
    cont, a = divisionAux(a,b)
    print('\tResultados:\n')
    print('\t%d dividido a %d es ='%(nuevoA,nuevoB),cont)
    print('\t%d modulo %d es ='%(nuevoA,nuevoB),a)
    print('\n\t*Fin de la operacion*')

def divisores(): 
    print('╔═════════════════════════════════════════╗')
    print('║\t2. Divisores de un numero:        ║')
    print('╚═════════════════════════════════════════╝')

    num = int(input('   Ingrese numero mayor a 99999999999999\n   (mas de 14 digitos): '))
    if num > 99999999999999:
        cont = 1
        print('\tLos divisores son:\n')
        while cont <= num**0.5: 
            cociente, resto = divisionAux(num,cont)
            if (resto == 0):    
                if (cociente != cont): 
                    print('\t%d\t\t%d'%(cont,cociente)) 
                else: 
                    print('\t%d'%(cont))
            cont += 1
    else:
        print('\t*Numero invalido*')
    print('\n\t*Fin de la operacion*')

def capicua():
    print('╔═════════════════════════════════════════╗')
    print('║\t3. Numeros Capicua                ║')
    print('╚═════════════════════════════════════════╝')

    num = input('\tIngrese numero mayor a 99999999: ')
    if int(num) > 99999999:
        size = len(num)
        print('\tResultados:\n')
        for index in range(size):
            if index <= size-3 and num[index] == num[index+2]:
                print('\tEl numero: %s%s%s Es capicua'%(num[index],num[index+1],num[index+2]))
            index += 1
    else:
        print('\t*Numero invalido*')
    print('\n\t*Fin de la operacion*')

def cambioDeBase():
    print('╔═════════════════════════════════════════╗')
    print('║\t4. Cambio de base de un numero    ║')
    print('╚═════════════════════════════════════════╝')

    num = int(input('\tIngrese numero: '))
    base = int(input('\tIngrese base (2 a 16): '))
    nuevoNum = ''
    if num > -1 and 1 < base < 17 :
        while num >= base:
            cocienteCDB, restoCDB = divisionAux(num,base)
            if restoCDB > 9:
                restoCDB = hexEquiv(restoCDB)
            nuevoNum = str(restoCDB) + nuevoNum 
            num = cocienteCDB
        nuevoNum = str(hexEquiv(num)) + nuevoNum  
        print('\tResultado:\n')
        print('\tNumero en base %d: '%(base)+ nuevoNum)
    else: 
        print('Valores invalidos')
    print('\n\t*Fin de la operacion*')
#######################################################
############## Programa principal #######################

usuarioA = 'admin'
passwordA = 'o8l.6C4533a9M'

verificacion = False
valorVerif = inicioSesion(verificacion)
if valorVerif != False:
    menu()
