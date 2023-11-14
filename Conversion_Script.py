import pandas as pd
import math
import numpy as np

#Import Dataset
data = pd.read_csv("cities.csv")

tableofleastdistances = []

#Initialises a 5000x5000 matrix (the benchmark)
def _create_distance_matrix(citycount):
    for i in range(0,citycount):
        nullList = []
        for j in range(0,citycount):
            nullList.append(-1)
        tableofleastdistances.append(nullList)

#Sets up the matrix to be the euclidean distances between each pair of cities
def _find_initial_distances(citycount):
    for i in range(0,citycount):
        for j in range(0,citycount):
            #Doesnt run on connections to itself
            if i == j:
                pass
            #Only checks elements that are NULL (-1)
            elif tableofleastdistances[i][j] == -1:
                x_length = data.at[data.index[i],'X'] - data.at[data.index[j],'X'] # gets the x distance between cities
                y_length = data.at[data.index[i],'Y'] - data.at[data.index[j],'Y'] # gets the y distance between cities
                path_length = (x_length*x_length) + (y_length*y_length)
                path_length = math.sqrt(path_length) # calculate the euclidean distance
                tableofleastdistances[i][j] = path_length # sets the distance between nodes, as it is undirected it is a square matrix e.g. [0][1] == [1][0]
                tableofleastdistances[j][i] = path_length

#Saves the matrix of distances to a file
def _write_to_file():
    dataToWrite = pd.DataFrame(tableofleastdistances)
    dataToWrite.to_csv('converteddata.csv', index = False)

#External function called to run this script
def _convert_data():
    citycount = int(input("How many cities do you want in your dataset?"))
    _create_distance_matrix(citycount)
    _find_initial_distances(citycount)
    _write_to_file()

