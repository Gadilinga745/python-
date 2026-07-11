def smart_operation(func):

    def inner(a, b):
        if a < b:
            a, b = b, a

        return func(a, b)

    return inner


@smart_operation
def div(a, b):
    print("Division:", a / b)


@smart_operation
def sub(a, b):
    print("Subtraction:", a - b)


@smart_operation
def add(a, b):
    print("Addition:", a + b)


div(2, 8)
sub(3, 10)
add(2, 8)
# def logger(func):

#     def wrapper():

#         print("Function Started")

#         func()

#         print("Function Ended")

#     return wrapper

# @logger
# def display():

#     print("Hello Python")

# display()




# def logger(func):

#     def wrapper(a, b):
#         print("Calling Function")

#         func(a, b)

#         print("Function Finished")

#     return wrapper

# @logger
# def add(a, b):
#     print(a + b)

# add(10, 20)