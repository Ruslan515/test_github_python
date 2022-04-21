# put your python code here
import sys
from collections import defaultdict

dict_d = defaultdict(set)

for line in sys.stdin:
    key, value = line.strip().split("\t", 1)
    dict_d[value].add(key)

ans = set()
key = list(dict_d.keys())[0]
set_no_key = set(dict_d.keys()).difference(key)
for no_key in set_no_key:
    ans = dict_d[key].intersection(dict_d[no_key])

for key in ans:
    print(key)




