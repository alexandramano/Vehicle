class Car(object):
    def __init__(self, brand, model, km, service_date):
        self.brand = brand
        self.model = model
        self.km = km
        self.service_date = service_date

    def show(self):
        item = self.get_info()
        print item

    def get_info(self):
        item = "Brand: %s Model: %s KM: %s service_date: %s" % (self.brand, self.model, self.km, self.service_date)
        return item

    def edit(self, new_km, new_date):
         self.km = new_km
         self.service_date = new_date






























