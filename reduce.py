from functools import reduce
sum=lambda a,b:a+b
# nums=[1,2,3,4,5,6,7,8,9]

# sums=reduce(sum,nums)
# print(sums)


nums=[1,2,3,4,5,6,7,8,9]
fun = lambda num: num%2 == 0
double= lambda num :num*2
evens=list(filter(fun,nums))
doubles=list(map(double,evens))
sums=reduce(sum,doubles)
print(evens)
print(doubles)
print(sums)

