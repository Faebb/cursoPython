import calculadora_indices as calc

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
edad = int(input("Ingrese su edad: "))
genero = input("Ingrese su género (hombre/mujer): ").lower()

if genero == "hombre":
    valor_genero = 5
elif genero == "mujer":
    valor_genero = -161
else:
    print("Género no reconocido.")
    
resultado = calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)
print(resultado)