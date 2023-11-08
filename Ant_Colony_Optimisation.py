import pandas as pd
import math
import random
import numpy

data = pd.read_csv("coverteddata.csv")
pheremones = pd.read_csv("pheremones.csv")


def _degrade_pheremones(pheremone):
    return pheremone*0.95

def _add_pheremones(route):
    for i in range (0, 5000):
        if i == 4999:
            data.iloc[route[i],route[0]] = data.iloc[route[i],route[0]]*1.3
        else:
            data.iloc[route[i],route[i+1]] = data.iloc[route[i],route[i+1]]*1.3

def _apply_pheremone(route):
    pheremones.apply(_degrade_pheremones)
    _add_pheremones(route)


def _traverse_graph(startnode):
    ALPHA = 0.9
    BETA = 1.5
    
    visitedList = {}
    for i in range(0,5000):
        visitedList[i] = -1
    visitedList[startnode] = 0
    
    route = [startnode]
    steps = 0
    currentnode = startnode
    totaldistance = 0
    
    while steps < 5000:
        jumps_neighbors = []
        jumps_values = []
        
        for i in range(0, 5000):
            if visitedList[i] != 0:
                pheromone_level = max(pheremones.iat[currentnode, i], 1e-5) #constant added to encourage exploration
                v = (pheromone_level**ALPHA ) / (data.iat[currentnode, i]**BETA)
                jumps_neighbors.append(i)
                jumps_values.append(v)

        if len(jumps_neighbors) > 0:
            next_node = random.choices(jumps_neighbors, weights = jumps_values)[0]
        else:
            next_node = 0

        totaldistance += data.iat[currentnode, next_node]
        visitedList[next_node] = 0
        currentnode = next_node
        route.append(currentnode)
        steps +=1
    

    return route, totaldistance

def _run_ants():
    iterations = 50
    bestroute = []
    bestdistance = 0
    for i in range(0, iterations):
        route, totaldistance = _traverse_graph(0)
        if bestroute == []:
            bestroute = route
            bestdistance = totaldistance
        _apply_pheremone(route)
    print(bestroute)
    print(bestdistance)
  


def _find_shortest_route():
    _run_ants()



