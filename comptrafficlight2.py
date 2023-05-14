import tkinter as tk
import tkinter.ttk as ttk
from comptrafficlight import CompTrafficLight


class CompTrafficLightapp:

    def __init__(self):
        root=tk.Tk()
        root.title("Traffic Light")
        frame=ttk.frame(root)
        frame.pack()
        buttom=ttk.buttom(frame,text='Change', command=self.do_buttom_press)
        self.light=CompTrafficLight(frame,100,padding=25)
        buttom.grid(roe=0,column=0)
        self.light.frame.grid(row=0,column=1)
        root.mainloop()

        def do_button_press(self):
            self.light.change()
            
            CompTrafficLightapp()