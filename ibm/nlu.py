from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions

from simple_imdb import settings

nlu_authenticator = IAMAuthenticator(settings.IMB_NLU_TOKEN)

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2021-08-01',
    authenticator=nlu_authenticator
)
natural_language_understanding.set_service_url(' https://api.eu-gb.natural-language-understanding.watson.cloud.ibm.com')


def get_anger(text):
    response = natural_language_understanding.analyze(
        text=text,
        features=Features(emotion=EmotionOptions())).get_result()

    print(response)
    anger = response['emotion']['document']['emotion']['anger']
    return anger

