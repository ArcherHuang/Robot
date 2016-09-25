import httplib, json, urllib

accessToken = ""
wavBody = ""
accessTokenHost = "api.cognitive.microsoft.com"
tokenPath = "/sts/v1.0/issueToken"
msBingSpeechAPIKey = ""

headers = {
            "Content-type": "application/x-www-form-urlencoded",
            "Ocp-Apim-Subscription-Key": msBingSpeechAPIKey
        }

params = urllib.urlencode({})
conn = httplib.HTTPSConnection(accessTokenHost)
conn.request("POST", tokenPath, "", headers)
response = conn.getresponse()
accessToken = response.read()
conn.close()
print(response.status, response.reason, accessToken)
