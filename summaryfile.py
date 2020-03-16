from categories6 import di2
from mainfile import finallist1

summary_list = []
for k in di2.keys():
    for i in finallist1:
        if i==k:
            summary_list.append(i)

summary = [item + '.' for item in summary_list]

summ = "".join(summary)
print(summ)




