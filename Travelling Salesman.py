import pandas as pd

data = pd.read_csv("cities.csv")

#tableofleastdistances 

tableofleastdistances = {}

def _create_distance_matrix():
    i = 0
    nullList = []
    for item in data.index:
        i += 1
        nullList.append(-1)
    print("next")
    j = 0
    for item in data.index:
        tableofleastdistances[j] = [nullList]
        j+=1

def _find_initial_distances():
    for i in data.index:
        for j in data.index:
            if i == j:
                break
            else:
                x_length = data.iloc[i][1] + data.iloc[j][1]
                y_length = data.iloc[i][2] + data.iloc[j][2]
                path_length = (x_length*x_length) + (y_length*y_length)
                path_length = math.sqrt(path_length)
                tableofleastdistances[i][j] = path_length
                print(path_length)
                                

                
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
    #IsPrime = _is_prime_(2)
    #print(IsPrime)
    _create_distance_matrix()
    _find_initial_distances()

main()



 
#(  o   >     l
