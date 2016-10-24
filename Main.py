from Car import Car
from Book import Book

vehicle_list = Book ()
car1 = Car ("VW", "Polo", 0, "12.08.1986")
car2 = Car ("BMW", "x5", 15, "12.08.2006")
car3 = Car ("VW", "Yolo", 23, "15.08.1986")
car4 = Car ("BMW", "Z5", 76, "18.08.2006")

vehicle_list.add(car1)
vehicle_list.add(car2)
vehicle_list.add(car3)
vehicle_list.add(car4)

vehicle_list.display()
car1.edit(5, "20.10.1981")
car1.show()

vehicle_list.text_file()