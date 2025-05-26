n = 20


def prime_checker(n):
    prime_list = []
    for x in range(2, n):
        if n % x == 0:
            prime_list.append(x)

    if len(prime_list) == 0:
        print(n, "is a prime number")
    else:
        print(n, "is not a Prime Number")


prime_checker(n)

prime_list = []
for y in range(1,n):
    if n % y != 0:
        prime_list.append(y)

for i in prime_list:
    if i % y != 0:
        prime_list.append(i)

print(prime_list)
