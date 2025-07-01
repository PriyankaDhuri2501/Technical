def exponention(a,b):
    if b==0:
        return 1
    else:
        return a*exponention(a,b-1)
    
a= int(input("Enter number:"))
b= int(input("Enter Base:"))
print(exponention(a,b))