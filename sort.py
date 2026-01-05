def bubbleSort(x):

    indexNumber = len(x)-1

    for i in range(indexNumber):
        swapped = False

        for h in range(0, n-i-1):
            if x[h] > x[h+1]:
                x[h], x[h+1] = x[h+1], x[i]
                swapped = True
        if (swapped == False):
            break
