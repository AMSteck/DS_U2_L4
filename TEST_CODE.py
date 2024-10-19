
from numpy import matmul
from mat_arith import *
from SAMPLE_MATRICES import *

##### Global color variables #####
from colorama import Fore
R = Fore.RED
G = Fore.GREEN
W = Fore.RESET
P = Fore.CYAN

'''IF COLORAMA NOT FOUND - ENTER INTO TERMINAL:
pip install colorama'''
####################################################################

def TEST_valid_mat_add():
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Valid Matrix Addition{W}\n")
    
    ## Test 1
    attempt = mat_sum(A, B)
    solution = AplusB

    if compare(attempt, solution):
        print(f"Test A + B: {G}PASSED{W}")
    else:
        print(f"Test A + B: {R}FAILED{W}")
        print(f"\nSolution:")
        display(solution)

        print(f"\nYour Result:")
        display(attempt)

    ## Test 2
    attempt = mat_sum(B, C)
    solution = BplusC

    if compare(attempt, solution):
        print(f"\n\nTest B + C: {G}PASSED{W}")
    else:
        print(f"\n\nTest B + C: {R}FAILED{W}")
        print(f"\nSolution:")
        display(solution)

        print(f"\nYour Result:")
        display(attempt)

    ## Test 3
    attempt = mat_sum(E, F)
    solution = EplusF

    if compare(attempt, solution):
        print(f"\n\nTest E + F: {G}PASSED{W}")
    else:
        print(f"\n\nTest E + F: {R}FAILED{W}")
        print(f"\nSolution:")
        display(solution)

        print(f"\nYour Result:")
        display(attempt)

    print("~" * 50, "\n\n")

####################################################################

def TEST_invalid_mat_add():
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Invalid Matrix Addition{W}\n")
    
    ## Test 1
    attempt = mat_sum(C, D)
    solution = "no solution"

    if attempt.lower() == solution:
        print(f"Test C + D: {G}PASSED{W}")
    else:
        print(f"Test C + D: {R}FAILED{W}")
        print(f"\nSolution: {solution}")
        print(f"Your Result: {attempt.lower()}")

    ## Test 2
    attempt = mat_sum(F, G)
    solution = "no solution"

    if attempt.lower() == solution:
        print(f"\n\nTest F + G: {G}PASSED{W}")
    else:
        print(f"\n\nTest F + G: {R}FAILED{W}")
        print(f"\nSolution: {solution}")
        print(f"Your Result: {attempt.lower()}")

    print("~" * 50, "\n\n")

####################################################################

def TEST_valid_mat_mul():
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Valid Matrix Multiplication 3.6{W}\n")
    
    ## Test 1
    attempt = mat_mul(A, B)
    solution = matmul(A, B)

    if compare(attempt, solution):
        print(f"Test AB: {G}PASSED{W}")
    else:
        print(f"Test AB: {R}FAILED{W}")
        print(f"\nSolution:")
        display(solution)

        print(f"\nYour Result:")
        display(attempt)
    
    ## Test 2
    attempt = mat_mul(E, F)
    solution = matmul(E, F)

    if compare(attempt, solution):
        print(f"\n\nTest EF: {G}PASSED{W}")
    else:
        print(f"\n\nTest EF: {R}FAILED{W}")
        print(f"\nSolution:")
        display(solution)

        print(f"\nYour Result:")
        display(attempt)

    ## Test 3
    attempt = mat_mul(C, D)
    solution = matmul(C, D)

    if compare(attempt, solution):
        print(f"\n\nTest CD: {G}PASSED{W}")
    else:
        print(f"\n\nTest CD: {R}FAILED{W}")
        print(f"\nSolution:")
        display(solution)

        print(f"\nYour Result:")
        display(attempt)
        
     ## Test 4
    attempt = mat_mul(J, J)
    solution = matmul(J, J)

    if compare(attempt, solution):
        print(f"\n\nTest JJ: {G}PASSED{W}")
    else:
        print(f"\n\nTest JJ: {R}FAILED{W}")
        print(f"\nSolution:")
        display(solution)

        print(f"\nYour Result:")
        display(attempt)
    
    print("~" * 50, "\n\n")

