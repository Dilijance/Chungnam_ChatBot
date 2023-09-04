import datetime
import turtle as t

# def test():
#     print("A 지점 통과")
#     yield 1
#     print("B 지점 통과")
#     yield 2
#     print("C 지점 통과")

# output = test()

# print("D 지점 통과")
# a = next(output)
# print(a)
# print("E 지점 통과")
# b = next(output)
# print(b)
# print("F 지점 통과")
# c = next(output)
# print(c)

# next(output)


# list_a = ["52", '32', 'fds', '61']

# list_nums = []

# for item in list_a:
#     try:
#         float(item)
#         list_nums.append(item)
#     except:
#         pass

# print(f"{list_a}")
# print(f"{list_nums}")


# try:
#     file = open("info.txt", "w")

#     file.close
# except Exception as e:
#     print(e)

# print("파일이 제대로 닫혔는지 확인하기")
# print("file.closed", file.closed)


# def test():
#     print("test()함수의 첫 줄입니다")
#     try:
#         print("try")
#         return
#     except:
#         print("except")
#     else:
#         print("else")
#     finally:
#         print("finally")
#     print("test()")

# test()


# now = datetime.datetime.now


# print("datetime.timedelta로 시간 더하기")

# after = now + datetime.timedelta(
#     weeks = 1,
#     days = 1,
#     hours = 1,
#     minutes = 1,
#     seconds = 1
# )

# print(now)
# print(after.strftime("%Y{} %m{} %D{} %H{} %M{} %s{}").format(*"년월일시분초"))
# print()

# print("now.replace()로 1년 더하기")

# output = now.replace(year=(now.year + 1))
# print(output.strftime("%Y{} %m{} %D{} %H{} %M{} %s{}").format(*"년월일시분초"))




# import time

# print('지금부터 5초동안 정지합니다!!')

# time.sleep(5)

# print("프로그램을 종료합니다.")



# from urllib import request


# target = request.urlopen("https://google.com")

# output = target.read()
# print(output)


