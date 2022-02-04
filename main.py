import pandas as pd

df_csv = pd.read_csv(r"path of file.csv")

pd.set_option('display.max_rows', df_csv.shape[0])
pd.set_option('display.max_columns', None)

dups = df_csv.pivot_table(index = ['name of what you want to count duplicates'], aggfunc = 'size')


print(dups)


dups.to_csv(r"path where you want to save the generated file\name.csv", index = True)
