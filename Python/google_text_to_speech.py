#pip install gTTS

#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gtts import gTTS
tts = gTTS(text='你好，我來自台灣', lang='zh-tw')
tts.save("hello.mp3")
