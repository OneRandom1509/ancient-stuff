import json

elements = {} 
Symbols = {}
f = open('data.json')
data = json.load(f)

list1 = []
for a in data["Table"]["Row"]:
    for key in a.keys():
        list1.append(key)

for element in data["Table"]["Row"]:                                        #for numbers.json
    number = data["Table"]["Row"].index(element)
    elements[list1[number]] = data["Table"]["Row"][number][list1[number]][0] 

with open('numbers.json', 'w') as outfile:
    json.dump(elements, outfile)

for element in data["Table"]["Row"]:                                         #for symbols.json
    number = data["Table"]["Row"].index(element)
    Symbols[data["Table"]["Row"][number][list1[number]][1]] = [data["Table"]["Row"][number][list1[number]][0], data["Table"]["Row"][number][list1[number]][2]]

with open('symbols.json', 'w') as outfile:
    json.dump(Symbols, outfile)