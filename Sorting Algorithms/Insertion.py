from random import randint
from time import time

"""

Creates a random array with the numbers 1 to arrSize that contains all the numbers and none of them repeating.

Then it sorts them from smallest to biggests using the Insertion sort algorithm.

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

def InsertionSort (arr): # This is the main function, which is in charge of ordering the array
    
    iterations = 0

    for i in range (1, len(arr)):
        for n in range (i, 0, -1):
            iterations += 1

            if arr[n] < arr[n - 1]:
                Swap (arr, n, n - 1)
            else:
                break
    
    iterationsArr.append(iterations)
        

def Start (times):
    start_time = time()
    for _ in range (times):
        arr = GenRandArr(10**3)
        #print (arr)
        InsertionSort(arr)
        #print (arr)

    average = CalculateAverage(iterationsArr) # Calculates the average number of iterations when ordering random arrays
    print ("Insertion Sort has an average iterations of {} and the time is {} seconds".format(average, time() - start_time))

if __name__ == "__main__":
    Start (1)