def calculo_tarifa(precio, estado_laboral, edad):
    per_tarifa = 100
    if edad < 18 and estado_laboral:
        per_tarifa = 95
    elif edad > 18 and not estado_laboral:
        per_tarifa = 75
    elif edad < 18 and not estado_laboral:
        per_tarifa = 50
    tarifa_final = precio * per_tarifa/100
    return tarifa_final

precio_final = calculo_tarifa(1000, True, 16)
print(precio_final)
