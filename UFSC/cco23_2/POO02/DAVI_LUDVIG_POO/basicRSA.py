def gcd(a, b):
    while 1:
        r = a % b
        if not r:
            break
        a = b
        b = r
    return b


def findCoPrime(n):
    num = 1
    for i in range(2, int(n**1 / 2) + 1):
        if gcd(n, i) == 1:
            num = i
            break
    return num


pq = input("Insert p and q: ")
p, q = [int(a) for a in pq.split()]

n = p * q

t = (p - 1) * (q - 1)
e = findCoPrime(t)

m = int(input("Insert the message: "))
c = (m**e) % n

print(f"Your encripted message is {c}.")

d = ()
