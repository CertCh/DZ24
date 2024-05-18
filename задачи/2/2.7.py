class Airline:
    def __init__(self):
        self.airplanes = []
        self.routes = []

    def add_airplane(self, airplane):
        self.airplanes.append(airplane)
    
    def remove_airplane(self, airplane):
        if airplane in self.airplanes:
            self.airplanes.remove(airplane)
    
    def create_route(self, route):
        self.routes.append(route)
    
    def remove_route(self, route):
        if route in self.routes:
            self.routes.remove(route)
    
    def find_airplane_by_model(self, model):
        for airplane in self.airplanes:
            if airplane.model == model:
                return airplane
        return None

    def find_routes_from_city(self, city):
        return [route for route in self.routes if route.start_city == city]


class Airplane:
    def __init__(self, model):
        self.model = model

class Route:
    def __init__(self, start_city, end_city):
        self.start_city = start_city
        self.end_city = end_city

airline = Airline()
airplane1 = Airplane("Boeing 737")
airplane2 = Airplane("Airbus A320")
route1 = Route("New York", "London")
route2 = Route("Paris", "Berlin")
airline.add_airplane(airplane1)
airline.add_airplane(airplane2)
airline.create_route(route1)
airline.create_route(route2)
found_airplane = airline.find_airplane_by_model("Airbus A320")
print(found_airplane.model)  
routes_from_paris = airline.find_routes_from_city("Paris")
print([(route.start_city, route.end_city) for route in routes_from_paris])  # Вывод: [('Paris', 'Berlin')]
