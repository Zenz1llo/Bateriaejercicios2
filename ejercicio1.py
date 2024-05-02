"""
Algoritmo para el cálculo del año bisiesto.
"""

def bisiesto_calc(año):
    es_bisiesto = False
    if año % 4 == 0: # Paso 1
        if año % 100 == 0: # Paso 2
            if año % 400 == 0: # Paso 3
                es_bisiesto = True # Paso 4
        else:
            es_bisiesto = True # Paso 4
    else:
        es_bisiesto = False # Paso 5
    
    return es_bisiesto

if bisiesto_calc(2024):
    print("Print es bisiesto!!")

