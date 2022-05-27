product = 0
products = []

for n1 in range(100,1000):
  for n2 in range(100,1000):
    product = n1*n2
    if str(product) == str(product)[::-1]:
      products.append(product)
print(max(products))
      