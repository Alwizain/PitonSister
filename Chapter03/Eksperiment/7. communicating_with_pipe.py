import multiprocessing
  
def adm(conn, events):
    for event in events:
        conn.send(event)
        print(f"Admin check informasi: {event}")
  
def user(conn):
    while True:
        event = conn.recv()
        if event == "refuse": 
            print("Daftar ditolak")    
            return
        print(f"username : {event} disetujui menjadi Owner")
  


if __name__ == "__main__":
    events = ["Faisal", "Dzul", "Ahmad", "Burhan", "refuse"]
    conn1, conn2 = multiprocessing.Pipe()
    process_1 = multiprocessing.Process(target=adm, args=(conn1, events))
    process_2 = multiprocessing.Process(target=user, args=(conn2,))
    process_1.start()
    process_2.start()
    process_1.join()
    process_2.join()