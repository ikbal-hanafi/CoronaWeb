from covid19.main import COVID

negara = "Indo"
covid = COVID()
covid.get()
dataMeninggal = covid.getRecov(country=negara)
for data in dataMeninggal:
    print ("Negara: " + data["country"]) # Mengambil nama negara
    print ("Sembuh: " + str(data["recovered"])) # Mengambil jumlah yang meninggal
    print ("-" * 25) # Garis
