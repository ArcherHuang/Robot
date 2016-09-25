import httplib, json, urllib

accessToken = ""
wavBody = ""
accessTokenHost = "api.cognitive.microsoft.com"
tokenPath = "/sts/v1.0/issueToken"
msBingSpeechAPIKey = "9b4c82c9b8c342aa8beac43cf33a12bc"

def getAccessToke():

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
	return accessToken

