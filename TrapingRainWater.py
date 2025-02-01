"""
Trapping Rain Water Solver

This script reads a height map from a file "input.txt" and then calculates the amount of trapped water between heights.
The algorithm works by iterating through each possible height level and counting the spaces where water can accumulate.

Methodology:
- Load the heights from a text file where values are separated by commas.
- Determine the maximum height in the map.
- Iterate through each height level from 1 up to the maximum height.
- Find the left and right boundaries of heights for each level and count the trapped water between them.

Variables:
- height_map (list[int]): List of column heights.
- max_height (int): Maximum height in the map.
- sum_water (int): Total trapped water.
- current_h (int): Current height level being analyzed.
- left_index (int): Index of the left boundary of trapped water.
- right_index (int): Index of the right boundary of trapped water.
- found (bool): Flag indicating whether a right boundary has been found.

Input:
- A file "input.txt" containing a list of heights separated by commas.

Output:
- Displays the total trapped water in the console.
"""

# Read heights from input file and store them in the height_map list
height_map = []
with open("input.txt") as file:
    for line in file:
        for elem in line.split(","):
            height_map.append(int(elem))

# Get the maximum height to determine the highest level to check
max_height = max(height_map)
sum_water = 0 # Variable to store the total trapped water
current_h = 1 # Start analyzing from the first level


# Loop through each height level from 1 to max_height
while current_h <= max_height:

    left_index = 0
    right_index = len(height_map) - 1
    found = False # Flag to check if we found a valid right boundary corresponding to the left one

    # Find the left and right boundaries for the current height level
    while left_index < right_index and not found:
        if height_map[left_index] >= current_h:

            while right_index > left_index and not found:
                if height_map[right_index] >= current_h:

                    found = True
                    # Count trapped water between left and right boundaries for the current level
                    for item in height_map[left_index:right_index]:
                        if item < current_h:
                            sum_water += 1
                else:
                    right_index -= 1
        else:
            left_index += 1

    current_h +=1
    
# Print the total amount of trapped water
print(sum_water)