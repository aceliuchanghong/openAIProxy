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
    model="gpt-4-0613",  # gpt-3.5-turbo
    messages=[
        #{"role": "system", "content": "尝试一下写一首七言绝句诗,每行的结尾分别是:丽,看,完,离"},
        {"role": "system", "content": "write a poem which ends with the words start a,b,c-...-z"}
    ]
)
print(completion.choices[0].message.content)
