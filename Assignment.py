# is it a prime number?
# 1 not prime
def is_prime(p):
    if p == 2:
        return False
    for i in range(2, int(p/2)+1):
        if p % i == 0:
            return False
    return True

#Enter Number
p = float(input("Enter Number:"))

#Result
if is_prime(p):
    print("number is prime")
else:
    print("number not prime")


