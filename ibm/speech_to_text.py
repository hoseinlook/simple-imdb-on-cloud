import json

from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from simple_imdb import settings

authenticator = IAMAuthenticator(settings.IMB_SPEECH_TOKEN)
speech_to_text = SpeechToTextV1(
    authenticator=authenticator
)
speech_to_text.set_service_url(' https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/')


def convert_speech_to_text(audio_file: open) -> str:
    item = speech_to_text.recognize(
        audio=audio_file,
        content_type='audio/ogg',
        timestamps=True,
        word_confidence=True).get_result()
    text = item['results'][0]['alternatives'][0]['transcript']
    print(text)
    return text


