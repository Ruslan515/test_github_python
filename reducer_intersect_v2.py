import sys

prev_key = None
for line in sys.stdin:
    tokens = line.strip().split('\t')
    if tokens[0] == prev_key:
        print(tokens[0])
    prev_key = tokens[0]