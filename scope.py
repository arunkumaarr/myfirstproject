x=50

def printer():
    global x
    print(x)
    #change value locally
    x=200
    print(x)

printer()