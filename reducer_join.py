import sys
from collections import defaultdict

current_user = None
current_row = None
QUERY = "query"
URL = "url"

my_dict = defaultdict(list)

for line in sys.stdin:
    id_user, row = line.strip().split("\t", 1)
    marker, value = row.split(":", 1)
    if id_user != current_user:
        if current_user:
            for query in my_dict["query"]:
                for url in my_dict["url"]:
                    print(f"{current_user}\t{query}\t{url}")
            my_dict = defaultdict(list)
        current_user = id_user
    my_dict[marker].append(value)

if current_user:
    for q in my_dict[QUERY]:
        for u in my_dict[URL]:
            print(f"{current_user}\t{q}\t{u}")
    my_dict = defaultdict(list)
