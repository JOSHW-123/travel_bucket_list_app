import pdb 
from models.country import Country
from models.city import City

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

city_repository.delete_all()
country_repository.delete_all()

country_1 = Country("UK", "London", 67000000, "English", "Pound")
country_repository.save(country_1)

country_2 = Country("Germany", "Berlin", 83000000, "German", "Euro")
country_repository.save(country_2)

country_3 = Country("Russia", "Moscow", 144000000, "Russian", "Ruble")
country_repository.save(country_3)

country_repository.select_all()











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