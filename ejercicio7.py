dict_prec_frut = {"platano": 1.35,
                    "manzana": 0.80,
                    "pera":0.85,
                    "naranja": 0.70}

fruta_key = input("Que fruta vas a comprar?").lower()
n_kilos = float(input("Cuántos kilos quieres?"))

try:
    precio_final = n_kilos * dict_prec_frut[fruta_key]

    print("En total vas a pagar: ", precio_final)
except KeyError:
    print(f"Los sentimos pero no tenemos {fruta_key} en stock")
