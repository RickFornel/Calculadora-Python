# importando tkinter

from tkinter import *
from tkinter import ttk


# cores

cinza = "#877776"
preto = "#0a0a0a"
laranja = "#db8802"
branco = "#fafafa"

# criando janela

janela =Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(bg=preto)

# criando frames

frame_tela = Frame(janela, width=235, height=50, bg=cinza)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268, bg=preto)
frame_corpo.grid(row=1, column=0)

todos_valores = ''
valor_texto = StringVar()

#criando função

def entrar_valores(event):
    global todos_valores
    todos_valores = todos_valores+str(event)
    valor_texto.set(todos_valores)

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(resultado)
    todos_valores = ""

def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")
    

#criando label

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=preto, fg=branco)
app_label.place(x=0, y=0)

# criando botoes
# linha 1
b_1 = Button(frame_corpo, command= limpar_tela, text="C", width=11, height=2, bg=cinza, fg=preto, font=('Ivy 13 bold'), overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, command= lambda: entrar_valores('%'), text="%", width=5, height=2, bg=cinza, fg=preto, font=('Ivy 13 bold'), overrelief=RIDGE)
b_2.place(x=120, y=0)
b_3 = Button(frame_corpo, command= lambda: entrar_valores('/'), text="/", width=5, height=2, bg=laranja, fg=branco, font=('Ivy 13 bold'), overrelief=RIDGE)
b_3.place(x=180, y=0)
# linha 2
b_4 = Button(frame_corpo, command= lambda: entrar_valores('7'), text="7", width=5, height=2, bg=cinza, fg=preto, font=('Ivy 13 bold'), overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(frame_corpo, command= lambda: entrar_valores('8'), text="8", width=5, height=2, bg=cinza, fg=preto, font=('Ivy 13 bold'), overrelief=RIDGE)
b_5.place(x=60, y=52)
b_6 = Button(frame_corpo, command= lambda: entrar_valores('9'), text="9", width=5, height=2, bg=cinza, fg=preto, font=('Ivy 13 bold'), overrelief=RIDGE)
b_6.place(x=120, y=52)
b_7 = Button(frame_corpo, command= lambda: entrar_valores('*'), text="x", width=5, height=2, bg=laranja, fg=branco, font=('Ivy 13 bold'), overrelief=RIDGE)
b_7.place(x=180, y=52)
# linha 3
b_8 = Button(frame_corpo, command= lambda: entrar_valores('4'), text="4", width=5, height=2, bg=cinza, fg=preto, font=('Ivy 13 bold'), overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button(frame_corpo, command= lambda: entrar_valores('5'), text="5", width=5, height=2, bg=cinza, fg=preto, font=('Ivy 13 bold'), overrelief=RIDGE)
b_9.place(x=60, y=104)
b_10 = Button(frame_corpo, command= lambda: entrar_valores('6'), text="6", width=5, height=2, bg=cinza, fg=preto, font=('Ivy 13 bold'), overrelief=RIDGE)
b_10.place(x=120, y=104)
b_11 = Button(frame_corpo, command= lambda: entrar_valores('-'), text="-", width=5, height=2, bg=laranja, fg=branco, font=('Ivy 13 bold'), overrelief=RIDGE)
b_11.place(x=180, y=104)
# linha 4
b_12 = Button(frame_corpo, command= lambda: entrar_valores('1'), text="1", width=5, height=2, bg=cinza, fg=preto, font=('Ivy 13 bold'), overrelief=RIDGE)
b_12.place(x=0, y=156)
b_13 = Button(frame_corpo, command= lambda: entrar_valores('2'), text="2", width=5, height=2, bg=cinza, fg=preto, font=('Ivy 13 bold'), overrelief=RIDGE)
b_13.place(x=60, y=156)
b_14 = Button(frame_corpo, command= lambda: entrar_valores('3'), text="3", width=5, height=2, bg=cinza, fg=preto, font=('Ivy 13 bold'), overrelief=RIDGE)
b_14.place(x=120, y=156)
b_15 = Button(frame_corpo, command= lambda: entrar_valores('+'), text="+", width=5, height=2, bg=laranja, fg=branco, font=('Ivy 13 bold'), overrelief=RIDGE)
b_15.place(x=180, y=156)
# linha 5
b_16 = Button(frame_corpo, command= lambda: entrar_valores('0'), text="0", width=11, height=2, bg=cinza, fg=preto, font=('Ivy 13 bold'), overrelief=RIDGE)
b_16.place(x=0, y=208)
b_17 = Button(frame_corpo, command= lambda: entrar_valores('.'), text=".", width=5, height=2, bg=cinza, fg=preto, font=('Ivy 13 bold'), overrelief=RIDGE)
b_17.place(x=120, y=208)
b_18 = Button(frame_corpo, command= calcular, text="=", width=5, height=2, bg=laranja, fg=branco, font=('Ivy 13 bold'), overrelief=RIDGE)
b_18.place(x=180, y=208)



janela.mainloop()