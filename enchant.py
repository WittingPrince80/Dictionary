from tkinter import*
import random

root=Tk()
root.title("Dictionary")
root.geometry("600x600")


random = Label(root)

dictionary = {'Colour': 'maroon1',
              'Colour': "lawn green",
              'Colour': "magenta2",
              'Colour': "purple1",
              'Colour':"springgreen2",
              'Colour':"chocolate1",
              'Colour':"deep pink",
              'Colour':"cyan"
              }
def enchant():
  
   col = random.randint(0,7)
   print(dictionary[col])  
    
   btn = Button(root,text = "Colours",command = enchant)
   btn.place(relx = 0.5, rely = 0.2, anchor = CENTER)
   
    
   
    root.mainloop()


