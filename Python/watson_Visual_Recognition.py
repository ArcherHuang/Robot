# -*- coding: UTF-8 -*-
# http://www.ibm.com/watson/developercloud/doc/visual-recognition/
# http://www.ibm.com/watson/developercloud/visual-recognition/api/v3/#detect_faces

# ******************************************************************************************
# Import Package                                                                           #
# ******************************************************************************************

import ConfigParser
import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

# ******************************************************************************************
# Get Service API Key and Check Local File or URL                                          #
# ******************************************************************************************

Config = ConfigParser.ConfigParser()
Config.read("watson_Visual_Recognition_config.ini")
apiKey = Config.get('VisualRecognition', 'apiKey')
imageURL = "http://i.imgur.com/WyfYIwZ.jpg"

# ******************************************************************************************
# IBM Bluemix Watson Visual Recognition API - Classify an image                            #
# ******************************************************************************************

visual_recognition = VisualRecognitionV3('2016-05-20', api_key=apiKey)
print(json.dumps(visual_recognition.classify(images_url=imageURL), indent=2))

# ******************************************************************************************
# IBM Bluemix Watson Visual Recognition API - Detect faces                                 #
# ******************************************************************************************

print(json.dumps(visual_recognition.detect_faces(images_url=imageURL), indent=2))
