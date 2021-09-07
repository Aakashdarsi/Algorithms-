"""
This is a bubble sort example to demonstrate 
"""


def bubble_sort(array):
    n = len(array)
    for i in range(n):
        are_swaps = False 
        for j in range(0,n-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
                are_swaps = True 
        if are_swaps ==False:
            break
    return array
array = [22,1,15,3,4,2]
print(bubble_sort(array))