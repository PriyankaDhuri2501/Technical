# from array import *

# def sum():
#     arr = array('i',[])

#     x = int(input("Enter no. of elements to add "))
#     for i in range(x):
#         val = int(input("Enter elements in array"))
#         arr.append(val)
#     print("Array created")
#     return arr

# arr = sum()
# sum_array = sum(arr)
# print("Sum of array is:",sum_array)



def recursive_sum(list):
    total = 0
    for item in list:
        if(type(item))== type([]):     # we can also directly use list keyword instead of type
            total+=recursive_sum(item)
        else:
            total+=item
    return total

list = [1,2,[3,4],5,[6]]
print(recursive_sum(list))



