import tkinter as tk
from tkinter import messagebox, PhotoImage, ttk, filedialog
import sys, json

root = tk.Tk()
root.geometry("650x450")
root.title("PyNote")
configdata = json.load(open("config.json", encoding="UTF-8"))
fonts = ["Arial", "Arial Rounded MT", "Bahnschrift", "Bauhaus 93", "Calibri", "Castellar", "Cooper","新細明體", "標楷體"]
fontsizes = ["8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
             "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "36", "48", "72", "96"]
nowfile = ""

textframe = tk.Frame(root)
text = tk.Text(textframe, font=(configdata["font"][0], int(configdata["font"][1])), undo=1)
def backout():
    text.edit_undo()
def regain():
    text.edit_redo()

def about():
    messagebox.showinfo("PyNote", "版本:Beta\n日期:2023/1/26\n作者:阿滕")
def setting():
    set = tk.Tk()
    set.title("Setting")
    set.geometry("250x300")
    set.resizable(0, 0)
    
    setframe = tk.Frame(set)
    setframe.pack(pady=15)
    
    fontlabel = tk.Label(setframe, text="字形")
    fontCombobox = ttk.Combobox(setframe, values=fonts)
    fontCombobox.current(fonts.index(configdata["font"][0]))
    fontlabel.grid(column=0, row=0)
    fontCombobox.grid(column=1, row=0)
    fontsizelabel = tk.Label(setframe, text="大小")
    fontsizeCombobox = ttk.Combobox(setframe, values=fontsizes)
    fontsizeCombobox.current(fontsizes.index(configdata["font"][1]))
    fontsizelabel.grid(column=0, row=1, pady=5)
    fontsizeCombobox.grid(column=1, row=1, pady=5)
    
    def saveset():
        config = open("config.json", "w", encoding="UTF-8")
        configdata["font"][0] = fontCombobox.get()
        configdata["font"][1] = fontsizeCombobox.get()
        json.dump(configdata, config, ensure_ascii=0)
        set.destroy()
    
    savesetting = tk.Button(set, text="保存設定", command=saveset)
    savesetting.pack(side="bottom", pady=10)
    
def newfile():
    global nowfile
    nowfile = ""
    text.delete("1.0", "end")
    
def openfile():
    global nowfile
    try:
        nowfile = filedialog.askopenfilename()
        text.delete("1.0", "end")
        f = open(nowfile, "r", encoding="UTF-8")
        text.insert(1.0, str(f.read()))
        f.close()
    except:
        pass

def savefile():
    global nowfile
    if nowfile != "":
        f = open(nowfile, "w+", encoding="UTF-8")
        f.write(str(text.get(1.0, "end")))
        f.close()
    else:
        try:
            nowfile = filedialog.asksaveasfilename()
            f = open(nowfile, "w+", encoding="UTF-8")
            f.write(str(text.get(1.0, "end")))
            f.close()
        except:
            pass
        
def savenewfile():
    try:
        nowfile = filedialog.asksaveasfilename()
        f = open(nowfile, "w+", encoding="UTF-8")
        f.write(str(text.get(1.0, "end")))
        f.close()
    except:
        pass

fileimage = PhotoImage(file="file.png")
saveimage = PhotoImage(file="save.png")
settingimage = PhotoImage(file="set.png")

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="檔案(F)", menu=filemenu)
menubar.add_cascade(label="編輯(E)", menu=editmenu)
menubar.add_command(label="關於", command=about)
filemenu.add_command(label="新增檔案", command=newfile)
filemenu.add_command(label="開啟檔案", command=openfile)
filemenu.add_separator()
filemenu.add_command(label="儲存檔案", command=savefile)
filemenu.add_command(label="另存新檔", command=savenewfile)
filemenu.add_separator()
filemenu.add_command(label="結束", command=sys.exit)
editmenu.add_command(label="復原 Ctrl+Z", command=backout)
editmenu.add_command(label="取消復原 Ctrl+Y", command=regain)
editmenu.add_separator()
editmenu.add_command(label="尋找 Ctrl+F")
editmenu.add_separator()
editmenu.add_command(label="全選 Ctrl+A")

toolsbar = tk.Frame(root)
toolsbar.pack(anchor="nw")
openbutton = tk.Button(toolsbar, image=fileimage, command=openfile)
openbutton.grid(column=0, row=0)
openlabel = tk.Label(toolsbar, text="開啟")
openlabel.grid(column=0, row=1)
savebutton = tk.Button(toolsbar, image=saveimage, command=savefile)
savelabel = tk.Label(toolsbar, text="儲存")
savebutton.grid(column=1, row=0)
savelabel.grid(column=1, row=1)
setbutton = tk.Button(toolsbar, image=settingimage, command=setting)
setlabel = tk.Label(toolsbar, text="設置")
setbutton.grid(column=2, row=0)
setlabel.grid(column=2, row=1)

textframe.pack(fill=tk.BOTH, expand=tk.YES)
text.pack(fill=tk.BOTH, expand=tk.YES)

root.config(menu=menubar)

root.mainloop()