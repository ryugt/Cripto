from collections import Counter
import math
from cesar import filtrar_texto, cesar_decrypt
from cesar_des import encontrar_desplazamiento_mas_probable, calcular_frecuencia


def calcular_indice_coincidencia(texto):
    frecuencia = calcular_frecuencia(texto)
    n = len(texto)
    if n <= 1:
        return 0  # Evita la división por cero
    indice_coincidencia = sum(f * (f - 1) for f in frecuencia.values()) / (n * (n - 1))
    return indice_coincidencia

def encontrar_longitud_clave(texto_cifrado):
    IC = []
    texto_cifrado = texto_cifrado.replace(" ", "")  # Elimina los espacios del texto cifrado
    max_longitud = len(texto_cifrado)  # Longitud máxima basada en el texto cifrado

    for longitud in range(1, max_longitud + 1):  # Probar longitudes de clave de 1 a la longitud del texto cifrado
        indice_suma = 0
        #segmentos = [''.join(texto_cifrado[i::longitud]) for i in range(longitud)]
        for i in range(longitud):
            segmento = texto_cifrado[i::longitud]
            print(f"Segmento {i}: {segmento}")  # Debug: Imprime el segmento actual
            indice_suma += calcular_indice_coincidencia(segmento)
        print(f"Segmento: {segmento}, longitud: {longitud}")  # Debug: Imprime los segmentos
        #indice_suma += calcular_indice_coincidencia(segmentos)
        print(f"Índice Suma: {indice_suma}")  # Debug: Imprime el índice de coincidencia
        indice_promedio = indice_suma / longitud
        print(f"Índice Promedio: {indice_promedio}")
        IC.append((longitud, indice_promedio))

    IC.sort(key=lambda x: abs(x[1] - 0.068))
    print(f"IC: {IC}")
        #diferencia = abs(indice_promedio - indice_ingles)
        #if diferencia < menor_diferencia:
        #    menor_diferencia = diferencia
        #    mejor_longitud = longitud
        #print(f"Longitud: {longitud}, Índice Promedio: {indice_promedio}, Diferencia: {diferencia}")  # Debug: Imprime la longitud, el índice promedio y la diferencia
    return IC[0][0]

def encontrar_clave(texto_cifrado, longitud_clave):
    clave = ""
    texto_cifrado = texto_cifrado.replace(" ", "")  # Elimina los espacios del texto cifrado
    for i in range(longitud_clave):
        segmento = ''.join(texto_cifrado[j] for j in range(i, len(texto_cifrado), longitud_clave))
        print(f"Segmento {i}: {segmento}")  # Debug: Imprime el segmento actual
        desplazamiento = encontrar_desplazamiento_mas_probable(segmento)
        print(f"Desplazamiento {i}: {desplazamiento}")  # Debug: Imprime el desplazamiento encontrado
        clave += chr(desplazamiento + 65)
    return clave

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
    longitud_clave = encontrar_longitud_clave(text)  # Encuentra la longitud de la clave
    print(f"Longitud de la clave: {longitud_clave}")  # Debug: Imprime la longitud de la clave encontrada
    key = encontrar_clave(text, longitud_clave)  # Encuentra la clave usando análisis de frecuencia
    print(f"Clave encontrada: {key}")  # Debug: Imprime la clave encontrada
    decrypted_text = vigenere_decrypt(text, key)  # Desencripta el texto usando la clave encontrada
    print(f"Texto desencriptado: {decrypted_text}")  # Imprime el texto desencriptado