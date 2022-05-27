sum = 0 
sum_not_squared = 0

def squares(x):
  return x**2

for i in range(1,101):
  sum += squares(i)

for n in range(1,101):
  sum_not_squared += n

answer = (squares(sum_not_squared) - sum)

print(answer)


  