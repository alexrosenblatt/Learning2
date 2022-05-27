count = 0
res = 0
finish = False

while finish != True:
  res+=2520
  count = 0
  for x in range(11, 21):
    if res % x == 0:
      count+=1
      if count == 10:
        finish = True
print('min:', res)
