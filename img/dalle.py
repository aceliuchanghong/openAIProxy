import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

proxyHost = "127.0.0.1"
proxyPort = 10809

proxies = {
    "http": f"http://{proxyHost}:{proxyPort}",
    "https": f"http://{proxyHost}:{proxyPort}"
}
prompt = input("Introduction:\n")
openai.proxy = proxies
response = openai.Image.create(
    prompt=prompt,
    n=1,
    size="512x512"
)
print(response)
image_url = response['data'][0]['url']
print(image_url)
