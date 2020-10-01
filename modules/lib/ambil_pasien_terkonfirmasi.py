from covid19.main import COVID

negara = "Indo"
covid = COVID()
covid.get()
terkonfirmasi = covid.getConfirmed(country=negara)
for data in terkonfirmasi:
    print ("Negara: " + data["country"]) # Mengambil nama negara
    print ("Terkonfirmasi: " + str(data["confirmed"])) # Mengambil jumlah yang terkonfirmasi
    print ("-" * 25) # Garis
