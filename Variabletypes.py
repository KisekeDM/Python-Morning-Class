# local variable
def car():
    x = "volvo"
    del x
    print(x)


car()

# global variables
y = "phone"


def device():
    global y
    print(y)

device()
