import requests
import json
from tkinter import *
def information_button():
    name = text.get()
    link = f"https://api.github.com/users/{name}"
    response = requests.get(link).json()
    keys = ['company','created_at','email','id','name','url']
    response_new = {}
    for i in keys:
        response_new[i] = response[i]
    with open('information.txt','w') as file:
        json.dump(response_new,file,indent=3)
window = Tk()
window.title('Репозитории')
window.configure(background='grey')
window.geometry('300x300')
lbl = Label(window, text='Введите название репозитория', width=30, height=1, bg='grey', font=45)
lbl.grid(row=0, column=1, padx=10)
text = Entry(window, width=20)
text.grid(column=1, row=1, pady=20)
button = Button(window ,text='Получить информацию',width=30,height=1, command=information_button)
button.grid(row=3, column=1, pady=20)
window.mainloop()
