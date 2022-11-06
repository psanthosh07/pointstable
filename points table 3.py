
from tkinter import *

root = Tk()

def getvals():
    print("Submitting form")

    print(f"{namevalue.get(), phonevalue.get(), resultvalue.get(), bat1runsvalue.get(), paymentmodevalue.get(), foodservicevalue.get()} ")



    with open("records.txt", "a") as f:
        f.write(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentmodevalue.get(), foodservicevalue.get()}\n ")
'''
def savals():
    hometeam=namevalue.get()
    results=resultvalue.get()
    bat1runs=batrunsvalue.get()
    over1pla=firoversvalue.get()
    print(hometeam,results,bat1runs,over1pla)
'''
root.geometry("644x344")
#Heading
Label(root, text="Welcome to Harry Travels", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)

#Text for our form
name = Label(root, text="Name")
phone = Label(root, text="matches")
result = Label(root, text="result(w,d,l)")
batruns = Label(root, text="batting score")
firovers = Label(root, text="overs batted")

#Pack text for our form
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
result.grid(row=3, column=2)
batruns.grid(row=4, column=2)
firovers.grid(row=5, column=2)

# Tkinter variable for storing entries
namevalue = StringVar()
phonevalue = StringVar()
resultvalue = StringVar()
batrunsvalue = StringVar()
firoversvalue = StringVar()
foodservicevalue = IntVar()


#Entries for our form
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
resultentry = Entry(root, textvariable=gendervalue)
batrunsentry = Entry(root, textvariable=emergencyvalue)
firoversentry = Entry(root, textvariable=paymentmodevalue)

# Packing the Entries
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
resultentry.grid(row=3, column=3)
batrunsentry.grid(row=4, column=3)
firoversentry.grid(row=5, column=3)

#Checkbox & Packing it
foodservice = Checkbutton(text="Want to prebook your meals?", variable = foodservicevalue)
foodservice.grid(row=6, column=3)

#Button & packing it and assigning it a command
Button(text="Submit to Harry Travels", command=savals).grid(row=7, column=3)

root.mainloop()


