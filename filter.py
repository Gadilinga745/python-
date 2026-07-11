nums=[1,2,3,4,5,6,7,8,9]
fun = lambda num: num%2 == 0

evens=list(filter(fun,nums))
print(evens)
