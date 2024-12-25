from collections import defaultdict

def read_file(file_path):
    with open(file_path, "r") as f:
        mat = []
        for line in f:
            mat.append(list(line.strip()))
    return mat

if __name__=="__main__":
    mat = read_file("./input.txt")
    hash_map = defaultdict(list)
    m ,n = len(mat), len(mat[0])
    visited = set()
    for i in range(m):
        for j in range(n):
            if mat[i][j] != ".":
                hash_map[mat[i][j]].append([i,j])
                
    # question one
    # def search_antinode(A, B):
    #     x1, y1 = A
    #     x2, y2 = B
    #     temp = 0
    #     dx1, dy1 = x1-x2, y1-y2
    #     antx1, anty1 = x1-2*dx1, y1-2*dy1
    #     if 0 <= antx1 < m and 0 <= anty1 < n and (antx1, anty1) not in visited:
    #         temp += 1
    #         visited.add((antx1, anty1))
    #     dx2, dy2 = x2-x1, y2-y1
    #     antx2, anty2 = x2-2*dx2, y2-2*dy2
    #     if 0 <= antx2 < m and 0 <= anty2 < n and (antx2, anty2) not in visited:
    #         temp += 1
    #         visited.add((antx2, anty2))
    #     return temp
    
    # res = 0
    # for k,v in hash_map.items():
    #     l = len(v)
    #     for i in range(l-1):
    #         for j in range(i+1, l):
    #             res += search_antinode(v[i], v[j])
    # print(res)
    
    # question two
    def search_antinode2(A, B):
        x1, y1 = A
        x2, y2 = B
        dx1, dy1 = x1-x2, y1-y2
        i = 2
        antx1, anty1 = x1-i*dx1, y1-i*dy1
        while 0 <= antx1 < m and 0 <= anty1 < n:
            if (antx1, anty1) not in visited:
                visited.add((antx1, anty1))
            i += 1
            antx1, anty1 = x1-i*dx1, y1-i*dy1
                
        dx2, dy2 = x2-x1, y2-y1
        j = 2
        antx2, anty2 = x2-j*dx2, y2-j*dy2
        while 0 <= antx2 < m and 0 <= anty2 < n:
            if (antx2, anty2) not in visited:
                visited.add((antx2, anty2))
            j += 1
            antx2, anty2 = x2-j*dx2, y2-j*dy2
        return
    
    for k,v in hash_map.items():
        if len(v) > 1:
            for x,y in v:
                visited.add((x,y))
    for k,v in hash_map.items():
        l = len(v)
        for i in range(l-1):
            for j in range(i+1, l):
                search_antinode2(v[i], v[j])
    print(len(visited))