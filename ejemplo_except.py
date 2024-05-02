
# Error
def func_dividir(a, b):
    try:
        resultado = a/b
    except ZeroDivisionError:
        resultado = 10 ** 20
    return resultado

print(func_dividir(10, 0))

