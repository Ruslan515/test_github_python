# put your python code here
import sys

current_key = None
current_value = None

for line in sys.stdin:
    key, value = line.strip().split("\t", 1)
    key = int(key)
    if key == current_key:
        if value != current_value and current_key:
            print(key)
    else:
        current_key = key
        current_value = value