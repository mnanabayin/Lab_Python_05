##Problem 2 FACTORIAL

def factorial(x):
    fact = 1
    for i in range(1,x+1,1):
        fact*=i
    return fact



##Problem 3 FIBONACCI

def fibonacci(n):
    fib_list = [1,1]
    if n == 0:
        fib_list.remove(1)
        return fib_list
    if n == 1:
        fib_list.remove(1)
        return fib_list
    if n < 0:
        return 'Error: Parameter undefined'
    for i in range(2,n,1):
        fib_list.append(fib_list[i-1] + fib_list[i-2])

    return fib_list



        
##Problem 4  PRIME

def prime(x):
    num = x
    i = 2
    while(i <= x-1):
        if(x%i == 0):
            return False
        i+=1
    if(i == num):
        return True


## CHALLENGE PROBLEMS
    ##Problem 4
    ##PALINDROME
    
def isPalindrome(st):
    n = len(st)
    i=0
    while i < n:
        if st[i] == st[-(i+1)]:
           i+=1
        else:
            return False
    return True


##Problem 5
##isSubstring

def isSubstring(str1, str2):
    n = len(str2)
    i=0
    while i < n:
        if str(str1) == str2[i:(len(str1)+i)]:
            return True
        i+=1
    return False



##Problem 7
## 
    



