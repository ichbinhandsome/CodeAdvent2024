def read_file(file_path):
    with open(file_path, "r") as f:
        res = []
        for line in f:
            res.append(list(line.strip()))
    return res

if __name__=="__main__":
    # build turn around directions
    dir_switch = {
        (1,0): (0,-1),
        (0,1): (1,0),
        (-1,0): (0,1),
        (0,-1): (-1,0)    
    }
    matrix = read_file("./input.txt")
    m ,n = len(matrix), len(matrix[0])
    guard_x, guard_y = None, None
    curr_dir = None
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == "^":
                guard_x, guard_y = i, j
                curr_dir = (-1,0)
            elif matrix[i][j] == ">":
                guard_x, guard_y = i, j
                curr_dir = (0,1)
            elif matrix[i][j] == "v":
                guard_x, guard_y = i, j
                curr_dir = (1,0)
            elif matrix[i][j] == "<":
                guard_x, guard_y = i, j
                curr_dir = (0,-1)
    # question one     
    visited = set()
    visited.add((guard_x, guard_y))
    def traversal(start, curr_dir):
        x, y = start
        if x < 0 or x >= m or y < 0 or y >= n:
            return
        a, b = curr_dir
        x, y = x + a, y + b
        while 0 <= x < m and 0 <= y < n and matrix[x][y] != "#":
            visited.add((x,y))
            x, y = x + a, y + b
        if 0 <= x < m and 0 <= y < n and matrix[x][y] == "#":
            traversal((x-a, y-b), dir_switch[curr_dir])
        return
    
    traversal((guard_x, guard_y), curr_dir)
    print(len(visited))
    
    # question two
    import copy
     
    def traversal2(start, curr_dir, matrix, start_points):
        if start in start_points and start != start_points[-1]:
            # print(start_points)
            # print(start)
            return True
        start_points.append(start)
        x, y = start
        if x < 0 or x >= m or y < 0 or y >= n:
            return False
        a, b = curr_dir
        x, y = x + a, y + b
        while 0 <= x < m and 0 <= y < n and matrix[x][y] != "#":
            x, y = x + a, y + b
            
        if 0 <= x < m and 0 <= y < n and matrix[x][y] == "#":
            return traversal2((x-a, y-b), dir_switch[curr_dir], matrix, start_points)
        return False
    
    res = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == ".":
                matrix[i][j] = "#"
                if traversal2((guard_x, guard_y), curr_dir, matrix, []):
                    # print("####", i,j)
                    res += 1
                matrix[i][j] = "."
                
    print(res)        