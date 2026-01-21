from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="none")

template = """
Твой длинный промпт...
Ключевое слово: {word}
...
"""

words = ["alpha", "beta", "gamma"]

prompts = [template.format(word=w) for w in words]

response = client.chat.completions.create(
    model="meta-llama/Llama-3.3-70B-Instruct",
    messages=[{"role": "user", "content": p} for p in prompts],
    max_tokens=100
)