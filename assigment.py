def classify(value):
    if value < 748:
        return "Below range"
    elif value <= 752:
        return "In range"
    else:
        return "Above range"


def calculate_average(total, count):
    return total / count


number_of_tins = int(input("Enter the number of paint tins: "))

total_volume = 0
below_count = 0
in_count = 0
above_count = 0

for i in range(number_of_tins):
    volume = int(input("Enter the paint tin volume: "))
    result = classify(volume)
    print(result)

    total_volume += volume

    if result == "Below range":
        below_count += 1
    elif result == "In range":
        in_count += 1
    else:
        above_count += 1

average = calculate_average(total_volume, number_of_tins)

print(f"Total volume: {total_volume} ml")
print(f"Average volume: {average} ml")
print(f"In range: {in_count}")
print(f"Above range: {above_count}")
