DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    city_name VARCHAR(255),
    visited BOOLEAN,
    attractions VARCHAR(255)

)

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    country_name VARCHAR(255),
    visited BOOLEAN,
    popular_destinations VARCHAR(255)

)