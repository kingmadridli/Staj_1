from tkinter import *
from tkinter import messagebox
from tkinter import IntVar
import socket


#DEFINE WINDOW
root = Tk()
root.geometry("600x675+820+40")
root.resizable(0,0)
root.iconbitmap("Form1.ico")

#DEFINE FONTS AND COLORS
all_fonts = ("Times New Roman",12)
label_font = ("Times New Roman",18)
name_frame_color = "#9400D3"
button_frame_color = "#00FFFF"
state_frame_color = "#FF69B4"
root.config(bg="Blue")


# Variables
HEADER = 64
FORMAT = "utf-8"
read_data = 256
string_separators = " | "
connected = False


#DEFINE FUNCTIONS

# Connection Function

def Connect():
    global connected
    global server
    if not connected:
        try:
            server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)           
            server.settimeout(2)
            server.connect(("192.168.25.70", 61))
            server.settimeout(None)
            conneciton_label.config(text="Bağlandı")
            conneciton_button.config(text="DURDUR")
            connected = True
        except Exception as err:
            messagebox.showinfo("Error","Connection Error {}".format(err))
            connected = False
            conneciton_button.config(text="Bağlan")
    else:
        try:
            socket.shutdown(socket.SHUT_RDWR)
            socket.close()
            conneciton_button.config(text="Bağlan")
            conneciton_label.config(text="Bağlantı kesildi")
            connected = False
        except Exception as err:
            messagebox.showinfo("Error","Connection Error : {}".format(err))
            connected = False
            conneciton_button.config(text="DURDUR")


def ReadCSV():
    global liste
    with open("Proje_5.csv","r") as file:
        content = file.readline
        i = 0
        liste = []
        while True:
            if i == 15:
                break
            else:
                var = content[i].split(",")[1]
                i +=1
                liste.append(var)
        return liste
    


# Led On Functions

def Led1_On():
    if connected:
        var1 = ReadCSV()[0]
        # state_label_1.config(text=ReadCSV()[0])
        server.sendall(ReadCSV()[0].encode())
        data_from_server = server.recv(HEADER)
        # print(data_from_server.decode(FORMAT))
        var = str(data_from_server)
        var2 = var.split("|")[1]
        string = f"Konum: {var1}, Durum: {var2}"
        state_label_1.config(text=string)

def Led2_On():
    if connected:
        state_label_2.config(text=ReadCSV()[1])
        

def Led3_On():
    if connected:
        state_label_3.config(text=ReadCSV()[2])

def Led4_On():
    if connected:
        state_label_4.config(text=ReadCSV()[3])

def Led5_On():
    if connected:
        state_label_5.config(text=ReadCSV()[4])

def Led6_On():
    if connected:
        state_label_6.config(text=ReadCSV()[5])

def Led7_On():
    if connected:
        state_label_7.config(text=ReadCSV()[6])

def Led8_On():
    if connected:
        state_label_8.config(text=ReadCSV()[7])

def Led9_On():
    if connected:
        state_label_9.config(text=ReadCSV()[8])

def Led10_On():
    if connected:
        state_label_10.config(text=ReadCSV()[9])


# Led Off Functions

def Led1_Off():
    pass

def Led2_Off():
    pass

def Led3_Off():
    pass

def Led4_Off():
    pass

def Led5_Off():
    pass

def Led6_Off():
    pass

def Led7_Off():
    pass

def Led8_Off():
    pass

def Led9_Off():
    pass

def Led10_Off():
    pass


# Reader read_functions

def Reader1_Read():
    pass

def Reader2_Read():
    pass

def Reader3_Read():
    pass

def Reader4_Read():
    pass

def Reader5_Read():
    pass


# Reader stop_functions

def Reader1_Stop():
    pass

def Reader2_Stop():
    pass

def Reader3_Stop():
    pass

def Reader4_Stop():
    pass

def Reader5_Stop():
    pass