####################################################################

def TEST_matmul_3_1():
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Valid Matrix Multiplication 3.1{W}\n")
    
    ## Test 1
    attempt = mat_mul(X1, Y1)
    solution = matmul(X1, Y1)

    if compare(attempt, solution):
        print(f"Test X1Y1: {G}PASSED{W}")
    else:
        print(f"Test X1Y1: {R}FAILED{W}")
        print(f"\nSolution:")
        display(solution)

        print(f"\nYour Result:")
        display(attempt)

    print("~" * 50, "\n\n")

####################################################################

def TEST_matmul_3_2():
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Valid Matrix Multiplication 3.2{W}\n")
    
    ## Test 1
    attempt = mat_mul(X2, Y1)
    solution = matmul(X2, Y1)

    if compare(attempt, solution):
        print(f"Test X2Y1: {G}PASSED{W}")

    else:
        print(f"Test X2Y1: {R}FAILED{W}")
        print(f"\nSolution:")
        display(solution)

        print(f"\nYour Result:")
        display(attempt)

    print("~" * 50, "\n\n")
    
####################################################################

def TEST_matmul_3_3():
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Valid Matrix Multiplication 3.3{W}\n")
    
    ## Test 1
    attempt = mat_mul(X3, Y1)
    solution = matmul(X3, Y1)

    if compare(attempt, solution):
        print(f"Test X3Y1: {G}PASSED{W}")

    else:
        print(f"Test X3Y1: {R}FAILED{W}")
        print(f"\nSolution:")
        display(solution)

        print(f"\nYour Result:")
        display(attempt)

    print("~" * 50, "\n\n")

####################################################################

def TEST_matmul_3_4():
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Valid Matrix Multiplication 3.4{W}\n")
    
    ## Test 1
    attempt = mat_mul(X1, Y2)
    solution = matmul(X1, Y2)

    if compare(attempt, solution):
        print(f"Test X1Y2: {G}PASSED{W}")

    else:
        print(f"Test X1Y2: {R}FAILED{W}")
        print(f"\nSolution:")
        display(solution)

        print(f"\nYour Result:")
        display(attempt)

    print("~" * 50, "\n\n")

####################################################################

def TEST_matmul_3_5():
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Valid Matrix Multiplication 3.5{W}\n")
    
    ## Test 1
    attempt = mat_mul(X1, Y3)
    solution = matmul(X1, Y3)

    if compare(attempt, solution):
        print(f"Test X1Y3: {G}PASSED{W}")

    else:
        print(f"Test X1Y3: {R}FAILED{W}")
        print(f"\nSolution:")
        display(solution)

        print(f"\nYour Result:")
        display(attempt)

    print("~" * 50, "\n\n")

####################################################################

def TEST_invalid_mat_mul():
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Invalid Matrix Multiplication{W}\n")
    
    ## Test 1
    attempt = mat_mul(C, E)
    solution = "no solution"

    if attempt.lower() == solution:
        print(f"Test CE: {G}PASSED{W}")
    else:
        print(f"Test CE: {R}FAILED{W}")
        print(f"\nSolution: {solution}")
        print(f"Your Result: {attempt.lower()}")

    ## Test 2
    attempt = mat_mul(D, C)
    solution = "no solution"

    if attempt.lower() == solution:
        print(f"\nTest DC: {G}PASSED{W}")
    else:
        print(f"\nTest DC: {R}FAILED{W}")
        print(f"\nSolution: {solution}")
        print(f"Your Result: {attempt.lower()}")

    print("~" * 50, "\n\n")

####################################################################

def display(mat):
    for row in mat:
        print(row)

def compare(list_mat, np_mat):
    try:
        for row in range(len(list_mat)):
            for col in range(len(list_mat[0])):
                if list_mat[row][col] != np_mat[row][col]:
                    return False
        return True
    except:
        return False

