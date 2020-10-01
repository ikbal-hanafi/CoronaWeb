from covid19.main import COVID

covid = COVID()
covid.get()
semua = covid.all
for data in semua:
    print ("Negara: " + data["country"]) # Mengambil nama negara
    print ("Aktif : " + str(data["active"])) # Mengambil jumlah yang aktif
    print ("Meninggal: " + str(data["deaths"])) # Mengambil jumlah yang meninggal
    print ("Sembuh: " + str(data["recovered"])) # Mengambil jumlah yang sembuh
    print ("Terkonfirmasi: " + str(data["confirmed"])) # Mengambil jumlah yang terkonfirmasi
    print ("-" * 25) # Garis
