class Dog:
    def __init__(self, name):
        self.name = name
        print("Dog ~~")

    def speak(self):
        print("GGGG", self.name)

    def __del__(self):
        print("del")


class Puppy(Dog):
    def __init__(self):
        self.name = "puppy"

ddd = Dog("ddd")
aaa = Dog("aaaa")


ddd.speak()

p = Puppy()
p.speak()



print(p.name)


