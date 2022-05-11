import multiprocessing
import time

def Cbf():
    name = multiprocessing.current_process().name
    print ("Starting %s \n" %name)
    if name == 'calCulateRekomendation':  
        for i in range(0,5):
            print('---> %d \n' %i)
        time.sleep(1)
    else:
        for i in range(5,10):
            print('---> %d \n' %i)
        time.sleep(1)
    print ("Exiting %s \n" %name)
    

if __name__ == '__main__':
    
    calCulateRekomendation = multiprocessing.Process\
                         (name='calCulateRekomendation',\
                          target=Cbf)
    calCulateRekomendation.daemon = False

    MenampilkanRekomendasi = multiprocessing.Process\
                            (name='MenampilkanRekomendasi',\
                             target=Cbf)
    
    MenampilkanRekomendasi.daemon = True
    
    calCulateRekomendation.start()
    MenampilkanRekomendasi.start()
    

