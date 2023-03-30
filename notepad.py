import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os
import AppOpener
import pyttsx3

main_application = tk.Tk()
main_application.geometry("800x600")
main_application.title("Untitled - Simulation Notepad")


main_menu = tk.Menu()

# File Menu Icon
new_icon = tk.PhotoImage(file = "icon/new.png")
open_icon = tk.PhotoImage(file = "icon/open.png")
save_icon = tk.PhotoImage(file = "icon/save.png")
save_as_icon = tk.PhotoImage(file = "icon/save_as.png")
exit_icon = tk.PhotoImage(file = "icon/exit.png")

file = tk.Menu(main_menu, tearoff = False)

# Edit Menu Icon
undo_icon = tk.PhotoImage(file= "icon/undo.png")
redo_icon = tk.PhotoImage(file= "icon/redo.png")
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

# Pronounce Menu Icon
prono = tk.PhotoImage(file="icon/pronounce.png")
prono_all = tk.PhotoImage(file="icon/pronounce_all.png")

pronounce = tk.Menu(main_menu, tearoff = False)

# Theme Color
light_theme = tk.PhotoImage(file="icon/light_default.png")
light_plus_theme = tk.PhotoImage(file="icon/light_plus.png")
dark_theme = tk.PhotoImage(file="icon/dark.png")
red_theme = tk.PhotoImage(file="icon/red.png")
monokai_theme = tk.PhotoImage(file="icon/monokai.png")
night_theme = tk.PhotoImage(file="icon/night_blue.png")

color_theme = tk.Menu(main_menu, tearoff=False)
theme_choose = tk.StringVar()

# System App Icon
calculator_icon = tk.PhotoImage(file = "icon/calculator.png")
calendar_icon = tk.PhotoImage(file = "icon/calendar.png")
chrome_icon = tk.PhotoImage(file = "icon/chrome.png")
camera_icon = tk.PhotoImage(file = "icon/camera.png")
photos_icon = tk.PhotoImage(file = "icon/photos.png")

apps = tk.Menu(main_menu, tearoff = False)

# System Apps Function

def calculator_fun(event = None):  
    os.system("calc.exe")
apps.add_command(label="Calculator", image=calculator_icon, compound=tk.LEFT, command=calculator_fun)

def calendar_fun(event = None):  
    AppOpener.open("calendar")
    #os.system("calendar.exe")
apps.add_command(label="Calendar", image=calendar_icon, compound=tk.LEFT, command=calendar_fun)

def chrome_fun(event = None):  
    AppOpener.open("google chrome")
apps.add_command(label="Chrome", image=chrome_icon, compound=tk.LEFT, command=chrome_fun)

def camera_fun(event = None):  
    AppOpener.open("Camera")
apps.add_command(label="Camera", image=camera_icon, compound=tk.LEFT, command=camera_fun)

def photos_fun(event = None):  
    AppOpener.open("Photos")
apps.add_command(label="Photos", image=photos_icon, compound=tk.LEFT, command=photos_fun)

# Theme Menu 
color_icons = (light_theme, light_plus_theme, dark_theme, red_theme, monokai_theme, night_theme)
color_dict = {
    'Light Default' : ('#000000',"#ffffff"),
    'Light Plus' : ('#474747',"#e0e0e0"),
    'Dark' : ('#c4c4c4',"#2d2d2d"),
    'Red' : ('#2d2d2d',"#ffe8e8"),
    'Monokai' : ('#d3b774',"#474747"), 
    'Night Blue' : ('#ededed',"#6b9dc2")
}

theme_choose.set('Light Default')

main_menu.add_cascade(label="File", menu=file)
main_menu.add_cascade(label="Edit", menu=edit)
main_menu.add_cascade(label="View", menu=view)
main_menu.add_cascade(label="Pronounce", menu=pronounce)
main_menu.add_cascade(label="Theme", menu=color_theme)
main_menu.add_cascade(label="Apps", menu=apps)


tool_bar_label = ttk.Label(main_application)
tool_bar_label.pack(side=tk.TOP,fill=tk.X)

# Font Style Box
font_tuple = font.families()
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
text_editor = tk.Text(main_application, undo=True)
text_editor.config(wrap="word", relief=tk.FLAT)


scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# Font Family and Function

font_now = "Arial"
font_size_now = 12

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
    if not text_editor.tag_ranges("sel"):
        return
    
    bold_font = font.Font(text_editor, text_editor.cget("font"))
    bold_font.configure(weight="bold")
    text_editor.tag_configure("bold", font=bold_font)

    current_tags = text_editor.tag_names("sel.first")
    if "bold" in current_tags:
        text_editor.tag_remove("bold", "sel.first", "sel.last")
    else:
        text_editor.tag_add("bold", "sel.first", "sel.last")
    

