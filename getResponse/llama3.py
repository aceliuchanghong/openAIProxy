from openai import OpenAI
import os

# Create an OpenAI client with your deepinfra token and endpoint
api_key = os.getenv("DEEPINFRA_API_KEY")
openai = OpenAI(
    api_key=api_key,
    base_url="https://api.deepinfra.com/v1/openai",
)

chat_completion = openai.chat.completions.create(
    model="meta-llama/Meta-Llama-3-70B-Instruct",
    messages=[{"role": "user", "content": "你叫什么?中文回答"}],
    temperature=0.7,
)

print(chat_completion.choices[0].message.content)
