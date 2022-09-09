from tkinter import *


def main():
    window = Tk()
    window.title('Kilometers <--> Miles Converter')
    window.config(padx=20,pady=20)


    def miles2kilo():
        miles = miles_input.get()
        kilo = float(miles)*1.609344
        kilo_input.insert(0,str(kilo))
    
    def kilo2miles():
        kilo = kilo_input.get()
        miles = float(kilo)*0.62137119
        miles_input.insert(0,str(miles))
    
    kilometers = Label(text='Kilometers')
    kilometers.grid(column=1,row=3)
    m2k_button = Button(text='Miles to Kilometers',command=miles2kilo)
    m2k_button.grid(column=3,row=2)
    k2m_button = Button(text='Kilometers to miles',command=kilo2miles)
    k2m_button.grid(column=3,row=3)
    input_label = Label(text='Miles')
    input_label.grid(column=1,row=2)
    kilo_input = Entry(width=10)
    kilo_input.grid(column=2,row=3)
    miles_input = Entry(width=10)
    miles_input.grid(column=2,row=2)    
    window.mainloop() 

if __name__ == "__main__":
    main()