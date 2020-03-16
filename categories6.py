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

di = dict()

for i in lin:
    response = service.analyze(
        text = i,
        features=Features(categories=CategoriesOptions(limit=3))).get_result()

    di[i] = json.dumps(response['categories'])
    
f.close()

di1 = dict()
for k,v in di.items():
    v = json.loads(v)
    t1 = v[0]
    try:
        t2 = v[1]
        t3 = t1["score"]
        t4 = t2["score"]
        if((t3-t4)>0.1):
            di1[k] = t1["label"]
        else:
            di1[k] = t2["label"]
    except IndexError:
        di1[k] = t1["label"]

di2 = dict()

for k,v in di1.items():
    di2[k] = "/".join(v.split("/")[:2])


vals = []
for k,v in di2.items():
    if v not in vals:
        vals.append(v)

di3 = dict()
#print(vals)

for i in vals:
    di3[i] = 0
    for k,v in di2.items():
        if v==i:
            di3[i]+=1

sorted_li = sorted(di3.items(), key=lambda kv: kv[1], reverse = True)

sorted_di3 = dict((x, y) for x, y in sorted_li)

num_of_elems = 0

for k,v in sorted_di3.items():
    num_of_elems = num_of_elems + 1

els = list(sorted_di3.items())
fi = els[0][1] #returns tuple of first key-value in reverse_sorted dictionary
lt = els[-1][1]
optimum_cnt = (fi + lt) / num_of_elems

include_categories = []
for k, v in di3.items():
    if(float(v) >= optimum_cnt):
        include_categories.append(k)


di4 = dict()

for i in include_categories:
    for k,v in di2.items():
        if(v==i):
            di4[k] = v
'''   
for k, v in di4.items():
    print(k, "\n", v)
    print("\n")
'''


di5 = dict()

for i in include_categories:
    for k,v in sorted_di3.items():
        if(k==i):
            di5[k] = v

sorted_lis = sorted(di5.items(), key=lambda kv: kv[1], reverse = True)

sorted_di5 = dict((x, y) for x, y in sorted_lis)

num_of_elems1 = 0
for k, v in sorted_di5.items():
    num_of_elems1 += 1
   # print(k, "\n", v)

cnt1 = int((num_of_elems1 * 40) / 100)  #for first cnt1 number of category, select its 60% sentences
cnt2 = int((num_of_elems1 * 40) / 100)  #for next cnt2 number of category, select its 40% sentences
cnt3 = num_of_elems1 - cnt1 - cnt2     #for remaining cnt3 number of category, select its 20% sentences

#print(cnt1, cnt2, cnt3)


di6 = dict()
c1 = []
c2 = []
c3 = []
for k, v in sorted_di5.items():
    if(cnt1!=0):
       c1.append(k)
       cnt1=cnt1-1
    elif cnt1==0 and cnt2!=0:
        if(cnt2==0):
            break
        c2.append(k)
        cnt2=cnt2-1
    else:
        c3.append(k)
        
"""
print(c1)
print(c2)
print(c3)
"""

top1 = []
mid1 = []
bottom1 = []

for k, v in di4.items():
    if v in c1:
        top1.append(k)
    if v in c2:
        mid1.append(k)
    if v in c3:
        bottom1.append(k)



    




  



