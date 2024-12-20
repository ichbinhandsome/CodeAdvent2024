def read_file(file_path):
    with open(file_path, "r") as f:
        res = []
        for line in f:
            target, nums = line.strip().split(":")
            nums = list(map(int, nums.strip().split(" ")))
            res.append((int(target), nums))
    return res

def backtrack(target, nums, res, idx):
    if idx == len(nums):
        if res == target:
            return True
        else:
            return False
    return backtrack(target, nums, res+nums[idx], idx+1) or backtrack(target, nums, res*nums[idx], idx+1)


def backtrack2(target, nums, res, idx):
    if res > target:
        return False
    if idx == len(nums):
        if res == target:
            return True
        else:
            return False
    return backtrack2(target, nums, res+nums[idx], idx+1) or backtrack2(target, nums, res*nums[idx], idx+1) or backtrack2(target, nums, int(str(res)+str(nums[idx])), idx+1)
    

if __name__=="__main__":
    # question one
    bridges = read_file("./input.txt")
    # print(bridges)
    res = 0
    for t, nums in bridges:
        if backtrack(t, nums, nums[0], 1):
            res += t
    print(res)
    # question two
    res = 0
    for t, nums in bridges:
        if backtrack2(t, nums, nums[0], 1):
            res += t
    print(res)
    
    