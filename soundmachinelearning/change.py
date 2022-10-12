import pydub

#sound = pydub.AudioSegment.from_mp3("backaround.mp3")
#sound.export("backaround.wav", format="wav")

sound = pydub.AudioSegment.from_mp3("./猫怒り時.mp3")
sound.export("猫怒り時.wav",format="wav")