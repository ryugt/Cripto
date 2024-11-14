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
            # Calcula el nuevo carácter encriptado y lo añade al resultado
            # 1. Convierte el carácter a su valor ASCII con ord(char).
            # 2. Suma el desplazamiento (desplazamiento) al valor ASCII del carácter.
            # 3. Resta el valor base (65 para mayúsculas, 97 para minúsculas) para normalizar el rango.
            # 4. Aplica el módulo 26 para asegurar que el resultado esté dentro del rango del alfabeto.
            # 5. Suma el valor base nuevamente para obtener el valor ASCII del nuevo carácter.
            # 6. Convierte el valor ASCII de vuelta a un carácter con chr().
            cifrado += chr((ord(char) + desplazamiento - shift_amount) % 26 + shift_amount)
        else:
            cifrado += char  # Si no es una letra, añade el carácter original al resultado
    return cifrado  # Devuelve el texto encriptado

# Función para desencriptar un texto usando el cifrado César
def cesar_decrypt(text, desplazamiento):
    return cesar_encrypt(text, -desplazamiento)  # Llama a la función de encriptar con el desplazamiento negativo

# Punto de entrada del programa
if __name__ == "__main__":
    text = input("Ingrese el texto a encriptar: ")  # Solicita al usuario el texto a encriptar
    text = filtrar_texto(text)  # Filtra el texto para eliminar signos y números pero respetando los espacios
    desplazamiento = int(input("Ingrese el desplazamiento para el cifrado: "))  # Solicita al usuario el desplazamiento para el cifrado
    encrypted_text = cesar_encrypt(text, desplazamiento)  # Encripta el texto
    print(f"Texto encriptado: {encrypted_text}")  # Imprime el texto encriptado
    #decrypted_text = cesar_decrypt(encrypted_text, desplazamiento)  # Desencripta el texto
    #print(f"Texto desencriptado: {decrypted_text}")  # Imprime el texto desencriptado