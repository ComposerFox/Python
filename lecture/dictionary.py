dic1 = {1:'a', 2:'b', 3:'c'}
print(dic1)

dic2 = {'a':1, 'b':2, 'c':3}
print(dic2)

student1 = {"학번":1000, "이름":"홍길동", "학과":"컴퓨터학과"}
print(student1)

student1["연락처"] = "010-1111-2222"
print(student1)

student1["학과"] = "파이썬학과"
print(student1)

del(student1["학과"])
print(student1)

print(student1.get("학번"))