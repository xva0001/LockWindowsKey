import keyboard
import tkinter as tk
import threading


def lockwin(stop_threads):
    if stop_threads():
        keyboard.block_key("left windows")
    else:
        keyboard.unblock_key("left windows")


def changestat():
    global blnb, t1
    blnb = not blnb
    if blnb == True:
        #lock
        mBtn["text"] = "unlock win"
        t1 = threading.Thread(target=lockwin,args=(lambda: blnb,))
        t1.start()
    else:
        #unlock
        mBtn["text"] = "lock win"
        t1 = threading.Thread(target=lockwin,args=(lambda: blnb,))
        t1.start()


blnb = False
root = tk.Tk()
root.title("Lock windows key")
root.geometry("400x400")

mlabel  =  tk.Label(root,text="lock windows", font=("Arial",18))
mlabel.pack()

mBtn = tk.Button(root,text="lock win", command=changestat)
mBtn.pack()

root.mainloop()
