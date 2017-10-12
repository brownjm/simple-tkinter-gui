"""A simple Tkinter GUI"""

import os
from tkinter import Tk, Menu, filedialog, Button
import plotting


class MyApp:
    """An example application using tkinter"""
    def __init__(self):
        # directory of where data is located
        self.current_directory = '.'
        
        # create the main window
        self.root = Tk()

        # customize some global properties of the GUI
        self.root.option_add('*tearOff', False)
        self.root.option_add('*Font', ('TkDefaultFont', 12))
        self.root.title("Title")

        # create a menu bar
        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label='Open', command=self.set_data_directory)
        filemenu.add_command(label='Exit', command=self.root.destroy)
        menubar.add_cascade(label='File', menu=filemenu)
        self.root.config(menu=menubar)


        # create a button and connect it to the self.plot() function
        button = Button(self.root, text='Plot Data', command=self.plot)

        # you must tell the button where to appear in the gui window
        button.grid(row=0, column=0, padx='3m', pady='3m')

        
    def run(self):
        """Start the GUI"""
        self.root.mainloop()
        

    def plot(self):
        """Plot the contents of the file 'data' within the current directory"""
        path = os.path.join(self.current_directory, 'data')
        plotting.plot_file_contents(path)
        

    def set_data_directory(self):
        """Opens a dialog to choose the directory where data is located"""
        name = filedialog.askdirectory()
        if len(name) > 0:
            self.current_directory = name




if __name__ == '__main__':
    app = MyApp()
    app.run()

        
