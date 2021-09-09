from tkinter import *
from tkinter import messagebox
from tkinter import IntVar

#DEFINE WINDOW
root = Tk()
root.geometry("500x675+820+40")
root.resizable(1,1)
root.iconbitmap("Form1.ico")

#DEFINE FONTS AND COLORS
all_fonts = ("Times New Roman",12)
label_font = ("Times New Roman",18)
name_frame_color = "#9400D3"
button_frame_color = "#00FFFF"
state_frame_color = "#FF69B4"
root.config(bg="Blue")



#DEFINE MAIN FRAME
name_frame = Frame(root,bg=name_frame_color,width=200,height=600)
button_frame = Frame(root,bg=button_frame_color,width=200,height=600)
state_frame = Frame(root,bg=state_frame_color,width=200,height=600)
conneciton_frame = Frame(root,bg="blue",width=200,height=600)
name_frame.grid(row=0,column=0)
button_frame.grid(row=0,column=1)
state_frame.grid(row=0,column=2)
conneciton_frame.grid(row=0,column=3)


#CONNECTION FRAME
conneciton_button = Button(conneciton_frame,text="CONNECT",font=all_fonts,bg="yellow",width=20,height=10)
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
led_button_1 = Button(button_frame,text="ON",bg=button_frame_color,font=all_fonts)
led_button_2 = Button(button_frame,text="ON",bg=button_frame_color,font=all_fonts)
led_button_3 = Button(button_frame,text="ON",bg=button_frame_color,font=all_fonts)
led_button_4 = Button(button_frame,text="ON",bg=button_frame_color,font=all_fonts)
led_button_5 = Button(button_frame,text="ON",bg=button_frame_color,font=all_fonts)
led_button_6 = Button(button_frame,text="ON",bg=button_frame_color,font=all_fonts)
led_button_7 = Button(button_frame,text="ON",bg=button_frame_color,font=all_fonts)
led_button_8 = Button(button_frame,text="ON",bg=button_frame_color,font=all_fonts)
led_button_9 = Button(button_frame,text="ON",bg=button_frame_color,font=all_fonts)
led_button_10 = Button(button_frame,text="ON",bg=button_frame_color,font=all_fonts)
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



led_button_1_1 = Button(button_frame,text="OFF",bg=button_frame_color,font=all_fonts)
led_button_2_1 = Button(button_frame,text="OFF",bg=button_frame_color,font=all_fonts)
led_button_3_1 = Button(button_frame,text="OFF",bg=button_frame_color,font=all_fonts)
led_button_4_1 = Button(button_frame,text="OFF",bg=button_frame_color,font=all_fonts)
led_button_5_1 = Button(button_frame,text="OFF",bg=button_frame_color,font=all_fonts)
led_button_6_1 = Button(button_frame,text="OFF",bg=button_frame_color,font=all_fonts)
led_button_7_1 = Button(button_frame,text="OFF",bg=button_frame_color,font=all_fonts)
led_button_8_1 = Button(button_frame,text="OFF",bg=button_frame_color,font=all_fonts)
led_button_9_1 = Button(button_frame,text="OFF",bg=button_frame_color,font=all_fonts)
led_button_10_1 = Button(button_frame,text="OFF",bg=button_frame_color,font=all_fonts)
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




reader_button_1 = Button(button_frame,text="OKU",bg=button_frame_color,font=all_fonts)
reader_button_2 = Button(button_frame,text="OKU",bg=button_frame_color,font=all_fonts)
reader_button_3 = Button(button_frame,text="OKU",bg=button_frame_color,font=all_fonts)
reader_button_4 = Button(button_frame,text="OKU",bg=button_frame_color,font=all_fonts)
reader_button_5 = Button(button_frame,text="OKU",bg=button_frame_color,font=all_fonts)
reader_button_1.grid(row=10,column=0,padx=10,pady=6)
reader_button_2.grid(row=11,column=0,padx=10,pady=6)
reader_button_3.grid(row=12,column=0,padx=10,pady=6)
reader_button_4.grid(row=13,column=0,padx=10,pady=6)
reader_button_5.grid(row=14,column=0,padx=10,pady=5)

reader_button_1_1 = Button(button_frame,text="DUR",bg=button_frame_color,font=all_fonts)
reader_button_2_1 = Button(button_frame,text="DUR",bg=button_frame_color,font=all_fonts)
reader_button_3_1 = Button(button_frame,text="DUR",bg=button_frame_color,font=all_fonts)
reader_button_4_1 = Button(button_frame,text="DUR",bg=button_frame_color,font=all_fonts)
reader_button_5_1 = Button(button_frame,text="DUR",bg=button_frame_color,font=all_fonts)
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