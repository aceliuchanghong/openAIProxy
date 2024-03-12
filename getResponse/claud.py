import anthropic
import httpx

proxyHost = "127.0.0.1"
proxyPort = 10809
client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    http_client=httpx.Client(proxies=f"http://{proxyHost}:{proxyPort}")
)
message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1000,
    temperature=0,
    messages=[
        {"role": "user",
         "content": "python写一个冒泡排序"
         }
    ]
)

print(message.content[0].text)
