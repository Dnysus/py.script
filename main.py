import pandas as pd

df_csv = pd.read_csv(r"path of file.csv")

pd.set_option('display.max_rows', df_csv.shape[0])
pd.set_option('display.max_columns', None)

dups = df_csv.pivot_table(index = ['Column name'], aggfunc = 'size')


print(dups)


dups.to_csv(r"path where to save csv\name for file.csv", index = True)
