import re

import numpy as np
from scipy import spatial as sp

def create_unique_sequence(npArr):
    uniqueList = []

    for i in range(len(npArr)):
        for j in range(len(npArr[i])):
            if a[i][j] not in uniqueList:
                uniqueList.append(npArr[i][j])

    return uniqueList

def create_matrix(npArr, uniqueList):
    matrix = np.zeros((len(npArr), len(uniqueList)))

    for i in range(len(npArr)):
        for j in range(len(uniqueList)):
            matrix[i][j] = npArr[i].count(uniqueList[j])

    return matrix

def write_in_file(answer):
    answerFile = open('answer_for_similarity.txt', 'w')

    answer = np.delete(answer, numpy.where(answer == min(answer)))
    first_index = numpy.where(answer == min(answer))
    answerFile.write(str(first_index[0][0]))
    answerFile.write(' ')

    answer = np.delete(answer, numpy.where(answer == min(answer)))
    second_index = numpy.where(answer == min(answer))
    answerFile.write(str(second_index[0][0]))
    print(first_index, second_index)

file = open('sentences.txt', 'r')
a = np.array([re.split("[^a-z]", line.lower()) for line in file], dtype=object)
uniqueList = create_unique_sequence(a)
matrix = create_matrix(a, uniqueList)

answer = np.array([sp.distance.cosine(i, matrix[0]) for i in matrix])
write_in_file(answer)
