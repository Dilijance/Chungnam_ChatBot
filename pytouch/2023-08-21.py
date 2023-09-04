# score = float(input("학점 입력: "))

# if score == 4.5:
#     print("신")
# elif score >= 4.2:
#     print("교수님의 사랑")
# elif score >= 3.5:
#     print("현 체제의 수호자")
# elif score >= 2.8:
#     print("일반인")
# elif score >= 2.3:
#     print("일탈을 꿈구는 소시민")
# elif score >= 1.75:
#     print("오락문화의 선구자")
# elif score >= 1.0:
#     print("불가촉천민")
# elif score >= 0.5:
#     print("자벌레")
# elif score > 0:
#     print("프랑크톤")
# else:
#     print("시대를 앞서가는 혁망의 씨앗")


# a, b, c, = float(input()), float(input()), float(input())

# if a > b:
#     if a > c:
#         print(a)
#     else:
#         print(c)
# else:
#     if b > c:
#         print(b)
#     else:
#         print(c)


# max = float(input())
# for i in range(2):
#     n = float(input())
#     if n > max:
#         max = n

# print(max)


# money = int(input("돈 입력해주세요: "))

# print("""
# |==================
# |       메뉴       
# |==================
# |1번 코카콜라 1000원
# |2번 사이다   800원
# |3번 환타     900원 
# |4번 밀키스   700원
# |5번 솔의눈   600원 
# |6번 삼다수   500원
# |-------------------
# """)

# x = int(input("음료 번호를 선택 해주세요. "))

# if x > 6 or x < 1:
#     print("이런 번호가 없습니다.")
# elif x == 1 and money - 1000 >= 0:
#     money -= 1000
#     print('코카콜라를 선택했습니다.', money, "원 남았습니다.")
# elif x == 2 and money - 900 >= 0:
#     money -= 900
#     print('환타를 선택했습니다.', money, "원 남았습니다.")
# elif x == 3 and money - 800 >= 0:
#     money -= 800
#     print('사이다를 선택했습니다.', money, "원 남았습니다.")
# elif x == 4 and money - 700 >= 0:
#     money -= 700
#     print('밀키스를 선택했습니다.', money, "원 남았습니다.")
# elif x == 5 and money - 600 >= 0:
#     money -= 600
#     print('솔의눈 선택했습니다.', money, "원 남았습니다.")
# elif x == 6 and money - 500 >= 0:
#     money -= 500
#     print('삼다수를 선택했습니다.', money, "원 남았습니다.")
# else:
#     print("돈이 부족합니다.", money,"원 남았습니다.")


# list_a = [273, 21, 103, "문자열", True, False]

# # print(list_a[0])
# # print(list_a[1])
# # print(list_a[2])
# # print(list_a[1:3])

# print(list_a[3][2])


# list_a = [1, 2, 3]

# print("리스트 뒤에 요소 추가하기")
# list_a.append(4)
# list_a.append(5)

# print(list_a)
# print()
# print("리스트 중간에 요소 추가하기")
# list_a.insert(0, 10)
# print(list_a)

# treeHit = 0
# while treeHit < 10:
#     treeHit = treeHit + 1
#     print("나무를%d번 찍었습니다."% treeHit)
#     if treeHit == 10:
#         print("나무 넘어갑니다.")


# coffee = 10
# while True:
#     money = int(input("돈을 넣어주세요:"))
#     if money == 300:
#         print("커피 줍니다")
#     elif money > 300:
#         print(f"거스름돈{money - 300}를 주고 커피를 줍니다.")
#     else:
#         print(f"{money}을 다시 돌려주고 커피를 주지않습니다.")
#     if not coffee:
#         print("커피다 다 떨어졌습니다. 판매를 중지합니다.")
#         break

#     print(f"남은 커피의 양은{coffee}개 입니다.")


# n = int(input())
# power = 1
# for i in range(n):
#     print("*" * power)
#     power += 1
#     if power == n:
#         break
# for i in range(n):
#     print("*" * power)
#     power -= 1

# j = 0
# i = 0
# while i < 10:
#     j = 0
#     print(f"i = {i}")
#     while j < 10:
#         print(f"j = {j}\t", end='')
#         j += 1
#     print()
#     i += 1

# dan = 2
# while dan < 10:
#     i = 1
#     while i < 10:
#         print(f"{dan} * {i} = {dan * i}\t", end="")
#         i += 1
#     print()
#     dan += 1