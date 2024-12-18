import re

def read_file(file_path):
    with open(file_path, "r") as f:
        res = []
        for line in f:
            res.append(list(line.strip()))
    return res


if __name__=="__main__":
    # question one
    matrix = read_file("./input.txt")
    m ,n = len(matrix), len(matrix[0])
    target = ["X", "M", "A", "S"]
    
    res = 0
    directions = []
    
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue
            directions.append((x,y))
    
    # question one
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == target[0]:
                for x,y in directions:
                    curr_i , curr_j = i, j
                    flag = True
                    for k in range(1, 4):
                        curr_i , curr_j = curr_i + x, curr_j + y
                        if curr_i < 0 or curr_i >= m or curr_j < 0 or curr_j >= n:
                            flag = False
                            break
                        curr = matrix[curr_i][curr_j]
                        t = target[k]
                        if curr != t:
                            flag = False
                            continue
                    if flag:
                        res += 1       
                        
    print(res)
    
    # question two
    target = ["M", "M", "S", "S"]
    res_2 = 0
    def search_around(i,j):
        collect = []
        for x,y in [(-1,-1), (1,1), (-1,1), (1,-1)]:
            new_i, new_j = i+x, j+y
            if new_i < 0 or new_i >= m or new_j < 0 or new_j >= n:
                return False
            collect.append(matrix[new_i][new_j])
        if collect[0] == collect[1] or collect[2] == collect[3]: # avoid same number in diag
            return False
        if sorted(collect) == sorted(target):
            return True
        return False
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == "A":
                if search_around(i,j):
                    res_2 += 1
    print(res_2)    