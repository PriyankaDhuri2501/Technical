def gcd(a,b):
    if b==0:
        return 1
    else:
        return gcd(b,a%b)
     
a= int(input("Enter 1st number:"))
b= int(input("Enter 2nd number:"))

print(gcd(a,b))
