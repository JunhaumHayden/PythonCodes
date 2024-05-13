import openai

# Defina sua chave da API do OpenAI
api_key = "your_key"
openai.api_key = api_key

# engines = openai.Engine.list()

# for engine in engines:
#     print(engine)
#     print('-'*20)
# print('='*20)

def chat(prompt):
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    prompt = "Que empresa criou o modelo de IA Gemini?"
    response = chat(prompt)
    print(response)