from gui import *

# window = Tk()
# mywin = MyWindow(window)
# window.mainloop()

tmp = []
tmp.append(random.choice(list(range(1, 30))))
tmp.append(random.choice(list(range(1, 30))))

a = max(tmp)
b = min(tmp)

print(a,b)