#David Zhuzhunashvili

import random
import math


#Generates random numbers, with 0 being the most common
def random_generator():
    #If a random number x in the range 0 < x < 1 is less than or equal to 0.4 then the random number
    #that this function generates comes out ot be 0
    if(random.random() <= 0.4):
        return 0
    #Otherwise, if 0.4 < x < 1 then this function generates a number from 1 to 5 with equal probabilities
    else:
        return int((random.random()*5) + 1)


#Makes a deep copy of a matrix
def copy_matrix(matrix):
    new_matrix = [[0 for x in range(len(matrix[0]))] for x in range(len(matrix))]
    for i in range(len(matrix)):                                               
        for j in range(len(matrix[0])):                                        
            new_matrix[i][j] = matrix[i][j]                                         
    return new_matrix     


#Print the matrix in a nice format
def print_matrix(matrix):
    for row in matrix:
        form = ', '.join("%4.4f" for _ in row)
        print ("[" + form + "]") % tuple(row)


#Returns the transpose of an inputted matrix
def transpose_matrix(matrix):
    new_matrix = [[0 for x in range(len(matrix))] for x in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix


#Creates a matrix with random values form 1 to 5
def random_matrix(rows, columns):
    matrix = [[int((random.random()*6)) for x in range(columns)] for x in range(rows)]
    return matrix


#Creates a matrix with random values form 1 to 5 with 0 being most common
def random_zero_matrix(rows, columns):
    matrix = [[random_generator() for x in range(columns)] for x in range(rows)]
    return matrix


#Allows the user to make a specific matrix
def make_matrix(rows, columns):
    matrix = [[0 for x in range(columns)] for x in range(rows)]
    for i in range(0, rows):
        for j in range(0, columns):
            user_input = input("Enter the value for [%d, %d]: " %(i, j))
            matrix[i][j] = user_input
            print_matrix(matrix)
    return matrix


#Computes the euclidian dot product
def eucl_dot_product(list1, list2):
    return sum(x*y for x,y in zip(list1, list2))


#Computes the euclidian norm
def eucl_norm(list1):
    return math.sqrt(sum(x*x for x in list1))


#Computes the dot product divided by the product of the two vectors' norms
def cos_angle(list1, list2):
    if eucl_norm(list1) == 0 or eucl_norm(list2) == 0:
        return -1
    else:
        return eucl_dot_product(list1, list2) / (eucl_norm(list1)*eucl_norm(list2)) 


#Produces a matrix of cosine distances between rows for a given matrix
def dist_calculator(matrix):
    dist_matrix = [[0.00 for x in range(len(matrix))] for x in range(len(matrix))]

    for i,r1 in enumerate(matrix[:-1]):
        for j,r2 in enumerate(matrix[i+1:], start=i+1):
            dist_matrix[i][j] = cos_angle(r1,r2) 
    return dist_matrix


#Calculates the number of non-zero terms in a vector
def non_zero_length(vector):
    length = 0
    for i in range(len(vector)):
        if vector[i] > 0:
            length += 1
    return length


#Combines the value of one vector with 0 plus the difference between the averave values of the two vectors
def combine_vectors(vector1, vector2):
    average_difference = round(sum(vector1)/(1.0 * non_zero_length(vector1)) - sum(vector2)/(1.0 * non_zero_length(vector2)), 0)

    for i in range(len(vector1)):
        if vector1[i] == 0 and vector2[i] != 0:
            vector1[i] = vector2[i] + average_difference
            if vector1[i] <= 0:
                vector1[i] = 1
            if vector1[i] > 5:
                vector1[i] = 5
    return vector1 


#Orders the cosine distances in a new matrix from highest to lowest starting with 1 and ending with the number of non-zero terms
def closest_pairs(matrix):
    dist_matrix = dist_calculator(matrix)
    turn_matrix = [[0 for x in range(len(dist_matrix))] for x in range(len(dist_matrix))]
    iterations = (len(dist_matrix) - 1) * len(dist_matrix) / 2
    max_value = 0.0
    row = 0
    column = 0

    for k in range(iterations):
        for i in range(len(dist_matrix)):
            for j in range(i + 1, len(dist_matrix)):
                if dist_matrix[i][j] > max_value:
                    max_value = dist_matrix[i][j]
                    row = i
                    column = j
        if max_value > 0:
            turn_matrix[row][column] = k + 1
        max_value = 0.0
        dist_matrix[row][column] = 0.0
    return turn_matrix


#Rebuilds the matrix by using the combine_vectors function to predict peoples ratings
def rebuild_matrix(matrix):
    new_matrix = copy_matrix(matrix)
    new_matrix_1 = copy_matrix(matrix)
    dist_matrix = dist_calculator(matrix)
    closest_pair_matrix = closest_pairs(matrix)
    iterations = (len(closest_pair_matrix) - 1) * len(closest_pair_matrix) / 2
    turn = 1

    for k in range(iterations):
        for i in range(len(closest_pair_matrix)):
            for j in range(i + 1, len(dist_matrix)):
                if closest_pair_matrix[i][j] == turn:
                    new_matrix[i] = combine_vectors(matrix[i], matrix[j])
                    new_matrix[j] = combine_vectors(matrix[j], matrix[i])
        turn += 1
    turn = 1
    while new_matrix != new_matrix_1:
        new_matrix_1 = copy_matrix(new_matrix)
        turn = 1
        for k in range(iterations):
            for i in range(len(closest_pair_matrix)):
                for j in range(i + 1, len(closest_pair_matrix)):
                    if closest_pair_matrix[i][j] == turn:
                        new_matrix[i] = combine_vectors(new_matrix_1[i], new_matrix_1[j])
                        new_matrix[j] = combine_vectors(new_matrix_1[j], new_matrix_1[i])
            turn += 1
    return new_matrix


#Rebuilds the matrix by using the combine_vectors function to predict peoples ratings but in this cases it looks at the transpose of the matrix
def rebuild_matrix_transpose(matrix):
    new_matrix = transpose_matrix(matrix)
    new_matrix_a = transpose_matrix(matrix)
    new_matrix_1 = copy_matrix(new_matrix_a)
    dist_matrix = dist_calculator(new_matrix)
    closest_pair_matrix = closest_pairs(new_matrix)
    iterations = (len(closest_pair_matrix) - 1) * len(closest_pair_matrix) / 2
    turn = 1
    
    for k in range(iterations):
        for i in range(len(closest_pair_matrix)):
            for j in range(i + 1, len(dist_matrix)):
                if closest_pair_matrix[i][j] == turn:
                    new_matrix[i] = combine_vectors(new_matrix[i], new_matrix[j])
                    new_matrix[j] = combine_vectors(new_matrix[j], new_matrix[i])
        turn += 1
    
    while new_matrix != new_matrix_1:
        new_matrix_1 = new_matrix
        turn = 1
        for k in range(iterations):
            for i in range(len(closest_pair_matrix)):
                for j in range(i + 1, len(dist_matrix)):
                    if closest_pair_matrix[i][j] == turn:
                        new_matrix[i] = combine_vectors(new_matrix[i], new_matrix[j])
                        new_matrix[j] = combine_vectors(new_matrix[j], new_matrix[i])
            turn += 1
        
    new_matrix = transpose_matrix(new_matrix)
    return new_matrix


#Wheneer the rating went from a 0 to a 4 or a 5, that index gets printed out
def recommend(original, rebuilt):
    for i in range(len(original)):
        for j in range(len(original[0])):
            if original[i][j] == 0 and rebuilt[i][j]  >= 4.0:
                print "Person %d will most likely enjoy movie %d." % (i + 1, j + 1) 
            




print
#matrix = random_matrix(5, 7)
#matrix = [[0, 0, 5, 3], [2, 2, 2, 0], [0, 0, 0, 3], [0, 3, 0, 2]]
matrix = random_zero_matrix(15,17)
#original_1 = [[0, 1, 2, 3], [5, 1, 2, 3]]

original_1 = copy_matrix(matrix)
matrix_1 = copy_matrix(matrix)

original_2 = copy_matrix(matrix)
matrix_2 = copy_matrix(matrix)

example_matrix = copy_matrix(matrix)
example_matrix_1 = copy_matrix(matrix)


#matrix = [[5.0000, 3.0000, 1.0000, 0.0000, 1.0000], [5.0000, 5.0000, 0.0000, 2.0000, 2.0000], [2.0000, 5.0000, 4.0000, 1.0000, 0.0000], [4.0000, 5.0000, 1.0000, 0.0000, 2.0000], [5.0000, 5.0000, 1.0000, 2.0000, 0.0000]]
print "Original matrix: "
print
print_matrix(matrix)
print
print

#print_matrix(transpose_matrix(matrix))
#dist_matrix = dist_calculator(matrix)
#print_matrix(dist_matrix)
#print

#closest_pair_matrix = closest_pairs(matrix)
#print_matrix(closest_pair_matrix)
#print

#new_matrix = rebuild_matrix(matrix)
#new_matrix = rebuild_matrix_transpose(matrix)
#print_matrix(new_matrix)
#print
#print
#print_matrix(matrix_1)
matrix_3 = rebuild_matrix(matrix_1)
print "Recommendation matrix based on user similarity: "
print
print_matrix(matrix_3)
print
print

#print_matrix(matrix_2)
print "List of recommendations based on user similarity: "
print
recommend(matrix_2, matrix_3)
print
print

original_3 = rebuild_matrix_transpose(original_1)
print "Recommendation matrix based on movie/item similariy: "
print
print_matrix(original_3)
print
print

#print_matrix(original_2)
print "List of recommendations based on movie/item similarity: "
print
recommend(original_2, original_3)
#print random_generator()
            
#print_matrix(random_matrix(5, 5))
#print
#print_matrix(random_zero_matrix(5,5))

#example_matrix = dist_calculator(example_matrix_1)
#print_matrix(example_matrix)

#example_matrix = closest_pairs(example_matrix_1)
#print_matrix(example_matrix)
