import random
import time

######################################################################
# Insertion Sort
######################################################################

def insertionsort(arrayY):
   for i in range(1, len(arrayY)):

     current = arrayY[i]
     p = i

     while p>0 and arrayY[p-1] > current:
         arrayY[p] = arrayY[p-1]
         p = p-1

     arrayY[p] = current

######################################################################
# Quicksort
######################################################################

def randomize(arrayY, low, high): # this will choose a random pivot point for the quicksort
    rand = random.randint(low, high)
    temp = arrayY[high]
    
    arrayY[high] = arrayY[rand]
    arrayY[rand] = temp
    
    return partition(arrayY, low, high)
    
def partition(arrayY, low, high):
    i = low-1 # this is the index
    p = arrayY[high]   # this is the pivot
    for j in range(low, high):
        if arrayY[j] <= p:
            i = i+1
            temp = arrayY[i]
            arrayY[i] = arrayY[j]
            arrayY[j] = arrayY[temp]
    temp = arrayY[i+1]
    arrayY[i+1] = arrayY[high]
    arrayY[high] = arrayY[temp]
    return i+1

def quicksort(arrayY, low, high):
    if low < high:
        index = randomize(arrayY,low,high)
        quicksort(arrayY, low, index-1)
        quicksort(arrayY, index+1, high)
        return arrayY

######################################################################
# Radix Sort - https://www.geeksforgeeks.org/radix-sort/
######################################################################
def countingsort(arrayY, exp1):
    n = len(arrayY)
    output = [0] * (n)
    count = [0] * (10)
    for i in range(0, n):
        index = (arrayY[i]//exp1)
        count[(index)%10] += 1
    for i in range(1,10):
        count[i] += count[i-1]
    i = n-1
    while i>=0:
        index = (arrayY[i]//exp1)
        output[count[(index)%10] - 1] = arrayY[i]
        count[(index)%10] -= 1
        i -= 1
    i = 0
    for i in range(0,len(arrayY)):
        arrayY[i] = output[i]
 
def radixsort(arrayY):
    if max(arrayY) != []:
        max1 = max(arrayY)
    exp = 1
    while max1//exp > 0:
        countingsort(arrayY,exp)
        exp *= 10
    
    return arrayY

######################################################################
# The Tests
######################################################################
# fills arraysize with the different array sizes we will use for our test
arraySize = []
loops = 20 # number of time each algorithm will be run and number of random arrays that will be generated
TaArray = []
TbArray = []
TcArray = []

count = 0

for x in range(14):
    arraySize.append(2**(x+1))

print(arraySize)

for n in range(len(arraySize)):    # this is how many times we will run the total loop structure
    Ta = Tb = Tc = 0
    arrayX = []
    for noOfInputs in range(loops):      # run each array length 20 times and average
        for x in range(arraySize[n]): # fill array to be sorted with random ints length at position arraySize
            arrayX.append(random.randint(1, 20001))
        start = time.perf_counter()
        arrayY = arrayX # this copies array in order to sort it
        arrayY = insertionsort(arrayY) # calls method to sort array
        Ta = Ta + (time.perf_counter() - start) # totals the time which will be divided later
    TaArray.append(Ta)
    for noOfInputs in range(loops):
        for x in range(arraySize[n]): # fill array to be sorted with random ints length at position arraySize
            arrayX.append(random.randint(1, 20001))
        start = time.perf_counter()
        arrayY = arrayX
        arrayY = quicksort(arrayY, 0, len(arrayY)-1)
        Tb = Tb + (time.perf_counter() - start)
        TbArray.append(Tb)
    for noOfInputs in range(loops):
        for x in range(arraySize[n]): # fill array to be sorted with random ints length at position arraySize
            arrayX.append(random.randint(1, 20001))
        start = time.perf_counter()
        arrayY = arrayX
        arrayY = radixsort(arrayY)
        Tc = Tc + (time.perf_counter() - start)
    TcArray.append(Tc)
    count += 1
    print("Count = " + str(count))

for x in range(len(TaArray)): # this divides the totaled times by 20 in order to get the average times
    TaArray[x] = TaArray[x] / loops
    TbArray[x] = TbArray[x] / loops
    TcArray[x] = TcArray[x] / loops

print("Insertion Sort")
for x in range(len(TaArray)): # prints out the times
    print("Length: " + str(arraySize[x]) + " Time: " + str(TaArray[x]))

print("Quick Sort")
for x in range(len(TbArray)):
    print("Length: " + str(arraySize[x]) + " Time: " + str(TbArray[x]))
                          
print("Radix Sort")
for x in range(len(TcArray)):
    print("Length: " + str(arraySize[x]) + " Time: " + str(TcArray[x]))


