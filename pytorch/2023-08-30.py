# class Test:
#     def __init__(self, name):
#         self.name = name
#         print("{} - 생성되었습니다.".format(self.name))
#     def __del__(self):
#         print(f"{self.name} - 파괴되었습니다.")


# Test("A")
# Test("B")
# Test("C")

# import math

# class Circle:
#     def __init__(self, radius):
#         self.__radius = radius
#     def get_circumference(self):
#         return 2 * math.pi * self.__radius
#     def get_area(self):
#         return math.pi * (self.__radius ** 2)
#     def set_radius(self, value):
#         if value <= 0:
#             raise TypeError("길이는 양의 숫자여야 합니다.")
#         self.__radius = value

# circle = Circle(10)
# print("# 원의 둘례와 넓이를 구합니다.")
# print("원의 둘례:", circle.get_circumference())
# print("원의 넓이:", circle.get_area())
# print()

# class Parent:
#     def __init__(self):
#         self.value = "테스트"
#         print("Parent 클래스외 __init()__ 메소드가 호출되었습니다.")
#     def test(self):
#         print("Parent 클래스의 test() 메소드입나다.")

# class Child(Parent):
#     def __init__(self):
#         super().__init__(self)
#         print("Child 클래스의 __init()__ 메소드가 호출되었습니다.")
    

# child = Child()
# child.test()
# print(child.value)


# class CustomException(Exception):
#     def __init__(self):
#         Exception.__init__(self)

# raise CustomException


# res1 = 0
# res2 = 0

# def adder1(num):
#     global res1
#     res1 += num
#     return res1

# def adder2(num):
#     global res2
#     res2 += num
#     return res2

# adder1(1)
# adder2(3)
# adder2(2)
# adder1(4)

# print(res1, res2)


# class Calculator:
#     def __init__(self):
#         self.result = 0

#     def adder(self, num):
#         self.result += num
#         return self.result

# cal1 = Calculator()
# cal2 = Calculator()

# cal1.adder(7)
# cal2.adder(5)
# cal1.adder(1)
# cal2.adder(5)

# print(cal2.result)
# print(cal1.result)


# class Service:
#     secret = "영구는 배꼽이 두 개다"
#     def setname(self, name):
#         self.name = name
#     def sum(self, a, b):
#         result = a + b
#         print(f"{self.name}님 {a} + {b}는 {a+b}입니다.")

# pey = Service()
# pey.setname("홍길동")
# pey.sum(1, 1)

# pal = Service()
# pal.setname("김홍균")
# pal.sum(3, 5)


# class HousePark:
#     lastname = "박"
#     def __init__(self, name):
#         self.fullname = self.lastname + name
#     def travel(self, where):
#         print(f"{self.fullname}, {where}여행을 가다")



# pey = HousePark("응용")
# pey.setname("응용")
# pey.travel("부산")

# pes = HousePark()

# print(pey.travel)


# class HousePark:
#     lastname = "박"
#     def __init__(self, name):
#         self.fullname = self.lastname + name
#     def travel(self, where):
#         print(f"{self.fullname}, {where}여행을 가다")
#     def love(self, other):
#         print(f"{self.fullname}, {other.fullname} 사랑에 빠졌네")
#     def __add__(self, other):
#         print(f"{self.fullname}, {other.fullname} 결혼했네")

# class HouseKim(HousePark):
#     lastname = "김"
#     def travel(self, where, day):
#         print(f"{self.fullname}, {where}여행 {day}일 가다")

# pey = HousePark("응용")
# juliet = HouseKim("졸리엣")
# pey.love(juliet)
# pey + juliet


# print(list(filter(lambda x: x > 0, [1, -3, 2, 0 ,-5, 6])))


# a = 3 
# print(id(3))
# print(id(a))
# b = a
# print(id(b))


# myList = [lambda a, b: a+b, lambda a,b :a*b]

# print(myList[0](3, 4))
# print(myList[1](3, 4))


# def two_times(x):return x * 2

# print(list(map(two_times,[1,2,3,4])))
1, 2
def test(*args):
    result = 0
    for i in args:
        result += 1
    return result / i
print(test(2,2,5,6,5))