# Insertion sort

import random
import time

def InsertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index        
        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position -= 1
        alist[position] = currentvalue

alist = range(10000)
random.shuffle(alist)
print alist[0:10]
start = time.time()
InsertionSort(alist)
print time.time() - start, " seconds"
print alist[0:10]

        
        
