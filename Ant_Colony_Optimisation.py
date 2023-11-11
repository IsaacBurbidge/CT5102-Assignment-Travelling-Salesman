import pandas as pd
import math
import random
import numpy

data = pd.read_csv("coverteddata.csv")
#pheremones = pd.read_csv("pheremones.csv")



def _degrade_pheremones(pheremone):
    if pheremone == -1:
        return -1
    else:
        return int((pheremone *0.95)//1)
    print(pheremones)

def _add_pheremones(route):
    for i in range (0, 5000):
        if i == 4999:
            pheremones.iloc[route[i],route[0]] = int((pheremones.iloc[route[i],route[0]]*1.2)//1)
        else:
            pheremones.iloc[route[i],route[i+1]] = int((pheremones.iloc[route[i],route[i+1]]*1.2)//1)
    #return pheremones
    print(pheremones)

#def _apply_pheremone(route):
    #pheremones =
    #pheremones.map(_degrade_pheremones)
    #pheremones =
    #_add_pheremones(route, pheremones)
    #print(pheremones)
    #return pheremones

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
            next_node = startnode

        totaldistance += data.iat[currentnode, next_node]
        visitedList[next_node] = 0
        currentnode = next_node
        route.append(currentnode)
        steps +=1
    _add_pheremones(route)
    #_apply_pheremone(route)
    return route, totaldistance


def _run_ants():
    antsperiteration = 2
    iterations = 3
    bestroute = []
    bestdistance = 0
    for i in range(0, iterations):
        antRouteList = [_traverse_graph(random.randint(0,5000)) for i in range (0, antsperiteration)]
        antRouteList.sort(key = lambda x: x[1])
        #route, totaldistance = _traverse_graph(0)
        if bestroute == []:
            bestroute = antRouteList[0][0]
            bestdistance = antRouteList[0][1]
        elif antRouteList[0][1] < bestdistance:
            bestroute = antRouteList[0][0]
            bestdistance = antRouteList[0][1]
        print(i)
        print(antRouteList[0])
        #print(totaldistance)
        pheremones.map(_degrade_pheremones)
    print(bestroute)
    print(bestdistance)
    _write_to_file()
  
def _write_to_file():
    pheremones.to_csv('finalpheremones.csv', index = False)

def _find_shortest_route():
    global pheremones
    pheremones = pd.read_csv("pheremones.csv")
    _run_ants()
    



