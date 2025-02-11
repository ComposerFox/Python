for i in range(5):
  print("방문을 환영합니다!")

sum = 0
for i in range(1, 101):
  sum += i
print("1부터 100까지의 합은 : ", sum)

for i in range(5):
  for j in range(10):
    print("*", end=" ")
  print("")

for i in range(1, 6):
  for j in range(1, i + 1):
    print("*", end=" ")
  print("")
