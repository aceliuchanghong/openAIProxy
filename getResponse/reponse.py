import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

proxyHost = "127.0.0.1"
proxyPort = 10809

proxies = {
    "http": f"http://{proxyHost}:{proxyPort}",
    "https": f"http://{proxyHost}:{proxyPort}"
}
openai.proxy = proxies


completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", #gpt-4-0613
  messages=[
    {"role": "system", "content": "tell me are u gpt-4 or gpt 3.5?"}
  ]
)

print(completion.choices[0].message)
