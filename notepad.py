import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os

main_application = tk.Tk()
main_application.geometry("800x600")
main_application.title("PM Notepad")


main_menu = tk.Menu()

# File Menu Icon
new_icon = tk.PhotoImage(file = "icon/new.png")
open_icon = tk.PhotoImage(file = "icon/open.png")
save_icon = tk.PhotoImage(file = "icon/save.png")
save_as_icon = tk.PhotoImage(file = "icon/save_as.png")
exit_icon = tk.PhotoImage(file = "icon/exit.png")

file = tk.Menu(main_menu, tearoff = False)

# Edit Menu Icon
copy_icon = tk.PhotoImage(file= "icon/copy.png")
paste_icon = tk.PhotoImage(file= "icon/paste.png")
cut_icon = tk.PhotoImage(file= "icon/cut.png")
clear_icon = tk.PhotoImage(file= "icon/clear.png")
find_icon = tk.PhotoImage(file= "icon/find.png")

edit = tk.Menu(main_menu, tearoff = False)

# View Menu Icon
tool_bar = tk.PhotoImage(file="icon/tool_bar.png")
status_bar = tk.PhotoImage(file="icon/status_bar.png")

view = tk.Menu(main_menu, tearoff = False)

# Theme Color
light_theme = tk.PhotoImage(file="icon/light_default.png")
light_plus_theme = tk.PhotoImage(file="icon/light_plus.png")
dark_theme = tk.PhotoImage(file="icon/dark.png")
red_theme = tk.PhotoImage(file="icon/red.png")
monokai_theme = tk.PhotoImage(file="icon/monokai.png")
night_theme = tk.PhotoImage(file="icon/night_blue.png")

color_theme = tk.Menu(main_menu, tearoff=False)

main_menu.add_cascade(label="File", menu=file)
main_menu.add_cascade(label="Edit", menu=edit)
main_menu.add_cascade(label="View", menu=view)
main_menu.add_cascade(label="Theme", menu=color_theme)


tool_bar_label = ttk.Label(main_application)
tool_bar_label.pack(side=tk.TOP,fill=tk.X)

# Font Style Box
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar_label,width=30,textvariable=font_family,state="readonly")
font_box["values"] = font_tuple
font_box.current(font_tuple.index("Arial"))
font_box.grid(row=0,column=0,padx=5)

# Font Size Box
size_variable = tk.IntVar()
font_size = ttk.Combobox(tool_bar_label,width=20,textvariable=size_variable,state="readonly")
font_size["values"] = tuple(range(8,100,2))
font_size.current(4)
font_size.grid(row=0,column=1,padx=5)

# Bold Button
bold_icon = tk.PhotoImage(file="icon/bold.png")
bold_btn = ttk.Button(tool_bar_label,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=5)

# Italic Button
italic_icon = tk.PhotoImage(file="icon/italic.png")
italic_btn = ttk.Button(tool_bar_label,image=italic_icon)
italic_btn.grid(row=0,column=3,padx=5)

# UnderLine Button
underline_icon = tk.PhotoImage(file="icon/underline.png")
underline_btn = ttk.Button(tool_bar_label,image=underline_icon)
underline_btn.grid(row=0,column=4,padx=5)

# Font Color Button
font_color_icon = tk.PhotoImage(file="icon/font_color.png")
font_color_btn = ttk.Button(tool_bar_label,image=font_color_icon)
font_color_btn.grid(row=0,column=5,padx=5)

# Align Left
align_left_icon = tk.PhotoImage(file="icon/align-left.png")
align_left_btn = ttk.Button(tool_bar_label,image=align_left_icon)
align_left_btn.grid(row=0,column=6,padx=5)

# Align Center
align_center_icon = tk.PhotoImage(file="icon/align-center.png")
align_center_btn = ttk.Button(tool_bar_label,image=align_center_icon)
align_center_btn.grid(row=0,column=7,padx=5)

# Align Left
align_right_icon = tk.PhotoImage(file="icon/align-right.png")
align_right_btn = ttk.Button(tool_bar_label,image=align_right_icon)
align_right_btn.grid(row=0,column=8,padx=5)

# Text Editor
text_editor = tk.Text(main_application)
text_editor.config(wrap="word", relief=tk.FLAT)


scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# Font Family and Function

font_now = "Arial"
font_size_now = 16

def change_font(main_application):
    global font_now
    font_now = font_family.get()
    text_editor.configure(font=(font_now,font_size_now))

def change_size(main_application):
    global font_size_now
    font_size_now = size_variable.get()
    text_editor.configure(font=(font_now,font_size_now))

font_box.bind("<<ComboboxSelected>>",change_font)
font_size.bind("<<ComboboxSelected>>",change_size)

# Bold Function

# print(tk.font.Font(font=text_editor["font"]).actual())

def bold_fun():
    text_get = tk.font.Font(font=text_editor["font"])
    if text_get.actual()["weight"] == 'normal':
        text_editor.configure(font=(font_now,font_size_now,"bold"))
    if text_get.actual()["weight"] == 'bold':
        text_editor.configure(font=(font_now,font_size_now,"normal"))

bold_btn.configure(command=bold_fun)

# Italic Function

def italic_fun():
    text_get = tk.font.Font(font=text_editor["font"])
    if text_get.actual()["slant"] == 'roman':
        text_editor.configure(font=(font_now,font_size_now,"italic"))
    if text_get.actual()["slant"] == 'italic':
        text_editor.configure(font=(font_now,font_size_now,"roman"))

italic_btn.configure(command=italic_fun)

# UnderLine Function

