class City:

    def __init__(self, name, country, attractions, temperature, id = None, visited = False):
        self.name = name
        self.country = country
        self.attractions = attractions
        self.temperature = temperature
        self.id = id
        self.visited = visited

    def mark_visited(self):
        self.visited = True