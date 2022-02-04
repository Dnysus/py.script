import pandas as pd

df_csv = pd.read_csv(r"C:\Users\Dion\Desktop\Serial.csv")

pd.set_option('display.max_rows', df_csv.shape[0])
pd.set_option('display.max_columns', None)

dups = df_csv.pivot_table(index = ['Serial Number'], aggfunc = 'size')


print(dups)


dups.to_csv(r"C:\Users\Dion\Desktop\OnlyDups.csv", index = True)
