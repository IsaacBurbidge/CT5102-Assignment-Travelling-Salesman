import pandas as pd
import Pheremone_Script as ps
import math
import random
import numpy

EPSILON=1e-5

def _find_shortest_route():
    global pheremones, data
    antsperiteration = int(input("How many Ants per iteration?"))
    iterations = int(input("How many iterations?"))
    data = pd.read_csv("converteddata.csv")
    ps._generate_pheremones(data.shape[0])
    pheremones = pd.read_csv("pheremones.csv")
    _run_ants(antsperiteration, iterations)

def _degrade_pheremones(pheremone):
    if pheremone == -1:
        return -1
    else:
        return int((pheremone *0.95)//1)

def _add_pheremones(route):
    for i in range (0, data.shape[0]):
        nextindex = (i+1)%data.shape[0]
        pheremones.iat[route[i],route[nextindex]] = int((pheremones.iat[route[i],route[nextindex]]*1.2)//1)

def _traverse_graph(startnode):
    ALPHA = 0.9
    BETA = 1.5
    
    visitedList = list(range(0,data.shape[0]))
    visitedList[startnode] = 0
    
    route = []
    currentnode = startnode
    totaldistance = 0
    
    for steps in range(0,data.shape[0]):
        route.append(currentnode)
        jumps_neighbors = []
        jumps_values = []
        
        for i in range(0,data.shape[0]):
            if visitedList[i] != 0:
                pheromone_level = max(pheremones.iat[currentnode, i], EPSILON) #constant added to encourage exploration
                v = math.pow(pheromone_level,ALPHA) / math.pow(data.iat[currentnode, i], BETA)
                jumps_neighbors.append(i)
                jumps_values.append(v)

        if len(jumps_neighbors) > 0:
            next_node = random.choices(jumps_neighbors, weights = jumps_values)[0]
        else:
            next_node = startnode

        totaldistance += data.iat[currentnode, next_node]
        visitedList[next_node] = 0
        currentnode = next_node
        
    return route, totaldistance


def _run_ants(antsperiteration, iterations):
    global pheremones
    
    bestroute = []
    bestdistance = 0
    for i in range(0, iterations):
        antRouteList = [_traverse_graph(random.randint(0,data.shape[0])) for i in range (0, antsperiteration)]
        antRouteList.sort(key = lambda x: x[1])
        for j in range(0,len(antRouteList)):
            _add_pheremones(antRouteList[j][0])
        if bestroute == []:
            bestroute = antRouteList[0][0]
            bestdistance = antRouteList[0][1]
        elif antRouteList[0][1] < bestdistance:
            bestroute = antRouteList[0][0]
            bestdistance = antRouteList[0][1]
        print(i)
        print(antRouteList[0])
        print(bestdistance)
        pheremones = pheremones.map(_degrade_pheremones)
        print(pheremones)
    print(bestroute)
    print(bestdistance)
    _write_best_distance_to_file(bestroute, bestdistance)
    #_write_pheremones_to_file()
  
def _write_pheremones_to_file():
    pheremones.to_csv('finalpheremones.csv', index = False)

def _write_best_distance_to_file(bestroute, bestdistance):
    #with open('Distance.txt') as file:
        
    
    linesToWrite = ["Best Distance = "+str(bestdistance), "Best Route = "+str(bestroute)]
    with open('Distance.txt', 'w') as file:
        for line in linesToWrite:
            file.write(line)
            file.write("\n")
    



