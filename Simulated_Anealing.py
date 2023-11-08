import pandas as pd
import math
import random

data = pd.read_csv("coverteddata.csv")

iterations = 1000
start_temperature = 800.0
current_temperature = start_temperature

def _simulated_anealing():
    global current_temperature, cities


    for i in range(0, iterations):
        new_cities = city_swap(cities)

        current_objective_score = objective_function(cities)
        new_objective_score = objective_function(new_cities)

        if make_swap(current_objective_score, new_objective_score, current_temperature):
            cities = new_cities

        current_temperature = current_temperature - 1
    print(cities)
    print(objective_function(cities))


def make_swap(original_score, new_score, temperature):
    random_chance = random.randint(0, start_temperature)

    swap = True

    if original_score < new_score:
        swap = False
        if random_chance < temperature:
            swap = True

    if original_score > new_score:
        swap = True
        if random_chance < temperature:
            swap = False
        
    return swap

def city_swap(cities_list):
    citya = random.randrange(0, len(cities_list))
    cityb = random.randrange(0, len(cities_list))

    new_cities_list = list(cities_list)

    new_cities_list[citya], new_cities_list[cityb] = cities_list[cityb], cities_list[citya]

    return new_cities_list

def objective_function(cities_list):
    cumulative_dist = euclidean_distance(cities_list[0], cities_list[-1])

    for i in range(0, len(cities_list) - 1):
        cumulative_dist = cumulative_dist + euclidean_distance(cities_list[i], cities_list[i+1])

    return cumulative_dist

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 +
              (city1[1] - city2[1])**2)
