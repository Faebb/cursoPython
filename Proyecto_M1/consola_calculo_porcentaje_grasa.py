import calculadora_indices as calc

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
edad = int(input("Ingrese su edad: "))
genero = input("Ingrese su género (hombre/mujer): ").lower()
    
if genero == "hombre":
    valor_genero = 10.8
elif genero == "mujer":
    valor_genero = 0
else:
    print("Género no reconocido.")

resultado = calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
print(resultado)