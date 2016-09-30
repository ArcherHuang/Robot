# -*- coding: UTF-8 -*-

# ******************************************************************************************
# Import Package                                                                           #
# ******************************************************************************************

import ConfigParser
import httplib, json, urllib, base64

# ******************************************************************************************
# Get Service API Key and Check Local File or URL                                          #
# ******************************************************************************************

isImageFromURL = 1
Config = ConfigParser.ConfigParser()
Config.read("microsoft_Computer_Vision_config.ini")
apiKey = Config.get('ComputerVision', 'apiKey')

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

params = urllib.urlencode({
    'visualFeatures': 'Categories,Tags,Description,Faces,ImageType,Color,Adult',
    'details': 'Celebrities',
})

host = 'api.projectoxford.ai'
requestURL = "/vision/v1.0/analyze?%s" % params
imageURL = "http://i.imgur.com/WyfYIwZ.jpg"
jsonImageURL = { 'url': imageURL } 
localFilePath = '/Users/Archer/Downloads/recognition2.jpg'

# ******************************************************************************************
# POST Microsoft Computer Vision API                                                       #
# ******************************************************************************************

try:
	conn = httplib.HTTPSConnection(host)
	if isImageFromURL:
		conn.request("POST", requestURL, json.dumps(jsonImageURL), headers)
	else:
		conn.request("POST", requestURL, open(localFilePath, 'rb'), headers)
	response = conn.getresponse()
	print(response.status, response.reason)
	data = response.read()
	conn.close()
	print(data)
except Exception as e:
	print("[Errno {0}] {1}".format(e.errno, e.strerror))
	print(e.message)