names = open("names.txt", "r")
all_names = names.read()
name_list = all_names.split(",")
for name_index in range(len(name_list)):
    name_list[name_index] = name_list[name_index][1 : len(name_list[name_index]) - 1]
sorted_name_list = sorted(name_list)

char_values = {
    "A" : 1,
    "B" : 2,
    "C" : 3,
    "D" : 4,
    "E" : 5,
    "F" : 6,
    "G" : 7,
    "H" : 8,
    "I" : 9,
    "J" : 10,
    "K" : 11,
    "L" : 12,
    "M" : 13,
    "N" : 14,
    "O" : 15,
    "P" : 16,
    "Q" : 17,
    "R" : 18,
    "S" : 19,
    "T" : 20,
    "U" : 21,
    "V" : 22,
    "W" : 23,
    "X" : 24,
    "Y" : 25,
    "Z" : 26
}
name_res = []

def letter_sum(string):
    result = 0
    for char in string:
        result += char_values[char]
    return result

index_tracker = 1
for ordered_name in sorted_name_list:
    name_res.append(letter_sum(ordered_name) * index_tracker)
    index_tracker += 1

print(sum(name_res))
