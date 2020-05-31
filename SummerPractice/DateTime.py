import threading

def numbers():
    i = 0
    print(threading.current_thread().getName())
    while i<25:

            print (i)
            i += 1


t = threading.Thread(target = numbers)
t.start()
