""" Write a python program to reverse an array without using the built-in reverse. You will swap the first and last values, then use a loop to swap every pair and test your function on 
different arrays."""

arr = [7,6,5,4,3,2]

print(f"Original Array: {arr}")

def arrayReverse(arr):
    for a in range(len(arr) // 2):
        b = len(arr) - 1 - a
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp

arrayReverse(arr)
print(f"Reversed Array: {arr}")