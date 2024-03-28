import tkinter

def change_text():
    if button.cget('text') == 'Click Me':
        button.config(text='Clicked')
    else:
        button.config(text='Click Me')

root = tkinter.Tk()
root.title('Button Clicker')
root.geometry('640x480')

button = tkinter.Button(root, text='Click Me', command=change_text)

button.pack(expand=False, fill='none', padx=20, pady=20)

# add a smiley face (jpg)
smiley = tkinter.PhotoImage(file='smiley.png')
label = tkinter.Label(root, image=smiley)

# resize image to 300x300
smiley = smiley.subsample(10, 10)
label = tkinter.Label(root, image=smiley)

label.pack()

root.mainloop()
