# List Comprehension
# Listas avanzadas en 1 linea de código:
# lista=[ expresion for elemento in iterable]

# Método Tradicional
# lista = []
# for numero in range (0,11):
#     lista.append(numero**2)
# print (lista)
#
# # Con conprensión de Listas
# lista = [numero**2 for numero in range(0,11)]
# print (lsita)



# Lambda
# Funciones Anónimas
# def doblar(num):
#     resultado = num * 2
#     return resultado
#
# doblar(2)

# def doblar(num):
#     return num*2
#
# lambda num: num*2

doblar = lambda num: num*2

doblar(2)
