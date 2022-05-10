f = open ('kelompok.txt', 'w')
f.write ('Ahmad Fathoni R 1194002 \n') #menginputkan tulisan kedalam file dan /n adalah perintah untuk tab tulisannya
f.write ('Alwizain Almas T 1194004 \n') #menginputkan tulisan kedalam file dan /n adalah perintah untuk tab tulisannya
f.write ('Faisal Abdullah 1194014 \n') #menginputkan tulisan kedalam file dan /n adalah perintah untuk tab tulisannya

f.close()
f = open ('kelompok.txt')
content = f.read()
print (content)

f.close()