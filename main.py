from api_chatGPT import GPTResponse
from excel_adm_test import extract_data_excel
from pdf_adm_mack_test import extract_data_pdf


def main():
    pdf = extract_data_pdf("adm_mack_test.pdf")
    excel = extract_data_excel("adm_test.xlsm")
    response = GPTResponse("Correlacione as duas e veja se x aluno sera aprovado e em qual semestre: " + str(pdf) + str(excel))
    print(response)


if __name__ == "__main__":
    main()