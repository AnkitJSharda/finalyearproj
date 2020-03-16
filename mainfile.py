from tfidf import summarized_list

finallist =[]

for i in summarized_list:
    if list(i.split("."))==['']:
        continue
    finallist.append(i.split(".")) 

finallist1 = []
for i in finallist:
    i.pop()
    for j in i:
        finallist1.append(j)

#print(finallist1)
'''                          
for i in finallist1:
    print(type(i))
'''
