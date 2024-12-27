def read_file(file_path):
    with open(file_path, "r") as f:
        res = []
        for line in f:
            nums = list(map(int, line.strip()))
            res.append(nums)
    return res

# def read_file(file_path):
#     with open(file_path, "r") as f:
#         res = []
#         for line in f:
#             nums = []
#             for i in range(len(line.strip())):
#                 if line[i] == ".":
#                     nums.append(float("inf"))
#                 else:
#                     nums.append(int(line[i]))
#             res.append(nums)
#     return res


if __name__=="__main__":
    # question one
    maps = read_file("./input.txt")
    m, n = len(maps), len(maps[0])
    
    def dfs(i, j, visited, nine_set):
        if i < 0 or i >= m or j < 0 or j >= n:
            return 0
        if maps[i][j] == 9:
            if (i,j) not in nine_set:
                nine_set.add((i,j))
                return 1
            else:
                return 0
        res = 0
        for a,b in [(1,0), (-1,0), (0,1), (0,-1)]:
            x, y = i + a, j + b
            if 0 <= x < m and 0 <= y < n and (x,y) not in visited:
                if maps[x][y] == maps[i][j] + 1:
                    visited.add((x, y))
                    res += dfs(x, y, visited, nine_set)
                    visited.remove((x, y))
        return res
    
    res = 0
    for i in range(m):
        for j in range(n):
            if maps[i][j] == 0:
                visited = set()
                nine_set = set()
                visited.add((i,j))
                res += dfs(i, j, visited, nine_set)
    print(res)
    
    # question two
    def dfs2(i, j, visited):
        if i < 0 or i >= m or j < 0 or j >= n:
            return 0
        if maps[i][j] == 9:
            return 1
        res = 0
        for a,b in [(1,0), (-1,0), (0,1), (0,-1)]:
            x, y = i + a, j + b
            if 0 <= x < m and 0 <= y < n and (x,y) not in visited:
                if maps[x][y] == maps[i][j] + 1:
                    visited.add((x, y))
                    res += dfs2(x, y, visited)
                    visited.remove((x, y))
        return res
    
    res = 0
    for i in range(m):
        for j in range(n):
            if maps[i][j] == 0:
                visited = set()
                visited.add((i,j))
                res += dfs2(i, j, visited)
    print(res)
            
                
        
            