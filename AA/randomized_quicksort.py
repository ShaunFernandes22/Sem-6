import random
import time
c1 , c2 = 0, 0

def randomizedQs(arr):
    global c1
    if (len(arr) < 1):
        return arr
    
    pivot = random.choice(arr)
    left = []
    right = []
    middle = []

    for i in range(len(arr)):
        if (arr[i] < pivot):
            c1 += 1
            left.append(arr[i])
        elif (arr[i] > pivot):
            c1 += 1
            right.append(arr[i])
        else:
            middle.append(arr[i])
    return randomizedQs(left) + middle + randomizedQs(right)

def quicksort(arr):
    global c2
    if (len(arr) < 1):
        return arr
    
    pivot = arr[0]
    left = []
    right = []
    for i in range(1, len(arr)):
        c2 += 1
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quicksort(left) + [pivot] + quicksort(right)

arr = [random.randint(0, 200) for i in range(100)]
arr1 = arr.copy()

print("Normal Quicksort")
st = time.time()
print("Sorted array : ", quicksort(arr))
print("Time taken", time.time() - st, "No of Comparisons : ", c2)


print("Randomized Quicksort")
st = time.time()
print("Sorted array : ", randomizedQs(arr1))
print("Time taken", time.time() - st, "No of Comparisons : ", c1)
