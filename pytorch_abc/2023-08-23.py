import random

# dictionary = {
#     "name": "7D 검조 망고",
#     "type": "당절임",
#     "ingredient": ['망고', '설탕'],
#     "origin": "필리핀"
# }

# print("name", dictionary["name"])
# print("type", dictionary["type"])
# print("ingredient", dictionary["ingredient"])
# print("origin", dictionary["origin"])
# print()

# dictionary['name'] = "8D 건조 망고"
# print("name: ", dictionary["name"])


# print(random.random())

# print(random.randint(0, 3))


# numbers = []
# while len(numbers) < 7:
#     number = random.randint(1, 10)
#     if number not in numbers:
#         numbers.append(number)
# print(numbers)


# key = input("> 접근하고자 하는 키: ")

# if key in dictionary:
#     print(dictionary[key])
# else:
#     print("존재하지 않는 키에 접근하고 있습니다.")

# value = dictionary.get("존재하지 않는 키")
# print("값", value)

# if value == None:
#     print("존재하지 않는 키에 접근했었습니다.")


# for key in dictionary:
#     print(key, ":", dictionary[key])


# character = {"name":"기사", "level": 12, "items":{"sword":"불꽃의 검", "armor":"풀플레이트"}, "skill":["베기","세게 베기", "아주 세게 베기"]}

# for key in character:
#     if type(character[key]) == dict:
#         for j in character[key]:
#             print(j, ":", character[key][j])
#     elif type(character[key]) == list:
#         for j in character[key]:
#             print(key, ":", j)
#     else:
#         print(key, ":", character[key])


# array = [273, 32, 103, 57, 52]

# for i in range(len(array)):
#     print(f"{i}번째 반복: {array[i]}")


# for i in range(4, 0, -1):
#     print(f"현재 반복 변수: {i}")


# numbers = [5, 15, 6, 20, 7, 25]

# for number in numbers:
#     if number < 10:
#         continue
#     print(number)


# key = ["name", "hp", "mp", "level"]
# value = ["기사", 200, 30, 5]
# character = {}

# for i in range(4):
#     character[key[i]] = value[i]

# print(character)


# limit = 10000
# i = 1
# sum = 0

# while sum < limit:
#     sum = 0
#     for j in range(i + 1):
#         sum += j
#     i += 1

# print(i - 1, limit, sum)


# # max =0
# # a = 0
# # b = 0

# for i in range(101):
#     j = 100 - i
#     if j * i > max:
#         max = j * i
#         a = j
#         b = i
    
# # print(b, a, max)


# example_dictionary = {
#     "키A":"값A",
#     "키B":"값B",
#     "키C":"값C"
# }

# print("")

# print(example_dictionary.items())
# print()

# for key, element in example_dictionary.items():
#     print(f"dictionary[{key}] = {element}")


# array = []

# for i in range(0, 20, 2):
#     array.append(i * i)

# print(array)

# array = [i * i for i in range(0, 20, 2)]
# print(array)


# array = ["사과", "자두", "초콜릿", "바나나", "체리"]
# output = []
# for fruit in array:
#     if fruit != "초콜릿":
#         output.append(fruit)

# print(output)

# output = [fruit for fruit in array if fruit != "초콜릿"]

# print(output)


# n = int(input())

# i = 0
# space = 0
# for i in range(n):
#     space = n - i
#     print("* " * (i + 1), "  " * (space - 1), "* " * (n - i), sep="")

# i = 0
# space = 0
# for i in range(n, i, -1):
#     space = i
#     print("  " * (space - 1), "* " * (n - i + 1), "  " * (n - i), "* " * i, sep="")


# tank = 1000
# fish = 2
# day = 1

# print(f"day:{0}\tfishes:{fish}\tborn: +{0}\tdead: -{0}")
# while fish < tank:
#     born = 0
#     dead = 0
#     for birth in range(fish // 2):
#         born += random.randint(1, 10)
#         if fish > tank:
#             break
#     fish += born
#     if day >= 2:
#         dead = (random.randint(1, 5)) * 2
#         fish -= dead
#         if fish <= 1:
#             break
#     print(f"day:{day}\tfishes:{fish}\tborn: +{born}\tdead: -{dead}")
#     day += 1




