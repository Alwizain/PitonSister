# meriksa berapa banyak yang tambahan yang diambil banyak, cukup, atau berkurang
# menampilkan pesan yang sesuai dengan kondisinya
#%%

tambahan_makanan = int(input('berapa yang kamu ambil :'))  # ini variable

if tambahan_makanan >= 5:  # jika tambahan_makanan lebih besar dari 5 maka 
    print("Terlalu banyak") # print ini
elif tambahan_makanan > 0 < 5: #jika tambahan_makanan lebih besar dari 0 dan lebih kecil dari 5
    print("Cukup lah") #print ini
else: # apabila tidak memenuhi kedua kondisi tersebut maka
    print("Ko malah ngurangin sih") # print ini

#%%
# Program to find the sum of all numbers stored in a list
# List of numbers
numbers = [1,21,21,2,12,12,1,2,12,12,12,12,12,1,12,121,-10000000000000]  # list yang berisikan items angka angka



# variable untuk menyimpan nilai sum
sum = 0 #


# for loop untuk variable numbers
for val in numbers:
	sum = sum+val # sum = value dari sum ditambah dengan jumlah seluruh item pada list numbers

# Output
print("The sum is", sum) #print string, kemudian print output dari sum

if sum > 0: # jika output sum lebih besar dari 0 maka
    print("Positive number") # print ini
elif sum == 0: # jika output sum sama dengan 0 maka
    print("Zero") #print ini
else: # apabila tidak memenuhi kedua kondisi tersebut maka
    print("Negative number") #print ini