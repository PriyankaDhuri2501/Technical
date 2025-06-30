#Intersection of 2 arrays

def intersection_of_arrays(arr1,arr2):
    i = arr1[0]
    if i in arr2:
        print(arr1[i])
        arr1[i+1]
    else:
        return False
        



#check for Duplicates

def contain_duplicates(nums1,nums2):
    for i in nums1:
        if i in nums2:
            print(i)
        else:
            return False

nums1 = [1,3,1]
nums2 = [1,2,3,4]
print(contain_duplicates(nums1,nums2))


