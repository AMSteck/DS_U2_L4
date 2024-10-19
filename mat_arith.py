#Alannah
#U2L4
#Matrix Arithmetic
# after possible new = [[0]*width for i in range(height)]

def mat_sum(m1, m2):
    possible = False
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        possible = True
    if possible:
        new = [[0]*len(m2) for i in range(len(m1))]
        for row in range(len(new)):
            for spot in range(len(new[0])):
                answer = m1[row][spot] + m2[row][spot]
                new[row][spot] = answer
        return new
    else:
        return "no solution"



def mat_mul(m1, m2):
    possible = False
    if len(m1[0]) == len(m2):
        possible = True
    if possible:
        new = [[0]*len(m2[0]) for i in range(len(m1))]
        
        for row in range(len(m1)):#for each row in m1
            ans_row = 0
            ans_column = 0 
            answer = 0
            
            for column in range(len(m2)):
              x = m1[row][column] * m2[column][row]
              answer += x
            new[ans_row][ans_column] = answer
            if ans_column + 1 >= len(new[0]):
              ans_column = 0
              ans_row +=1
            else:
              ans_column += 1
              
        return new
    else:
        return "no solution"
