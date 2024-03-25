import pandas as pd

def rooster_output(filename = "rooster.xlsx"):
  try:
    rooster = pd.read_excel("rooster.xlsx")
  except:
    rooster = pd.read_excel(input("Vul bestandsnaam in + .xlsx "))
  rooster["end date"] = rooster["start date"].copy()
  rooster["subject"] = rooster["subject"].fillna("Werk")
  rooster = rooster.dropna()
  begin_tijd = [x.split("-")[0] for x in rooster["tijd"]]
  eind_tijd = [x.split("-")[1] for x in rooster["tijd"]]
  rooster["start time"] = begin_tijd
  rooster["end time"] = eind_tijd
  rooster.drop("tijd", axis=1, inplace=True)
  rooster.to_csv("output.csv", index=False)

if __name__ == "__main__":
  rooster_output()
