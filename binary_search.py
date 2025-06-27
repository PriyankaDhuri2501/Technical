from array import *

def binary_search(arr,target):
    left,right=0, len(arr)-1
    while left<=right:
        mid = (left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left = mid+1
        else:
            right = mid-1
    return -1

def create():
    arr = array('i',[])

    x = int(input("Enter no. of elements to add in array"))
    for i in range(x):
        val = int(input("Enter elements in array"))
        arr.append(val)
    print("Array created")
    return arr

arr = create()
sorted_array = sorted(arr)
print("Sorted array is:",sorted_array)
target = int(input("Enter element to search:"))
index = binary_search(arr,target)

print(f"Element found at index{index}")