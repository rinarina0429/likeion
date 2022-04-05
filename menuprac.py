import random
import time

for x in range(30):
    print(x)
    #0~29
while True: #무한 반복 #파이썬은 들여쓰기 맞춰주는게 굉장히 중요
    break #이거 만나면 바로 프로그램 시행 멈춤
    print(random.choice(["된장찌개","치킨","떡볶이","라면","감자튀김"]))
    print("이 문장도 반복되나")
    time.sleep(1)
lunch = random.choice(["김치찌개","피자","제육볶음"]) #이름 붙이기
print(lunch) #이름 붙인거 출력하는 법

# lunch = random.choice(["김치찌개","피자","제육볶음"])
# lunch = "냉장고"
# print(lunch)
# 하면 냉장고만 출력 (파이썬은 상자 비우기 안해도 된다는 것)

information = {"고향":"수원", "취미":"영화관람", "좋아하는 음식":"국수"}
print(information)
print(information.get("취미"))

information = {"특기":"피아노", "사는곳":"서울"}
print(information.get("특기"))
print(information.get("사는곳"))

information = {"고향":"수원", "취미":"영화관람","좋아하는 음식":"국수"} #dictionary
foods = ["된장찌개", "피자", "제육볶음"] #list

information = {"고향":"수원", "취미":"영화관람","좋아하는 음식":"국수"}
print(information.get("취미"))
information["특기"] = "피아노"
information["사는곳"] = "서울"
#inforation 보기 추가
del information["좋아하는 음식"]
#inforation 보기 삭제
print(information)
print(len(information)) #length (개수)
information.clear() #비우기
print(information)

foods = ["된장찌개", "피자", "제육볶음"]
print(foods[-2]) #0이 첫번째 (-3~2)
foods.append("김밥") #list 보기 추가
del foods[1] #list 보기 삭제
print(foods)

foods = ["된장찌개", "피자", "제육볶음"]
for x in range(3):
    print(foods[x])
for x in foods:
    print(x)

information = {"고향":"수원", "취미":"영화관람", "좋아하는 음식":"국수"}
for x, y in information.items():
    print(x)
    print(y)

foods = ["된장찌개", "피자", "제육볶음"]
#집합 만들기
foods_set1 = set(foods)
foods_set2 = set(["된장찌개", "피자", "제육볶음"])
#2개 같은 집합
print(foods_set1)
print(foods_set2)
#집합 출력은 순서 바뀜

foods = ["된장찌개", "피자", "제육볶음", "된장찌개"]
foods_set = set(foods)
print(foods) #된찌 2번 그대로
print(foods_set) #된찌 1번

menu1 = set(["된장찌개", "피자", "제육볶음"])
menu2 = set(["된장찌개", "떡국", "김밥"])
menu3 = menu1 | menu2 #합집합
print(menu3)
menu3 = menu1 & menu2 #교집합
menu3 = menu1 - menu2 #차집합 -> "피자","제육볶음"

import random

food = random.choice(["된장찌개","피자","제육볶음"])

print(food)
if(food == "제육볶음"):
    print("곱배기 주세요")
else:
    print("그냥 주세요")
print("종료")

lunch = ["된장찌개", "피자", "제육볶음", "짜장면"]
lunch.append("돈까스") #추가
print(lunch)

lunch = ["된장찌개", "피자", "제육볶음", "짜장면"]
input() #사용자직접추가
print(lunch)

lunch = ["된장찌개", "피자", "제육볶음", "짜장면"]
input("음식을 추가 해주세요 : ")
print(lunch)

lunch = ["된장찌개", "피자", "제육볶음", "짜장면"]
item = input("음식을 추가 해주세요 : ")
lunch.append(item)
print(lunch)

lunch = ["된장찌개", "피자", "제육볶음", "짜장면"]
while True:
    item = input("음식을 추가 해주세요 : ")
    lunch.append(item)
    print(lunch)
#무한반복 추가 끄기는 ctrl + C

lunch = ["된장찌개", "피자", "제육볶음", "짜장면"]

while True:
    print(lunch)
    item = input("음식을 추가 해주세요 : ")
    if(item == "q"):
        break
    else:
        lunch.append(item)
    
print(lunch)
set_lunch = set(lunch)

set_lunch = set(["된장찌개", "피자", "제육볶음", "짜장면"])
item = "짜장면"
print(set_lunch - set([item]))
set_lunch = set_lunch - set([item])
print(set_lunch)