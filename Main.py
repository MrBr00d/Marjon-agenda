import pandas as pd
from datetime import date

datum = ["03/11/2023", "04/11/2023"]
datum2 = []
datum_final = []
for i in datum:
    datum1 = [int(item) for item in i.split("/")]
    datum2.append(datum1)

for i in datum2:
    datum_final.append(date(i[2], i[1], i[0]))