#DEFINE MAIN FRAMES
name_frame = Frame(root,bg=name_frame_color,width=200,height=600)
button_frame = Frame(root,bg=button_frame_color,width=200,height=600)
state_frame = Frame(root,bg=state_frame_color,width=200,height=600)
conneciton_frame = Frame(root,bg="blue",width=200,height=600)
name_frame.grid(row=0,column=0)
button_frame.grid(row=0,column=1)
state_frame.grid(row=0,column=2)
conneciton_frame.grid(row=0,column=3)


#CONNECTION FRAME
conneciton_button = Button(conneciton_frame,text="CONNECT",font=all_fonts,bg="yellow",width=20,height=10,command=Connect)
conneciton_button.grid(row=0,column=0,padx=5,pady=5)
conneciton_label = Label(conneciton_frame,text="Not Connected yet",font=label_font)
conneciton_label.grid(row=1,column=0)


#DEFINE NAME FRAME
led_1 = Label(name_frame,text="LED1",font=all_fonts,bg=name_frame_color)
led_2 = Label(name_frame,text="LED2",font=all_fonts,bg=name_frame_color)
led_3 = Label(name_frame,text="LED3",font=all_fonts,bg=name_frame_color)
led_4 = Label(name_frame,text="LED4",font=all_fonts,bg=name_frame_color)
led_5 = Label(name_frame,text="LED5",font=all_fonts,bg=name_frame_color)
led_6 = Label(name_frame,text="LED6",font=all_fonts,bg=name_frame_color)
led_7 = Label(name_frame,text="LED7",font=all_fonts,bg=name_frame_color)
led_8 = Label(name_frame,text="LED8",font=all_fonts,bg=name_frame_color)
led_9 = Label(name_frame,text="LED9",font=all_fonts,bg=name_frame_color)
led_10 = Label(name_frame,text="LED10",font=all_fonts,bg=name_frame_color)
led_1.grid(row=0,column=0,padx=10,pady=10)
led_2.grid(row=1,column=0,padx=10,pady=10)
led_3.grid(row=2,column=0,padx=10,pady=10)
led_4.grid(row=3,column=0,padx=10,pady=10)
led_5.grid(row=4,column=0,padx=10,pady=10)
led_6.grid(row=5,column=0,padx=10,pady=10)
led_7.grid(row=6,column=0,padx=10,pady=10)
led_8.grid(row=7,column=0,padx=10,pady=10)
led_9.grid(row=8,column=0,padx=10,pady=10)
led_10.grid(row=9,column=0,padx=10,pady=10)



reader_1 = Label(name_frame,text="Reader1",font=all_fonts,bg=name_frame_color)
reader_2 = Label(name_frame,text="Reader2",font=all_fonts,bg=name_frame_color)
reader_3 = Label(name_frame,text="Reader3",font=all_fonts,bg=name_frame_color)
reader_4 = Label(name_frame,text="Reader4",font=all_fonts,bg=name_frame_color)
reader_5 = Label(name_frame,text="Reader5",font=all_fonts,bg=name_frame_color)
reader_1.grid(row=10,column=0,padx=10,pady=10)
reader_2.grid(row=11,column=0,padx=10,pady=10)
reader_3.grid(row=12,column=0,padx=10,pady=10)
reader_4.grid(row=13,column=0,padx=10,pady=10)
reader_5.grid(row=14,column=0,padx=10,pady=10)


