import os
from collections import Counter
data = {'Eusebio': 120, 'Cruyff': 104, 'Pele': 150, 'Ronaldo': 132, 'Messi': 125}
sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)
convected_data = dict(sorted_data)
print(convected_data)
top3 = dict(Counter(convected_data).most_common(3))
print(top3)

