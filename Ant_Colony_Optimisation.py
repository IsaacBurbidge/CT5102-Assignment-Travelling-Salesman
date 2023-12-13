import pandas as pd
import Pheromone_Script as ps
import math
import random
import numpy
import os.path

EPSILON = 1e-5 #constant 

def _find_shortest_route():
    global pheromones, data
    previousdist, previousroute = _read_from_file() # get the data from a file
    antsperiteration = int(input("How many Ants per iteration?"))
    iterations = int(input("How many iterations?"))
    data = pd.read_csv("converteddata.csv")
    loaddata = _check_to_load_data(previousroute) # see if the data can be loaded
    if loaddata: # if we load data, get the previous pheromone file
        pheromones = pd.read_csv("finalpheromones.csv")
    else: # generate a pheromone map
        ps._generate_pheromones(data.shape[0])
        pheromones = pd.read_csv("pheromones.csv")
    _run_ants(antsperiteration, iterations, previousdist, previousroute, loaddata)

#Map function that reduces all pheromones
def _degrade_pheromones(pheromone):
    if pheromone == -1:
        return -1
    else:
        return int((pheromone *0.95)//1)

#adds 50 pheremones to any pair of cities that were in a route, e.g. if an ant goes from [1] to [0] then [1][0] would get +50
def _add_pheromones(route):
    for i in range (0, data.shape[0]):
        nextindex = (i+1)%data.shape[0]
        pheromones.iat[route[i],route[nextindex]] = pheromones.iat[route[i],route[nextindex]] + 50

def _traverse_graph(startnode):
    ALPHA = 0.9 # constants for weighting jumps later on
    BETA = 1.5
    
    
    visitedList = numpy.asarray([1 for _ in range(data.shape[0])]) # an array of 1's
    visitedList[startnode] = 0 # if it is visited, we set it to be 0
    
    route = [] # current route is null
    currentnode = startnode # get the start node
    totaldistance = 0
    
    for steps in range(0,data.shape[0]):
        route.append(currentnode) # add the current node
        jumps_neighbors = [] # the list of possible nodes to go to
        jumps_values = [] # the weights of each node
        
        for i in range(0,data.shape[0]):
            if visitedList[i] != 0: # if unvisited
                pheromone_level = max(pheromones.iat[currentnode, i], EPSILON) # we get the max between the current pheromone level and EPSILON, EPSILON added to encourage exploration
                v = math.pow(pheromone_level,ALPHA) / math.pow(data.iat[currentnode, i], BETA) # V is our value of weighting, pheromones to the power of 0.9 and distance to 1.5
                jumps_neighbors.append(i)
                jumps_values.append(v)

        if len(jumps_neighbors) > 0: # if we have at least one option
            next_node = random.choices(jumps_neighbors, weights = jumps_values)[0] # randomly picks the next node using the weights assigned above
        else:
            next_node = startnode # loop

        totaldistance += data.iat[currentnode, next_node] # gets the distance between the current and next node
        visitedList[next_node] = 0 # the next node is visited
        currentnode = next_node # next node is current

    if len(route) == data.shape[0]: # make sure the route is a loop
        route.append(startnode)

    
    return route, totaldistance


def _run_ants(antsperiteration, iterations, previousdist, previousroute, loaddata):
    global pheromones
    
    bestroute = []
    bestdistance = 0
    if loaddata: # if the user wants to load data, we do so
        print("loaded")
        bestroute = previousroute
        bestdistance = previousdist

    for i in range(0, iterations): # for each iteration
        antRouteList = [_traverse_graph(random.randint(0,data.shape[0]-1)) for i in range (0, antsperiteration)] # returns a list of routes and distances for each ant in the iteration, starting at a random point
        antRouteList.sort(key = lambda x: x[1]) # sort by distance
        for j in range(0,len(antRouteList)): # we add pheromones to each route
            _add_pheromones(antRouteList[j][0])
        if bestroute == []: # if there isnt a best route yet
            bestroute = antRouteList[0][0]
            bestdistance = antRouteList[0][1]
        elif antRouteList[0][1] < bestdistance: # if the best of this iteration is the new best
            bestroute = antRouteList[0][0]
            bestdistance = antRouteList[0][1]
        print(i)
        print(antRouteList[0])
        print(bestdistance)
        pheromones = pheromones.map(_degrade_pheromones) # degrades all the pheromones
        print(pheromones)
        _write_best_distance_to_file(bestroute, bestdistance) # checks if we should save it to a file
    print(bestroute)
    print(bestdistance)
    _write_best_distance_to_file(bestroute, bestdistance) # saves the best 
    _write_pheromones_to_file() # saves our pheromone map
  
#writes the final pheromones to a file
def _write_pheromones_to_file():
    if os.path.isfile('./finalpheromones.csv'):
        os.remove('finalpheromones.csv')
    pheromones.to_csv('finalpheromones.csv', index = False)

#writes distance and route to file, only writes if a) the size of the data is different or b) a better route has been found
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
        
#gets the data from BestDistance.txt
def _read_from_file():
    route = []
    if os.path.isfile('./BestDistance.txt'):
        with open('BestDistance.txt') as file:
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
    
    return dist, route

#if our best route (from bestdistance.txt) is the same as our current route size, we check if they want to continue
def _check_to_load_data(route):
    if len(route)-1 == data.shape[0]:
        useloadeddata = input("Would you like to load data? Y/N")
        if useloadeddata == "Y":
            return True
    return False

