from pynput import keyboard
from pynput.keyboard import Key
import socket
from queue import Queue
import threading
import time
import os

data_queue = Queue()
lock = threading.Lock()

def on_press(key):  
    if isinstance(key ,Key):
        if key == keyboard.Key.esc:
            # Stop listener and exit
            data_queue.put(None)
            keyboard.Listener.stop			
            os._exit(0)             
    
        elif Key.space == key:
            data_queue.put(" ")
            print(" ",end="",flush=True)
        elif Key.enter == key:
            data_queue.put("\n")
            print("\n",end="",flush=True)
    else:
        print(key.char,end="",flush=True)
        data_queue.put(key.char)

def handle_client(conn, address,data_queue):
    while True:  
        with lock:       
            var = data_queue.get()
            if var is None:
                print("\nconnection shut down")
                conn.shutdown(socket.SHUT_RDWR)
                conn.close()
                break
            try:
                conn.sendall(var.encode('utf-8'))
                time.sleep(0.2)
            except:
                print("\nconnection shut down")
                conn.shutdown(socket.SHUT_RDWR)
                conn.close()
                break
    

def makeConnection():
    print("Server is running")
    host = socket.gethostname()
    print(host)
    port = 9980
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))
    s.listen(1)    
    scount = 0
    while True:
        try:
            if scount <1:
                #s.settimeout(500)                
                print("waiting for a connection...")
            (conn, addr) = s.accept()            
            print("Connection from: "+str(addr)) 
            scount+=1
            s.settimeout(None)
            print("Please write your message for client(press ESC to exit):")       
            t = threading.Thread(target=handle_client, args=(conn, addr,data_queue))
            t.daemon = True
            t.start()  
            t.join()
            scount-=1
        except:
            print("Connection timed out")
            os._exit(0)

def main():
    try:
        with keyboard.Listener(
                on_press=on_press) as listener:
                makeConnection() 
                listener.join() 
                           
                            
                    
    except KeyboardInterrupt:
        print("Keyboard interrupt")

if __name__ == '__main__':
    main()