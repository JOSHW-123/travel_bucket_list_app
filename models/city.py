class City:

    def __init__(self, name, attractions, visited = False):
        self.name = name
        self.attractions = attractions
        self.visited = visited

    def mark_visited(self):
        self.visited = True