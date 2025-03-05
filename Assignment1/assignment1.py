import math

def generate_keys(p,q):
    n = p*q
    t = (p-1)*(q-1)

    e=3
    while math.gcd(e,t) != 1:
        e+=2

    for d in range(2,t):
        if(d*e)%t==1:
            return e,d,n
        
    return None

def encrypt(m, e, n):
    return pow(m,e,n)

def decrypt(c, d, n):
    return pow(c, d, n)

def prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    p = int(input("Enter Number 1: "))
    q = int(input("Enter Number 2: "))

    if(not(prime(p))and not(prime(q))):
        exit()

    k = generate_keys(p,q)

    e,d,n = k

    m = int(input("Enter the message: "))

    print(f"Public key is {e}, {n}")
    print(f"Private key is {d}, {n}")

    c = encrypt(m,e,n)
    print(f"Cipher text is: {c}")

    dec = decrypt(c,d,n)
    print(f"Message is: {dec}")


