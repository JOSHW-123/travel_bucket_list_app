class Country:

    def __init__(self, name, popular_destinations, population, language, currency, id = None, visited = False):
        self.name = name
        self.popular_destinations = popular_destinations
        self.population = population
        self.language = language
        self.id = id
        self.visited = visited
