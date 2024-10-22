import csv
import os
from pathlib import Path

def readfile(file_path):
    fout = []
    with open(Path(".", file_path)) as fin:
        reader = csv.reader(fin, delimiter=',')
        for line in reader:
            fout.append(line)
    return fout
new_file = readfile('data.csv')


#### Read 

unique_values = list(new_file)


def read_vehicle_1_only(line):
    """ takes in column 17 (at index 16)
        returns: the string of vehicle one before ; """
    listy = []
    if ';' in line:
        before_semicolon = line.split(';', 1)[0]  # Split at the semicolon and take the first part 
    else:
        before_semicolon = line  # If no semicolon, take the entire line
    listy.append(before_semicolon)
    return listy

def read_vehicle_2_only(line):
    """ takes in column 17 (at index 16)
        returns: the string of vehicle one after ; """
    listy = []
    if ';' in line:
        after_semicolon = line.split(';')[1]  # Split at the semicolon and take the second 
        listy.append(after_semicolon[1:])
    return listy

### the above code 'read_vehicle_x_only' can be consolidated into one function where it take in the vehicle number unique inputs

def get_unique_driver_action(vehicle_number):
    if vehicle_number == int(1):
        unique_values = []
        for row in new_file:   
            temp = read_vehicle_1_only(row[16])
            if temp not in unique_values:
                unique_values.append(temp)
        return unique_values[1:]
    elif vehicle_number == int(2):
        unique_values = []
        for row in new_file:   
            temp = read_vehicle_2_only(row[16])
            
            if temp not in unique_values:
                unique_values.append(temp)
        return unique_values[1:]

        
if __name__ == "__main__":
    


            
    print(f"list_of_possible_driver_actions:")
    driver_action = get_unique_driver_action(1) # CHANGE ME 
    for element in driver_action:
        print(element)

"""
list_of_possible_ Driver Actions

list_of_possible_driver_actions
driver actions is column 17

"""
