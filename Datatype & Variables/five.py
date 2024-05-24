#global scope & global variable
x="global variable"
def funct():
    print("value of x:",x)

funct()

#local scope & local variable
def funct2():
    y="local variable"
    print(y)
    
funct2()