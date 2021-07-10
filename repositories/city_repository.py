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

def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['name'], country, row['attractions'], row['temperature'], row['id'], row['visited'])
        cities.append(city)
    return cities

def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = country_repository.select(result["id"])
        city = City(result["name"], country, result["attractions"], result["temperature"], result["id"], result["visited"])
    return city

# def select_all():
#     tasks = []

#     sql = "SELECT * FROM tasks"
#     results = run_sql(sql)

#     for row in results:
#         user = user_repository.select(row['user_id'])
#         task = Task(row['description'], user, row['duration'], row['completed'], row['id'] )
#         tasks.append(task)
#     return tasks

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
