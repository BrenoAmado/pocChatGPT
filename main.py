from api_chatGPT import GPTResponse
from excel_adm_test import extract_data_excel
from pdf_adm_mack_test import extract_data_pdf


def main():
    pdf = extract_data_pdf("adm_mack_test.pdf")
    excel = extract_data_excel("adm_test.xlsm")
    response = GPTResponse("Reformule passando carga horaria / nome da materia / aprovado ou não, retire de todas as paginas (total 3) e 48 registros / materias, e mande no formato de lista, mande na estrutura correta para ser jogado dentro de pd.DataFrame(response)" + str(pdf))
    print(response)


if __name__ == "__main__":
    main()