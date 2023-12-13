import pandas as pd
import math

visitedcities = []

#Finds the nearest city to the current city
def _find_closest_path(currentcity, distance):
    global data # gets the data file
    currentcitydistancedict = list(data.loc[currentcity]) # gets all connections 
    sorteddistancelist = sorted(currentcitydistancedict) # sorts connections from smallest to greatest
    nextcity = 0 # the next city we visit
    i = 0
    if sorteddistancelist[0] == -1: # link to itself
        i = 1
    while nextcity in visitedcities: # while the next city is in our visited list
        currentdistance = sorteddistancelist[i] # the next element
        nextcity = currentcitydistancedict.index(currentdistance)
        i += 1 # increment our index
        if(i == len(data.index)): # if we are at the size of the data
            break
    if(i == len(data.index)):
        distance += currentcitydistancedict[0] # the distance from the end node to the start node
    else:
        distance += currentcitydistancedict[i] # the distance from the current node to the end node
    visitedcities.append(nextcity) # add the next city
    currentcity = nextcity # set it to be the current city
    return currentcity, distance

#External function called to run this script                                    
def _route_finder(firstcity):
    global data
    data = pd.read_csv("converteddata.csv") # read the data
    currentcity = firstcity # the initial city we start at, for this it is always 0
    distance = 0 # the current route distance
    visitedcities.append(currentcity) # add the first city to our visited list
    while len(visitedcities) < len(data.index):
        currentcity, distance = _find_closest_path(currentcity, distance)
    visitedcities.append(0) # makes it loop
    print(distance)#outputs the final values
    print(visitedcities)
    

