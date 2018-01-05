# def cycle_length(denom):
#     value = 1 / denom
#     pattern = ""
#     recur = False
#     if 1000 % denom == 0:
#         return False
#     while not recur:
#         check = str(int(value * pow(10, len(pattern))))
#         print("check: " + check)
#         value *= 10
#         if len(pattern) > 0 and check in pattern:
#             recur = True
#         else:
#             pattern += str(int(value % 10))
#             print("pattern: " + pattern)
#             value %= 1
#     return len(pattern)
#
# print(cycle_length(99))
value = 1 / 7

def floyd_cycle(value):
    tortoise = value * 10
    hare = value * 10 * 10
    while tortoise * 10 != hare * 10:
        tortoise *= 10
        tortoise %= 1
        hare *= (10 * 10)
        hare %= 1
        print(tortoise)
        print(hare)

    print(tortoise)
    print(hare)

    """first_pos = 0
    tortoise = value
    while tortoise != hare:
        tortoise *= 10
        #hare *= 10
        first_pos += 1

    cycle_length = 1
    hare = tortoise * 10
    while tortoise != hare:
        hare *= 10
        cycle_length += 1

    return cycle_length, first_pos"""

print(floyd_cycle(value))
