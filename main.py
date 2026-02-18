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

def _solve_equation(dividend_line, divisor_line, index_variable_to_solve):
    index_for_calc=0
    if(index_variable_to_solve==0):
        index_for_calc=1
    faktor=dividend_line[index_for_calc]/divisor_line[index_for_calc]
    res = dividend_line[index_variable_to_solve]/faktor
    return res

def _calculate_solution(lineA, lineB):
    variable_to_solve_foundA = _find_non_number_index(lineA)
    variable_to_solve_foundB = _find_non_number_index(lineB)
    if(variable_to_solve_foundA>-1):
        res = _solve_equation(lineB,lineA,variable_to_solve_foundA)
        return res
    if(variable_to_solve_foundB>-1):
        res = _solve_equation(lineA,lineB,variable_to_solve_foundB)
        return res
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
    print("Ergebnis " + str(_calculate_solution(first_line,second_line)))