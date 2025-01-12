def is_prime (a):
    for i in range (2,a):
        if a%i ==0:
            return (False)
        else:
            return (True)
a = int(input())
print(is_prime(a))
