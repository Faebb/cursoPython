import calculadora_indices as calc

def obtener_valor_genero(genero):
    if genero == "hombre":
        return 5
    elif genero == "mujer":
        return -161
    else:
        print("Género no reconocido.")
        exit()

def obtener_valor_actividad(opcion_actividad):
    opciones = {
        "1.2": 1.2,
        "1.375": 1.375,
        "1.55": 1.55,
        "1.725": 1.725,
        "1.9": 1.9
    }
    valor_actividad = opciones.get(opcion_actividad)
    if valor_actividad is None:
        print("Opción de actividad no válida.")
        exit()
    return valor_actividad


peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
edad = int(input("Ingrese su edad: "))
genero = input("Ingrese su género (hombre/mujer): ").lower()

valor_genero = obtener_valor_genero(genero)

print("Opciones para valor de actividad:")
print("1.2: poco o ningún ejercicio")
print("1.375: ejercicio ligero (1 a 3 días a la semana)")
print("1.55: ejercicio moderado (3 a 5 días a la semana)")
print("1.725: deportista (6 -7 días a la semana)")
print("1.9: atleta (entrenamientos mañana y tarde)")

opcion_actividad = input("Ingrese el valor de actividad correspondiente: ")
valor_actividad = obtener_valor_actividad(opcion_actividad)

resultado = calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)
print(resultado)
