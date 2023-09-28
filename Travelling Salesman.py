import pandas as pd

data = pd.read_csv("cities.csv")

tableofleastdistances = []

def _create_distance_matrix():
    for i in data:
        print(i)
    
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


main()



 
#(  o   >     l
