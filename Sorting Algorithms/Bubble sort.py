from random import randint
from time import time

"""

Creates a random array with the numbers 1 to arrSize that contains all the numbers and none of them repeating.

Then it sorts them from smallest to biggests using the Bubble sort algorithm.

The program also keeps track of the number of iterations to order the array and calculates the average number of iterations.

"""

iterationsArr = []

def Swap (arr, a, b):# Swaps the values at positions a & b in the array
    
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

def GenRandArr (arrSize): # Clears the array and creates a random new one
    arr = []

    for _ in range (arrSize):
        arr.append(GenRandNum(arr, arrSize))
    
    return arr
def GenRandNum (arr, arrSize): # Finds a random number between 1 and the size of the array that is not already in the array
    
    rnd = randint(1, arrSize)
    
    return rnd

def CalculateAverage (arr): # Calculates the average number between the values of an array
    
    sum = 0 # The sum of the values of the array
    for value in arr:
        sum += value

    average = sum / len(arr)
    
    return average

def BubbleSort (arr): # This is the main function, which is in charge of ordering the array
    
    ready = False # This keeps track if there has been made a swap, in other words, if the array is in order or not
    iterations = 0

    while not ready:
        ready = True
        for n in range (len(arr) - 1):
            if arr[n] > arr[n + 1]:
                Swap (arr, n, n + 1)
                ready = False
            
            iterations += 1
    
    iterationsArr.append(iterations)
        
def Start (times):
    start_time = time()
    for _ in range (times):
        arr = GenRandArr(10**3)
        #print (arr)
        BubbleSort(arr)
        #print (arr)
    
    average = CalculateAverage(iterationsArr) # Calculates the average number of iterations when ordering random arrays
    print ("Bubble Sort has an average iterations of {} and the time was {} seconds".format(average, time() - start_time))


Start (1)
