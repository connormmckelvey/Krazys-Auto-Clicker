# importing time and threading
import time
import threading
from pynput.mouse import Button as bt, Controller
import customtkinter as ct
import clicker
import webbrowser
from PIL import Image


# pynput.keyboard is used to watch events of
# keyboard for start and stop of auto-clicker
from pynput.keyboard import Listener, KeyCode

#window creations
class App(ct.CTk):
    def __init__(self):
        super().__init__()


        self.settings = open('settings.txt').readlines()

        self.delay = float(self.settings[2])
        self.button = bt.left
        self.start_stop_key = KeyCode(char=self.settings[0])
        self.stop_key = KeyCode(char=self.settings[1])
        self.settings_img = ct.CTkImage(Image.open(r"C:\Users\conno\Desktop\CSI Files\__Python Programs\Personal\auto_clicker\settings-white-icon.png"))

        self.iconbitmap(r"C:\Users\conno\Desktop\CSI Files\__Python Programs\Personal\auto_clicker\clickericon.ico")



        self.geometry("400x300")
        self.title("Krazy's Auto Clicker")
        
        self.title_lbl = ct.CTkLabel(master=self,text='Krazy\'s Auto Clicker',text_color='green',font=('Power Green Small',30))
        self.subtitle_lbl = ct.CTkLabel(self,text_color='white',text='Made by Krazy099',font=('Power Green Small',15))

        self.entry_lbl = ct.CTkLabel(self, text_color= 'white',text='Start and Pause Key:')
        self.entry_ent = ct.CTkEntry(self,text_color='white',placeholder_text=self.settings[0])
        
        self.quit_lbl = ct.CTkLabel(self, text_color= 'white',text='Quit Hotkey:')
        self.quit_ent = ct.CTkEntry(self,text_color='white',placeholder_text=self.settings[1])
        
        self.delay_lbl = ct.CTkLabel(self, text_color= 'white',text='Delay (defaults to 0.001):')
        self.delay_ent = ct.CTkEntry(self,text_color='white',placeholder_text='0.001')

        self.run_btn = ct.CTkButton(self,text='Run Clicker',command=self.run,font=('Power Green Small',15),text_color='black',fg_color='green',anchor='center',width=120,height=32,border_width=0,corner_radius=8)

        self.support_btn = ct.CTkButton(self,image=self.settings_img,command=self.support,fg_color='grey',text='',width=20).place(x=350,y=260)

        self.display()
	
    def display(self):
        self.title_lbl.pack()
        self.subtitle_lbl.pack()
        self.entry_lbl.pack()
        self.entry_ent.pack()
        self.quit_lbl.pack()
        self.quit_ent.pack()
        self.delay_lbl.pack()
        self.delay_ent.pack()
        self.run_btn.pack(pady=10)
    def save(self):

        if self.entry_ent.get() != '':
            self.start_stop_key = KeyCode(char=self.entry_ent.get())
        if self.quit_ent.get() != '':
            self.stop_key = KeyCode(char=self.quit_ent.get())
        if self.delay_ent.get() != '':
            self.delay = float(self.delay_ent.get())
        
        with open('settings.txt','w') as tfile:
            tfile.write(self.entry_ent.get()+'\n')
            tfile.write(self.quit_ent.get()+'\n')
            tfile.write(str(self.delay))
                
    def support(self):
        webbrowser.open("https://github.com/Connor-McKelvey/AutoClicker")

    def run(self):
        self.save()
        self.destroy()
        clicker.main(d=self.delay,but=bt.left,sskey=self.start_stop_key,skey=self.stop_key)

if __name__ == "__main__":
	app = App()
	app.mainloop()