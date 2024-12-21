def read_file(file_path):
    with open(file_path, "r") as f:
        res = ""
        for line in f:
            res += line.strip()
    return res

if __name__=="__main__":
    file_num = read_file("./input.txt")
    # print(len(file_num))
    temp = []
    dot_record = [] # (idx, len)
    id_record = [] # (idx, id, len)
    for i, s in enumerate(file_num):
        if i % 2 == 0:
            x = i // 2
            id_record.append((len(temp), x, int(file_num[i])))
            temp.extend(int(file_num[i])*[x])
        else:
            dot_record.append((len(temp), int(file_num[i])))
            temp.extend(int(file_num[i])*["."])
    
    # question one     
    # print(temp)
    # i , j = 0, len(temp)-1
    # while i < j:
    #     while i < j and temp[i] != ".":
    #         i += 1
    #     while i < j and temp[j] == ".":
    #         j -= 1
    #     if i < j:
    #         temp[i], temp[j] = temp[j], temp[i]
    #         i += 1
    #         j -= 1
    # # print("".join(temp))
    # res = 0
    # for i in range(len(temp)):
    #     if temp[i] == ".":
    #         break
    #     res += i * int(temp[i])
    # print(res)
    
    #question two
    # print(dot_record)
    # print(id_record)
    for i in range(len(id_record)-1, -1, -1):
        idx, id, l = id_record[i]
        for j in range(len(dot_record)):
            idx_dot, l_dot = dot_record[j]
            if idx_dot < idx and l_dot >= l:
                for _ in range(l):
                    temp[idx_dot+_] = id
                    temp[idx+_] = "."
                idx_dot = idx_dot + l
                l_dot = l_dot - l
                dot_record[j] = (idx_dot, l_dot)
                break
    # print(temp)
    res = 0
    for i in range(len(temp)):
        if temp[i] == ".":
            continue
        res += i * int(temp[i])
    print(res)
        