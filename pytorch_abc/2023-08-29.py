from urllib import request
from bs4 import BeautifulSoup

# target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
# soup = BeautifulSoup(target, "html.parser")

# for location in soup.select('location'):
#     print("도시:", location.select_one("city").string)
#     print("날씨:", location.select_one("wf").string)
#     print("최저기온:", location.select_one("tmn").string)
#     print("최고기온:", location.select_one("tmx").string)
#     print()

from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello():
#     target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
#     soup = BeautifulSoup(target, "html.parser")
#     output = ""
#     for location in soup.select("location"):
#         output += "<h3>{}</h3>".format(location.select_one("city").string)
#         output += "날씨{}<br/>".format(location.select_one("wf").string)
#         output += "최저/최고 기온: {}/{}"\
#         .format(
#             location.select_one("tmn").string,
#             location.select_one("tmx").string
#         )
#         output += "<hr/>"

#     return output


import test_module as test

# radius = test.number_input()
# print(test.get_circle_area(10))

# print("# 모듈의 __name__ 출력하기")

# if __name__ == "__main__":
#     print("get_circumference(10):", test.get_circumference(10))
#     print("get_circle_area(10): ", test.get_circle_area(10))


# students = [
#     {"name": "윤인성", "korean": 87, "math": 98, "english": 88, "science": 95},
#     {"name": "연하진", "korean": 92, "math": 98, "english": 96, "science": 98},
#     {"name": "구지연", "korean": 76, "math": 96, "english": 94, "science": 90},
#     {"name": "나선주", "korean": 98, "math": 92, "english": 96, "science": 92},
#     {"name": "윤아린", "korean": 95, "math": 98, "english": 98, "science": 98},
#     {"name": "윤명원", "korean": 64, "math": 88, "english": 92, "science": 92},
# ]

# print("이름", "총점", "평균", sep="\t")

# for student in students:
#     score_sum = student["korean"] + student["math"] + \
#     student["english"] + student["science"]
#     score_average = score_sum / 4

#     print(student["name"], score_sum, score_average, sep="\t")


# class Student:
#     def __init__(self, name, korean, math, english, science):
#         self.name = name
#         self.korean = korean
#         self.math = math
#         self.english = english
#         self.science = science


# students = [
#     Student("윤인성", 87, 98, 88, 95),
#     Student("연하진", 92, 98, 96, 98),
#     Student("구지연", 76, 96, 94, 90),
#     Student("나선주", 98, 92, 96, 92),
#     Student("윤아린", 95, 98, 98, 98),
#     Student("윤인성", 64, 88, 92, 92)
# ]

# for student in students:
#     print(student.name, student.korean, student.math, student.english, student.science)


# class Human:
#     def __init__(self) -> None:
#         pass

# class Student(Human):
#     def __init__(self) -> None:
#         pass
        
# student = Student()

# print("isinstance(student,Human): ", isinstance(student, Human))
# print("type(student) == Human:", type(student) == Human)


# class Student:
#     count = 0

#     def __init__(self, name, korean, math, english, science):
#         self.name = name
#         self.korean = korean
#         self.math = math
#         self.english = english
#         self.science = science

#         Student.count += 1

# students = [
#     Student("윤인성", 87, 98, 88, 95),
#     Student("연하진", 92, 98, 96, 98),
#     Student("구지연", 76, 96, 94, 90),
#     Student("나선주", 98, 92, 96, 92),
#     Student("윤아린", 95, 98, 98, 98),
#     Student("윤명월", 64, 88, 92, 92)
# ]

# print(f"현재 생성된 총 학생 수는 {Student.count}명 입니다.")




# class Student:
#     count = 0
#     students = []

#     def __init__(self, name, korean, math, english, science):
#         self.name = name
#         self.korean = korean
#         self.math = math
#         self.english = english
#         self.science = science
#         Student.students.append(self)
#         Student.count += 1
    
#     @classmethod
#     def print(cls):
#         print("------- 학생 목록 -------")
#         print("이름\t총점\t평균")
#         for student in cls.students:
#             print(str(student))
#         print("------- ------- -------")


# Student("윤인성", 87, 98, 88, 95)
# Student("연하진", 92, 98, 96, 98)
# Student("구지연", 76, 96, 94, 90)
# Student("나선주", 98, 92, 96, 92)
# Student("윤아린", 95, 98, 98, 98)
# Student("윤명월", 64, 88, 92, 97)
# Student("김미화", 77, 68, 92, 92)
# Student("김연화", 55, 82, 93, 82)
# Student("시준시", 42, 67, 90, 72)


# print(f"현재 생성된 총 학생 수는 {Student.count}명 입니다.")

# Student.print()