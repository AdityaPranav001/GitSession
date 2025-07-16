class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def display(self):
        print(f"Car Brand: {self.brand}")
        print(f"Car Model: {self.model}")

car1 = Car("Toyata","Corolla")

car1.display()