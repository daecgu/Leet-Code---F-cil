"""Crea un programa de Python que muestre en consola las siguientes frases ordenadas de mayor
a menor en función del número de palabras que forma cada frase, utilizando funciones lambda.

Frases para ordenar:

Los lunes son los mejores días para programar
Python es moderno
Veremos Inteligencia Artificial más adelante
Lambda simplifica el código"""

frases = ["Los lunes son los mejores días para programar", "Python es moderno", "Veremos Inteligencia Artificial más adelante", "Lambda simplifica el código"]

def ordenar(f):
    return (len(f.split()))

frases.sort(key = ordenar, reverse=True)


print(frases)

#frases.sort(key = lambda f: len(f.split()), reverse = True)

