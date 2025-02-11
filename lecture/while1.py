i = 0
while i < 3:
    print("%d while문 공부중" %i)
    i += 1

hap = 0
i = 1

while i < 11:
    hap = hap + i
    i += 1

print("1에서 10까지의 합계 : %d" %hap)

# 제어변수 선언
i = 0
sum = 0

# i값이 10보다 작거나 같으면 반복
while i <= 10:
    sum = sum + i
    i += 1

print("합계는", sum)