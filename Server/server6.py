from pynput import keyboard
from pynput.keyboard import Key

def on_press(key):  
    if isinstance(key ,Key):
        if key == keyboard.Key.esc:
            # Stop listener and exit           
            keyboard.Listener.stop			
            return False           
    
        elif Key.space == key:
            
            print(" ",end="",flush=True)
        elif Key.enter == key:
           
            print("\n",end="",flush=True)
    else:
        print(key.char,end="",flush=True)
        
print("hi")
with keyboard.Listener(on_press=on_press) as listener:
    listener.join() 