import sys

current_key = None
current_value = None
current_count = 1

for line in sys.stdin:
    key, value = line.strip().split("\t", 1)
    if key != current_key:
        if current_count == 1 and current_value == "A":
            print(current_key)
        current_key = key
        current_value = value
        current_count = 1
    current_value = value

if current_count == 1 and current_value == "A":
    print(current_key)
