# 집합 선언
s = set()
s = {1, 2, 5}

# 집합에 원소 추가
s.add(10)
s.add(3)
print(s)

# 집합에서 원소 삭제
s.discard(5)
print(s)
s.remove(2)
print(s)
s.clear()
print(s)

# 집합을 리스트로 변환
list = [1, 2, 3, 4, 5]
print(set(list))

# 교집합에 해당하는 연산
list1 = [2, 3, 5]
list2 = [1, 3, 6]
result1 = []

for i in list2:
    if i in list1:
        result1.append(i)
print(result1)

# 합집합에 해당하는 연산
list1 = [2, 3, 5]
list2 = [1, 3, 6]
result1 = list1.copy()

for i in list2:
    if i not in result1:
        result1.append(i)
print(result1)

# 차집합에 해당하는 연산
list1 = [2, 3, 5]
list2 = [1, 3, 6]
result1 = []

for i in list2:
    if i in list1:
        list1.remove(i)
print(list1)