# -*- coding: UTF-8 -*-

import ConfigParser
import json
from watson_developer_cloud import ToneAnalyzerV3

Config = ConfigParser.ConfigParser()
Config.read("watson_Tone_Analyzer_config.ini")

userName = Config.get('ToneAnalyzer', 'userName')
passWord = Config.get('ToneAnalyzer', 'passWord')

tone_analyzer = ToneAnalyzerV3(
    username = userName,
    password = passWord,
    version = '2016-02-11')

print(json.dumps(tone_analyzer.tone(text='我好高興'), indent=2))
