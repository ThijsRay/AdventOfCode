read_data = ""
with open('input', 'r') as f:
    read_data = f.read()

lines = read_data.splitlines()

def differ(string1, string2):
    diff = 0
    for (i, char) in enumerate(string1):
        if char is not string2[i]:
            diff += 1
    return diff

min = 100
for (index1, line1) in enumerate(lines):
    for (index2, line2) in enumerate(lines):
        if index1 is not index2:
            diff = differ(line1, line2)
            if diff < min:
                min = diff
                print(diff, line1, line2)

