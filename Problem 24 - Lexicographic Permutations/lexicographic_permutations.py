digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
index = 1000000

def all_perms(digits):
    if len(digits) <= 1:
        yield digits
    else:
        for perm in all_perms(digits[1:]):
            for i in range(len(digits)):
                yield perm[:i] + digits[0:1] + perm[i:]

print(sorted(list(all_perms(digits)))[index - 1])

# [2, 7, 8, 3, 9, 1, 5, 4, 6, 0]
# 2783915460
