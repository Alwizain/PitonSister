import socket
s =socket.socket()
host=socket.gethostname()
port=60000
s.connect((host,port))
s.send('Pesan Rahasia'.encode())
with open('received.txt','wb') as f:
    print ('file opened')
    while True :
        print ('Menerima data...')
        data=s.recv(1024)
        if not data:
            break
        print ('Respon Server =>',data.decode())
         # write data to a file
        f.write(data)
f.close()
print ('Berhasil menerima paket pesan rahasia')
s.close()
print ('Komunikasi diakhiri')