bold_btn.configure(command=bold_fun)

# Italic Function

def italic_fun():
    if not text_editor.tag_ranges("sel"):
        return
    
    italic_font = font.Font(text_editor, text_editor.cget("font"))
    italic_font.configure(slant="italic")
    text_editor.tag_configure("italic", font=italic_font)

    current_tags = text_editor.tag_names("sel.first")
    if "italic" in current_tags:
        text_editor.tag_remove("italic", "sel.first", "sel.last")
    else:
        text_editor.tag_add("italic", "sel.first", "sel.last")

italic_btn.configure(command=italic_fun)

# UnderLine Function

def under_line_fun():
    if not text_editor.tag_ranges("sel"):
        return
    
    underline_font = font.Font(text_editor, text_editor.cget("font"))
    underline_font.configure(underline=True)
    text_editor.tag_configure("underline", font=underline_font)

    current_tags = text_editor.tag_names("sel.first")
    if "underline" in current_tags:
        text_editor.tag_remove("underline", "sel.first", "sel.last")
    else:
        text_editor.tag_add("underline", "sel.first", "sel.last")

underline_btn.configure(command=under_line_fun)


# Color Choose
def color_choose():
    color = colorchooser.askcolor()
    if color:
        text_editor.tag_configure("color", foreground=color)

        current_tags = text_editor.tag_names("sel.first")
        if "color" in current_tags:
            text_editor.tag_remove("color", "sel.first", "sel.last")
        text_editor.tag_add("color", "sel.first", "sel.last")

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
        row, col = map(int, text_editor.index("end-1c").split("."))
        word = len(text_editor.get(1.0,"end-1c").split())
        character = len(text_editor.get(1.0,"end-1c").replace(" ",""))
        status_bars.config(text=f"Line: {row} | Character : {character} | Word : {word}")
    text_editor.edit_modified(False)

text_editor.bind("<<Modified>>", change_word)



# Color Theme Function

def change_theme():
    get_theme = theme_choose.get()
    colour_tuple = color_dict.get(get_theme)
    if colour_tuple is not None:
        fg_color = colour_tuple[0]
        bg_color = colour_tuple[1]
        text_editor.config(background=bg_color, fg=fg_color)
    else:
        pass
    

count = 0
for i in color_dict:
    color_theme.add_radiobutton(label=i, image=color_icons[count],compound=tk.LEFT, variable=theme_choose, value=i, command=change_theme)
    count+=1

# View Menu

# Tool Bar & Status Bar Hide
show_status_bar = tk.BooleanVar()
show_status_bar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar_label.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bars.pack_forget()
        tool_bar_label.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bars.pack(side=tk.BOTTOM)
        show_toolbar = True

def hide_statusbar():
    global show_status_bar
    if show_status_bar:
        status_bars.pack_forget()
        show_status_bar = False
    else:
        status_bars.pack(side=tk.BOTTOM)
        show_status_bar = True
    

view.add_checkbutton(label="Tool Bar", onvalue=True, offvalue=0, variable=show_toolbar, image=tool_bar, compound=tk.LEFT, command=hide_toolbar)
view.add_checkbutton(label="Status Bar", onvalue=True, offvalue=0, variable=show_status_bar, image=status_bar, compound=tk.LEFT, command=hide_statusbar)


# Pronounce Menu

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_selected_text(event = None):
    if text_editor.tag_ranges("sel"):
        selected_text = text_editor.selection_get()
        speak_text(selected_text)

def get_all_text():
    all_text = text_editor.get("1.0", "end-1c")
    speak_text(all_text)

pronounce.add_command(label="Read", image=prono, compound=tk.LEFT, accelerator="Ctrl+P", command=get_selected_text)
main_application.bind("<Control-p>", get_selected_text)
pronounce.add_command(label="Read All", image=prono_all, compound=tk.LEFT, accelerator="Ctrl+r", command=get_all_text)
main_application.bind("<Control-r>", lambda event: get_all_text())

# Edit Munu

def undo(event = None):
    try:
        text_editor.edit_undo()
    except:
        pass
edit.add_command(label="Undo", image=undo_icon, compound=tk.LEFT,accelerator="Ctrl+Z", command=undo)
main_application.bind("<Control-z>", undo)

def redo(event = None):
    try:
        text_editor.edit_redo()
    except:
        pass

edit.add_command(label="Redo", image=redo_icon, compound=tk.LEFT,accelerator="Ctrl+Shift+Z", command=redo)
main_application.bind("<Control-Shift-z>", redo)

