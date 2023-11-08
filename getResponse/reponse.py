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
    model="gpt-4-1106-preview",  # gpt-3.5-turbo gpt-4-1106-preview gpt-4-0613
    messages=[
        {"role": "system", "content": "项目名称 GDSN ,统一监管报送有关 其中GDSN是汉字拼音首字母缩写,猜GDSN的汉字"},
        #{"role": "system", "content": "免费使用chatgpt4的方法"}
    ]
)
print(completion.choices[0].message.content)
