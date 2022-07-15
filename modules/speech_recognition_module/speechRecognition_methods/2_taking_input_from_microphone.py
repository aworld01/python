"""
mc=sr.Microphone()
print(mc.list_microphone_names()) #to check mics available in your computer.
mc=sr.Microphone(device_index=0) #to select a particular microphone.
"""

import speech_recognition as sr

mc=sr.Microphone()
