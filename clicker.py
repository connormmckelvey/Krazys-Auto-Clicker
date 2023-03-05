# importing time and threading
import time
import threading
from pynput.mouse import Button as bt, Controller
from pynput.keyboard import Listener, KeyCode


# threading.Thread is used
# to control clicks
def main(d,but,sskey,skey):
    class ClickMouse(threading.Thread):
        
    # d and but is passed in class
    # to check execution of auto-clicker
        def __init__(self, d, but):
            super(ClickMouse, self).__init__()
            self.d = d
            self.but = but
            self.running = False
            self.program_running = True

        def start_clicking(self):
            self.running = True

        def stop_clicking(self):
            self.running = False

        def exit(self):
            self.stop_clicking()
            self.program_running = False

        # method to check and run loop until
        # it is true another loop will check
        # if it is set to true or not,
        # for mouse click it set to but
        # and d.
        def run(self):
            while self.program_running:
                while self.running:
                    mouse.click(self.but)
                    time.sleep(self.d)
                time.sleep(0.1)


    # instance of mouse controller is created
    mouse = Controller()
    click_thread = ClickMouse(d, but)
    click_thread.start()


    # on_press method takes
    # key as argument
    def on_press(key):
        
    # sskey will stop clicking
    # if running flag is set to true
        if key == sskey:
            if click_thread.running:
                click_thread.stop_clicking()
            else:
                click_thread.start_clicking()
                
        # here exit method is called and when
        # key is pressed it terminates auto clicker
        elif key == skey:
            click_thread.exit()
            listener.stop()


    with Listener(on_press=on_press) as listener:
        listener.join()