import random

# def print_n_times(n, *values):
#     for i in range(n):
#         for value in values:
#             print(value)
#         print()

# print_n_times(5, "ew")


# def print_n_times(value, n=2):
#     for i in range(n):
#         print(value)

# print_n_times("안녕하세요")


# def return_test():
#     return 200

# value = return_test()
# print(value)


# def sum_all (start, end):
#     output = 0
#     for i in range(start, end + 1):
#         output += i
#     return output

# output = sum_all(0, 100)
# print(f"0 to 100: {output}")
# print(f"0 to 1000: {sum_all(0, 1000)}")

# def mul(*values):
#     res = 1
#     for i in values:
#         res *= i
#     return res

# print(mul(2, 3, 5))

# hanguls = list("가나다라마바사아자차카타파하")

# with open("info.txt", "w") as file:
#     for i in range(1000):
#         name = random.choice(hanguls) + random.choice(hanguls)
#         weight = random.randrange(40, 100)
#         height = random.randrange(140, 200)

#         file.write(f"{name}, {weight}, {height}")


# with open("info.txt", "r") as file:
#     for line in file:
#         (name, weight, height) = line.strip().split(", ")

#         if (not name) or (not weight) or (not height):
#             continue
#         bmi = int(weight) / ((int(height)/ 100) ** 2)

#         if 25 <= bmi:
#             result = "과세중"
#         elif 18.5 <= bmi:
#             result = "정상 체중"
#         else:
#             result = "저체중"
        
#         print("\n".join([
#             "이름: {}", 
#             "몸무게: {}",
#             "키: {}",
#             "BMI: {}",
#             "결과: {}",
#         ]).format(name, weight, height, bmi, result))
#         print()



