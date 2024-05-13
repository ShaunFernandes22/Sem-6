def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, (n**0.5)+1):
        if n % i == 0:
            return False
    return True

def isPrimitive(p, g):
    mod_list = []
    for i in range(1, p):
        mod_list.append((g**i)%p)
    for i in range(1, p):
        if mod_list.count(i) > 1:
            return False
    return True

while True:
    p = int(input("Enter values of p  : "))
    if (not isPrime):
        print("Not prime")
        continue
    g = int(input("Enter values of g  : "))
    if (not isPrimitive(p, g)):
        print(f"{g} is not a primitive root of {p}")
        continue

    a = int(input("Enter value of a : "))
    b = int(input("Enter value of b : "))
    if (a >= p or b >= p):
        print(f"Values of a and b should be less than {p}")
        continue

    Xa = (g ** a)%p
    Xb = (g ** b)%p

    Ka = (Xb**a)%p
    Kb = (Xa**b)%p

    print(f"Secret key of user A is {Ka}\nSecret key of user B is {Kb}")
    if Ka == Kb:
        print("Successful exchange of keys between A and B")
    else:
        print("Keys have not been successfully exchanged")
    break
