def encontrar_caracter(cadena, objetivo):
    cadena = cadena.lower()
    contador = 0
    for caracter in cadena:
        if caracter == objetivo:
            contador += 1
    return contador
cadena = input("Ingrese una cadena de texto: ")
objetivo = input("Ingrese el carácter objetivo: ")
cantidad = encontrar_caracter(cadena, objetivo)

print(f"El carácter '{objetivo}' aparece {cantidad} veces en la cadena")

