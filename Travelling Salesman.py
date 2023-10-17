import pandas as pd
import math

tableofleastdistances = []

visitedcities = []

distance = 0

data = pd.read_csv("coverteddata.csv")

visitedcities = []


def _find_closest_path(currentcity, distance):
    i = 0
    currentcitydistancelist = []
    for item in tableofleastdistances[currentcity]:
        currentcitydistancelist[i] = [item]
    currentcitydistancelist.sort()
    nextcity = 0 
    i = 0
    while nextcity in visitedcities:
        citylist = list(currentcitydistancelist) 
        nextcity = citylist[i][0]
        i+= 1
        if(i == len(tableofleastdistances)):
            break
    if(i == len(tableofleastdistances)):
        distance += currentcitydistancelist.get(0)#[0][1]
        nextcity = 0
    else:
        distance += currentcitydistancelist.get(i)#[i][1]
    visitedcities.append(nextcity)
    currentcity = nextcity
    print(currentcity)
    return currentcity
                                    

def _route_finder():
    currentcity = 0
    distance = 0
    print(len(tableofleastdistances))
    while len(visitedcities) < len(tableofleastdistances):
        currentcity = _find_closest_path(currentcity, distance)
    print(distance)
    print(visitedcities)

def _is_prime_(Number):
    factoramount = 0

    for i in range(1, Number+1):
        if Number%i == 0:
            factoramount += 1
            if factoramount > 2:
                break
    if factoramount == 2 or Number == 1:
        return True
    else:
        return False

def _write_to_file():
    newdata = pd.DataFrame(tableofleastdistances)
    newdata.to_csv('coverteddata.csv', index=False)

def main():
    _create_distance_matrix()
    _find_initial_distances()
    _write_to_file()
    _route_finder()

main()

