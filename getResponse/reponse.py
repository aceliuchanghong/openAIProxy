import os

import openai
from openai import OpenAI
from requests import Session
from requests.adapters import HTTPAdapter


proxyHost = "127.0.0.1"
proxyPort = 10809
# proxies = {
#     "http": f"http://{proxyHost}:{proxyPort}",
#     "https": f"http://{proxyHost}:{proxyPort}"
# }


client = OpenAI()
client.api_key = os.getenv("OPENAI_API_KEY")
completion = client.chat.completions.create(
    model="gpt-4-1106-preview",
    messages=[
        {"role": "system",
         "content": "windows环境下,openai-1.2.4的模型如何设置代理,其中from openai import OpenAI,client = OpenAI()"},
        # {"role": "user", "content": "Hello!"}
    ]
)

print(completion.choices[0].message.content)
