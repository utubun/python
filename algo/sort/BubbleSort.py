# Bubble sort algorithm
from random import *
import time

def BubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                
a = range(1,100)
shuffle(a)
print(a[0:10])
BubbleSort(a)
print(a[0:10])

# short BubbleSort algorithm

def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while (passnum > 0 and exchanges):
       exchanges = False
       for i in range(passnum):
           if (alist[i] > alist[i+1]):
               exchanges = True
               alist[i], alist[i+1] = alist[i+1], alist[i]
       passnum -= 1

print "BubbleSort"        
a = range(1,100000)
shuffle(a)
print(a[0:10])
start_time = time.time()
BubbleSort(a)
print time.time() - start_time, "seconds"
print(a[0:10])
print "shortBubbleSort"
#a[4], a[432] = a[432], a[4]
shuffle(a)
print(a[0:10])
start_time = time.time()
shortBubbleSort(a)
print time.time() - start_time, "seconds"
print(a[0:10])
