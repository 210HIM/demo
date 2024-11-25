from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

class Data_Analysis:

    def __init__(self):
        pass

    def Analysis(self, root):
        self.root = root

        self.Datafreame1 = Frame(self.root, bd=2, bg='white', relief=RIDGE)
        self.Datafreame1.place(x=0, y=0, width=1200, height=800)

        self.child = Frame(self.Datafreame1, bg='#a7d5ef')
        self.child.place(x=0, y=0, width=400, height=400)

        self.child2 = Frame(self.Datafreame1, bg='#a7d5ef')
        self.child2.place(x=500, y=0, width=600, height=400)

        self.child3 = Frame(self.Datafreame1, bg='white')
        self.child3.place(x=50, y=400, width=700, height=300)

        stockListExp = ['PAID', 'UNPAID', ]
        stockSplitExp = [40, 80]
        fig = Figure()
        ax = fig.add_subplot(111)
        ax.pie(stockSplitExp, labels=stockListExp, autopct='%0.2f%%', )
        chart1 = FigureCanvasTkAgg(fig, self.child)
        chart1.get_tk_widget().pack()



        f = Figure(figsize=(6, 4), dpi=100)
        ax = f.add_subplot(111)
        # Sample data for the bar chart
        data = (21, 25, 30, 25, 25)
        ind = np.arange(5)  # X locations for the bars
        width = 0.5
        # Create the bar chart
        rects1 = ax.bar(ind, data, width)
        # Embed the FigureCanvasTkAgg widget in the Tkinter window
        canvas = FigureCanvasTkAgg(f, master=self.child2)
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
