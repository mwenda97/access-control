import tkinter as tk

root = tk.Tk()
canvas1 = tk.Canvas(root, width=400, height=300, relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='WELCOME TO KONZA')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='PLACE YOUR CARD ON THE READER')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 50, window=label2)

labl2 = tk.Label(root, text='card')
labl2.config(font=('helvetica', 10))
canvas1.create_window(200, 120, window=labl2)

#labl3 = tk.Label(root, text='prints')
#labl3.config(font=('helvetica', 10))
#canvas1.create_window(200, 160, window=labl3)

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)



def getSquareRoot():
    x1 = entry1.get()

    # label3 = tk.Label(root, text='the square root of ' + x1 + ' is', font=('helvetica', 10))
    # canvas1.create_window(200, 240, window=label3)

    a1 = float(x1) ** 0.5
    if a1 == 5:
        print('steve')
        label2 = tk.Label(root, text='PLACE YOUR FINGER ON THE SCANNER')
        label2.config(font=('helvetica', 10))
        canvas1.create_window(200, 50, window=label2)
        label4 = tk.Label(root, text=a1, font=('helvetica', 10, 'bold'))
        canvas1.create_window(200, 260, window=label4)
        labl2 = tk.Label(root, text='fingerprints')
        labl2.config(font=('helvetica', 10))
        canvas1.create_window(200, 120, window=labl2)
        button2 = tk.Button(text='ENTER', command=gettwo, bg='brown', fg='white', font=('helvetica', 10, 'bold'))
        canvas1.create_window(200, 220, window=button2)
        canvas1.create_window(200, 140, window=entry2)


def gettwo():
    x1 = entry2.get()

    a1 = float(x1) ** 0.5
    if a1 == 4:
        print('mwenda')
        button1 = tk.Button(text='ENTER', command=getSquareRoot, bg='brown', fg='white', font=('helvetica', 10, 'bold'))
        canvas1.create_window(200, 220, window=button1)




button1 = tk.Button(text='ENTER', command=getSquareRoot, bg='brown', fg='white', font=('helvetica', 10, 'bold'))
canvas1.create_window(200, 220, window=button1)

root.mainloop()
