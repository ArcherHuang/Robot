# -*- coding: UTF-8 -*-

# ******************************************************************************************
# Import Package                                                                           #
# ******************************************************************************************

import ConfigParser
import httplib, json, urllib, base64

# ******************************************************************************************
# Get Service API Key and Check Local File or URL                                          #
# ******************************************************************************************

isImageFromURL = 0
Config = ConfigParser.ConfigParser()
Config.read("microsoft_Emotion_config.ini")
apiKey = Config.get('Emotion', 'apiKey')

# ******************************************************************************************
# Set Request Header                                                                       #
# ******************************************************************************************

if isImageFromURL:
	contentType = "application/json"
else:
	contentType = "application/octet-stream"

headers = {
	'Content-Type': contentType,
	'Ocp-Apim-Subscription-Key': apiKey,
}

host = 'api.projectoxford.ai'
requestURL = '/emotion/v1.0/recognize'
imageURL = "http://i.imgur.com/XR1hU0S.jpg"
jsonImageURL = { 'url': imageURL } 
localFilePath = '/Users/Archer/Downloads/recognition2.jpg'

# ******************************************************************************************
# POST Microsoft Emotion API                                                               #
# ******************************************************************************************

try:
	conn = httplib.HTTPSConnection(host)
	if isImageFromURL:
		conn.request("POST", requestURL, json.dumps(jsonImageURL), headers)
	else:
		conn.request("POST", "/emotion/v1.0/recognize", open(localFilePath, 'rb'), headers)
	response = conn.getresponse()
	print(response.status, response.reason)
	data = response.read()
	conn.close()
	print(data)
except Exception as e:
	print("[Errno {0}] {1}".format(e.errno, e.strerror))
	print(e.message)