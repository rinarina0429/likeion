# name='Nakyeong'
# age=20
# print('Hallo ich heisse {} und bin {} Jahre alt.'.format(name,age))
# print('Hallo ich heisse %s und bin %d Jahre alt.'%(name,age))

# grade=input("Your grade:")
# if (grade>=90):
#     print("A")
# elif (grade>=70):
#     print("B")
#     print("work HARDER!")
# else:
#     print("BOMB!!")

a = int(input("숫자 a를 입력해주세요 : "))
b = int(input("숫자 b를 입력해주세요 : "))
c = int(input("a*b의 값은?"))
if (a*b == c):
    print("Correct!")
else:
    print("Again...")

color=["pink","green","gray"]
color.append("ivory")
color.insert(3,"skyblue") #2번째 자리에 특정 삽입
del color[1]
x=color.pop()
color.remove("gray")