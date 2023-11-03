import pandas as pd
from datetime import date

df = pd.read_csv("agenda.csv", index_col=False)
cols = df.columns
datum = cols[1:]
persoon = cols[0]
diensten = {"V": ["0700", "1530"],
            "LOP": ["0800", "1630"],
            "L": ["1430", "2300"]}
print(diensten)

###
datum2 = []
datum_final = []
for i in datum:
    datum1 = [int(item) for item in i.split("/")]
    datum2.append(datum1)

for i in datum2:
    datum_final.append(date(i[2], i[1], i[0]))

print(datum_final)

###
# Output file
df_out = pd.DataFrame(columns=["Subject","Start date","Start time","End date","End time"])
df_out.loc[len(df_out)] = ["test", 1,2,3,4]
df_out.loc[len(df_out)] = ["test2", 3,4,5,6]
print(df_out)