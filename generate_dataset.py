import random

print('Weight')

w = []

for x in range(120):
  new = random.randint(50 * 100000, 500 * 100000)
  w.append(new)
  print(new)

print('Profit')

for x in range(120):
  print(random.randint(500 * 100000, 5000 * 100000))

print('Limit')

print(sum(w) / 2)
