from covid19.main import COVID

negara = "Indo"
covid = COVID()
covid.get()
dataMeninggal = covid.getDeath(country=negara)
for data in dataMeninggal:
    print ("Negara: " + data["country"]) # Mengambil nama negara
    print ("Meninggal: " + str(data["deaths"])) # Mengambil jumlah yang meninggal
    print ("-" * 25) # Garis
