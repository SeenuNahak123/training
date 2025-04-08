'''def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(4))'''

'''def list_sum(num_list):
    if len(num_list)==1:
        return num_list[0]
    else:
        return num_list[0]+list_sum(num_list[1:])
print(list_sum([2,4,5,6,7]))'''


'''def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)

n=5
for i in range(n):
    print(fib(i))'''


'''def count(n):
    if n<10:
        return 1
    else:
        return 1+count(n/10)
print(count(12345))'''


'''def reverse(n):
    
    if len(n)==1:
        print(n,end='')
    else:
        print(n[-1],end='')
        reverse(n[0:len(n)-1])

reverse('string reverse')'''
