a =10             #global variabel

def something():
    a = 15              #local variabel
    globals()['a']=20
    print("inside: ", a)
something()    
print("outside:",a )    