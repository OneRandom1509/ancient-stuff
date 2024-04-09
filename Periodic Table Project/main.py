import json
#opening both json files
f = open('data.json')
data = json.load(f)
a = open('numbers.json')
numbers = json.load(a)
b = open('symbols.json')
symbols = json.load(b)

element = input(">>> Enter the element\n>>> ").capitalize()

try: #If the input is the name of the element
    index= int(numbers[element])
    AN = "Atomic Number: " + str(data["Table"]["Row"][index-1][element][0])
    Symbol = "Symbol: " + str(data["Table"]["Row"][index-1][element][1])
    AM = "Atomic Mass: " + str(data["Table"]["Row"][index-1][element][3])
    EC = "Electron Configuration: " + str(data["Table"]["Row"][index-1][element][5])
    EN = "Electronegativity: " + str(data["Table"]["Row"][index-1][element][6])
    AR = "Atomic Radius: " + str(data["Table"]["Row"][index-1][element][7])
    IE = "Ionization Energy: " + str(data["Table"]["Row"][index-1][element][8])
    EA = "Electron Affinity: " + str(data["Table"]["Row"][index-1][element][9])
    OS = "Oxidation States: " + str(data["Table"]["Row"][index-1][element][10])
    SS = "Standard State: " + str(data["Table"]["Row"][index-1][element][11])
    MP = "Melting Point: " + str(data["Table"]["Row"][index-1][element][12])
    BP = "Boiling Point: " + str(data["Table"]["Row"][index-1][element][13])
    Density = "Density: " + str(data["Table"]["Row"][index-1][element][14])
    GB = "Group Block: " + str(data["Table"]["Row"][index-1][element][15])
    YD = "Discovered in " + str(data["Table"]["Row"][index-1][element][16])
    if YD == "Discovered in Ancient Period":
        YD = "Discovered during Ancient Period"

    print(f"{element}\n{YD}\n\n\t{AN}\n\t{Symbol}\n\t{AM}\n\t{EC}\n\t{EN}\n\t{AR}\n\t{IE}\n\t{EA}\n\t{OS}\n\t{SS}\n\t{MP}\n\t{BP}\n\t{Density}\n\t{GB}")


except: #If the input is a symbol
    try:
        index= int(symbols[element][0])
        name = symbols[element][1]
        AN = "Atomic Number: " + str(data["Table"]["Row"][index-1][name][0])
        Symbol = "Symbol: " + str(data["Table"]["Row"][index-1][name][1])
        AM = "Atomic Mass: " + str(data["Table"]["Row"][index-1][name][3]) + " u"
        EC = "Electron Configuration: " + str(data["Table"]["Row"][index-1][name][5])
        EN = "Electronegativity: " + str(data["Table"]["Row"][index-1][name][6])
        AR = "Atomic Radius: " + str(data["Table"]["Row"][index-1][name][7]) + " pm"
        IE = "Ionization Energy: " + str(data["Table"]["Row"][index-1][name][8])
        EA = "Electron Affinity: " + str(data["Table"]["Row"][index-1][name][9])
        OS = "Oxidation States: " + str(data["Table"]["Row"][index-1][name][10])
        SS = "Standard State: " + str(data["Table"]["Row"][index-1][name][11])
        MP = "Melting Point: " + str(data["Table"]["Row"][index-1][name][12]) + " K"
        BP = "Boiling Point: " + str(data["Table"]["Row"][index-1][name][13]) + " K"
        Density = "Density: " + str(float(data["Table"]["Row"][index-1][name][14])*1000) + " kg/m³"
        GB = "Group Block: " + str(data["Table"]["Row"][index-1][name][15])
        YD = "Discovered in " + str(data["Table"]["Row"][index-1][name][16])
        if YD == "Discovered in Ancient Period":
            YD = "Discovered during Ancient Period"

        print(f"{name}\n{YD}\n\n\t{AN}\n\t{Symbol}\n\t{AM}\n\t{EC}\n\t{EN}\n\t{AR}\n\t{IE}\n\t{EA}\n\t{OS}\n\t{SS}\n\t{MP}\n\t{BP}\n\t{Density}\n\t{GB}\n")

    except:
        print("Element not found")