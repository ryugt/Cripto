# -*- coding: utf-8 -*-
# Desencriptado Cesar

# Función para desencriptar un texto usando el cifrado César
def desincriptar_cesar(texto_cifrado, desplazamiento):
    texto_descifrado = ""  # Variable para almacenar el resultado desencriptado
    for caracter in texto_cifrado:  # Itera sobre cada carácter en el texto cifrado
        if caracter.isalpha():  # Verifica si es una letra
            desplazamiento_real = desplazamiento % 26  # Asegura que el desplazamiento esté en el rango de 0 a 25
            if caracter.islower():  # Verifica si la letra es minúscula
                # Calcula el nuevo carácter desencriptado y lo añade al resultado
                texto_descifrado += chr((ord(caracter) - desplazamiento_real - 97) % 26 + 97)
            else:  # Si la letra es mayúscula
                # Calcula el nuevo carácter desencriptado y lo añade al resultado
                texto_descifrado += chr((ord(caracter) - desplazamiento_real - 65) % 26 + 65)
        else:
            texto_descifrado += caracter  # Si no es una letra, añade el carácter original al resultado
    return texto_descifrado  # Devuelve el texto desencriptado

# Función para calcular la frecuencia de cada letra en el texto
def calcular_frecuencia(texto):
    frecuencia = {}  # Diccionario para almacenar la frecuencia de cada letra
    total_letras = 0  # Contador para el total de letras en el texto
    for caracter in texto:  # Itera sobre cada carácter en el texto
        if caracter.isalpha():  # Verifica si es una letra
            total_letras += 1  # Incrementa el contador de letras
            if caracter in frecuencia:  # Si la letra ya está en el diccionario
                frecuencia[caracter] += 1  # Incrementa su frecuencia
            else:
                frecuencia[caracter] = 1  # Añade la letra al diccionario con frecuencia 1
    for caracter in frecuencia:  # Normaliza las frecuencias dividiendo por el total de letras
        frecuencia[caracter] /= total_letras
    return frecuencia  # Devuelve el diccionario de frecuencias

# Función para encontrar el desplazamiento más probable usando análisis de frecuencia
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
    
    frecuencia_cifrado = calcular_frecuencia(texto_cifrado)  # Calcula la frecuencia de las letras en el texto cifrado
    mejor_desplazamiento = 0  # Variable para almacenar el mejor desplazamiento encontrado
    menor_diferencia = float('inf')  # Inicializa la menor diferencia como infinito
    
    for desplazamiento in range(26):  # Prueba todos los posibles desplazamientos (0 a 25)
        diferencia_total = 0  # Variable para almacenar la diferencia total para el desplazamiento actual
        for letra in frecuencia_ingles:  # Itera sobre cada letra en la frecuencia esperada
            letra_desplazada = chr((ord(letra) - 65 + desplazamiento) % 26 + 65)  # Calcula la letra desplazada
            frecuencia_observada = frecuencia_cifrado.get(letra_desplazada, 0)  # Obtiene la frecuencia observada de la letra desplazada
            diferencia_total += abs(frecuencia_ingles[letra] - frecuencia_observada)  # Suma la diferencia absoluta a la diferencia total
        
        if diferencia_total < menor_diferencia:  # Si la diferencia total es menor que la menor diferencia encontrada
            menor_diferencia = diferencia_total  # Actualiza la menor diferencia
            mejor_desplazamiento = desplazamiento  # Actualiza el mejor desplazamiento
    
    return mejor_desplazamiento  # Devuelve el mejor desplazamiento encontrado

# Punto de entrada del programa
if __name__ == "__main__":
    texto_cifrado = input("Ingrese el texto cifrado: ").upper()  # Solicita al usuario el texto cifrado y lo convierte a mayúsculas
    desplazamiento = encontrar_desplazamiento_mas_probable(texto_cifrado)  # Calcula el desplazamiento más probable
    texto_descifrado = desincriptar_cesar(texto_cifrado, desplazamiento)  # Desencripta el texto
    print(f"Desplazamiento más probable: {desplazamiento}")  # Imprime el desplazamiento más probable
    print(f"Texto desencriptado: {texto_descifrado}")  # Imprime el texto desencriptado