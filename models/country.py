class Country:
    def __init__(self, name, geographical_area, population, language, currency, visited = None, id = None):
        self.name = name
        self.geographical_area = geographical_area
        self.population = population
        self.language = language
        self.currency = currency
        self.visited = visited
        self.id = id

def mark_visited(self):
        self.visited = True