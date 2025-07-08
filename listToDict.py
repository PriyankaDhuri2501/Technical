#convert the list to dict [1,2,2,3,3,3,4,4] it should look like this {1:1,2:2,3:3,4:2}
l1= [1,2,2,3,3,3,4,4,4,4,4,4,5,5,6]
dict ={}
for i in l1:
    if i in dict:
        dict[i] +=1
    else:
        dict[i] = 1
print(dict)