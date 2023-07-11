import os
import openai

proxyHost = "127.0.0.1"
proxyPort = 10809

proxies = {
    "http": f"http://{proxyHost}:{proxyPort}",
    "https": f"http://{proxyHost}:{proxyPort}"
}
openai.proxy = proxies
openai.api_key = os.getenv("OPENAI_API_KEY")
print(openai.api_key)
print(openai.Model.list())
