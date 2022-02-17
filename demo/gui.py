
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog
from tkinter.ttk import Scrollbar

from breast_cancer_prediction import get_predictions

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")




def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_file():
    path = filedialog.askopenfilename(initialdir="C:\\Users", title="Open", filetypes=[("Csv", '*.csv')])
    return path

def event_handler():
    path = open_file()
    predictions = get_predictions(path)
    entry_1.configure(state='normal')
    entry_1.delete('1.0', "end")
    entry_1.insert('1.0', predictions)
    entry_1.configure(state='disabled')


window = Tk()

window.geometry("865x866")
window.configure(bg = "#FBF8F1")
window.title("BC Analysis")
window.iconbitmap(bitmap="ribbon.ico")
# Add a Scrollbar(horizontal)
v=Scrollbar(window, orient='vertical')
v.pack(side="right", fill='y')




canvas = Canvas(
    window,
    bg = "#FBF8F1",
    height = 866,
    width = 865,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    432.0,
    93.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    432.5,
    530.0,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#FFFFFF",
    state='disabled',
    highlightthickness=0,
    yscrollcommand=v.set
)
entry_1.place(
    x=162.0,
    y=291.0,
    width=541.0,
    height=476.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    text='Carica file .csv',
    compound="center",
    borderwidth=0,
    highlightthickness=0,
    command=event_handler,
    relief="flat"
)
button_1.place(
    x=311.0,
    y=197.0,
    width=242.0,
    height=48.0
)



window.resizable(False, False)
window.mainloop()
