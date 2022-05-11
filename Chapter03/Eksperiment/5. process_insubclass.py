import multiprocessing

class Rekomendasi(multiprocessing.Process):
    def run(self): 
        print ('memberi alamat kost dengan nomor: %s' %self.name)
        # for j in range (0,i):
        #     print('serta ruangan berjumlah berjumlah :%s' %j)
        return

if __name__ == '__main__': 
    for i in range(6):
        process = Rekomendasi()
        # process = multiprocessing.Process(target=run, args=(i,))
        process.start()
        process.join()