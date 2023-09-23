def suma(lista):
  suma = 0
  for numero in lista:
    suma += numero
  return suma
def promedio(lista):
  promedio = suma(lista) / len(lista)
  return promedio
if __name__ == "__main__":
  valores = input("Introduce una lista de números separados por comas: ")
  lista = valores.split(",")
  lista = [int(numero) for numero in lista]
  print("La suma es", suma(lista))
  print("El promedio es", promedio(lista))