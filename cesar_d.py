# cesar_des.py
# -*- coding: utf-8 -*-
# Desencriptado Cesar

def desincriptar_cesar(texto_cifrado, desplazamiento):
    texto_descifrado = ""
    for caracter in texto_cifrado:
        if caracter.isalpha():  # Verifica si es una letra
            desplazamiento_real = desplazamiento % 26
            if caracter.islower():
                texto_descifrado += chr((ord(caracter) - desplazamiento_real - 97) % 26 + 97)
            else:
                texto_descifrado += chr((ord(caracter) - desplazamiento_real - 65) % 26 + 65)
        else:
            texto_descifrado += caracter
    return texto_descifrado

def calcular_frecuencia(texto):
    frecuencia = {}
    total_letras = 0
    for caracter in texto:
        if caracter.isalpha():
            total_letras += 1
            if caracter in frecuencia:
                frecuencia[caracter] += 1
            else:
                frecuencia[caracter] = 1
    for caracter in frecuencia:
        frecuencia[caracter] /= total_letras
    return frecuencia

def encontrar_desplazamiento_mas_probable(texto_cifrado):
    # Frecuencia esperada de las letras en inglés
    frecuencia_ingles = {
        'A': 0.08167, 'B': 0.01492, 'C': 0.02782, 'D': 0.04253, 'E': 0.12702,
        'F': 0.02228, 'G': 0.02015, 'H': 0.06094, 'I': 0.06966, 'J': 0.00153,
        'K': 0.00772, 'L': 0.04025, 'M': 0.02406, 'N': 0.06749, 'O': 0.07507,
        'P': 0.01929, 'Q': 0.00095, 'R': 0.05987, 'S': 0.06327, 'T': 0.09056,
        'U': 0.02758, 'V': 0.00978, 'W': 0.02360, 'X': 0.00150, 'Y': 0.01974,
        'Z': 0.00074
    }
    
    frecuencia_cifrado = calcular_frecuencia(texto_cifrado)
    mejor_desplazamiento = 0
    menor_diferencia = float('inf')
    
    for desplazamiento in range(26):
        diferencia_total = 0
        for letra in frecuencia_ingles:
            letra_desplazada = chr((ord(letra) - 65 + desplazamiento) % 26 + 65)
            frecuencia_observada = frecuencia_cifrado.get(letra_desplazada, 0)
            diferencia_total += abs(frecuencia_ingles[letra] - frecuencia_observada)
        
        if diferencia_total < menor_diferencia:
            menor_diferencia = diferencia_total
            mejor_desplazamiento = desplazamiento
    
    return mejor_desplazamiento