import Conversion_Script as cs
import Nearest_Neighbour as nn
import Ant_Colony_Optimisation as aco
import Pheremone_Script as ps
#import Simulated_Anealing as sa
import math


def _display_options():
    validoptions = ["1","2","3", "4"]
    userinput = 0
    while userinput not in validoptions: 
        print("Welcome to the Travelling Salesman Program! Please select one of the options from below!")
        print("1. Convert Data. Please run this once on your computer before attempting to run any of the other options.")
        print("2. Nearest Neighbour Algorithm.")
        print("3. Ant Colony Optimisation Algorithm")
        print("4. Exit program")
        userinput = input("What would you like to do:")
        if userinput not in validoptions:
             print("Please enter a valid input!")
    return userinput
    
def _main_menu():
    userinput = _display_options()
    match userinput:
        case "1":
            cs._convert_data()
            print("\n\n\n\n")
            _main_menu()
        case "2":
            nn._route_finder(0)
            print("\n\n\n\n")
            _main_menu()
        case "3":
            ps._generate_pheremones()
            aco._find_shortest_route()
            print("\n\n\n\n")
            _main_menu()
        case "4":
            exit()
    

def main():
    _main_menu()


main()
