import json
import re
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, CategoriesOptions

authenticator = IAMAuthenticator('syvCtnQCZoxqdJBqWRBFQQ-6jny7hUUOA8f9WQZdjEGH')
service = NaturalLanguageUnderstandingV1(version='2018-03-16',authenticator=authenticator)
service.set_service_url('https://gateway.watsonplatform.net/natural-language-understanding/api')


with open("C:/Users/ankit.sharda/Desktop/FinalyearProject/testfile.txt", "r") as f:
    content_list = f.read()

op = content_list.split(".")
op.pop()

lin = []
for i in op:
    li = re.sub(r" ?\([^)]+\)", "", i)
    l = re.sub(r'\[.*\]', '', li)
    lin.append(l)
'''
for i in lin:
    print()
    print(i)
    response = service.analyze(
        text = i,
        features=Features(categories=CategoriesOptions(limit=3))).get_result()

    print(json.dumps(response['categories']], indent = 2))

f.close()'''


for i in lin:
    print()
    print(i)
    response = service.analyze(
        text = i,
        features=Features(categories=CategoriesOptions(limit=3))).get_result()

    for i in json.dumps(response['categories']):
        print(i, end= '')


f.close()


