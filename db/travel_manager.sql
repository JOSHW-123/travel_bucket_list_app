DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;


CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    country_name VARCHAR(255),
    geographical_area VARCHAR(255),
    country_population VARCHAR(255),
    country_language VARCHAR(255),
    currency VARCHAR(255),
    visited BOOLEAN
    
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    city_name VARCHAR(255),
    country VARCHAR(255),
    attractions VARCHAR(255),
    temperature VARCHAR(255),
   
    visited BOOLEAN
    

);



