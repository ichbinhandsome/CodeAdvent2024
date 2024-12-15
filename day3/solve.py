import re

def read_file(file_path):
    with open(file_path, "r") as f:
        res = ""
        for line in f:
            res += str(line)
    return res


def validate_mul(idx, s):
    if s[idx] != "(":
        return False
    max_end_idx = idx+8
    left_num = []
    right_num = []
    switch = False
    valid = False
    for i in range(idx+1, max_end_idx+1):
        if left_num and s[i] == ",":
            switch = True
            continue
        if left_num and right_num and s[i] == ")":
            valid = True
            break
        if not s[i].isdigit():
            return False
        if not switch:
            if len(left_num) >= 3:
                return False
            else:
                left_num.append(s[i])
        else:
            if len(right_num) >= 3:
                return False
            else:
                right_num.append(s[i])
    if valid:
        return (left_num, right_num), idx
    else:
        return False


if __name__=="__main__":
    # question one
    s = read_file("./input.txt")
    res = 0
    matches = re.finditer(r"mul", s)
    valid_idx_res = {}
    for match in matches:
        end_idx = match.end()
        validated_res = validate_mul(end_idx, s)
        if validated_res:
            (l, r), i = validated_res
            l = int("".join(l))
            r = int("".join(r))
            valid_idx_res[i] = l*r
            res += l * r
    print(res)
    # question two
    # find don't() and do() index
    matches_1 = re.finditer(r"do()", s)
    matches_2 = re.finditer(r"don't()", s)
    do_list = []
    dont_list = []
    for m in matches_1:
        do_idx = m.end()
        do_list.append(do_idx-1)
    for m in matches_2:
        dont_idx = m.end()
        dont_list.append(dont_idx-1)
    res = 0
    flag_add = True
    new_list = list(valid_idx_res.keys()) + do_list + dont_list
    new_list.sort()
    for idx in new_list:
        if idx in valid_idx_res and flag_add == True:
            res += valid_idx_res[idx]
        if idx in do_list:
            flag_add = True
        if idx in dont_list:
            flag_add = False
    print(res) 