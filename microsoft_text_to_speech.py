import get_microsoft_token
import httplib, json, urllib
import requests
import uuid
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

getUUID = uuid.uuid4()
accessToken = get_microsoft_token.getAccessToke()
lang = "en-US"
female = True
text = "I come from Taiwan"
template = """
        <speak version='1.0' xml:lang='{0}'>
            <voice xml:lang='{0}' xml:gender='{1}' name='{2}'>
                {3}
            </voice>
        </speak>
"""

speechHost = "speech.platform.bing.com"
headers = {
    "Content-type": "application/ssml+xml",
    "X-Microsoft-OutputFormat": "riff-16khz-16bit-mono-pcm",
    "Authorization": "Bearer " + accessToken,
    "X-Search-AppId": str(getUUID).replace('-', ''),
    "X-Search-ClientID": str(getUUID).replace('-', ''),
    "User-Agent": "TTSForPython"
}
name = "Microsoft Server Speech Text to Speech Voice (en-US, ZiraRUS)"
data = template.format(lang, "Female" if female else "Male", name, text)

conn = httplib.HTTPSConnection(speechHost)
conn.request("POST", "/synthesize", data, headers)
response = conn.getresponse()
ttsResponse = response.read()
conn.close()
print(response.status, response.reason)
if response.status == 200:
    f = open('test.wav','wb')
    f.write(ttsResponse)
    f.close()
