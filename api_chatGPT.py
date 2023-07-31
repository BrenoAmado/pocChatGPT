import openai


def GPTResponse(question):
    # Configure o seu token de autenticação
    openai.api_key = "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"

    # Texto que você quer que o modelo complete
    texto_para_completar = f"{question}"

    # Fazendo a chamada à API com o motor gpt-3.5-turbo
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Modelo de chat gpt-3.5-turbo
        messages=[
            {"role": "system", "content": "Você é um assistente de chat."},
            {"role": "user", "content": texto_para_completar}
        ]
    )

    # Acessando a resposta do modelo
    gpt_response = resposta['choices'][0]

    return gpt_response