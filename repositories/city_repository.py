from db.run_sql import run_sql

from models.city import City
from models.country import Country

import repositories.country_repository as country_repository

def save(city):
    sql = "INSERT INTO cities (name, country, attractions, temperature, country_id, visited) VALUES (%s,%s,%s,%s,%s,%s) RETURNING *"
    values = [city.name, city.country, city.attractions, city.temperature, city.country.id, city.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city


# self.name = name
# self.country = country
# self.attractions = attractions 
# self.temperature = temperature
# self.id = id
# self.visited = visited

# def save(task):
#     sql = "INSERT INTO tasks (description, user_id, duration, completed) VALUES (%s, %s, %s, %s) RETURNING *"
#     values = [task.description, task.user.id, task.duration, task.completed]
#     results = run_sql(sql, values)
#     id = results[0]['id']
#     task.id = id
#     return task
