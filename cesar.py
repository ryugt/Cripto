# cesar.py
# -*- coding: utf-8 -*-
# Cifrado Cesar

import re  # Importa el módulo de expresiones regulares

# Función para filtrar el texto, eliminando signos y números pero respetando los espacios
def filtrar_texto(text):
    # Utiliza una expresión regular para reemplazar cualquier carácter que no sea una letra (a-z, A-Z) o un espacio (\s) con una cadena vacía
    return re.sub(r'[^a-zA-Z\s]', '', text)

# Función para encriptar un texto usando el cifrado César
def cesar_encrypt(text, desplazamiento):
    cifrado = ""  # Variable para almacenar el resultado encriptado
    for char in text:  # Itera sobre cada carácter en el texto
        if char.isalpha():  # Verifica si el carácter es una letra
            shift_amount = 65 if char.isupper() else 97  # Determina el valor base (65 para mayúsculas, 97 para minúsculas)
            cifrado += chr((ord(char) + desplazamiento - shift_amount) % 26 + shift_amount)
        else:
            cifrado += char  # Si no es una letra, añade el carácter original al resultado
    return cifrado  # Devuelve el texto encriptado

# Función para desencriptar un texto usando el cifrado César
def cesar_decrypt(text, desplazamiento):
    return cesar_encrypt(text, -desplazamiento)  # Llama a la función de encriptar con el desplazamiento negativo
