class Country:
    def __init__(self, name, geographical_area, population, language, currency, id = None, visited = False):
        self.name = name
        self.geographical_area = geographical_area
        self.population = population
        self.language = language
        self.currency = currency
        self.id = id
        self.visited = visited

def mark_visited(self):
        self.visited = True