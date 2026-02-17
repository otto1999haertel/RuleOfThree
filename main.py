from collections import Counter 
import numpy as np
def _validate_input(input, variable_to_solve_found):
    if(Counter(input)['=']!=1):
        raise Exception("Input String does not contain =")
    splitted_input = input.split('=')
    if(str.isdigit(splitted_input[0])==False or str.isdigit(splitted_input[1])==False):
        if(variable_to_solve_found):
            raise Exception("Input sides should contain number but does not")
        else:
            variable_to_solve_found=True
        if(str.isdigit(splitted_input[0])==True):
            splitted_input = [int(splitted_input[0]),splitted_input[1]]
        if(str.isdigit(splitted_input[1])==True):
            splitted_input = [splitted_input[0],int(splitted_input[1])]
    else:
        splitted_input = [int(splitted_input[0]),int(splitted_input[1])]
    return variable_to_solve_found, splitted_input

def _find_non_number_index(lst):
    for i, value in enumerate(lst):
        if not str(value).isdigit():
            return i
    return -1 

def _calculate_solution(lineA, lineB):
    variable_to_solve_foundA = _find_non_number_index(lineA)
    variable_to_solve_foundB = _find_non_number_index(lineB)
    if(variable_to_solve_foundA>-1):
        print("Found")
    if(variable_to_solve_foundB>-1):
        print("Found") 
    return 0


if __name__ == '__main__':
    print("Rule of three calculator")
    print("Format:")
    print("object1 = object2")
    print("object4 = object5")
    print("For object to solve enter x")
    first_line=input()
    second_line=input()
    variable_to_solve_found, first_line=_validate_input(first_line,False)
    variable_to_solve_found,second_line=_validate_input(second_line,variable_to_solve_found)
    print("Ergebnis " + _calculate_solution(first_line,second_line))