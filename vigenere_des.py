# vigenere_des.py
# -*- coding: utf-8 -*-
# Desencriptado Vigenere

from collections import Counter
import math
from cesar import filtrar_texto, cesar_decrypt
from cesar_des import encontrar_desplazamiento_mas_probable, calcular_frecuencia

def calcular_indice_coincidencia(texto):
    frecuencia = calcular_frecuencia(texto)  # Calcula la frecuencia de cada letra en el texto
    n = len(texto)  # Obtiene la longitud del texto
    if n <= 1:
        return 0  # Evita la división por cero si el texto tiene una longitud de 1 o menos
    # Calcula el índice de coincidencia
    indice_coincidencia = sum(f * (f - 1) for f in frecuencia.values()) / (n * (n - 1))
    return indice_coincidencia  # Devuelve el índice de coincidencia

def encontrar_longitud_clave_kasiski(texto_cifrado):
    texto_cifrado = texto_cifrado.replace(" ", "")  # Elimina los espacios del texto cifrado
    secuencias = {}  # Diccionario para almacenar las secuencias y sus posiciones
    for i in range(len(texto_cifrado) - 2):
        secuencia = texto_cifrado[i:i + 3]  # Obtiene una secuencia de 3 caracteres
        print(f"Secuencia: {secuencia}, Posición: {i}")  # Debug: Imprime la secuencia y su posición

        if secuencia in secuencias:
            secuencias[secuencia].append(i)  # Añade la posición de la secuencia al diccionario
        else:
            secuencias[secuencia] = [i]  # Crea una nueva entrada en el diccionario para la secuencia
    #print(secuencias)  # Debug: Imprime las secuencias y sus posiciones
    distancias = []  # Lista para almacenar las distancias entre las posiciones de las secuencias repetidas
    
    for secuencia, posiciones in secuencias.items():
        if len(posiciones) > 1:  # Si la secuencia se repite
            for i in range(len(posiciones) - 1):
                distancias.append(posiciones[i + 1] - posiciones[i])  # Calcula la distancia entre las posiciones
                print(f"Secuencia: {secuencia}, Distancia: {distancias[-1]}")  # Debug: Imprime la secuencia y la distancia
    if not distancias:
        return 1  # Si no se encuentran repeticiones, se asume una longitud de clave de 1

    factores = Counter()  # Contador para almacenar los factores de las distancias
    for distancia in distancias:
        for i in range(2, distancia + 1):
            if distancia % i == 0:  # Si i es un factor de la distancia
                factores[i] += 1  # Incrementa el contador para el factor

    mejor_longitud = factores.most_common(1)[0][0]  # Obtiene el factor más común como la mejor longitud de clave
    return mejor_longitud  # Devuelve la mejor longitud de clave

def encontrar_clave(texto_cifrado, longitud_clave):
    clave = ""
    for i in range(longitud_clave):
        segmento = ''.join(texto_cifrado[j] for j in range(i, len(texto_cifrado), longitud_clave))  # Crea un segmento del texto cifrado
        desplazamiento = encontrar_desplazamiento_mas_probable(segmento)  # Encuentra el desplazamiento más probable para el segmento
        clave += chr(desplazamiento + 65)  # Convierte el desplazamiento a una letra y la añade a la clave
    return clave  # Devuelve la clave

def vigenere_decrypt(text, key):
    text = text.upper()
    key = key.upper()
    descifrado = ""  # Variable para almacenar el resultado desencriptado
    key_index = 0
    key_length = len(key)
    
    for char in text:  # Itera sobre cada carácter en el texto
        if char.isalpha():  # Verifica si el carácter es una letra
            desplazamiento = ord(key[key_index % key_length]) - 65  # Calcula el desplazamiento basado en la clave
            descifrado += cesar_decrypt(char, desplazamiento)  # Usa la función cesar_decrypt para desencriptar el carácter
            key_index += 1
        else:
            descifrado += char  # Si no es una letra, añade el carácter original al resultado
    return descifrado  # Devuelve el texto desencriptado

# Punto de entrada del programa
if __name__ == "__main__":
    text = input("Ingrese el texto a desencriptar: ").upper()  # Solicita al usuario el texto a desencriptar y lo convierte a mayúsculas
    text = filtrar_texto(text)  # Filtra el texto para eliminar signos y números pero respetando los espacios
    print(f"Texto filtrado: {text}")  # Debug: Imprime el texto filtrado
    longitud_clave = encontrar_longitud_clave_kasiski(text)  # Encuentra la longitud de la clave usando el método Kasiski
    print(f"Longitud de la clave: {longitud_clave}")  # Debug: Imprime la longitud de la clave encontrada
    key = encontrar_clave(text, longitud_clave)  # Encuentra la clave usando análisis de frecuencia
    print(f"Clave encontrada: {key}")  # Debug: Imprime la clave encontrada
    decrypted_text = vigenere_decrypt(text, key)  # Desencripta el texto usando la clave encontrada
    print(f"Texto desencriptado: {decrypted_text}")  # Imprime el texto desencriptado