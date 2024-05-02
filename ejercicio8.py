# Declaramos un diccionario vacio
lista_de_la_compra = {}

while True:
    articulo = input("Que vas a comprar?" \
                    "(Para terminar introducir FIN)")
    if articulo == "FIN":
        break
    precio = float(input("Que precio tiene?"))
    n_unidades = int(input("Cuantas unidades?"))
    lista_de_la_compra[articulo] = [precio, n_unidades]

precio_final = 0.0
for articulo in lista_de_la_compra:
    item = lista_de_la_compra[articulo]
    precio_producto = item[0] * item[1]
    precio_final += precio_producto

print("El precio total de la compra es:", round(precio_final, 2))
