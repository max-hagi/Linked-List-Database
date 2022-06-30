from List import List
from tkinter import *



def main():

    global count
    count = 0

    ll = List()


    def bClick():
        global count
        count += 1
        ll.insert(count)
        label2 = Label(root, text=f"Inserted {count} to the list!")
        print(ll)
        label2.grid(row=3, column=0)

    root = Tk()
    label1 = Label(root, text="Hello There")
    button1 = Button(root, text="Click", padx=25, command=bClick)
    label1.grid(row=0, column=0)
    button1.grid(row=2, column=0)



    root.mainloop()



if __name__ == '__main__':
    main()
