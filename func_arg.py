# def add (num1=0,num2=0):   default arguments
#     return num1+num2

# def add (num1,*num2):   #variabel length arguments
#     sum=num1
#     for n in num2:
#         sum = sum+n

#     return sum
# print(add(9,4,5,6,2))


# def person(name,age):                #key word arguments
#     print("name is: ",name)
#     print("age is: ",age)

# print(person(age=30,name='gadi') )   


def person(name, ** kwlargs):     #keywordlength arguments
    print("name : ", name)
    for k,v in kwlargs.items():
        print(k,":",v)
person(name = input("Enter name: "),
age = int(input("Enter age: ")),
loc = input("Enter location: "),
tech = input("Enter technology: ")
)