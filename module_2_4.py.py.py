numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
not_primes = []
primes = []
for number in numbers:
    if number < 2:
        continue

    is_prime = True

    for div in range(2, number):
        if number % div == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)

print(not_primes)
print(primes)
