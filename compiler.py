import tkinter as tk
from tkinter.constants import FALSE
from tkinter.filedialog import asksaveasfilename, askopenfilename
from core import *

APPLICATION_NAME = "8085 Simulator"
FILE_EXTENTION = "8085"
current_file_path = None
load_loc = ""

def set_file_path(path):
   global current_file_path
   current_file_path = path
   root.title(f"{APPLICATION_NAME}: {current_file_path}")


def terminate():
    root.quit()


def compile(event=""):

    # try:
        load_location = get_load_location()
        if "h" in load_location:
            load_location = load_location.replace("h","")
        if not current_file_path:
            save_as()
        transpiled_list = transpile(editor.get("1.0",tk.END),load_loc)

        code_output.delete("1.0",tk.END)
        output_text = ""
        for codes in transpiled_list:
            output_text += f"{hex(int(load_location,base=16) + transpiled_list.index(codes))}-> {codes} \n"
        code_output.insert("1.0",output_text)
        code_output.config(foreground="black")
    # except Exception as e:
    #     code_output.insert("1.0",f"\n{e}")
    #     code_output.config(foreground="red")

def new(even=""):
    save_as()
    editor.insert("1.0","")

def save(event=""):
    if not current_file_path:
        path = asksaveasfilename(filetypes=[(f"{APPLICATION_NAME} Files",f"*.{FILE_EXTENTION}")])
    else:
        path = current_file_path
    
    if not path:
        return
    set_file_path(path)
    data = editor.get("1.0",tk.END)
    if not f".{FILE_EXTENTION}" in path:
        path = path +f".{FILE_EXTENTION}"
    with open (path,"w") as f:
        f.write(data)

def save_as(event=""):
    path = asksaveasfilename(filetypes=[(f"{APPLICATION_NAME} Files",f"*.{FILE_EXTENTION}")])
    if not path:
        return
    set_file_path(path)
    data = editor.get("1.0",tk.END)
    if not f".{FILE_EXTENTION}" in path:
        path = path +f".{FILE_EXTENTION}"
    with open (path,"w") as f:
        f.write(data)

def open_file(event=""):
    path = askopenfilename(filetypes=[(f"{APPLICATION_NAME} Files",f"*.{FILE_EXTENTION}")])
    if not path:
        return
    set_file_path(path)
    with open (path,"r") as f:
        data = f.read()
    editor.delete("1.0",tk.END)
    editor.insert("1.0", data)

def get_load_location():
    global load_loc
    load_loc_temp = load_loc_text.get("1.0",tk.END)
    if load_loc_temp != "":
        load_loc = load_loc_temp
    return load_loc

if __name__ == "__main__":

    #init the components
    root = tk.Tk()
    editor = tk.Text(height=30,width=90)
    main_menu = tk.Menu(root)
    file_bar = tk.Menu(main_menu,tearoff=0)
    run_bar = tk.Menu(main_menu,tearoff=0)
    name_editor = tk.Label(text="Editor:")
    name_output = tk.Label(text="Output:")
    code_output = tk.Text(height= 30,width= 40)
    load_loc_text = tk.Text(root,height=1,width=4)

    #customize the components
    root.resizable(FALSE,FALSE)
    root.title(f"{APPLICATION_NAME}")
    main_menu.add_cascade(label="Files",menu=file_bar)
    file_bar.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
    file_bar.add_command(label="New", command=new, accelerator="Ctrl+N")
    file_bar.add_command(label="Save", command=save, accelerator="Ctrl+S")
    file_bar.add_command(label="Save As", command=save_as, accelerator="Ctrl+Shift+S")
    file_bar.add_command(label="Exit", command=terminate)
    main_menu.add_cascade(label="Execute",menu=run_bar)
    run_bar.add_command(label="Compile", command=compile, accelerator="Ctrl+R")
    root.config(menu=main_menu)
    load_loc_text.insert("1.0","c000")

    #binds
    root.bind("<Control-s>",save)
    root.bind("<Control-Shift-s>",save_as)
    root.bind("<Control-o>",open_file)
    root.bind("<Control-n>",new)
    root.bind("<Control-r>",compile)

    #grid
    load_loc_text.grid  (column=1,row=1,padx=5,pady=5)
    name_editor.grid    (column=1,row=1,padx=5,pady=5,sticky="w")
    editor.grid         (column=1,row=2,padx=5,pady=5)
    name_output.grid    (column=2,row=1,padx=5,pady=5,sticky="w")
    code_output.grid    (column=2,row=2,padx=5,pady=5)


    root.mainloop()