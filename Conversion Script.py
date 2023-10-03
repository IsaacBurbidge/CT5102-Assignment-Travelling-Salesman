import pandas as pd
import math
import numpy as np
import time

data = pd.read_csv("cities.csv")

emptyArray = []

tableofleastdistances = pd.DataFrame(emptyArray)

for i in data.index:
    tableofleastdistances = tableofleastdistances.assign(**{str(i): []})
print(tableofleastdistances)

def _create_distance_matrix():
    i = 0
    nullList = []
    for item in data.index:
        i += 1
        nullList.append(-1)
   

    for item in data.index:
        i = 0
        tableofleastdistances.loc[len(tableofleastdistances)] = nullList
        i += 1
    print("matrixmade")

def _find_initial_distances():
    for i in data.index:
        for j in data.index:
            if i == j:
                break
            elif tableofleastdistances[i][j] == -1:
                x_length = data.at[data.index[i],'X'] + data.at[data.index[j],'X']
                y_length = data.at[data.index[i],'Y'] + data.at[data.index[j],'Y']
                path_length = (x_length**2) + (y_length**2)
                path_length = math.sqrt(path_length)
                tableofleastdistances.at[i, j] = path_length
                tableofleastdistances.at[j, i] = path_length
    print("distancesinitialised")

def _write_to_file():
    #newdata = pd.DataFrame(tableofleastdistances)
    tableofleastdistances.to_csv('coverteddata.csv', index=False)

def main():
    _create_distance_matrix()
    #_find_initial_distances()
    _write_to_file()

main()
