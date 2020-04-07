import pandas as pd
import os

pd.set_option('display.max_rows', None)

def only_numerics(seq):
    seq_type= type(seq)
    return seq_type().join(filter(seq_type.isdigit, seq))

# Define function to remove characters
def only_numericsT(seq):
    seq = str(seq)
    seq_type= type(seq)
    return seq_type().join(filter(seq_type.isdigit, seq))

# Read file
df = pd.read_excel('BD_consolidado.xlsx', sheet_name='beneficiarios')
print(df.iloc[287])

# Remove charcaters from id and phone numer
df['cedula'] = df['cedula'].apply(only_numericsT)
df['telefono'] = df['telefono'].apply(only_numericsT)

# export to an Excel file
filepath = os.getcwd() + "\data.xlsx"
df.to_excel(filepath, index=False, header=True)



