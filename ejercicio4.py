count = 0
lista_de_numeros = []
while count < 10:
    numero = int(input("Ingrese un número: "))
    lista_de_numeros.append(numero)
    count += 1

print(sum(lista_de_numeros))
print(sum(lista_de_numeros) / len(lista_de_numeros))
print(max(lista_de_numeros))
print(min(lista_de_numeros))

