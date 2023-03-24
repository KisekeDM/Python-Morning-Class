try:
    x = 10
    print(x)
except:
    print("x is not defined")
finally:
    print("hello world")

try:
    num1 = 0
    num2 = 56
    print(num1/num2)
except:
    print("An arithmetic error occurred")
finally:
    print("Hello World")