def under_line_fun():
    text_get = tk.font.Font(font=text_editor["font"])
    if text_get.actual()["underline"] == 0:
        text_editor.configure(font=(font_now,font_size_now,"underline"))
    if text_get.actual()["underline"] == 1:
        text_editor.configure(font=(font_now,font_size_now,"normal"))

underline_btn.configure(command=under_line_fun)


# Color Choose
def color_choose():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])

font_color_btn.configure(command=color_choose)

# Align Left
def align_left():
    text_get_all = text_editor.get(1.0,"end")
    text_editor.tag_config("left",justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_get_all,"left")

align_left_btn.configure(command=align_left)

# Align Center
def align_center():
    text_get_all = text_editor.get(1.0,"end")
    text_editor.tag_config("center",justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_get_all,"center")

align_center_btn.configure(command=align_center)

# Align Right
def align_right():
    text_get_all = text_editor.get(1.0,"end")
    text_editor.tag_config("right",justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_get_all,"right")

align_right_btn.configure(command=align_right)


# Status Bar (word & character) 
status_bars = ttk.Label(main_application,text = "Status Bar")
status_bars.pack(side=tk.BOTTOM)

text_change = False

def change_word(event = None):
    global text_change
    if text_editor.edit_modified():
        text_change = True
        word = len(text_editor.get(1.0,"end-1c").split())
        character = len(text_editor.get(1.0,"end-1c").replace(" ",""))
        status_bars.config(text=f"character : {character} word : {word}")
    text_editor.edit_modified(False)

text_editor.bind("<<Modified>>", change_word)

# Theme Menu 
color_icons = (light_theme, light_plus_theme, dark_theme, red_theme, monokai_theme, night_theme)
color_dict = {
    'Light Default' : ("#000000","#ffffff"),
    'Light Plus' : ("#474747","#e0e0e0"),
    'Dark' : ("#c4c4c4","#2d2d2d"),
    'Red' : ("#2d2d2d","#ffe8e8"),
    'Monokai' : ("#d3b774","#474747"), 
    'Night Blue' : ("#ededed","#6b9dc2")
}



count = 0
for i in color_dict:
    color_theme.add_radiobutton(label=i, image=color_icons[count],compound=tk.LEFT)
    count+=1

# View Menu
view.add_checkbutton(label="Tool Bar", onvalue=True, offvalue=0, image=tool_bar, compound=tk.LEFT)
view.add_checkbutton(label="Status Bar", onvalue=True, offvalue=0, image=status_bar, compound=tk.LEFT)


# Edit Munu
edit.add_command(label="Copy", image=copy_icon, compound=tk.LEFT,accelerator="Ctrl+C")
edit.add_command(label="Paste", image=paste_icon, compound=tk.LEFT,accelerator="Ctrl+V")
edit.add_command(label="Cut", image=cut_icon, compound=tk.LEFT,accelerator="Ctrl+X")
edit.add_command(label="Clear all", image=clear_icon, compound=tk.LEFT,accelerator="Ctrl+Alt+X")
edit.add_command(label="Find", image=find_icon, compound=tk.LEFT,accelerator="Ctrl+F")

# File Menu

text_url = " "

def new_file(event = None):
    global text_url
    text_url = " "
    text_editor.delete(1.0,tk.END)


file.add_command(label="New", image=new_icon, compound=tk.LEFT,accelerator="Ctrl+N", command=new_file)

def open_file(event = None):
    global text_url
    text_url = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select File",filetypes=(("Text File","*.txt"),("All Files", "*.*")))
    try:
        with open(text_url,"r") as for_read:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,for_read.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(text_url))

file.add_command(label="Open", image=open_icon, compound=tk.LEFT,accelerator="Ctrl+O", command=open_file)
 
def save_file(event=None):
    global text_url
    try:
        if text_url:
            content = str(text_editor.get(1.0,tk.END))
            with open(text_url,"w",encoding="utf-8") as for_read:
                for_read.write(content)
        else:
            text_url = filedialog.asksaveasfile(mode="w",defaultextension="txt",filetypes=(("Text File","*.txt"),("All Files", "*.*")))
            content2 = text_editor.get(1.0,tk.END)
            text_url.write(content2)
            text_url.close()
    except:
        return

file.add_command(label="Save", image=save_icon, compound=tk.LEFT,accelerator="Ctrl+S", command=save_file)

def save_as_file(event = None):
    global text_url
    try:
        content = text_editor.get(1.0,tk.END)
        text_url = filedialog.asksaveasfile(mode="w",defaultextension="txt",filetypes=(("Text File","*.txt"),("All Files", "*.*")))
        text_url.write(content)
        text_url.close()
    except:
        return

file.add_command(label="Save as", image=save_as_icon, compound=tk.LEFT,accelerator="Ctrl+Alt+S", command=save_as_file)

def exit_fun(event = None):
    global text_change
    try:
        if text_change:
            mbox = messagebox.askyesnocancel("Warning","Do you want to save this file")
            if mbox is True:
                if text_url:
                    content = text_editor.get(1.0,tk.END)
                    with open (text_url,"w",encoding="utf-8") as for_read:
                        for_read.write(content)
                        main_application.destroy()
                else:
                    content2 = text_editor.get(1.0,tk.END)
                    text_url = filedialog.asksaveasfile(mode = "w",defaultextension="txt",filetypes=(("Text File","*.txt"),("All Files", "*.*")))
                    text_url.write(content2)
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()

    except:
        return

file.add_command(label="Exit", image=exit_icon, compound=tk.LEFT,accelerator="Ctrl+Q", command=exit_fun)

main_application.config(menu=main_menu)

main_application.mainloop()