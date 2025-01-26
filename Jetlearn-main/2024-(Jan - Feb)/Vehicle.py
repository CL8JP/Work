class Vehicle:
    Power: int = 0
    Name: str = "Vehicle"

    def Start(self):
        print(self.Power)

        return self

    def __str__(self):
        return f"{self.Power} {self.Name}"

    def __init__(self, Power):
        self.Power = Power


class Car(Vehicle):
    Name: str = "Car"

    def __init__(self, Power):
        super().__init__(Power)


print(str(Car(100).Start()))

for _ in range(100):
    print(hash("h"))
