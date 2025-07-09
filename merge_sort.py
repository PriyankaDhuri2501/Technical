def Merge(l1,s,m,e):
    i = s
    j = m+1
    ans = []

    while(i<=m and j<=e):
        if(l1[i]<l1[j]):
            ans.append(l1[i])
            i+=1
        elif(l1[i]>l1[j]):
            ans.append(l1[j])
            j+=1
        elif(l1[i]==l1[j]):
            ans.append(l1[i])
            ans.append(l1[j])
            i+=1
            j+=1

    while(i<=m):
        ans.append(l1[i])
        i+=1

    while(j<=e):
        ans.append(l1[j])
        j+=1

    startOfmyAns = 0
    startOfmyList = 5

    while(startOfmyList<=e):
        l1[startOfmyList] = ans[startOfmyAns]
        startOfmyAns+=1
        startOfmyList+=1

    return

l1 = [6,5,12,10,9,1]
l1 = [5,6,12,1,9,10]

Merge(l1)
print(l1)