#DEFINE BUTTON FRAME
led_button_1 = Button(button_frame,text="ON",bg=button_frame_color,font=all_fonts,command=Led1_On)
led_button_2 = Button(button_frame,text="ON",bg=button_frame_color,font=all_fonts,command=Led2_On)
led_button_3 = Button(button_frame,text="ON",bg=button_frame_color,font=all_fonts,command=Led3_On)
led_button_4 = Button(button_frame,text="ON",bg=button_frame_color,font=all_fonts,command=Led4_On)
led_button_5 = Button(button_frame,text="ON",bg=button_frame_color,font=all_fonts,command=Led5_On)
led_button_6 = Button(button_frame,text="ON",bg=button_frame_color,font=all_fonts,command=Led6_On)
led_button_7 = Button(button_frame,text="ON",bg=button_frame_color,font=all_fonts,command=Led7_On)
led_button_8 = Button(button_frame,text="ON",bg=button_frame_color,font=all_fonts,command=Led8_On)
led_button_9 = Button(button_frame,text="ON",bg=button_frame_color,font=all_fonts,command=Led9_On)
led_button_10 = Button(button_frame,text="ON",bg=button_frame_color,font=all_fonts,command=Led10_On)
led_button_1.grid(row=0,column=0,padx=10,pady=6)
led_button_2.grid(row=1,column=0,padx=10,pady=6)
led_button_3.grid(row=2,column=0,padx=10,pady=6)
led_button_4.grid(row=3,column=0,padx=10,pady=6)
led_button_5.grid(row=4,column=0,padx=10,pady=6)
led_button_6.grid(row=5,column=0,padx=10,pady=6)
led_button_7.grid(row=6,column=0,padx=10,pady=6)
led_button_8.grid(row=7,column=0,padx=10,pady=6)
led_button_9.grid(row=8,column=0,padx=10,pady=6)
led_button_10.grid(row=9,column=0,padx=10,pady=6)



led_button_1_1 = Button(button_frame,text="OFF",bg=button_frame_color,font=all_fonts,command=Led1_Off)
led_button_2_1 = Button(button_frame,text="OFF",bg=button_frame_color,font=all_fonts,command=Led2_Off)
led_button_3_1 = Button(button_frame,text="OFF",bg=button_frame_color,font=all_fonts,command=Led3_Off)
led_button_4_1 = Button(button_frame,text="OFF",bg=button_frame_color,font=all_fonts,command=Led4_Off)
led_button_5_1 = Button(button_frame,text="OFF",bg=button_frame_color,font=all_fonts,command=Led5_Off)
led_button_6_1 = Button(button_frame,text="OFF",bg=button_frame_color,font=all_fonts,command=Led6_Off)
led_button_7_1 = Button(button_frame,text="OFF",bg=button_frame_color,font=all_fonts,command=Led7_Off)
led_button_8_1 = Button(button_frame,text="OFF",bg=button_frame_color,font=all_fonts,command=Led8_Off)
led_button_9_1 = Button(button_frame,text="OFF",bg=button_frame_color,font=all_fonts,command=Led9_Off)
led_button_10_1 = Button(button_frame,text="OFF",bg=button_frame_color,font=all_fonts,command=Led10_Off)
led_button_1_1.grid(row=0,column=1,padx=10,pady=6)
led_button_2_1.grid(row=1,column=1,padx=10,pady=6)
led_button_3_1.grid(row=2,column=1,padx=10,pady=6)
led_button_4_1.grid(row=3,column=1,padx=10,pady=6)
led_button_5_1.grid(row=4,column=1,padx=10,pady=6)
led_button_6_1.grid(row=5,column=1,padx=10,pady=6)
led_button_7_1.grid(row=6,column=1,padx=10,pady=6)
led_button_8_1.grid(row=7,column=1,padx=10,pady=6)
led_button_9_1.grid(row=8,column=1,padx=10,pady=6)
led_button_10_1.grid(row=9,column=1,padx=10,pady=6)




reader_button_1 = Button(button_frame,text="OKU",bg=button_frame_color,font=all_fonts,command=Reader1_Read)
reader_button_2 = Button(button_frame,text="OKU",bg=button_frame_color,font=all_fonts,command=Reader2_Read)
reader_button_3 = Button(button_frame,text="OKU",bg=button_frame_color,font=all_fonts,command=Reader3_Read)
reader_button_4 = Button(button_frame,text="OKU",bg=button_frame_color,font=all_fonts,command=Reader4_Read)
reader_button_5 = Button(button_frame,text="OKU",bg=button_frame_color,font=all_fonts,command=Reader5_Read)
reader_button_1.grid(row=10,column=0,padx=10,pady=6)
reader_button_2.grid(row=11,column=0,padx=10,pady=6)
reader_button_3.grid(row=12,column=0,padx=10,pady=6)
reader_button_4.grid(row=13,column=0,padx=10,pady=6)
reader_button_5.grid(row=14,column=0,padx=10,pady=5)

