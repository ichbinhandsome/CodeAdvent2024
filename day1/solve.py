
def read_file(file_path):
    list_a = []
    list_b = []
    with open(file_path, "r") as f:
        for line in f:
            num1, num2 = map(int, line.strip().split())
            list_a.append(num1)
            list_b.append(num2)
    return list_a, list_b


if __name__=="__main__":
    # question one
    list_a, list_b = read_file("./input.txt")
    list_a.sort()
    list_b.sort()
    res = 0
    for i in range(len(list_a)):
        res += abs(list_a[i] - list_b[i])
    print(res)
    
    # question two
    hash_map = {}
    for num in list_b:
        if num in hash_map:
            hash_map[num] += 1
        else:
            hash_map[num] = 1
    res_2 = 0
    for n in list_a:
        if n in hash_map:
            res_2 += n * hash_map[n]
    print(res_2)
            