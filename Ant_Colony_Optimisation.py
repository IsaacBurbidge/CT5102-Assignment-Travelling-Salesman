import pandas as pd
import Pheromone_Script as ps
import math
import random
import numpy
import os.path

EPSILON=1e-5

def _find_shortest_route():
    global pheromones, data
    previousdist, previousroute = _read_from_file()
    antsperiteration = int(input("How many Ants per iteration?"))
    iterations = int(input("How many iterations?"))
    data = pd.read_csv("converteddata.csv")
    loaddata = _check_to_load_data(previousroute)
    ps._generate_pheromones(data.shape[0])
    pheromones = pd.read_csv("pheromones.csv")
    _run_ants(antsperiteration, iterations, previousdist, previousroute, loaddata)

def _degrade_pheromones(pheromone):
    if pheromone == -1:
        return -1
    else:
        return int((pheromone *0.95)//1)

def _add_pheromones(route):
    for i in range (0, data.shape[0]):
        nextindex = (i+1)%data.shape[0]
        pheromones.iat[route[i],route[nextindex]] = pheromones.iat[route[i],route[nextindex]] + 50

def _traverse_graph(startnode):
    ALPHA = 0.9
    BETA = 1.5
    
    
    visitedList = numpy.asarray([1 for _ in range(data.shape[0])])
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
                pheromone_level = max(pheromones.iat[currentnode, i], EPSILON) #constant added to encourage exploration
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


def _run_ants(antsperiteration, iterations, previousdist, previousroute, loaddata):
    global pheromones
    
    bestroute = []
    bestdistance = 0
    if loaddata:
        print("loaded")
        bestroute = previousroute
        bestdistance = previousdist

    for i in range(0, iterations):
        antRouteList = [_traverse_graph(random.randint(0,data.shape[0]-1)) for i in range (0, antsperiteration)]
        antRouteList.sort(key = lambda x: x[1])
        for j in range(0,len(antRouteList)):
            _add_pheromones(antRouteList[j][0])
        if bestroute == []:
            bestroute = antRouteList[0][0]
            bestdistance = antRouteList[0][1]
        elif antRouteList[0][1] < bestdistance:
            bestroute = antRouteList[0][0]
            bestdistance = antRouteList[0][1]
        print(i)
        print(antRouteList[0])
        print(bestdistance)
        pheromones = pheromones.map(_degrade_pheromones)
        print(pheromones)
    print(bestroute)
    print(bestdistance)
    _write_best_distance_to_file(bestroute, bestdistance)
    _write_pheromones_to_file()
  
def _write_pheromones_to_file():
    if os.path.isfile('./finalpheromones.csv'):
        os.remove('finalpheromones.csv')
    pheromones.to_csv('finalpheromones.csv', index = False)

def _write_best_distance_to_file(bestroute, bestdistance):
    previousdist = math.inf
    if os.path.isfile('./BestDistance.txt'):
        with open('BestDistance.txt') as file:
            line = file.readline()
            i = 0
            while line:
                if i == 0:
                    characterlist = []
                    length = ""
                    for j in range(0, len(line)):
                        if line[j].isnumeric() or line[j] == ".":
                            characterlist.append(line[j])
                    length = "".join(characterlist)
                    previousdist = float(length)
                    i += 1
                line = file.readline()
        

    if bestdistance < previousdist:
        linesToWrite = ["Best Distance: "+str(bestdistance), "Best Route: "+str(bestroute)]
        with open('BestDistance.txt', 'w') as file:
            for line in linesToWrite:
                file.write(line)
                file.write("\n")
        
def _read_from_file():
    route = []
    if os.path.isfile('./CurrentBestDistance.txt'):
        with open('CurrentBestDistance.txt') as file:
            line = file.readline()
            i = 0
            isReadingRoute = False
            previousCharacter = ''
            while line:
                if i == 0:
                    characterlist = []
                    length = ""
                    for j in range(0, len(line)):
                        if line[j].isnumeric() or line[j] == ".":
                            characterlist.append(line[j])
                    length = "".join(characterlist)
                    dist = float(length)
                    i += 1
                else:
                    currentIndex = ""
                    for j in range(0, len(line)):
                        if previousCharacter == ":" and line[j] == " ":
                            isReadingRoute = True
                        elif isReadingRoute:
                            if line[j].isnumeric():
                                currentIndex += line[j]
                            elif line[j] == "," or line[j] == "]":
                                route.append(int(currentIndex))
                                currentIndex = ""
                            pass
                        previousCharacter = line[j]
                    pass
                line = file.readline()
    print(dist)
    print(route)
    
    return dist, route

def _check_to_load_data(route):
    if len(route) == data.shape[0]:
        useloadeddata = input("Would you like to load data? Y/N")
        if useloadeddata == "Y":
            return True
    return False

