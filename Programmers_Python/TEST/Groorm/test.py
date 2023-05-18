import math


def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def find_min_length(locations):
    min_length = 0
    n = len(locations)

    for i in range(n - 1):
        x1, y1 = locations[i]

        for j in range(i + 1, n):
            x2, y2 = locations[j]

            distance = calculate_distance(x1, y1, x2, y2)
            min_length += distance

    return min_length


# Read the number of test cases
num_test_cases = int(input())

# Process each test case
for _ in range(num_test_cases):
    # Read the number of locations
    num_locations = int(input())

    # Read the x, y locations
    locations = []
    for _ in range(num_locations):
        x, y = map(int, input().split())
        locations.append((x, y))

    # Calculate the minimum length
    min_length = find_min_length(locations)
    print('{:.2f}'.format(min_length))