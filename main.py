import math

a = 232792560

pyth
while True:
  if all(a % n == 0 for n in range(1, 21)):
    print(a)
    break
  else:
    a = a + 20
    print(a)
  