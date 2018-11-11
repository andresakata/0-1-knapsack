import random

print('Weight')

w = []

for x in range(30):
  new = random.randint(500000, 5000000)
  w.append(new)
  print(new)

print('Profit')

for x in range(30):
  print(random.randint(5000000, 50000000))

print('Limit')

print(sum(w) / 2)
