'''
Speech Recognition based Python packages:
-SpeechRecognition
-google-cloud-speech
-apiai
-pocketsphinx
-assemblyai
-watson-devloper-cloud
-wit

pip install SpeechRecognition #to install SpeechRecognition

import speech_recognition as sr #to import SpeechRecognition

print(sr.__version__) #to check version

    audio_data = sr.record(source, duration=100) #to give duration in seconds
sr.recognize_google(audio_data, show_all=True) #to see several possible transcripts form a single audio source.

mc=sr.Microphone()
mc.list_microphone_names() #to check mics available in your computer.
mc=sr.Microphone(device_index=0) #to select a particular microphone.
'''

import speech_recognition as sr #to import SpeechRecognition

r = sr.Recognizer()
info = sr.AudioFile("speech.wav")

with info as source:
    sr.adjust_for_ambient_noise(source) #to remove noise from audio
    audio_data = sr.record(source)
lis = sr.recognize_google(audio_data) #to recognize any speech in the 
print(lis)