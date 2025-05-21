import time
import random

def countingSort(inputArray):

    countArray = [0] * (max(inputArray) + 1)


    for num in inputArray:
        countArray[num] += 1


    for i in range(1, len(countArray)):
        countArray[i] += countArray[i - 1]


    outputArray = [0] * len(inputArray)


    i = len(inputArray) - 1
    while i >= 0:
        current_val = inputArray[i]
        position = countArray[current_val] - 1
        outputArray[position] = current_val
        countArray[current_val] -= 1
        i -= 1

    return outputArray

listaTempo = []

with open("resultado.txt", "w") as f:
    pass

for i in range(5):

    inputArray = []

    with open("numeros.txt", "r") as file:
        for line in file:
            inputArray.append(int(line.strip()))


    inicio = time.perf_counter()
    
    resultado = countingSort(inputArray)
    
    fim = time.perf_counter()

    tempo = fim - inicio

    print(tempo)

    listaTempo.append(tempo)

    
    mode = "w" if i == 0 else "a"
    with open("resultado.txt", "a") as f:
            f.write(f"{tempo} segundos\n")

tamanhoListaTempo = len(listaTempo)
tamanhoLista = len(inputArray)
mediaTempo = sum(listaTempo) / len(listaTempo)
with open("resultado.txt", mode) as f:
    f.write("\n\n\n")
    f.write(f"O codigo fez a ordenacao de uma lista com {tamanhoLista} numeros inteiros {tamanhoListaTempo} vezes \n")
    f.write("\n\n\n")
    f.write("tempo media :\n")
    f.write(f"{mediaTempo} segundos\n")
    
            
