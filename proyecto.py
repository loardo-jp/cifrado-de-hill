import numpy as np

def encriptar(mensaje, matriz_clave):
    while len(mensaje) % len(matriz_clave) != 0:
        mensaje += ' '

    matriz_mensaje = np.array([ord(caracter) - ord('a') for caracter in mensaje])
    matriz_mensaje = np.reshape(matriz_mensaje, (-1, len(matriz_clave)))

    matriz_encriptada = np.dot(matriz_mensaje, matriz_clave) % 26

    mensaje_encriptado = ''.join([chr(num + ord('a')) for fila in matriz_encriptada for num in fila])

    return mensaje_encriptado

def desencriptar(mensaje_encriptado, matriz_clave):
    matriz_encriptada = np.array([ord(caracter) - ord('a') for caracter in mensaje_encriptado])
    matriz_encriptada = np.reshape(matriz_encriptada, (-1, len(matriz_clave)))

    determinante = int(round(np.linalg.det(matriz_clave)))
    inverso_determinante = None
    for i in range(26):
        if (determinante * i) % 26 == 1:
            inverso_determinante = i
            break
    if inverso_determinante is None:
        raise ValueError("La matriz clave no es invertible.")

    matriz_inversa = np.linalg.inv(matriz_clave) * determinante * inverso_determinante
    matriz_inversa = matriz_inversa.round().astype(int) % 26

    matriz_desencriptada = np.dot(matriz_encriptada, matriz_inversa) % 26

    mensaje_desencriptado = ''.join([chr(num + ord('a')) for fila in matriz_desencriptada for num in fila])

    return mensaje_desencriptado

matriz_clave = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])

while True:
    print("\n---- Cifrado de Hill ----")
    print("1. Encriptar mensaje")
    print("2. Desencriptar mensaje")
    print("0. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        mensaje = input("Ingrese el mensaje a encriptar (solo letras minúsculas y espacios): ")
        mensaje_encriptado = encriptar(mensaje, matriz_clave)
        print("Mensaje encriptado: " + mensaje_encriptado)

    elif opcion == '2':
        mensaje_encriptado = input("Ingrese el mensaje a desencriptar (solo letras minúsculas y espacios): ")
        mensaje_desencriptado = desencriptar(mensaje_encriptado, matriz_clave)
        print("Mensaje desencriptado: " + mensaje_desencriptado)

    elif opcion == '0':
        break

    else:
        print("Opción inválida. Intente nuevamente.")