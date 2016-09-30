# -*- coding: UTF-8 -*-
# http://www.ibm.com/watson/developercloud/doc/language-translator/customizing.shtml
# http://www.ibm.com/watson/developercloud/language-translator/api/v2/

# ******************************************************************************************
# Import Package                                                                           #
# ******************************************************************************************

import ConfigParser
import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import LanguageTranslatorV2 as LanguageTranslator

# ******************************************************************************************
# Get Service username and password                                                        #
# ******************************************************************************************

Config = ConfigParser.ConfigParser()
Config.read("watson_Language_Translator_config.ini")
username = Config.get('LanguageTranslator', 'username')
password = Config.get('LanguageTranslator', 'password')

# ******************************************************************************************
# IBM Bluemix Watson Language Translator API - Identifiable languages                      #
# ******************************************************************************************

languages = language_translator.get_identifiable_languages()
print(json.dumps(languages, indent=2))

# ******************************************************************************************
# IBM Bluemix Watson Language Translator API - translate                                   #
# ******************************************************************************************

translation = language_translator.translate(
    text='hello',
    source='en',
    target='es')
print(json.dumps(translation, indent=2, ensure_ascii=False))

# ******************************************************************************************
# IBM Bluemix Watson Language Translator API - identify                                    #
# ******************************************************************************************

language = language_translator.identify('this is a test')
print(json.dumps(language, indent=2))

