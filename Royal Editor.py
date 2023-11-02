from tkinter import *
import tkinter.filedialog as fd
import tkinter.messagebox as mb

from PIL import Image, ImageTk
import os
import ctypes


def rev_up():
    global file
    file = fd.askopenfilename(defaultextension='.txt', filetypes=[('All Files', '*.*'), ("Text File", "*.txt*")])

    if file != '':
        root.title(f"{os.path.basename(file)}")
        text_area.delete(1.0, END)
        with open(file, "r") as file_:
            text_area.insert(1.0, file_.read())
            file_.close()
    else:
        file = None


def kickstart():
    file = None
    root.title("No Name - Royal Editor")
    text_area.delete(1.0, END)
    text_area.insert(END, "Welcome to the Royal Editor! \U0001F6E3")


def save_ride():
    global file
    if file:
        with open(file, "w") as f:
            f.write(text_area.get(1.0, END))
            root.title(f"{os.path.basename(file)} - Royal Editor")
    else:
        file = fd.asksaveasfilename(initialfile='No Name.txt', defaultextension='.txt',
                                    filetypes=[("Text File", "*.txt*"), ("Word Document", '*,docx*'), ("PDF", "*.pdf*")])
        
        if file:
            with open(file, "w") as f:
                f.write(text_area.get(1.0, END))
                root.title(f"{os.path.basename(file)} - Royal Editor")


def end_ride():
    root.title("No Name - Royal Editor")
    text_area.delete(1.0, END)
    file = None


def exit_application():
    if mb.askokcancel("Exit", "Exit Royal Editor?"):
        root.destroy()


def copy_bullet():
    active_window = ctypes.windll.user32.GetForegroundWindow()
    ctypes.windll.user32.SendMessageW(active_window, 0x0100, 0x43, 0)


def cut_bullet():
    active_window = ctypes.windll.user32.GetForegroundWindow()
    ctypes.windll.user32.SendMessageW(active_window, 0x0100, 0x58, 0)


def paste_bullets():
    active_window = ctypes.windll.user32.GetForegroundWindow()
    ctypes.windll.user32.SendMessageW(active_window, 0x0100, 0x56, 0)


def select_all_bullets():
  active_window = ctypes.windll.user32.GetForegroundWindow()
  ctypes.windll.user32.SendMessageW(active_window, 0x0100, 0x1F, 0)


def backspace():
  active_window = ctypes.windll.user32.GetForegroundWindow()
  ctypes.windll.user32.SendMessageW(active_window, 0x0100, 0x08, 0)


def about_notepad():
    about_dialog = Toplevel(root)
    about_dialog.title("About Royal Editor")
    about_dialog_label = Label(about_dialog, text="Royal Text Editor is a text editor inspired \n by the Royal Enfield Bullet motorcycle. \nIt is designed to be a tribute to the history of \nRoyal Enfield, an Indian brand that has become the \nlargest manufacturer of motorcycles, beating Harley-Davidson.")
    about_dialog_label.pack()
    about_dialog.mainloop()


def about_commands():
    commands = """
Under the File Menu:
- ‘Kickstart’ starts a new project from scratch
- ‘Rev Up’ opens a new window to work on another project
- ‘Save Ride’ saves your current project
- ‘Save Ride As’ saves your project in another format

Under the Edit Menu:
- ‘Copy Bullet’ copies the selected text to your clipboard
- ‘Cut Bullet’ cuts the selected text and removes it from the text area
- ‘Paste Bullet’ pastes the copied/cut text
- ‘Select All Bullets’ selects all bullet points in the text area
- ‘Delete Bullet’ deletes the last bullet point 
"""

    mb.showinfo(title="All commands", message=commands)


root = Tk()
root.title("No Name - Royal Editor \U0001F6E3 ")
root.geometry('800x500')
root.resizable(0, 0)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)



icon = ImageTk.PhotoImage(Image.open('icon.png'))
root.iconphoto(True, icon)
file = ''

