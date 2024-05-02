import string

# Obtenemos las letras del abecedario
palabra = "Espantapajaros"
abecedario = string.ascii_letters[:26]

# Declaramos un diccionario vacio y lo pupulamos
dict_letra_a_entero = dict()
for n in range(len(abecedario)):
    dict_letra_a_entero[abecedario[n]] = n
 
# Con este diccionario se implementa de forma sencilla la lógica del programaç
for letra in palabra:
    pos_abcedario = dict_letra_a_entero[letra.lower()]
    print("%s (%s) " % (letra, pos_abcedario)) 


dict_letra_a_entero.
