from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import json


root = Tk()
root.geometry("1042x700")
root.title("Todo")
root.columnconfigure(1, weight=2)
root.columnconfigure(99, weight=2)

def load():
    global task_list
    try:
        with open("task.json","r",encoding="utf-8") as f:
            task_list = json.load(f)
    except FileNotFoundError:
        task_list=[]

#新規追加
def add():
    #データ処理
    task = task_entry.get()
    deadline = deadline_entry.get()
    priority = priority_entry.get()
    if task and deadline and priority:
        task_list.append({"task":task,
                          "deadline":deadline,
                          "priority":priority,
                          "completed":False})
    else:
        messagebox.showinfo("エラー","入力項目不足")
        return
    update() 
    #入力クリア
    task_entry.delete(0,END) 
    deadline_entry.delete(0,END)
    priority_entry.delete(0,END)

#完了処理    
def complete(i):
    Label(text="済",justify=LEFT,relief=SOLID,width=8,height=2).grid(row=i+1,column=4,sticky="ns")
    return
#更新対応
def update():
    #入力欄とヘッダー残して全部消す
    for widget in root.grid_slaves():
        info = widget.grid_info()
        if info["row"] not in (0,99) and info["column"] != 0:
            widget.destroy()
    for i,task in enumerate(task_list):
        
        Label(root,text=task["task"],justify=LEFT,relief=SOLID,width=110,height=2).grid(row=i+1,column=1,sticky="ns")
        Label(root,text=task["deadline"],justify=LEFT,relief=SOLID,width=20,height=2).grid(row=i+1,column=2,sticky="ns")
        Label(root,text=task["priority"],justify=LEFT,relief=SOLID,width=7,height=2).grid(row=i+1,column=3,sticky="ns")
        Label(root,text="済" if task["completed"] else "未",justify=LEFT,relief=SOLID,width=8,height=2).grid(row=i+1,column=4,sticky="ns")
    
    with open("task.json","w",encoding="utf-8") as f :
        json.dump(task_list,f,ensure_ascii = False,indent=2)
    return


#定義
t_label_1 = Label(root,text="やること",justify="center",width=110,height=2,relief="solid")
t_label_2 = Label(root,text="締め切り",justify="center",height=2,relief="solid")
t_label_3 = Label(root,text="優先度",justify="center",height=2,relief="solid")
t_label_4 = Label(root,text="進捗",justify="center",height=2,relief="solid")

label = Label(root,text="新規",justify="center",height=2,relief="solid")
task_entry = Entry(root,font=("明朝体",22),relief="solid",width=50,borderwidth=2)
deadline_entry = Entry(root,font=("明朝体",22),relief="solid",width=8,borderwidth=2)
priority_entry = Entry(root,font=("明朝体",22),relief="solid",width=3,borderwidth=2)
task_button = Button(root,text = "確定",width=7,height=2,command=add,relief="solid")



#レイアウト
for i in range(15):
    Button(root,text = "任務\n完了",width=7,height=2,command=lambda i = i:complete(i)).grid(row=i+1,column=0,sticky="ew")

t_label_1.grid(row=0,column=1,sticky="ew")
t_label_2.grid(row=0,column=2,sticky="ew")
t_label_3.grid(row=0,column=3,sticky="ew")
t_label_4.grid(row=0,column=4,sticky="ew")

label.grid(row=99,column=0,sticky="ew")
task_entry.grid(row=99,column=1,sticky="ew")
deadline_entry.grid(row=99,column=2,sticky="ew")
priority_entry.grid(row=99,column=3,sticky="ew")
task_button.grid(row=99,column=4,sticky="ew")

load()
update()

root.mainloop()