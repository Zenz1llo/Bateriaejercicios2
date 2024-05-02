
asignaturas_dict = {"Matemáticas": None,
                "Física": None, 
                "Química": None, 
                "Historia": None,
                "Lengua": None}

for key in asignaturas_dict:
    nota = input(f"Que nota has sacado en {key}?\n")
    asignaturas_dict[key] = nota


print(asignaturas_dict)
