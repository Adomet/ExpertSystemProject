import contextlib
import sys

from pyke import knowledge_engine
#from pyke import krb_traceback

engine = knowledge_engine.engine(__file__)





def chatbot_response(text):
    res =""

    engine.reset()      # Allows us to run tests multiple times.
    engine.add_universal_fact('facts','electric',[True])
    engine.activate('rules')
    print("suggesting...")
    try:
        with engine.prove_goal('rules.what_to_buy($car)') as gen: 
            for vars, plan in gen:
                res = ("You should buy: %s" % (vars['car']))
                print(res)

    except Exception:
        print("Exception")
        # krb_traceback.print_exc()
        # This converts stack frames of generated python functions back to the .krb file.

    return res

#Creating GUI with tkinter
import tkinter
from tkinter import *
def send():
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)
    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
        res = chatbot_response(msg)
        ChatLog.insert(END, "Car_Finder: " + res + '\n\n')
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
base = Tk()
base.title("Car_Finder")
base.geometry("400x500")
base.resizable(width=FALSE, height=FALSE)
#Create Chat window
ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial",)
ChatLog.config(state=DISABLED)
#Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set
#Create Button to send message
SendButton = Button(base, font=("Verdana",11,'bold'), text="Send", width="12", height=5,
                    bd=0, bg="#ff2800", activebackground="#ff2800",fg='#ffffff',
                    command= send )
#Create the box to enter message
EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font="Arial")
#EntryBox.bind("<Return>", send)
#Place all components on the screen
scrollbar.place(x=376,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=370)
EntryBox.place(x=150, y=401, height=90, width=240)
SendButton.place(x=6, y=401, height=90)
base.mainloop()