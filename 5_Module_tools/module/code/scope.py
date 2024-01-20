## Scope of variables
# local scope
x = 20 # global by default
y = 15

def my_func1(order=5):
    
    x = 5 # local by default 
    x = x + order
    return x

res=my_func1(23)
res
x

def my_func2(order=5):
    global x, y
    x = x + order
    y = y + 5
    return x,y

res=my_func2(23)
res
x
y