from collections import defaultdict

def read_file(file_path):
    with open(file_path, "r") as f:
        rules, pages = [], []
        flag = True
        for line in f:
            if len(line) == 1:
                print(line)
                flag = False
                continue
            else:
                if flag:
                    rules.append(list(map(int, line.strip().split("|"))))
                else:
                    pages.append(list(map(int, line.strip().split(","))))
    return rules, pages

if __name__=="__main__":
    # question one
    rules, pages = read_file("./input.txt")
    hash_map = defaultdict(set)
    for [pre,curr] in rules:
        hash_map[curr].add(pre)
    
    res = 0
    for order in pages:
        temp = set()
        flag = True
        for o in order:
            if o in temp:
                flag = False
                break
            else:
                if o in hash_map:
                    temp = temp.union(hash_map[o])
        if flag:
            mid = len(order) // 2
            res += order[mid]
            
    print(res)
        
    def sort(nums):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] in hash_map[nums[i]]:
                    nums[j], nums[i] = nums[i], nums[j]
        return nums
    
    # question two
    res = 0
    for order in pages:
        temp = set()
        flag = True
        for o in order:
            if o in temp:
                flag = False
                break
            else:
                if o in hash_map:
                    temp = temp.union(hash_map[o])
                    
        if not flag:
            order = sort(order)
            mid = len(order) // 2
            res += order[mid]   
    print(res)       