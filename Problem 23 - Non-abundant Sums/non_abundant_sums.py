import math, itertools

limit = 28123

def divisor_sum(number):
    result = 0
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            if i != number / i and i != 1:
                result += (i + int(number / i))
            else:
                result += i
    return result

def is_abundant(number):
    if divisor_sum(number) > number:
        return True
    return False

def less_abun_nums(number):
    abun_nums = []
    for i in range(number):
        if is_abundant(i):
            abun_nums.append(i)
    return abun_nums

def detect_duplicates(lst):
    seen = {}
    result = []
    for item in lst:
        if item in seen:
            continue
        else:
            seen[item] = 1
            result.append(item)
    return result

def find_subsets(lst, limit):
    full_list = list(set(list(set(map(sum, set(itertools.combinations(lst, 2))))) +
    [2 * elem for elem in lst]))
    return [elem for elem in full_list if elem <= limit]

abundant_nums = less_abun_nums(limit)
subsets = find_subsets(abundant_nums, limit)
subset_sum = sum(subsets)
num_sum = int(limit * (limit + 1) / 2)
print(num_sum - subset_sum)
