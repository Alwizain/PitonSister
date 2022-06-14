import asyncio
import time
import random

print("Penelitian vaksin covid")


def peneliti_A(end_time, loop):
    print ("Peneliti A")
    print ("Memulai Penelitian")
    time.sleep(random.randint(0, 5))
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, peneliti_B, end_time, loop)
        print("Penelitian gagal, lanjut ke peneliti selanjutnya")
    else:
        print("Penelitian berhasil! vaksin covid ditemukan")
        print(end_time)
        loop.stop()

def peneliti_B(end_time, loop):
    print ("Peneliti B ")
    print ("Memulai Penelitian")
    time.sleep(random.randint(0, 5))
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, peneliti_C, end_time, loop)
        print("Penelitian gagal, lanjut ke peneliti selanjutnya")
    else:
        print("Penelitian berhasil! vaksin covid ditemukan")
        print(end_time)
        loop.stop()

def peneliti_C(end_time, loop):
    print ("Peneliti C")
    print ("Memulai Penelitian")
    time.sleep(random.randint(0, 5))
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, peneliti_A, end_time, loop)
        print("Penelitian gagal, lanjut ke peneliti selanjutnya")
    else:
        print("Penelitian berhasil! vaksin covid ditemukan")
        print(end_time)
        loop.stop()


loop = asyncio.get_event_loop()
end_loop = loop.time() + 30
loop.call_soon(peneliti_A, end_loop, loop)
loop.run_forever()
loop.close()

