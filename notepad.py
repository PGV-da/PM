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
font_family = tk.StringVar
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