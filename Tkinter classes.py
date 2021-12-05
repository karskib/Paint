import tkinter as tk
from tkinter import simpledialog

root = tk.Tk()
root.geometry('600x400')
root.grid_columnconfigure(0, weight = 1)
root.grid_rowconfigure(0,weight = 1)


class Window:

    def __init__(self, master):
        colours = ['yellow', 'green', 'red', 'blue', 'black','pink','purple']
        photo = tk.PhotoImage('users/karolskiba/downloads/image.png')
        self.click_counter = 0
        self.colour = ''
        self.size_of_drawing = 2

        self.myFrame1 = tk.Frame(master,height = 80, width = 80, bd = 4, relief = tk.RAISED)
        self.myFrame1.grid(row= 0 , column = 0, sticky= 'nw')

        self.myButton = tk.Button(self.myFrame1, text='Clear\nbackground', command=self.clear_background)
        self.myButton.grid(row=0, column=0, sticky = 'w')

        self.myButton2 = tk.Button(self.myFrame1, text='Change\nbackground\ncolor', command=self.change_color)
        self.myButton2.grid(row=1, column=0, sticky= 'n')

        self.myButton3 = tk.Button(self.myFrame1, text = 'bigger', command = self.bigger)
        self.myButton3.grid(row=10, column = 0, sticky ='nw')

        self.myButton4 = tk.Button(self.myFrame1, text = 'smaller', command = self.smaller)
        self.myButton4.grid(row=11,column = 0, sticky = 'nw')

        self.Canvas = tk.Canvas(root, bg='blue', width=500, height=500,bd = 4)
        self.Canvas.grid(row=0, column=1)

        self.Canvas.bind('<Double-Button-1>', self.create_line)
        self.Canvas.bind("<B1-Motion>", self.paint)


        i = 2
        for color in colours:
            butt=tk.Button(self.myFrame1, fg=color, text=color, relief=tk.RAISED, command = lambda col = color: self.select_colour(col))
            butt.grid(row=i, column=0, sticky= 'w')
            i += 1

    def bigger(self):
        self.size_of_drawing += 1

    def smaller(self):

        if self.size_of_drawing < 0:
            alert = tk.Toplevel()
            alert.geometry('250x50-300-200')
            alert.title('Size too small')
            tk.Label(alert,text = 'Size cannot be smaller than 0').pack()
        else:
            self.size_of_drawing -= 1

    def paint(self, event):
        x0, y0 = (event.x - self.size_of_drawing), (event.y - self.size_of_drawing)
        x1, y1 = (event.x + self.size_of_drawing), (event.y + self.size_of_drawing)
        self.Canvas.create_oval(x0, y0, x1, y1, fill=self.colour, width = 1, outline = self.colour)


    def clear_background(self):
        self.Canvas.delete('all')

    def select_colour(self,col):
        self.colour = col

    def change_color(self):
        box = tk.simpledialog.askstring('Please enter color', prompt='Enter color')
        try:
            self.Canvas.configure(bg=str(box))
        except:
            top = tk.Toplevel()
            top.geometry("250x50-300-200")
            top.title("Error")
            tk.Label(top, text="Please enter a valid color", font=('Mistral 18 bold')).pack()

    def create_line(self, event):
        if self.click_counter == 0:
            self.x0 = event.x
            self.y0 = event.y
            self.click_counter = 1
        else:
            self.x1 = event.x
            self.y1 = event.y
            line = self.Canvas.create_line(self.x0, self.y0, self.x1, self.y1, fill=self.colour, width = 3)
            self.click_counter = 0


if __name__ == '__main__':
    w = Window(root)
    tk.mainloop()
