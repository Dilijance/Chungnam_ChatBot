# marks = [90, 25, 67, 45, 80]

# number = 0

# for mark in marks:
#     number += 1
#     if mark >= 60:
#         print(f"{number}번 학생은 합격입나다.")
#     else:
#         print(f"{number}번 학생은 불합격입니다.")

# def fibonacci(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 1)
    

# dictionary = {
#     1: 1,
#     2: 1
# }

# def fibonacci(n):
#     if n in dictionary:
#         return dictionary[n]
#     else:
#         output = fibonacci(n - 1) + fibonacci(n - 2)
#         dictionary[n] = output
#         return output
    
# print(fibonacci(35))


# def flatten(data):
#     result = []
#     if type(data) is list:
#         for el in data:
#             result += flatten(el)
#     else:
#         result += [data]
#     return result

# example = [[1, 2, 3], [4,[5, 6]], 7, [8, 9]]
# example = flatten(example)
# print(example)


# def call_10_times(func):
#     for i in range(10):
#         func()

# def print_hello():
#     print("Hello")

# call_10_times(print_hello)


# def power(item):
#     return item * item
# def under_3(item):
#     return item < 3

# list_input_a = [1, 2, 3, 4, 5]

# output_a = map(power, list_input_a)
# print("# map() 함수의 실행결과")
# print("map(power, list_input_a):", output_a)
# print("map(power, list_input_a):", list(output_a))
# print()

# output_b = filter(under_3, list_input_a)
# print("# filter() 함수의 실행결과")
# print(output_b)
# print(list(output_b))
