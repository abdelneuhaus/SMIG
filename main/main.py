from gui import *

window = Tk()
mywin = MyWindow(window)
window.iconphoto(False, PhotoImage(file='logo.png'))
window.title("Single Molecule Image Generator")
window.mainloop()