import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

googleAPIHost = "https://www.googleapis.com"
key = "AIzaSyC7QHmUMZPSOa_ggF3x86VdwXWEjOq-eAM"
queryString = "hello world"

requestURL = googleAPIHost + "/language/translate/v2/detect?key=" + key + "&q=" + queryString
print "requestURL: " + requestURL

response = requests.get(requestURL, verify=False)

print response.status_code
print response.text

decodejson = json.loads(response.text)
print "\n" + decodejson["data"]["detections"][0][0]["language"]

