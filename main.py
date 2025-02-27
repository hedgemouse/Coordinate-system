original_input = input("Enter the coordinates of the line in the form '(x;y) (x;y) ...': ")

# Remove parentheses and spaces, then split the string into a list
input_table = original_input.replace("(", "").replace(")", "").replace(" ", ";").split(";")

# Convert the input_table to a list of integers
input_table = [int(coord) for coord in input_table]

# Create x and y tables
x_table = input_table[0::2]
y_table = input_table[1::2]

coordinates = list(zip(x_table, y_table))

# Find the maximum and minimum values if there are positive/negative values in the tables
if any(y > 0 for y in y_table):
    y_positive_max = max(y_table)
else:
    y_positive_max = 0

if any(y < 0 for y in y_table):
    y_negative_max = min([y for y in y_table if y < 0])   # Filter to get only negative numbers
    y_negative_max *= -1
else:
    y_negative_max = 0

if any(x > 0 for x in x_table):
    x_positive_max = max(x_table)
else:
    x_positive_max = 0

if any(x < 0 for x in x_table):
    x_negative_max = min([x for x in x_table if x < 0])   # Filter to get only negative numbers
    x_negative_max *= -1
else:
    x_negative_max = 0

# Coordinate line printing function
def print_coordinate_line(current_y, coordinates, x_negative_max, x_positive_max, middle=False):
    for coord in coordinates:
        if current_y == coord[1]:
            if coord[0] > 0:
                if middle:
                    print(f"{'-' * x_negative_max}+{'-' * (coord[0] - 1)}+{'-' * (x_positive_max - coord[0])}")
                else:
                    print(f"{' ' * x_negative_max}|{' ' * (coord[0] - 1)}+{' ' * (x_positive_max - coord[0])}")
            elif coord[0] < 0:
                if middle:
                    print(f"{'-' * (x_negative_max - coord[0] * -1 - 1)}+{'-' * (coord[0] * -1)}+{'-' * (x_positive_max)}")
                else:
                    print(f"{' ' * (x_negative_max - coord[0] * -1 - 1)}+{' ' * (coord[0] * -1)}|{' ' * (x_positive_max)}")
            elif coord[0] == 0 and coord[1] != 0:
                if middle:
                    print(f"{'-' * x_negative_max}+{'-' * x_positive_max}")
                else:
                    print(f"{' ' * x_negative_max}+{' ' * x_positive_max}")
            elif coord[0] == 0 and coord[1] == 0:
                print(f"{'-' * x_negative_max}+{'-' * x_positive_max}")
            elif coord[1] == 0 and current_y == 0:
                print(f"{'-' * x_negative_max}+{'-' * x_positive_max}")

def print_middle_line(x_negative_max, x_positive_max, coordinates):
    for coord in coordinates:
        if coord[1] == 0:
            if coord[0] > 0:
                print(f"{'-' * x_negative_max}+{'-' * (coord[0] - 1)}+{'-' * (x_positive_max - coord[0])}")
            elif coord[0] < 0:
                print(f"{'-' * (coord[0] * -1 - 1 - x_negative_max)}+{'-' * (coord[0] * -1 - 1)}+{'-' * (x_positive_max)}")
            elif coord[0] == 0:
                print(f"{'-' * x_negative_max}+{'-' * x_positive_max}")
    else:
        print(f"{'-' * x_negative_max}+{'-' * x_positive_max}")

# Prints the top part of the coordinate system
current_y = y_positive_max
for i in range(y_positive_max):
    if current_y in y_table:
        print_coordinate_line(current_y, coordinates, x_negative_max, x_positive_max)
    else:
        print(f"{' ' * x_negative_max}|{' ' * x_positive_max}")
    
    current_y -= 1

# Prints the middle part of the coordinate system
print_middle_line(x_negative_max, x_positive_max, coordinates)

# Prints the bottom part of the coordinate system
current_y = -1
for i in range(y_negative_max):
    if current_y in y_table:
        print_coordinate_line(current_y, coordinates, x_negative_max, x_positive_max)
    else:
        print(f"{' ' * x_negative_max}|{' ' * x_positive_max}")
    
    current_y -= 1