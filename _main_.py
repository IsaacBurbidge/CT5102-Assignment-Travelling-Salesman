import Conversion_Script as cs
import Nearest_Neighbour as nn
#import Christofides_Algorithm as ca
import math


def main():
    #cs._convert_data()
    bestdistance = 0
    bestvisitedcitiedset = []
    distance, visitedcities = nn._route_finder(0,0)
    bestdistance = distance
    bestvisitedcitiedset = list(visitedcities)
    for i in range(1,20):
        nn.visitedcities = []
        distance, visitedcities = nn._route_finder(i,0)
        if distance < bestdistance:
            #print("hi")
            bestdistance = distance
            bestvisitedcitiedset = list(visitedcities)
    print(bestdistance)
    print(bestvisitedcitiedset)

main()
