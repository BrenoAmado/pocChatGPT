from tabula import read_pdf

def extract_data_pdf(arquivo):
    dataframes = read_pdf(arquivo, pages='all')
    return dataframes


