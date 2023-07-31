from tabula import read_pdf

dataframes = read_pdf('adm_mack_test.pdf', pages='all')

print(dataframes)