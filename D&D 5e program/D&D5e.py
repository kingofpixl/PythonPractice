import tkinter as tk

#window creation
window = tk.Tk()
window.title("D&D 5e helper")

#window dimensions
#width = window.winfo_screenwidth()
#height = window.winfo_screenheight()
#window.geometry("%dx%d" % (width, height))
window.geometry("1280x1024")

#frame
frame = tk.Frame(window)
frame.pack(side = "top", expand=False, fill="both")


# Create a label widget in Tkinter
label = tk.Label(frame, text="Click the Button to update this Text",
font=('Calibri 15 bold'))
label.pack(pady=10)

# Function to update the label text for first button click in Tkinter
def on_click_btn1():
    label["text"] = "You selected " + menu.get()

my_Text = tk.Text(frame, width = 70, height  = 30)
my_Text.pack(pady = 20)

# Function to update the label text for second button click in Tkinter
def on_click_btn2():
    label["text"] = "You selected " + menu.get()
    my_Text.delete('1.0', tk.END)
    chosenClass = str(menu.get())
    txt_File = open(chosenClass + "basics.txt", 'r')
    basics = txt_File.read()
    my_Text.insert(tk.END, basics)
    txt_File.close()
    
# Create 1st button to update the label widget
btn1 = tk.Button(frame, text="Button1", command=on_click_btn1)
btn1.pack(pady=20)
 
# Create 2nd button to update the label widget
btn2 = tk.Button(frame, text="Button2", command=on_click_btn2)
btn2.pack(pady=40)

#clearing button


#drop down menu
menu = tk.StringVar()
menu.set("Select a D&D 5e class")

dropDown = tk.OptionMenu(frame, menu, "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorceror", "Warlock", "Wizard")
dropDown.pack()

def ok():
    print ("value is:" + menu.get())

button = tk.Button(frame, text="OK", command=ok)
button.pack()

# Run main loop
window.mainloop()