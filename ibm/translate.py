import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Prepare the Authenticator
from simple_imdb import settings

authenticator = IAMAuthenticator(settings.IMB_TRANSLATION_TOKEN)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com')


# Translate
def translate(text, to_lang, from_lang='en'):
    translation = language_translator.translate(
        text=text, source=from_lang, target=to_lang).get_result()
    print(text,to_lang ,translation)
    return translation['translations'][0]['translation']

print(translate('hi my name is joun' , 'fr'))
