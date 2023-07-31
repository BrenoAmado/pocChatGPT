import openai

# Configure o seu token de autenticação
openai.api_key = "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"

# Texto que você quer que o modelo complete
texto_para_completar = "qual a cor de uma banana e um morango? "

# Fazendo a chamada à API com o motor gpt-3.5-turbo
resposta = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # Modelo de chat gpt-3.5-turbo
    messages=[
        {"role": "system", "content": "Você é um assistente de chat."},
        {"role": "user", "content": texto_para_completar}
    ]
)

# Acessando a resposta do modelo
texto_completado = resposta['choices'][0]['message']['content']

print(texto_completado)