menu_bar = Menu(root)

text_area = Text(root, font=("Courier Prime", 16), bg="white", fg="black", wrap=WORD)
text_area.grid(sticky=NSEW)

scroller = Scrollbar(text_area, orient=VERTICAL)
scroller.pack(side=RIGHT, fill=Y)

scroller.config(command=text_area.yview)
text_area.config(yscrollcommand=scroller.set)

RE_menu = Menu(menu_bar, tearoff=False, activebackground='#204070')

RE_menu.add_command(label="Kickstart", command=kickstart)
RE_menu.add_command(label="Rev Up", command=rev_up)
RE_menu.add_command(label="Save Ride", command=save_ride)
RE_menu.add_separator()
RE_menu.add_command(label="End Ride", command=end_ride)
RE_menu.add_command(label="Exit", command=exit_application)


menu_bar.add_cascade(label="Royal Enfield Menu", menu=RE_menu)

edit_menu = Menu(menu_bar, tearoff=False, activebackground='#204070' )

edit_menu.add_command(label='Copy Bullet', command=copy_bullet)
edit_menu.add_command(label='Cut Bullet', command=cut_bullet)
edit_menu.add_command(label='Paste Bullet', command=paste_bullets)
edit_menu.add_separator()
edit_menu.add_command(label='Select All Bullets', command=select_all_bullets)
edit_menu.add_command(label='Delete Bullet', command=backspace)

menu_bar.add_cascade(label="Bullet Menu", menu=edit_menu)
# The Edit Menu works only in Windows devices as of now.
"""
The Edit Menu in Royal Editor currently only works in Windows devices. This includes the following commands:
* Copy Bullet
* Cut Bullet
* Paste Bullet
* Select All Bullets
* Delete Bullet
We are working on adding support for the Edit Menu in other operating systems.
"""


about_menu = Menu(menu_bar, tearoff=False, activebackground='#204070')

about_menu.add_command(label='About Royal Editor', command=about_notepad)
about_menu.add_command(label='About RE Commands', command=about_commands)

menu_bar.add_cascade(label="About", menu=about_menu)

root.config(menu=menu_bar)

Label(root, text=f"Built Like a Gun",font=("Kingthings Peony", 12)).place(relx= 1, rely = 1, anchor=SE)

root.update()

image = ImageTk.PhotoImage(Image.open("splash.png"))
splash_screen = Toplevel(root)
splash_screen.overrideredirect(True)
splash_screen.title("Royal Editor Splash Screen")
splash_screen.geometry('256x256')
splash_screen_image = Label(splash_screen, image=image)
splash_screen_image.pack()
splash_screen.after(1000, splash_screen.destroy)
root.mainloop()

"""

Key to Menu Bar
~~~~~~~~~~~~~~~

Royal Enfield Menu --> File menu
Rev Up = Open file
Kickstart = Open New file
Save Ride = Save file
Exit = Exit

Bullet menu --> Edit menu
Copy Bullet = Copy Text
Cut Bullet = Cut Text
Paste Bullets = Paste Text
Select All Bullets = Select All
Delete Bullet = Delete Last Character

"""

print("───────╔╗──╔╦═══╗──────╔╗─────╔╗")
print("───────║╚╗╔╝║╔═╗║─────╔╝╚╗───╔╝╚╗")
print("╔══╦═╗─╚╗║║╔╣╚═╝║╔╦═╗╔╬╗╔╬╦══╬╗╔╬╦╗╔╦══╗")
print("║╔╗║╔╗╗─║╚╝║║╔╗╔╝╠╣╔╗╬╣║║╠╣╔╗║║║╠╣╚╝║║═╣")
print("║╔╗║║║║─╚╗╔╝║║║╚╗║║║║║║║╚╣║╔╗║║╚╣╠╗╔╣║═╣")
print("╚╝╚╩╝╚╝──╚╝─╚╝╚═╝╚╩╝╚╩╝╚═╩╩╝╚╝╚═╩╝╚╝╚══╝")
