import speech_recognition as sr
# success
# print(sr.__version__)
# obtain audio from the microphone
r = sr.Recognizer()

harvard = sr.AudioFile('/Users/neel.kanani/Desktop/Python/speechApp/harvard.wav')
# type(harvard)
with harvard as source:
    audio = r.record(source)


trans = r.recognize_google(audio)
print(trans)

# print(audio)
