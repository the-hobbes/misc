u = [10, 2, 9, 8, 8, 7, 6]

# loop once, swapping elements to satisfy the condition
for i in range(len(u) - 1):
  if i % 2 == 0:
    u[i] = min(u[i], u[i+1])
  else:
    u[i] = max(u[i], u[i+1])

# verify the condition is met
for x in range(len(u) - 1):
  if x % 2 == 0:
    assert u[x] <= u[x+1]
  else:
    assert u[x] >= u[x+1]
  
print u
