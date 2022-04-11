from tkinter import *
from tkinter import ttk

class Calculator:
    def __init__(self):
        self.root = Tk()
        self.root.title('Calculator')

        self.mainframe = Frame(self.root)
        self.mainframe.grid(column = 0, row = 0)

        self.display()
        self.root.mainloop()

    def display(self):
        self.entryInfo = StringVar()
        self.entry = ttk.Entry(self.mainframe, width=50, textvariable=self.entryInfo)
        self.button1 = ttk.Button(self.mainframe, text='1', command=lambda: self.btnClick('1'))
        self.button2 = ttk.Button(self.mainframe, text='2', command=lambda: self.btnClick('2'))
        self.button3 = ttk.Button(self.mainframe, text='3', command=lambda: self.btnClick('3'))
        self.button4 = ttk.Button(self.mainframe, text='4', command=lambda: self.btnClick('4'))
        self.button5 = ttk.Button(self.mainframe, text='5', command=lambda: self.btnClick('5'))
        self.button6 = ttk.Button(self.mainframe, text='6', command=lambda: self.btnClick('6'))
        self.button7 = ttk.Button(self.mainframe, text='7', command=lambda: self.btnClick('7'))
        self.button8 = ttk.Button(self.mainframe, text='8', command=lambda: self.btnClick('8'))
        self.button9 = ttk.Button(self.mainframe, text='9', command=lambda: self.btnClick('9'))
        self.button0 = ttk.Button(self.mainframe, text='0', command=lambda: self.btnClick('0'))
        self.divideBtn = ttk.Button(self.mainframe, text='/', command=lambda: self.btnClick('/'))
        self.multiplyBtn = ttk.Button(self.mainframe, text='*', command=lambda: self.btnClick('*'))
        self.additionBtn = ttk.Button(self.mainframe, text='+', command=lambda: self.btnClick('+'))
        self.subtractionBtn = ttk.Button(self.mainframe, text='-', command=lambda: self.btnClick('-'))
        self.equalsBtn = ttk.Button(self.mainframe, text='=', command=lambda: self.btnClick('='))
        self.clearBtn = ttk.Button(self.mainframe, text='c', command = lambda: self.entry.delete(0, END))
    
        self.entry.grid(column=0, row=0, columnspan=4)
        self.button1.grid(column=0, row=1)
        self.button2.grid(column=1, row=1)
        self.button3.grid(column=2, row=1)
        self.additionBtn.grid(column=3, row=1)
        self.button4.grid(column=0, row=2)
        self.button5.grid(column=1, row=2)
        self.button6.grid(column=2, row=2)
        self.subtractionBtn.grid(column=3, row=2)
        self.button7.grid(column=0, row=3)
        self.button8.grid(column=1, row=3)
        self.button9.grid(column=2, row=3)
        self.divideBtn.grid(column=3, row=3)
        self.clearBtn.grid(column=0, row=4)
        self.button0.grid(column=1, row=4)
        self.equalsBtn.grid(column=2, row=4)
        self.multiplyBtn.grid(column=3, row=4)
        
    def btnClick(self, numOp):
        if numOp in '1234567890':
            self.entryInfo.set(f'{self.entryInfo.get()}{numOp}')
        elif numOp in '+-*/':
            self.currentEval = f'{self.entryInfo.get()}{numOp}'
            self.entry.delete(0, END)
        elif numOp == '=':
            self.currentEval = f'{self.currentEval}{self.entryInfo.get()}'
            self.entry.delete(0, END)
            self.entryInfo.set(eval(self.currentEval))
        
if __name__ == '__main__':
    Calculator()