edit.add_command(label="Copy", image=copy_icon, compound=tk.LEFT,accelerator="Ctrl+C", command= lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label="Paste", image=paste_icon, compound=tk.LEFT,accelerator="Ctrl+V", command= lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label="Cut", image=cut_icon, compound=tk.LEFT,accelerator="Ctrl+X", command= lambda:text_editor.event_generate("<Control x>"))

def clear_all():
    text_editor.delete(1.0, tk.END)

edit.add_command(label="Clear all", image=clear_icon, compound=tk.LEFT,accelerator="Ctrl+Alt+X", command= clear_all)
main_application.bind("<Control-Alt-x>", clear_all)

def find_fun(event = None):

    def find():
        word = find_input.get()
        text_editor.tag_remove("match","1.0",tk.END)
        matches = 0
        if word:
            start_pos = "1.0"
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f"{start_pos}+{len(word)}c"
                text_editor.tag_add("match",start_pos,end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground="red", background="blue")

    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0,tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)
        pass

    find_popup = tk.Toplevel()
    find_popup.geometry("450x200")
    find_popup.title("Find Word")
    find_popup.resizable(0,0)

    # Frame for Find
    find_fram = ttk.LabelFrame(find_popup,text="Find and Replace Word")
    find_fram.pack(pady=20)

    # Lable
    text_find = ttk.Label(find_fram,text="Find")
    text_replace = ttk.Label(find_fram,text="Replace")

    # Entry Box
    find_input = ttk.Entry(find_fram, width=30)
    replace_input = ttk.Entry(find_fram, width=30)

    # Button
    find_button = ttk.Button(find_fram, text="Find", command=find)
    replace_button = ttk.Button(find_fram, text="Replace", command=replace)

    # Text Lable Grid
    text_find.grid(row=0, column=0, padx=4, pady=4)
    text_replace.grid(row=1, column=0, padx=4, pady=4)

    # Entry Grid
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    # Button Grid
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)

edit.add_command(label="Find", image=find_icon, compound=tk.LEFT,accelerator="Ctrl+F", command=find_fun)
main_application.bind("<Control-f>", find_fun)

# File Menu

text_url = " "

def new_file(event = None):
    global text_url
    text_url = " "
    text_editor.delete(1.0,tk.END)
    main_application.title("Untitled - Simulation Notepad")


file.add_command(label="New", image=new_icon, compound=tk.LEFT,accelerator="Ctrl+N", command=new_file)
main_application.bind("<Control-n>", new_file)

def open_file(event = None):
    global text_url
    text_url = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select File",filetypes=(("Text File","*.txt"),("All Files", "*.*")))
    try:
        with open(text_url,"r") as for_read:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,for_read.read())
        main_application.title(os.path.abspath(text_url) + " - Simulation Notepad")
    except FileNotFoundError:
        return
    except:
        return
    

file.add_command(label="Open", image=open_icon, compound=tk.LEFT,accelerator="Ctrl+O", command=open_file)
main_application.bind("<Control-o>", open_file)

def save_file(event=None):
    global text_url
    try:
        if text_url != " ":
            content = str(text_editor.get(1.0,tk.END))
            with open(text_url,"w",encoding="utf-8") as for_read:
                for_read.write(content)     
            main_application.title(text_url.name + " - Simulation Notepad")
        else:
            text_url = filedialog.asksaveasfile(initialfile = 'Untitled.txt', mode="w",defaultextension="txt",filetypes=(("Text File","*.txt"),("All Files", "*.*")))
            content2 = str(text_editor.get(1.0,tk.END))
            text_url.write(content2)
            text_url.close()
            main_application.title(text_url.name + " - Simulation Notepad")
    except Exception as e:
        pass   
    
file.add_command(label="Save", image=save_icon, compound=tk.LEFT,accelerator="Ctrl+S", command=save_file)
main_application.bind("<Control-s>", save_file)

def save_as_file(event = None):
    global text_url
    try:
        content = text_editor.get(1.0,tk.END)
        text_url = filedialog.asksaveasfile(initialfile = 'Untitled.txt', mode="w",defaultextension="txt",filetypes=(("Text File","*.txt"),("All Files", "*.*")))
        text_url.write(content)
        text_url.close()
        main_application.title(text_url.name + " - Simulation Notepad")
    except:
        return

file.add_command(label="Save as", image=save_as_icon, compound=tk.LEFT,accelerator="Ctrl+Alt+S", command=save_as_file)
main_application.bind("<Control-Alt-s>", save_as_file)

def exit_fun(event = None):
    global text_url, text_change
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
main_application.bind("<Control-q>", exit_fun)

main_application.config(menu=main_menu)

main_application.mainloop()