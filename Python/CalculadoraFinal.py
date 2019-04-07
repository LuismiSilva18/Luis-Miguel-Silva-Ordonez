#!/usr/bin/env python
# -*- coding: utf-8 -*-

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 // num2

def exponencial(num1, num2):
    return num1 ** num2

def seguir():
    print("¿Quieres seguir utilizando la calculadora?")
    print(" *Presione 1 -> SI ")
    print(" *Presione 2 -> NO ")
    elec = input()
    if elec == '1':
        calculadora()
    elif elec == '2':
        print("Gracias por usar nuestra calculadora")
    else:
        print("No valido")

def calculadora():
    print(".................................")
    print("Introduce el primer Número:")
    try:
        num1 = float(input())
    except:
        print("No válido")
        return
    print("Introduce el Segundo Número: ")
    try:
        num2 = float(input())
    except:
        print("No válido")
        return
    print( "¿Que operación quiere hacer?" )
    print(" *Presione 1 para Suma ")
    print(" *Presione 2 para Resta ")
    print(" *Presione 3 para Multiplicación ")
    print(" *Presione 4 para División ")
    print(" *Presione 5 para Exponencial ")
    print("**********************************")
    elec = input()
    if elec == '1':
        print("La suma total es: " + str(suma(num1, num2)))
    elif elec == '2':
        print("La resta Total es: " + str(resta(num1, num2)))
    elif elec == '3':
        print("La multriplicación es: " + str(multiplicacion(num1, num2)))
    elif elec == '4':
        print("El resultado de la division es: " + str(division(num1, num2)))
    elif elec == '5':
        print("El resultado exponencial es: " + str(exponencial(num1, num2)))
    else:
        print("No valido")
    print("**********************************")
    seguir()

calculadora()


