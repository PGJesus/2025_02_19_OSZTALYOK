class Student:
    name = ""
    age = 0
    sex = ""
    score = 0

    def introduce(self):
        print(f"Név: {self.name}, Kor: {self.age}, Pontszám: {self.score}")

    def learn(self, points):
        self.score += points 


tivadar = Student()
# print(tivadar)

tivadar.name = "El Tivadar"
tivadar.age = 16
tivadar.sex = "male"
tivadar.score = 20

# print(f"Név: {tivadar.name}, Kor: {tivadar.age}, Pontszám: {tivadar.score}")
tivadar.introduce()
tivadar.learn(12)
tivadar.introduce()
