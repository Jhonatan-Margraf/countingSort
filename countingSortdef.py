
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


inputArray = []
for i in range(5):
    inputArray.append(int(input(f"insira o {i+1}º valor: ")))
resultado = countingSort(inputArray)
print(resultado)
