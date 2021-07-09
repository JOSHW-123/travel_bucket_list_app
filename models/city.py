class City:

    def __init__(self, name, attractions, temperature, id = None, visited = False):
        self.name = name
        self.attractions = attractions
        self.temperature = temperature
        self.id = id
        self.visited = visited

    def mark_visited(self):
        self.visited = True