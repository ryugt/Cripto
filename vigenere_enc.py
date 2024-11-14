# vigenere.py
# -*- coding: utf-8 -*-
# Cifrado Vigenere

from cesar import filtrar_texto, cesar_encrypt, cesar_decrypt

# Función para encriptar un texto usando el cifrado Vigenère
def vigenere_encrypt(text, key):
    text = text.upper()
    key = key.upper()
    cifrado = ""  # Variable para almacenar el resultado encriptado
    key_index = 0
    key_length = len(key)
    
    for char in text:  # Itera sobre cada carácter en el texto
        if char.isalpha():  # Verifica si el carácter es una letra
            desplazamiento = ord(key[key_index % key_length]) - 65  # Calcula el desplazamiento basado en la clave
            cifrado += cesar_encrypt(char, desplazamiento)  # Usa la función cesar_encrypt para encriptar el carácter
            key_index += 1
        else:
            cifrado += char  # Si no es una letra, añade el carácter original al resultado
    return cifrado  # Devuelve el texto encriptado

# Función para desencriptar un texto usando el cifrado Vigenère
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
    text = input("Ingrese el texto a encriptar: ")  # Solicita al usuario el texto a encriptar
    text = filtrar_texto(text)  # Filtra el texto para eliminar signos y números pero respetando los espacios
    key = input("Ingrese la clave para el cifrado: ")  # Solicita al usuario la clave para el cifrado
    encrypted_text = vigenere_encrypt(text, key)  # Encripta el texto
    print(f"Texto encriptado: {encrypted_text}")  # Imprime el texto encriptado
    decrypted_text = vigenere_decrypt(encrypted_text, key)  # Desencripta el texto
    print(f"Texto desencriptado: {decrypted_text}")  # Imprime el texto desencriptado