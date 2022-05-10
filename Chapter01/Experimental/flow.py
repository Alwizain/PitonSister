
# In this program, we check if the number is positive or negative or zero and 
# display an appropriate message
#%%IF

harga = int(input('masukan harga: ')) # variable harga yang dapat diinputkan dengan tipe datanya integer
if harga > 10000: # jika harga nya lebih besar dari 10000 maka
    print("Mahal") # print ini
elif harga == 10000: # jika harga nya sama dengan 10000 maka
    print("Murah") # print ini
else: # jika tidak ada yang memenuhi 2 keadaan di atas
    print("Hutang") # maka print ini

#%% FOR

total_makanan = [10000,15000,20000] #list yang berisi items harga-harga
pajak = 5000 #variable untuk menampung nilai pajak
for total in total_makanan: #foor loop dengan nama total untuk variable total_makanan
	pajak = pajak+total # menambahkan value dari variable pajak dengan jumlah dari seluruh item yang ada pada list total_Makanan


print("Total semua menjadi:", total) #kemudian print string nya , dan print value variable total

#%%
#WHILE
# Program to add natural numbers upto sum = 1+2+3+...+n

n = 10 #variable untuk menampung value n

sum = 0
i = 1 # ini start awal
while i <= n: # i akan dijumlah berapa kali sesuai jumlah value n
    sum = sum + i # value sum akan ditambahkan dengan i
    i = i+2    # value i akan ditambahkan 2(selisish)
               # akan terus di ulang sampai i nya memenuhi jumlah n

# print 
print("The sum is", sum)


# %% Contoh WHILE

# variable untuk menyimpan value num
num = 1

while num == 1: # karena num sama dengan 1 maka akan terus menjalankan print
    print('Ini adalah infinite Loop')

# %%
nama = ''

while not nama:
    nama = input('Masukan nama: ')

print('Hello '+nama) 