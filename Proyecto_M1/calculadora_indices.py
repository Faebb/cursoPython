# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 13:30:59 2023

@author: Faeb2
"""

def calcular_IMC(peso:float, altura:float)->str:
    imc = (peso / altura ** 2)
    imc = round(imc, 2)
    
    return str(imc)


def calcular_porcentaje_grasa(peso:float, altura:float, edad:int, valor_genero:float)->str:
    imc = (peso / altura ** 2)
    imc = round(imc, 2)
    porcentaje_grasa = (1.2 * imc) + (0.23 * edad) - valor_genero - 5.4
    porcentaje_grasa = round(porcentaje_grasa,2)
    return str(porcentaje_grasa)+"%"
    
def calcular_calorias_en_reposo(peso:float, altura:float, edad:int, valor_genero:int)->str:
    altura_cm = altura * 100
    tmb = (10 * peso)+(6.25 * altura_cm)-(5 * edad) + valor_genero
    return str(tmb)+" cal"
    
def calcular_calorias_en_actividad(peso:float, altura:float, edad:int, valor_genero:float, valor_actividad:float)->None:
    altura_cm = altura * 100
    tmb = (10 * peso)+(6.25 * altura_cm)-(5 * edad) + valor_genero
    tmba = tmb * valor_actividad
    return str(tmba)+" cal"
    
def consumo_calorias_recomendado_para_adelgazar(peso:float, altura:float, edad:int, valor_genero:float):
    altura_cm = altura * 100
    tmb = (10 * peso)+(6.25 * altura_cm)-(5 * edad) + valor_genero
    tmb_para_adelgazar2 = tmb - (0.15 * tmb) 
    tmb_para_adelgazar1 = tmb - (0.20 * tmb)
    tmb_para_adelgazar1 = round(tmb_para_adelgazar1,2)
    tmb_para_adelgazar2 = round(tmb_para_adelgazar2,2)
    return "Para adelgazar es recomendado que consumas entre: "+str(tmb_para_adelgazar1)+" y "+str(tmb_para_adelgazar2)+" calorías al día."
    
    