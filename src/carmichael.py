k = 570

for i in range(-k, k):
  if (is_prime(i)):
    print(i, end = ' ')

print()

for i in range(-k, k):
  if (is_probably_prime(i, i)):
    print(i, end = ' ')