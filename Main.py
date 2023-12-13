import pandas as pd
from datetime import datetime, timedelta

def rooster_output(path):
  df = pd.read_csv(path, index_col=False, sep=";")
  diensten = {"V": [7, 8.5],
              "LOP": [8, 8.5],
              "L": [14.5, 8.5],
              "N": [23,8.5],
              "D": [8,8.5]}
  
  failed_df = df.loc[:, ~df.isin(list(diensten.keys())).all()]
  failed_df = failed_df.loc[:, ~df.isin(["X", "Vrij"]).all()]
  df = df.loc[:, df.isin(list(diensten.keys())).all()]
  rooster = df.loc[0].to_list()
  werkdatum = df.columns.to_list()
  
  lop_days = []
  for column in df.columns:
    if "LOP" in df[column].values:
        lop_days.append(column)
  lop_days_iso = [datetime.strptime(item, "%d-%m-%Y").date() for item in lop_days]
  
  datum2 = []
  for i in werkdatum:
    datum1 = [int(item) for item in i.split("-")]
    datum2.append(datum1)
  
  begindatum = [datetime(i[2], i[1], i[0]) for i in datum2]
  begintijden = [diensten[i][0] for i in rooster]
  begintijden_final = []
  eindtijden_final = []
  
  for i in range(len(rooster)):
    begintijden_final.append(begindatum[i] + timedelta(hours=begintijden[i]))
  
  start_date = []
  end_date = []
  start_time = []
  end_time = []
  df_out = pd.DataFrame(columns= ["Start date","Start time","End date","End time"])
  
  for i in range(len(begintijden_final)):
    temp = begintijden_final[i] + timedelta(hours=diensten[rooster[i]][1])
    eindtijden_final.append(temp)
    start_date.append(begintijden_final[i].date())
    start_time.append(begintijden_final[i].time())
    end_date.append(eindtijden_final[i].date())
    end_time.append(eindtijden_final[i].time())
    df_out.loc[len(df_out)] = [start_date[i], start_time[i], end_date[i], end_time[i]]
  
  df_out["Subject"] = "Werken"
  for item in lop_days_iso:
    df_out.loc[(df_out["Start date"] == item), "Subject"] = "LOP"
  
  print(df_out)
  print('======================================================'+ "\n")
  print("Fout in verwerking: ")
  print(failed_df.iloc[0,:])
  df_out.to_csv("output.csv", index=False)
  failed_df.to_excel("failed.xlsx", index=False)
  input("Geslaagd! Druk op een knop om te sluiten. ")

if __name__ == "__main__":
  rooster_output(input("Voer bestandsnaam in. "))