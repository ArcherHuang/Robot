# https://www.microsoft.com/cognitive-services/en-us/Speech-api/documentation/API-Reference-REST/BingVoiceOutput

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

token = "9b4c82c9b8c342aa8beac43cf33a12bc"
lang = "en-US"
female = True
text = "hello world"
template = """
        <speak version='1.0' xml:lang='{0}'>
            <voice xml:lang='{0}' xml:gender='{1}' name='{2}'>
                {3}
            </voice>
        </speak>
"""

url = "https://speech.platform.bing.com/synthesize"
headers = {
    "Content-type": "application/ssml+xml",
    "X-Microsoft-OutputFormat": "riff-16khz-16bit-mono-pcm",
    "Authorization": "Bearer " + token,
    "X-Search-AppId": "07D3234E49CE426DAA29772419F436CA",
    "X-Search-ClientID": "1ECFAE91408841A480F00935DC390960",
    "User-Agent": "OXFORD_TEST"
}
name = "Microsoft Server Speech Text to Speech Voice (en-US, ZiraRUS)"
data = template.format(lang, "Female" if female else "Male", name, text)

response = requests.post(url, data=data, headers=headers)

if response.ok:
    print response.content
else:
    raise response.raise_for_status()