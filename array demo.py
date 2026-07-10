# from array import array
# array1= array('i',[33,4,55,64,22])
# array2 = array(array1.typecode,(n for n in array1))

# array1[2]=54

# print(array1)
# print(array2)
from array import array
arrays=list(map(int,input("enter an array").split()))
array1= array('i',arrays)
array2 = array(array1.typecode,(n for n in array1))

array1[2]=54

print(array1)
print(array2)