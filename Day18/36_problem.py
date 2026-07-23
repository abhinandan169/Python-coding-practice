# Given a nested list (list containing lists), flatten it into a single list — without using built-in itertools, use nested loops.
# Example: [[1,2],[3,4],[5]] → [1,2,3,4,5]


nested_list = [[1,2],[3,4],[5]]
flat = []

for box in nested_list:
    for item in box:
        flat.append(item)

print(flat)