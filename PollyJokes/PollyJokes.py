import os, boto3, requests

defaultRegion = '' # AWS Region

jokeUrl = "" # Joke API
jokeGet = requests.get(jokeUrl)
jokeText = jokeGet.text



def connectToPolly(regionName=defaultRegion):
    return boto3.client('polly', region_name=regionName)

def speak(polly, text, format='mp3', voice='Amy'):
    resp = polly.synthesize_speech(OutputFormat=format, Text=text, VoiceId=voice)
    soundfile = open('sound.mp3', 'wb')
    soundBytes = resp['AudioStream'].read()
    soundfile.write(soundBytes)
    soundfile.close()

polly = connectToPolly()
speak(polly, jokeText)
os.system("sound.mp3")
