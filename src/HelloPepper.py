from naoqi import ALProxy

tts = ALProxy("ALTextToSpeech", "163.221.68.225", 9559)
tts.say("Hello")

