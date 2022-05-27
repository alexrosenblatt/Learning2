prime_list = [2]
num = 3
n = 100

while len(prime_list) < n:
  for p in prime_list:
    if num % p == 0:
      break
    else:
      prime_list.append(num)
    num += 2

print(prime_list[-1])
  