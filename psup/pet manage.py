class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof")

my_dog = Dog("coco", "chihuahua")
my_dog.bark()
