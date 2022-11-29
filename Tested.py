data = {'Eusebio': 120, 'Cruyff': 104, 'Pele': 150, 'Ronaldo': 132, 'Messi': 125}
sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)
convected_data = dict(sorted_data)
print(convected_data)
top_five = [{x: convected_data[x]} for x in convected_data]
print(top_five)