reader_button_1_1 = Button(button_frame,text="DUR",bg=button_frame_color,font=all_fonts,command = Reader1_Stop)
reader_button_2_1 = Button(button_frame,text="DUR",bg=button_frame_color,font=all_fonts,command = Reader2_Stop)
reader_button_3_1 = Button(button_frame,text="DUR",bg=button_frame_color,font=all_fonts,command = Reader3_Stop)
reader_button_4_1 = Button(button_frame,text="DUR",bg=button_frame_color,font=all_fonts,command = Reader4_Stop)
reader_button_5_1 = Button(button_frame,text="DUR",bg=button_frame_color,font=all_fonts,command = Reader5_Stop)
reader_button_1_1.grid(row=10,column=1,padx=10,pady=6)
reader_button_2_1.grid(row=11,column=1,padx=10,pady=6)
reader_button_3_1.grid(row=12,column=1,padx=10,pady=6)
reader_button_4_1.grid(row=13,column=1,padx=10,pady=6)
reader_button_5_1.grid(row=14,column=1,padx=10,pady=6)



#DEFINE STATE FRAME
state_label_1 = Label(state_frame,text="Son Durum",font=all_fonts,bg=state_frame_color)
state_label_2 = Label(state_frame,text="Son Durum",font=all_fonts,bg=state_frame_color)
state_label_3 = Label(state_frame,text="Son Durum",font=all_fonts,bg=state_frame_color)
state_label_4 = Label(state_frame,text="Son Durum",font=all_fonts,bg=state_frame_color)
state_label_5 = Label(state_frame,text="Son Durum",font=all_fonts,bg=state_frame_color)
state_label_6 = Label(state_frame,text="Son Durum",font=all_fonts,bg=state_frame_color)
state_label_7 = Label(state_frame,text="Son Durum",font=all_fonts,bg=state_frame_color)
state_label_8 = Label(state_frame,text="Son Durum",font=all_fonts,bg=state_frame_color)
state_label_9 = Label(state_frame,text="Son Durum",font=all_fonts,bg=state_frame_color)
state_label_10 = Label(state_frame,text="Son Durum",font=all_fonts,bg=state_frame_color)
state_label_11 = Label(state_frame,text="Son Durum",font=all_fonts,bg=state_frame_color)
state_label_12 = Label(state_frame,text="Son Durum",font=all_fonts,bg=state_frame_color)
state_label_13 = Label(state_frame,text="Son Durum",font=all_fonts,bg=state_frame_color)
state_label_14 = Label(state_frame,text="Son Durum",font=all_fonts,bg=state_frame_color)
state_label_15 = Label(state_frame,text="Son Durum",font=all_fonts,bg=state_frame_color)
state_label_1.grid(row=0,column=0,padx=5,pady=10)
state_label_2.grid(row=1,column=0,padx=5,pady=10)
state_label_3.grid(row=2,column=0,padx=5,pady=10)
state_label_4.grid(row=3,column=0,padx=5,pady=10)
state_label_5.grid(row=4,column=0,padx=5,pady=10)
state_label_6.grid(row=5,column=0,padx=5,pady=10)
state_label_7.grid(row=6,column=0,padx=5,pady=10)
state_label_8.grid(row=7,column=0,padx=5,pady=10)
state_label_9.grid(row=8,column=0,padx=5,pady=10)
state_label_10.grid(row=9,column=0,padx=5,pady=10)
state_label_11.grid(row=10,column=0,padx=5,pady=10)
state_label_12.grid(row=11,column=0,padx=5,pady=10)
state_label_13.grid(row=12,column=0,padx=5,pady=10)
state_label_14.grid(row=13,column=0,padx=5,pady=10)
state_label_15.grid(row=14,column=0,padx=5,pady=10)





#LOOP WINDOW
root.mainloop()