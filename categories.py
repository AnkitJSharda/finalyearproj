import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, CategoriesOptions

authenticator = IAMAuthenticator('syvCtnQCZoxqdJBqWRBFQQ-6jny7hUUOA8f9WQZdjEGH')
service = NaturalLanguageUnderstandingV1(version='2018-03-16',authenticator=authenticator)
service.set_service_url('https://gateway.watsonplatform.net/natural-language-understanding/api')


response = service.analyze(
    text = 'Donald Trump addressed a rally in texas',
    features=Features(categories=CategoriesOptions(limit=3))).get_result()

print(json.dumps(response, indent=2))


