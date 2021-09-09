from tkinter import *
import socket
from tkinter import messagebox
from socket import SHUT_RDWR
import time
from tkinter import IntVar
import threading

#Define The Window
root = Tk()
root.geometry("600x600")
root.resizable(0,0)
root.title("Form1")
root.iconbitmap("Form1.ico")
root.config(background="pink")

# Define Colors and Fonts
frames_color = "pink"
label_fonts = ("Times New Roman",12)
label_colors = "Black"

HEADER = 64
FORMAT = "utf-8"

led1 = "a"
lm34 = "b"
led2 = "c"
ldr = "d"
read_data = 256
string_separators = " | "
connected = False

# Functions

def ConnectButtonClick():
    global connected
    global server
    if not connected:
        try:
            server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)           
            server.settimeout(2)
            server.connect(("192.168.25.70", 61))
            server.settimeout(None)
            connect_label.config(text="Bağlandı")
            connect_button.config(text="DURDUR")
            connected = True
        except Exception as err:
            messagebox.showinfo("Error","Connection Error {}".format(err))
            connected = False
            connect_button.config(text="Bağlan")
    else:
        try:
            socket.shutdown(socket.SHUT_RDWR)
            socket.close()
            connect_button.config(text="Bağlan")
            connect_label.config(text="Bağlantı kesildi")
            connected = False
        except Exception as err:
            messagebox.showinfo("Error","Connection Error : {}".format(err))
            connected = False
            connect_button.config(text="DURDUR")

def Button1Click():
    global connected
    if connected:
        print ('server started and listening')
        server.sendall(led1.encode())                
        data_from_server = server.recv(HEADER)
        # print(data_from_server.decode(FORMAT))
        # print('recieved',repr(data_from_server))
        var = str(data_from_server)
        var2 = var.split("|")
        label_1.config(text=var2[1])

def Button2Click():
    global connected
    if connected:
        print ('server started and listening')
        server.sendall(led2.encode())                
        data_from_server = server.recv(HEADER)
        # print(data_from_server.decode(FORMAT))
        # print('recieved',repr(data_from_server))
        var = str(data_from_server)
        var2 = var.split("|")
        label_2.config(text=var2[1])

def Button3Click():
    global connected
    if connected:
        print ('server started and listening')
        server.sendall(lm34.encode())                
        data_from_server = server.recv(HEADER)
        # print(data_from_server.decode(FORMAT))
        # print('recieved',repr(data_from_server))
        var = str(data_from_server)
        var2 = var.split("|")
        label_3.config(text=var2[1])

def Button4Click():
    global connected
    if connected:
        print ('server started and listening')
        server.sendall(ldr.encode())                
        data_from_server = server.recv(HEADER)
        # print(data_from_server.decode(FORMAT))
        # print('recieved',repr(data_from_server))
        var = str(data_from_server)
        var2 = var.split("|")
        label_4.config(text=var2[1])


def Choose():
    if radio_var.get() == 1:
        Button3CheckClick()
    elif radio_var.get() == 2:
        Button4CheckClick()

def Stop():
    print("receiving is stopped by user")
    global key
    if key == 1:
        key =2
    elif key == 2:
        key = 1
    

def Button3CheckClick():
    global thread_1_statu,key
    if thread_1_statu == False:
        thread_1.start()
    else:
        key = 1

def Thread1Loop():
    global key,thread_1_statu
    thread_1_statu = True
    while True:
        time.sleep(0.2)
        while key == 1:
            Button3Click()
            print("LM34 data is received")
            time.sleep(1)

def Button4CheckClick(): 
    global thread_2_statu,key
    if thread_2_statu == False:
        thread_2.start()
    else:
        key = 1   

def Thread2Loop():
    global key,thread_2_statu
    thread_2_statu = True
    while True:
        time.sleep(0.2)
        while key == 1:
            Button3Click()
            print("LDR data is received")
            time.sleep(1)

thread_1 = threading.Thread(target=Thread1Loop)
thread_2 = threading.Thread(target=Thread2Loop)
key = 1
thread_1_statu = False
thread_2_statu = False

# Define Frames
connection_frame = Frame(root,bg=frames_color,highlightthickness=5,highlightbackground="green")
connection_frame.grid(row=0,column=0,pady=(10,50),padx=1)

button_frame_1 = Frame(root,bg=frames_color,highlightthickness=5,highlightbackground="green")
button_frame_1.grid(row=1,column=0,pady=10,padx=1)

button_frame_2 = Frame(root,bg=frames_color,highlightthickness=5,highlightbackground="green")
button_frame_2.grid(row=1,column=1,pady=10,padx=1)

# Define Layout
connect_button = Button(connection_frame,text="Bağlan",font=label_fonts,bg="blue",width=10,height=3,command=ConnectButtonClick)
connect_button.grid(row=0,column=0,padx=20,pady=10)
connect_label = Label(connection_frame,text="Bağlantı Yok",font=label_fonts)
connect_label.grid(row=0,column=1,padx=(20,20))

button_1 = Button(button_frame_1,text="LED 1",width=8,height=3,command=Button1Click)
button_1.grid(row=0,column=0,padx=(10,40),pady=40)
button_2 = Button(button_frame_1,text="LED 2",width=8,height=3,command=Button2Click)
button_2.grid(row=1,column=0,pady=40,padx=(10,40))

label_1 = Label(button_frame_1,text="--",font=label_fonts)
label_1.grid(row=0,column=1,padx=20)
label_2 = Label(button_frame_1,text="--",font=label_fonts)
label_2.grid(row=1,column=1,padx=20)

button_3 = Button(button_frame_2,text="LM35",width=8,height=3,command=Button3Click)
button_3.grid(row=0,column=0,padx=(20,20),pady=40)
button_4 = Button(button_frame_2,text="LDR",width=8,height=3,command=Button4Click)
button_4.grid(row=3,column=0,pady=40,padx=(20,20))

radio_var = IntVar()


button_3_check = Radiobutton(button_frame_2,text="Sürekli Oku",variable=radio_var,value=1)
button_3_check.grid(row=1,column=0) 
button_4_check = Radiobutton(button_frame_2,text="Sürekli Oku",variable=radio_var,value=2)
button_4_check.grid(row=4,column=0)

label_3 = Label(button_frame_2,text="--",font=label_fonts)
label_3.grid(row=0,column=1,padx=20)
label_4 = Label(button_frame_2,text="--",font=label_fonts)
label_4.grid(row=3,column=1,padx=20)

choose_button = Button(button_frame_2,text="CHOOSE",command=Choose)
choose_button.grid(row=2,column=1)
stop_button = Button(button_frame_2,text="STOP",command=Stop)
stop_button.grid(row=2,column=2)

# Loop The Main Window
root.mainloop()