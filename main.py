from TEST_CODE import *

'''
Write your code in mat_arith.py
Run main to run the official assignment tests.

IF COLORAMA NOT FOUND - ENTER INTO TERMINAL:
pip install colorama
'''

def main():

    # TEST 1 - valid matrix addition
    TEST_valid_mat_add()

    # TEST 2 - invalid matrix addition
    TEST_invalid_mat_add()

    # TEST 3 - Valid matrix multiplication
    # Mini Test 3.1 - One row, one column
    TEST_matmul_3_1()

    # Mini Test 3.2 - Two rows, one column
    #TEST_matmul_3_2()

    # Mini Test 3.3 - Three rows, one column
    #TEST_matmul_3_3()

    # Mini Test 3.4 - One row, two columns
    #TEST_matmul_3_4()

    # Mini Test 3.5 - One row, three columns
    #TEST_matmul_3_5()

    # Mini Test 3.6 - Many rows, many columns
    #TEST_valid_mat_mul()

    #TEST 4 - Invalid matrix multiplication
    #TEST_invalid_mat_mul()

if __name__ == "__main__":
    main()