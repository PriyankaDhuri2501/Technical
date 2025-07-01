# def fibonacci(n):
#     if n<=1:
#         return n
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
    

# n = int(input("Enter number:"))
# print(fibonacci(n))


#optimal code for fibonacci 

# def fibonacci(n):
#     a,b = 0,1
#     series = []
#     for _ in range(n):
#         series.append(a)
#         a,b = b, a+b
#     return series

# print(fibonacci(10))



#Memoization approach - top to bottom
# calls = {}
# diary = [-1] * (50+1)
# def fib_with_dp(n):
#     if(n<=1):
#         return 1
#     if(diary[n] != -1):
#         return diary[n]
#     if(n not in calls):
#         calls[n] =1 
#     else:
#         calls[n]+=1

#     fib1 = fib_with_dp(n-1)
#     fib2 = fib_with_dp(n-2)
#     diary[n-1] = fib1
#     diary[n-2] = fib2
#     ans = fib1 + fib2
#     diary[n] = ans
#     return ans

# print(fib_with_dp(5))
# print(calls)

#tabulation approach

def fib_with_tabulation(n):
    if n<=1:
        return 1
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

print(fib_with_tabulation(11))


# def minimise_steps(n):
#     dp = [0]* (n+1)
#     dp[1] = 1
#     for i in range(2,n+1):
#         if(i%2==0):



# min cost path 
# count of balance B.T
# Longest increasing subsequence
# nth tribonacci number
# pascals traingle 2
# min cost to climb stairs
# CLimbing stairs
# triangle array
# min falling path sum
# unique paths
            




    
    

