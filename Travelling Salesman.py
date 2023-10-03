import pandas as pd
import math

data = pd.read_csv("cities.csv")

#tableofleastdistances 

#tableofleastdistances = []

visitedcities = []

#distance = 0

#def _create_distance_matrix():
#    i = 0
#    nullList = []
#    for item in data.index:
#        i += 1
#        nullList.append(-1)
#   
#    for item in data.index:
##        tableofleastdistances.append(nullList)
#    print("matrixmade")
#
#def _find_initial_distances():
#    for i in data.index:
#        for j in data.index:
#            if i == j:
#                break
#            elif tableofleastdistances[i][j] == -1:
#                x_length = data.at[data.index[i],'X'] + data.at[data.index[j],'X']
#                y_length = data.at[data.index[i],'Y'] + data.at[data.index[j],'Y']
#                path_length = (x_length**2) + (y_length**2)
#                path_length = math.sqrt(path_length)
#                tableofleastdistances[i][j] = path_length
#                tableofleastdistances[j][i] = path_length
#    print("distancesinitialised")


def _find_closest_path(currentcity, distance):
    i = 0
    currentcitydistancelist = {}
    for item in tableofleastdistances[currentcity]:
        currentcitydistancelist[i] = [item]
        #= tableofleastdistances[currentcity]
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

def main():
    #_create_distance_matrix()
    #_find_initial_distances()
    _route_finder()

main()

