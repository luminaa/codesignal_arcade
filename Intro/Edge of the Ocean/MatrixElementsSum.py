def solution(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                continue
            flag = True
            for k in range(i):
                if matrix[k][j] == 0:
                    flag = False
                    break
            if flag:
                count += matrix[i][j]
    return count