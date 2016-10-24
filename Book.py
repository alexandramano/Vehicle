class Book():
    def __init__(self):
        self.cars = []

    def add(self, car):
        self.cars.append(car)

    def display(self):
        for car in self.cars:
            car.show()

    def text_file(self):
        file = open("Vehicles.txt", "w")

        for car in self.cars:
            file.write(car.get_info() + "\n")

        file.close()

