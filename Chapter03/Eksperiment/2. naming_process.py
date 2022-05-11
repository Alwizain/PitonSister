# memberi nama sebuah process
import multiprocessing
import time

def pemilik():
    name = multiprocessing.current_process().name
    print ("pemilik mulai melakukan = %s \n" %name)
    time.sleep(3)
    print ("pemilik selesai melakukan = %s \n" %name)

if __name__ == '__main__':
    proses_dengan_nama = multiprocessing.Process\
                        (name='Penambahan bangunan pada aplikasi',\
                         target=pemilik)

    #proses_dengan_nama.daemon = True

    proses_dengan_nama_default = multiprocessing.Process\
                                (target=pemilik)

    proses_dengan_nama.start()
    proses_dengan_nama_default.start()

    proses_dengan_nama.join()
    proses_dengan_nama_default.join()