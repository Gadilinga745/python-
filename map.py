# cube=lambda num:num*num*num 
# nums=[1,2,3,4,5,6,7,8,9]
# cubes=list(map(cube,nums))
# print(cubes)

nums=[1,2,3,4,5,6,7,8,9]
fun = lambda num: num%2 == 0
double= lambda num :num*2
evens=list(filter(fun,nums))
doubles=list(map(double,evens))
print(evens)
print(doubles)
