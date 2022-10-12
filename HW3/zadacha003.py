some_list = [
    1.1, 1.2, 3.1,
    5, 10.01
]

max_fraction = min_fraction = 0

for nm in some_list:
    if nm%1 > max_fraction:
        max_fraction = nm%1
    if nm%1 < min_fraction:
        min_fraction = nm%1
print(max_fraction - min_fraction)