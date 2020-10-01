from covid19.main import COVID

covid = COVID()
covid.get()
negara = covid.country
for data in negara:
    print ("Negara: " + data)