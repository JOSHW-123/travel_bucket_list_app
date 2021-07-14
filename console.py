import pdb 
from models.country import Country
from models.city import City

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

city_repository.delete_all()
country_repository.delete_all()

country_1 = Country("UK", "Europe", "67,000,000", "English", "Pound(£)", True)
country_repository.save(country_1)

country_2 = Country("Germany", "Europe", "83,000,000", "German", "Euro(€)", False)
country_repository.save(country_2)

country_3 = Country("Russia", "Europe/Asia", "144,000,000", "Russian", "Ruble(₽)", True)
country_repository.save(country_3)

country_4 = Country("USA", "North America", "328,000,000", "English", "Dollar($)", True)
country_repository.save(country_4)

country_repository.select_all()

# city.name, city.country, city.attractions, city.temperature, city.country.id, city.visited

city_1 = City("London", country_1, "Tower of London", "23°" )
city_repository.save(city_1)

city_2 = City("Berlin", country_2, "Brandenburg Gate", "24°", )
city_repository.save(city_2)

city_3 = City("Moscow", country_3, "Red Square", "24°", )
city_repository.save(city_3)

city_repository.select_all()

pdb.set_trace()

#         self.name = name
#         self.capital_city = capital_city
#         self.population = population
#         self.language = language
#         self.currency = currency
#         self.id = id
#         self.visited = visited


# from models.user import User

# import repositories.task_repository as task_repository
# import repositories.user_repository as user_repository

# task_repository.delete_all()
# user_repository.delete_all()