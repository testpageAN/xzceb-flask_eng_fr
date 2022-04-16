'''Translator

'''
import os
#import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

#language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com')
language_translator.set_service_url\
    ('https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/bebfd8c4-f6e6-4c72-832a-8c634f67fa67')
#language_translator.set_disable_ssl_verification(True)

def english_to_french(englishText):
    '''Translation fron English to French

    '''
    translation = language_translator.translate(
        text=englishText,
        model_id='en-fr').get_result()
    frenchText = translation['translations'][0]['translation']

    return frenchText


def french_to_english(frenchText):
    '''Translation fron French to English

    '''
    translation = language_translator.translate(
        text=frenchText,
        model_id='fr-en').get_result()
    englishText = translation['translations'][0]['translation']
    return englishText

