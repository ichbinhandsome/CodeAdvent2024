
def read_file(file_path):
    list_a = []
    with open(file_path, "r") as f:
        for line in f:
            list_b = list(map(int, line.strip().split()))
            list_a.append(list_b)
    return list_a


def check_safe(input_list):
    sorted_list = sorted(input_list)
    if input_list != sorted_list and input_list != sorted_list[::-1]:
        return False
    for i in range(len(input_list)-1):
        curr, nxt = input_list[i], input_list[i+1]
        if abs(nxt-curr) < 1 or abs(nxt-curr) > 3:
            return False
    return True


if __name__=="__main__":
    # question one
    list_a = read_file("./input.txt")
    res = 0
    wrong_list = []
    for i in range(len(list_a)):
        if check_safe(list_a[i]):
            res += 1
        else:
            wrong_list.append(list_a[i])
    print(res)
    # question two
    add_res = 0
    for i in range(len(wrong_list)):
        is_safe = False
        for j in range(len(wrong_list[i])):
            new_list = wrong_list[i][0:j] + wrong_list[i][j+1:]
            if check_safe(new_list):
                is_safe = True
                continue
        if is_safe:
            add_res += 1
    print(add_res)
    print(res+add_res)       