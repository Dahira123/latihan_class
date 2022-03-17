class Keranjang:
    def __init__(self,inputNama, inputWarna, inputJumlah):
        self.nama = inputNama
        self.warna = inputWarna
        self.jumlah = inputJumlah

keranjang1 = Keranjang("Mangga" ,"Hijau",5)
keranjang2 = Keranjang("Rambutan","Merah",25)

print(keranjang1.__dict__)

    
        
   
