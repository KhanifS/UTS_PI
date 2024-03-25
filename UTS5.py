path = r"C:\Users\HP Core i5\Documents\python\UTS"

def sum_of_numbers_from_file(filename):
    total = 0
    with open(filename, 'r') as file:
        for line in file:
            total += int(line.strip())
    return total

filename = path + '\\input.txt'
result = sum_of_numbers_from_file(filename)
print("{:,.3f}".format(result))
