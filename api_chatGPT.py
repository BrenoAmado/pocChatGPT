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
    gpt_response = resposta['choices'][0]['message']['content']

    return gpt_response