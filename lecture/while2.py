while True:
    light = input("신호등 색상을 입력하시오.")
    if light == "blue":
        break

print("전진")

hap, i = 0, 0

for i in range(1, 101):
    if i % 3 == 0:
        continue

    hap += i

print("1~100의 합계(3의 배수 제외) : %d" %hap)

for n in range(10):
    if n % 2 == 0:
        continue

    print(n)