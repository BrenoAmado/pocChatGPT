import camelot
import pandas as pd
tables = camelot.read_pdf("adm_mack_test.pdf", pages='all')



pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
tables_general = [table.df for table in tables]
x = pd.concat(tables_general)
print(x)
