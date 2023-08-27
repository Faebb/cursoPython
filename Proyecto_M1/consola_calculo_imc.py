import calculadora_indices as calc

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
    
resultado = calc.calcular_IMC(peso, altura)
print(resultado)