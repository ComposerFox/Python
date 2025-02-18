tt1 = (10, 20, 30)
tt2 = 10, 20, 30
print(tt1, tt2)

card = "red", 4, "다이아몬드", True
print(card)

card[2] # 세번째 항목값 확인
card[:2] # 앞에부터 3번째 항목까지 확인
card[2:] # 세번째부터 뒤의 항목까지 확인
card[:] # 전체 항목값 확인

# 튜플을 리스트에 넣어서 생성
programmer_list = [("python", 7), ("java", 2)]
print(programmer_list)

# 튜플리스트를 딕셔너리로 변경
programmer_dict = dict(programmer_list)
type(programmer_dict)

print(programmer_dict["python"])
print(programmer_dict["java"])