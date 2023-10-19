import os
import openai

proxyHost = "127.0.0.1"
proxyPort = 10809
proxies = {
        "http": f"http://{proxyHost}:{proxyPort}",
        "https": f"https://{proxyHost}:{proxyPort}"
    }
openai.proxy = proxies
openai.api_key = os.getenv("OPENAI_API_KEY")
    
audio_file = open("WeChat_20231007161725.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
