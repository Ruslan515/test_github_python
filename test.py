import pandas as pd
from my_lib import get_data

df = pd.DataFrame(get_data(), columns=["zz", "tt", "xx"])
df.to_csv("test_csv.csv", index=0)