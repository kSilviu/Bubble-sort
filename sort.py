def bubbleSort(x):

    indexNumber = len(x)
    sortedCheck = False

    for i in range(indexNumber):
        swapped = False

        for h in range(0, indexNumber-i-1):
            if x[h] > x[h+1]:
                x[h], x[h+1] = x[h+1], x[h]
                swapped = True
        if not swapped:
            break
    return x
