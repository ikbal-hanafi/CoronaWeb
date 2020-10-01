from covid19.main import COVID

negara = "Indo"
covid = COVID()
covid.get()
dataAktif = covid.getActive(country=negara)
for data in dataAktif:
    print ("Negara: " + data["country"]) # Mengambil nama negara
    print ("Aktif : " + str(data["active"])) # Mengambil jumlah yang aktif
    print ("-" * 25) # Garis
