import pandas as pd

df1 = pd.read_csv("DATA1.csv")
df2 = pd.read_csv("DATA2.csv")
pd_final = pd.merge(df1, df2, how="left", on="POLICY_NO", )

pd_final.to_csv("DATA_FINAL.csv")