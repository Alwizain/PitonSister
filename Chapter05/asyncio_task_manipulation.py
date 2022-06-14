"""Asyncio using Asyncio.Task to execute three math functions in parallel"""

import asyncio

# kemungkinan susunan duduk 7 orang pada ruang rapat - factorial
@asyncio.coroutine
def anggota(number):
    fact = 1
    for i in range(2, number + 1):
        print('Asyncio.Task: Total anggota rapat yang sudah memasuki ruangan adalah %s' % i)
        yield from asyncio.sleep(1)
        fact *= i
    print('\n -------------HASIL--------------- \n')
    print('Asyncio.Task - Kemungkinan susunan duduk dari %s anggota = %s kemungkinan' % (number, fact))


# Menentukan suku ke-7 dari bilangan 1,1,2,3,5,8,... - fibonacci
@asyncio.coroutine
def sukuN(number):
    a, b = 1, 1
    for i in range(number):
        print('Asyncio.Task: Membaca suku ke-%s' % i)
        yield from asyncio.sleep(1)
        a, b = b, a + b
    print('Asyncio.Task - Hasil suku ke-%s adalah bilangan %s' % (number, a))


# Menentukan jumlah cara 6 dari 20 orang terpilih sebagai staff IT - binomial coefficient (kombinasi)
@asyncio.coroutine
def staffIT(n, k):
    result = 1
    for i in range(1, k + 1):
        result = result*(n - i + 1)/i
        print('Asyncio.Task: Memilih orang ke-%s' % i)
        yield from asyncio.sleep(1)
    print('Asyncio.Task - Jadi jumlah cara dalam memilih dari %s orang menjadi %s orang terpilih adalah %s' % (n, k, result))


if __name__ == '__main__':
    task_list = [asyncio.Task(anggota(7)),
                 asyncio.Task(sukuN(6)),
                 asyncio.Task(staffIT(20, 6))]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(task_list))
    loop.close()
