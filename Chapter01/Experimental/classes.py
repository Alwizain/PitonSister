# class menuutama:
#     makanan = {"nasgor","mie","cek","capcay","soto","padang","rawon"}
#     def _init_ (self):
#         self.menu_favorit = {"nasgor"}
#     def favorit (self, arg1, arg2):
#         return self.menu_favorit

# menu = menuutama()
# print("menu.favorit(Senin, Selasa)" , menu.favorit(1, 2))

# menu2 = menuutama()
# print("menu.makanan ",menu.makanan)
# print("menu2.makanan ",menu2.makanan)

# menuutama.makanan = {"capcay","padang"}
# print("menu.makanan ", menu.makanan)
# print("menu2.makanan ", menu2.makanan)

# menu.makanan = {"soto"}
# print("menu.makanan ", menu.makanan)
# print("menu2.makanan " , menu2.makanan)

# menuutama.makanan = {"rawon"}
# print("menu.makanan ", menu.makanan)
# print("menu2.makanan " , menu2.makanan)

class Menu:
    hari = "Senin"
    def __init__(self):
        self.makanan = "Batagor"
    def minuman(self, makan):
        makanan = "Pada hari ini menu favoritnya adalah " + str(self.makanan) + " dan minuman yang disarankan adalah" 
        return makanan + ' ' + makan

# Mencoba memanggil function minuman
list = Menu()
print("Menu favorit hari" , list.hari)
print("list.minuman",list.minuman("Cincau"))

listKedua = Menu()
print("listKedua.minuman",listKedua.minuman("Lemon Tea"))
# Memanggil hari
print("listKedua.hari" , listKedua.hari)

listKedua.hari = "Selasa"
# Memanggil hari yang sudah dimasukkan nilai baru
print("listKedua.hari" , listKedua.hari)

print("\n ---Class Turunan--- \n")

# Membuat Class baru turunan dari Class Menu
class MenuLainnya (Menu):
    def __init__(self, kedua):
        self.makanan = "Soto"
        print(kedua)
    def ice(self, teman):
        return teman

perocbaanKetiga = MenuLainnya("Hari Kedua")

# Memanggil function dari class utama
perocbaanKetiga.hari = "Selasa"
print("Menu favorit hari" , perocbaanKetiga.hari)
print(perocbaanKetiga.minuman("Jeruk"))

# Menjalankan function milik Class turunan
print("Pada hari ini juga terdapat rekomendasi menu berupa ice dengan varian rasa" , perocbaanKetiga.ice("Cappucino"))