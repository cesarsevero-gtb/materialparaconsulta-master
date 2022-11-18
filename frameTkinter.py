from tkinter import *

janela = Tk()
janela.title('Frame em Tk inter')
janela.geometry('500x500')
janela.resizable(False, False)

frame = Frame(janela, width=300, height=300, bg='white').grid(row=0, column=0)
Label(frame, text='Ola pessoal').grid(row=0, column=0)
janela.mainloop()
