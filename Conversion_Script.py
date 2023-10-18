import pandas as pd
import math
import numpy as np


data = pd.read_csv("cities.csv")

tableofleastdistances = []

def _create_distance_matrix():
    for i in range(0,5000):
        nullList = []
        for j in range(0,5000):
            nullList.append(-1)
        tableofleastdistances.append(nullList)
    print("matrixmade")

def _find_initial_distances():
    for i in range(0,5000):
        for j in range(0,5000):
            if i == j:
                pass
            elif tableofleastdistances[i][j] == -1:
                x_length = data.at[data.index[i],'X'] - data.at[data.index[j],'X']
                y_length = data.at[data.index[i],'Y'] - data.at[data.index[j],'Y']
                path_length = (x_length*x_length) + (y_length*y_length)
                path_length = math.sqrt(path_length)
                tableofleastdistances[i][j] = path_length
                tableofleastdistances[j][i] = path_length
    print("distancesinitialised")


def _write_to_file():
    dataToWrite = pd.DataFrame(tableofleastdistances)
    dataToWrite.to_csv('coverteddata.csv', index = False)

def main():
    _create_distance_matrix()
    _find_initial_distances()
    _write_to_file()




main()
