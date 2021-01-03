
from gtts import gTTS
from io import BytesIO
from playsound import playsound

mp3_fp = BytesIO()
tts = gTTS('', lang='en-uk')
tts.save('goodMorning.mp3')
playsound('goodMorning.mp3') 