class Student:
    name = ""
    age = 0
    sex = ""
    score = 0

tivadar = Student()
print(tivadar)

tivadar.name = "El Tivadar"
tivadar.age = 16
tivadar.sex = "male"
tivadar.score = 20

print(f"Név: {tivadar.name}, Kor: {tivadar.age}, Pontszám: {tivadar.score}")