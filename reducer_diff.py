import sys

current_key = None
current_value = None

ans = set()
for line in sys.stdin:
    key, value = line.strip().split("\t", 1)
    if value == "A" and key not in ans:
        ans.add(key)
    else:
        ans = set(ans).difference(key)
for el in sorted(ans):
    print(el)