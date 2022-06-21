# server .py

import socket
port=60000
s =socket.socket()
host=socket.gethostname()
s.bind((host,port))
s.listen(15)
print('Server sedang standby....')
while True :
    conn,addr=s.accept()
    print ('Mendapat sinyal dari ip ',addr)
    data=conn.recv(1024)
    print ('Server menerima pesan rahasia ',repr(data.decode()))
    filename='mytext.txt'
    f =open(filename,'rb')
    l =f.read(1024)
    while (l):
        conn.send(l)
        print ('Merespon pesan ',repr(l.decode()))
        l =f.read(1024)
        f.close()
        print ('Berhasil terkirim!')
        conn.send('Terimakasih atas pesannya'.encode())
        conn.close()
