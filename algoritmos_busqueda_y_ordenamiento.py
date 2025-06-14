import random            # Sirve para crear números al azar
import time              # Lo usamos para medir cuánto tarda algo en ejecutarse

# Algoritmos de ordenamiento  
def bubble_sort(arr):                                       # Con esta función ordenamos la lista usando "bubble sort"
    n = len(arr)                                            # Calculamos cuantos elementos tiene la lista. Entonces, por ejemplo si la lista es [5, 3, 8, 1], n va a ser igual a 4
    for i in range(n):                                      
        for j in range(n - i - 1):                          # Comparamos los números de a pares 
            if arr[j] > arr[j + 1]:                         # Si el número actual es más grande que el siguiente
              arr[j], arr[j + 1] = arr[j + 1], arr[j]         # Los cambiamos de lugar 
    return arr                                              # Devolvemos la lista ordenada

def quick_sort(arr):                                        # Con esta funcion ordenamos la lista usando "quick sort"
    if len(arr) <= 1:                                       # Si la lista tiene 0 o 1 elemento, ya está ordenada y la devolvemos tal como está 
        return arr                  
    pivot = arr[0]                                                # Elegimos el primer número como pivote (referencia)
    menores = [x for x in arr[1:] if x <= pivot]                  # Números menores o iguales al pivote
    mayores = [x for x in arr[1:] if x > pivot]                   # Números mayores al pivote
    return quick_sort(menores) + [pivot] + quick_sort(mayores)    # Ordenamos cada parte

# Algoritmos de búsqueda
def busqueda_lineal(arr, objetivo):                 # Busca un número en la lista, uno por uno
    for i in range(len(arr)):                       # Va revisando cada número
        if arr[i] == objetivo:                      # Si lo encuentra
            return i                                # Devuelve la posición donde estaba
    return -1                                       # Si no lo encuentra, devuelve -1

def busqueda_binaria(arr, objetivo):                 # Usamos la busqueda binaria que es más rapida, pero solo si la lista está ordenada
    izquierda, derecha = 0, len(arr) - 1             # Empieza por los extremos de la lista
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2           # Busca el número del medio
        if arr[medio] == objetivo:                    # Si es el número que buscamos
            return medio                               # Lo encuentra y devuelve la posición  
        elif arr[medio] < objetivo:                  # Si el número del medio es menor
             izquierda = medio + 1                       # Buscamos en la parte de la derecha
        else:                                              # Si el número del medio es mayor
             derecha = medio - 1                               # Buscamos en la parte de la izquierda
    return -1                                             # Si no lo encuentra, devuelve -1

# Selección del algoritmo de ordenamiento               
def seleccionar_ordenamiento(nombre, arr):          # Recibe el tipo de ordenamiento y la lista
    algoritmos = {                          
        "bubble sort": bubble_sort,                         
        "quick sort": quick_sort,
    }
    if nombre in algoritmos:                                                                 # Si el nombre que elegimos es válido
        inicio = time.perf_counter()                                                         # Marcamos la hora antes de ordenar
        resultado = algoritmos[nombre](arr.copy())          
        fin = time.perf_counter()                                                           # Marcamos el tiempo después de ordenar
        print(f"→ Tiempo de ordenamiento con {nombre}: {fin - inicio:.6f} segundos")        # Mostramos cuánto tardó
        return resultado                                                                    # Devolvemos la lista ordenada 
    else:
        print("Algoritmo no válido.")                                                           # Si el nombre no es válido, avisamos
        return arr                                                                               # Devolvemos la lista sin ordenar
    
# Programa principal
if __name__ == "__main__":                                                      
    lista = [random.randint(0, 1000) for _ in range(10000)]                 # Generamos una lista de 1000 números aleatorios entre 0 y 10.000

    print("Lista generada completa:")                                        
    print(lista)                                                             # Mostramos la lista entera con los 10000 elementos

    print("Elige algoritmo de ordenamiento: bubble sort / quick sort")          
    metodo = input("→ ").lower()                                                # Preguntamos al usuario qué método de ordenamiento quiere usar
    ordenada = seleccionar_ordenamiento(metodo, lista)                          # Ordenamos la lista con ese método

    objetivo = int(input("¿Qué número querés buscar? "))                    # Le preguntamos al usuario qué número quiere buscar
print("Elige método de búsqueda: lineal / binaria")                         # Le preguntamos al usuario que método de búsqueda quiere usar para encontrar ese número  
metodo_busqueda = input("→ ").lower()                       

if metodo_busqueda == "lineal":                                              # Si eligió búsqueda lineal
        inicio = time.perf_counter()                                           # Marcamos el tiempo de inicio   
        posicion = busqueda_lineal(ordenada, objetivo)                       # Buscamos el número con este métdod 
        fin = time.perf_counter()                                               # Marcamos el tiempo final
        print(f"→ Tiempo de búsqueda lineal: {fin - inicio:.6f} segundos")          # Mostramos cuánto tardó en hacer la búsqueda lineal
elif metodo_busqueda == "binaria":                                              #Si eligió busqueda binaria
        inicio = time.perf_counter()                                            # Marcamos el tiempo de inicio
        posicion = busqueda_binaria(ordenada, objetivo)                         # Buscamos el número con este método
        fin = time.perf_counter()                                                           # Marcamos el tiempo final  
        print(f"→ Tiempo de búsqueda binaria: {fin - inicio:.6f} segundos")       # Mostramos cuánto tardó en hacer la búsqueda binaria
else:
        print("Método inválido.")                        # Si escribió mal el método, mostramos el error y cerramos el programa 
        exit()

if posicion != -1:                                                  
        print(f"Número encontrado en la posición {posicion}")           # Si encontramos el número mostramos en qué posicion está
else:       
        print(f"Numero no encontrado")                                  # Si no lo encontramos, mostramos que el número no fue encontrado
