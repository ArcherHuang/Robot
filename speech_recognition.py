# *************************************************************************************
# Version:     2016.09.23                                                             #
# Author:      Archer Huang                                                           #
# Description: chatbot (Microsoft Bing - STT, Conversation, TTS)                      #
# Hardware: Linkit Smart 7688 Duo                                                     #
# Language: Python 2.7                                                                #
# *************************************************************************************

import httplib, json, urllib
import uuid
import get_microsoft_token

getUUID = uuid.uuid4()
#print "getUUID: " + str(getUUID)
# *************************************************************************************
# Get Access Token
# https://dev.cognitive.microsoft.com/docs/services/57346a70b4769d2694911369/operations/57346edcb5816c23e4bf7421                                                                    #
# *************************************************************************************

accessToken = get_microsoft_token.getAccessToke()
print "accessToken: " + accessToken

# *************************************************************************************
# Read the binary from wave file                                                      #
# *************************************************************************************

f = open('turn_on_the_headlights.wav','rb')
try:
    wavBody = f.read();
finally:
    f.close()

# *************************************************************************************
# Speech Recognition                                                                  #
# *************************************************************************************

requestid = str(getUUID) #this can be any unique GUID
appid = "D4D52672-91D7-4C74-8AD8-42B1D98141A5"
locale = "en-US"
deviceOS = "linux"
version = "3.0"
instanceid = str(getUUID) #this can be any unique GUID
headers = { "Content-type": "audio/wav; samplerate=16000", "Authorization": "Bearer " + accessToken }
conn = httplib.HTTPSConnection("speech.platform.bing.com")
conn.request("POST", "/recognize/query?scenarios=ulm&appid=" + appid +"&locale=" + locale + "&device.os=" + deviceOS + "&version=" + version + "&format=json&requestid=" + requestid + "&instanceid=" + instanceid, wavBody, headers)
response = conn.getresponse()
print(response.status, response.reason)
data = response.read()
print(data)
conn.close()
encodedjson = json.dumps(data)
decodejson = json.loads(data)
print "\n" + decodejson["results"][0]["lexical"]


