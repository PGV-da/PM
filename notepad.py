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
file.add_command(label="New", image=new_icon, compound=tk.LEFT,accelerator="Ctrl+N")
file.add_command(label="Open", image=open_icon, compound=tk.LEFT,accelerator="Ctrl+O")
file.add_command(label="Save", image=save_icon, compound=tk.LEFT,accelerator="Ctrl+S")
file.add_command(label="Save as", image=save_as_icon, compound=tk.LEFT,accelerator="Ctrl+Alt+S")
file.add_command(label="Exit", image=exit_icon, compound=tk.LEFT,accelerator="Ctrl+Q")

main_application.config(menu=main_menu)

main_application.mainloop()