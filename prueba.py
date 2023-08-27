"""
def funcion_1()->str:
    return "Hola mi amigo "

def funcion_2(palabra:str)->str:
    return funcion_1()+(palabra)


resultado = (funcion_2("Juan"))
print("El resultado de mi funcion es: "+resultado)
"""
"""
def calcular_IMC (peso: float, altura: float)->float:
    imc = peso/((altura)**2)
    return imc
#PROGRAMA PRINCIPAL
peso = input("Digite su peso en kilogramos: ") 
estatura = input("Digite su estatura en metros: ") 
indice = calcular_IMC(float (peso), float(estatura)) 
print("Su índice de masa corporal es: ", indice)
"""
"""
def calcular_IMC (peso: float, altura: float)->float:
    imc = peso/((altura)**2)
    return imc
#PROGRAMA PRINCIPAL
peso = float(input("Digite su peso en kilogramos: "))
estatura = float (input("Digite su estatura en metros: "))
print("Su índice de masa corporal es: ", round (calcular_IMC (peso, estatura), 2))
"""
"""
import math

def velocidad_en_caida_libre(altura):
    velocidad_inicial = 0  # Velocidad inicial en caída libre
    aceleracion_gravedad = 9.8  # Aceleración debido a la gravedad

    # Cálculo de la velocidad final
    velocidad_final = math.sqrt(velocidad_inicial**2 + 2 * aceleracion_gravedad * altura)

    return round(velocidad_final, 2)  # Redondear a dos decimales

# Solicitar la altura al usuario
altura = float(input("Ingrese la altura a la que se soltó el objeto (metros): "))

# Calcular la velocidad y mostrar el resultado
velocidad = velocidad_en_caida_libre(altura)
print(f"La velocidad al tocar el suelo es de {velocidad} m/s")"""

def calcular_edad(dia_nacimiento, mes_nacimiento, year_nacimiento, dia_actual, mes_actual, year_actual):
    edad_anios = year_actual - year_nacimiento
    edad_meses = mes_actual - mes_nacimiento
    edad_dias = dia_actual - dia_nacimiento

    if edad_dias < 0:
        edad_meses -= 1
        edad_dias += 30

    if edad_meses < 0:
        edad_anios -= 1
        edad_meses += 12

    return edad_anios, edad_meses, edad_dias

# Ejemplo de uso
dia_nacimiento = 20
mes_nacimiento = 11
year_nacimiento = 1986
dia_actual = 16
mes_actual = 10
year_actual = 1987

edad_anios, edad_meses, edad_dias = calcular_edad(dia_nacimiento, mes_nacimiento, year_nacimiento, dia_actual, mes_actual, year_actual)
print("La edad es: " + str(edad_anios) + " años, " + str(edad_meses) + " meses y " + str(edad_dias) + " días")

