import datetime
from tkinter import * # represents all the function and built-in modules in the library.
from datetime import date

class Calculator:
    def __init__(self, root):
        self.c_date = date.today()
        self.format = str(self.c_date.strftime("%d-%m-%Y"))
        self.date = Label(root, text="Date : ")
        self.current_date = Label(root, text=str(self.format))
        #create lables
        self.id = Label(root, text="Item Description : ")
        self.size = Label(root, text="Size & Schedule : ")
        self.lbl1 = Label(root, text="Total Pipe Length(mm) : ")
        self.lbl2 = Label(root, text="Raw Material Length(mm) : ")
        self.lbl3 = Label(root, text="Weight/meter(Kg) : ")
        self.lbl4 = Label(root, text="Heat Treatment Cost/Kg(Rs.) : ")
        self.lbl5 = Label(root, text="Current Steel Price(Rs.) : ")
        self.lbl6 = Label(root, text="Total Products from 1 Pipe : ")
        self.lbl7 = Label(root, text="Total Weight of 1 Pipe(Kg) : ")
        self.lbl8 = Label(root, text="Total Price of 1 Pipe(Rs.) : ")
        self.lbl9 = Label(root, text="Total Machining Cost(Rs.) : ")
        self.lbl10 = Label(root, text="Total Heat Treatment Cost(Rs.) : ")
        self.lbl11 = Label(root, text="Manufacturing Cost/unit is(Rs.) : ")
        self.lbl12 = Label(root, text="**For Output Only",)


        #take input from user
        self.id_e = Entry()
        self.size_e = Entry()
        self.e1 = Entry()
        self.e2 = Entry()
        self.e3 = Entry()
        self.e4 = Entry()
        self.e5 = Entry()

        #to display calculated outputs
        self.e6 = Entry()
        self.e7 = Entry()
        self.e8 = Entry()
        self.e9 = Entry()
        self.e10 = Entry()
        self.e11 = Entry()



        # place lables and input fields
        self.date.place(x=20, y=50)
        self.current_date.place(x=200, y=50)

        self.id.place(x=20, y=100)
        self.id_e.place(x=200, y=100)

        self.size.place(x=400, y=100)
        self.size_e.place(x=575, y=100)

        self.lbl1.place(x=20, y=150)
        self.e1.place(x=200, y=150)

        self.lbl2.place(x=400, y=150)
        self.e2.place(x=575, y=150)

        self.lbl3.place(x=20, y=200)
        self.e3.place(x=200, y=200)

        self.lbl4.place(x=400, y=200)
        self.e4.place(x=575, y=200)

        self.lbl5.place(x=20, y=250)
        self.e5.place(x=200, y=250)

        self.lbl6.place(x=20, y=400)
        self.e6.place(x=200, y=400)

        self.lbl7.place(x=400, y=400)
        self.e7.place(x=575, y=400)

        self.lbl8.place(x=20, y=450)
        self.e8.place(x=200, y=450)

        self.lbl9.place(x=400, y=450)
        self.e9.place(x=575, y=450)

        self.lbl10.place(x=20, y=500)
        self.e10.place(x=200, y=500)

        self.lbl11.place(x=400, y=500)
        self.e11.place(x=575, y=500)

        self.lbl12.place(x=20, y=350)

        # Create button and bind all the functions to calculate desire output
        self.btn1 = Button(root, text="Calculate",
                           command=lambda: [self.output1(), self.output2(), self.output3(), self.output4(),
                                            self.output5(), self.output6(), self.getval()])
        self.btn1.place(x=250, y=300)

        # Create button to reset values
        self.btn2 = Button(root, text="Reset", command=self.reset)
        self.btn2.place(x=400, y=300)

    #calculate total products from 1 pipe
    def output1(self):

        x = float(self.e1.get())
        y = float(self.e2.get())
        result = x // y
        self.e6.insert(END, str(result))

    #calculate total weight of 1 pipe
    def output2(self):

        x = float(self.e3.get())
        #Define pipe length in meters
        y = 6
        result = x * y
        self.e7.insert(END, str(result))

    #calculate total price of 1 pipe
    def output3(self):

        x = float(self.e5.get())
        y = float(self.e7.get())
        result = x * y
        self.e8.insert(END, str(result))

    #calculate Machining cost
    def output4(self):

        x = float(self.e8.get())
        result = x * 50 // 100
        self.e9.insert(END, str(result))

    #calculate total heat treatment cost
    def output5(self):

        x = float(self.e7.get())
        y = float(self.e4.get())
        result = x * y
        self.e10.insert(END, str(result))

    #finally calculate manufacturing cost/unit
    def output6(self):

        x = float(self.e8.get())
        y = float(self.e9.get())
        z = float(self.e10.get())
        a = float(self.e6.get())
        add = x + y + z
        result = add / a
        self.e11.insert(END, str(result))

    def reset(self):
        self.id_e.delete(0, 'end')
        self.size_e.delete(0, 'end')
        self.e1.delete(0, 'end')
        self.e2.delete(0, 'end')
        self.e3.delete(0, 'end')
        self.e4.delete(0, 'end')
        self.e5.delete(0, 'end')
        self.e6.delete(0, 'end')
        self.e7.delete(0, 'end')
        self.e8.delete(0, 'end')
        self.e9.delete(0, 'end')
        self.e10.delete(0, 'end')
        self.e11.delete(0, 'end')

    def getval(self):
        with open("rec2.txt", "w") as f:
            f.write(f"""{self.format, self.id_e.get(), self.size_e.get(), self.e1.get(), self.e2.get(),
            self.e3.get(), self.e4.get(), self.e5.get(), self.e6.get(), self.e7.get(), self.e8.get(),
            self.e9.get(), self.e10.get(), self.e11.get()}\n""")



root = Tk()
mycal = Calculator(root)
root.title("GUI Based Manufacturing Cost/Unit Calculator")
root.geometry("800x600")
root.mainloop()