import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

googleAPIHost = "https://www.googleapis.com"
key = "AIzaSyC7QHmUMZPSOa_ggF3x86VdwXWEjOq-eAM"
queryString = "hello"
source = "en"
target = "zh-CN"

requestURL = googleAPIHost + "/language/translate/v2?key=" + key + "&source=" + source + "&target=" + target + "&q=" + queryString
print "requestURL: " + requestURL

response = requests.get(requestURL, verify=False)

print response.status_code
print response.text

decodejson = json.loads(response.text)
print "\n" + decodejson["data"]["translations"][0]["translatedText"]

