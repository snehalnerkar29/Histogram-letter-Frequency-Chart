from collections import Counter
import random
import numpy as np
import matplotlib.pyplot as plt

text_file = 'Sample_Letter_Frequencies.txt'

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# Initialize the dictionary of letter counts: {'A': 0, 'B': 0, ...}
lcount = dict([(l, 0) for l in letters])
print("Lcount: ",lcount)
# Read in the text and count the letter occurences
for l in open(text_file).read():
    try:
        lcount[l.upper()] += 1
    except KeyError:
        # Ignore characters that are not letters
        pass
# The total number of letters
norm = sum(lcount.values())
print("Updated Lcount: ",lcount)
fig = plt.figure()
ax = fig.add_subplot(111)
# The bar chart, with letters along the horizontal axis and the calculated
# letter frequencies as percentages as the bar height
x = range(26)
# ax.bar(x, [lcount[l]/norm * 100 for l in letters], width=0.8,
#        color='b', alpha=0.5, align='center')
ax.bar(x, [lcount[l] for l in letters], width=0.9,
       color='b', alpha=0.5, align='center')
ax.set_xticks(x)
ax.set_xticklabels(letters)
ax.tick_params(axis='x', direction='out')
#Set 26 params
ax.set_xlim(-0.5, 25.5)
ax.yaxis.grid(True)
ax.set_ylabel('Letter frequency, %')
plt.show()

######################################################################### 

msg_sample=""
with open("Sample_Letter_Frequencies.txt","r") as f:
    data=f.readlines()
#     print(data)
    for d in data:
        print(d)
        print("=========================")
        msg_sample=msg_sample+d

from collections import Counter

import numpy as np
import matplotlib.pyplot as plt

msg_sample=msg_sample.replace(" ","")
c_data = Counter(msg_sample)
print("MESSAE IS : ",msg_sample)
print(c_data)
# c_data=dict(sorted(c_data.items()))
# plt.bar(c.keys(),c.values())

from collections import Counter
a = list(msg_sample)
counts = Counter(a)
# print(counts)
width = 120  # Adjust to desired width
longest_key = max(len(key) for key in counts)
graph_width = width - longest_key - 2
widest = counts.most_common(1)[0][1]
scale = graph_width / float(widest)
# print("Sorted:")
# print(sorted(counts.items(),key=lambda k:(k[1],k[0])))
for key, size in sorted(counts.items(),key=lambda k:(k[1],k[0])):
    print('{}: {}'.format(key, int(size * scale) * '*'))
 
