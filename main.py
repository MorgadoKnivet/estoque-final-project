from tkinter import*
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
from webbrowser import BackgroundBrowser

from PIL import Image, ImageTk

from tkcalendar import Calendar, DateEntry
from datetime import date

from view import *

# cores
co0 = "#2e2d2b" # Preta
co1 = "#feffff" # Branca
co2 = "#4fa882" # Verde
co3 = "#38576b" # Valor
co4 = "#403d3d" # Letra
co5 = "#e06636" # - Profit
co6 = "#038cfc" # Azul
co7 = "#3fbfb9" # Verde
co8 = "#263238" # + Verde
co9 = "#e9edf5" # + Verde

janela = Tk()
janela.title('Gerenciamento de Estoque')
janela.geometry('900x600')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

frameCima = Frame(janela, width=1043, height=50, bg=co1, relief=FLAT)
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=1043, height=303, bg=co1, pady=20, relief=FLAT)
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=1043, height=300, bg=co1, relief=FLAT)
frameBaixo.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)

global tree

def inserir():
    lote = e_lote.get()
    tipo = e_tipo.get()
    local = e_local.get()
    status = e_status.get()
    entrada = e_cal0.get()
    saida = e_cal1.get()
    peso = e_peso.get()

    lista_inserir = [lote, tipo, local, status, entrada, saida, peso]

    for i in lista_inserir:
        if i=='':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
        
    inserir_form(lista_inserir)
    messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

    e_lote.delete(0, 'end')
    e_tipo.delete(0, 'end')
    e_local.delete(0, 'end')
    e_status.delete(0, 'end')
    e_cal0.delete(0, 'end')
    e_cal1.delete(0, 'end')
    e_peso.delete(0, 'end')

    mostrar()

def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']

        valor = treev_lista[0]

        e_lote.delete(0, 'end')
        e_tipo.delete(0, 'end')
        e_local.delete(0, 'end')
        e_status.delete(0, 'end')
        e_cal0.delete(0, 'end')
        e_cal1.delete(0, 'end')
        e_peso.delete(0, 'end')

        id = int(treev_lista[0])
        e_lote.insert(0, treev_lista[1])
        e_tipo.insert(0, treev_lista[2])
        e_local.insert(0, treev_lista[3])
        e_status.insert(0, treev_lista[4])
        e_cal0.insert(0, treev_lista[5])
        e_cal1.insert(0, treev_lista[6])
        e_peso.insert(0, treev_lista[7])

        def update():

            lote = e_lote.get()
            tipo = e_tipo.get()
            local = e_local.get()
            status = e_status.get()
            entrada = e_cal0.get()
            saida = e_cal1.get()
            peso = e_peso.get() 

            lista_atualizar = [lote, tipo, local, status, entrada, saida, peso, id]

            for i in lista_atualizar:
                if i=='':
                    messagebox.showerror('Erro', 'Preencha todos os campos')
                    return
                
            atualizar_(lista_atualizar)
            messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')

            e_lote.delete(0, 'end')
            e_tipo.delete(0, 'end')
            e_local.delete(0, 'end')
            e_status.delete(0, 'end')
            e_cal0.delete(0, 'end')
            e_cal1.delete(0, 'end')
            e_peso.delete(0, 'end')

            b_confirmar.destroy()

            mostrar()

        b_confirmar = Button(frameMeio, command=update, width=13, text='Confirmar'.upper(), overrelief=RIDGE, font=('Ivy 8 bold'), bg=co2, fg=co1)
        b_confirmar.place(x=330, y=185)

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados na tabela')

def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0]
        
        deletar_form([valor])

        messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')

        mostrar()

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados na tabela')

app_img = Image.open('inventorio.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text=' Inventário', width=900, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co4)
app_logo.place(x=0, y=0)

l_lote = Label(frameMeio, text='Lote', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_lote.place(x=10, y=10)
e_lote = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_lote.place(x=130, y=11)

l_tipo = Label(frameMeio, text='Tipo', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_tipo.place(x=10, y=40)
e_tipo = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_tipo.place(x=130, y=41)

l_local = Label(frameMeio, text='Local', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_local.place(x=10, y=70)
e_local = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_local.place(x=130, y=71)

l_status = Label(frameMeio, text='Status', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_status.place(x=10, y=100)
e_status = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_status.place(x=130, y=101)

l_cal0 = Label(frameMeio, text='Data de Entrada', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_cal0.place(x=10, y=130)
e_cal0 = DateEntry(frameMeio, width=12, background='darkblue', bordewidth=2, year=2024)
e_cal0.place(x=130, y=131)

l_cal1 = Label(frameMeio, text='Data de Retirada', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_cal1.place(x=10, y=160)
e_cal1 = DateEntry(frameMeio, width=12, background='darkblue', bordewidth=2, year=2024)
e_cal1.place(x=130, y=161)

l_peso = Label(frameMeio, text='Peso (Kg)', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_peso.place(x=10, y=190)
e_peso = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_peso.place(x=130, y=191)

img_add = Image.open('add.png')
img_add = img_add.resize((20,20))
img_add = ImageTk.PhotoImage(img_add)

b_inserir = Button(frameMeio, command=inserir, image=img_add, width=95, text='  Adicionar'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_inserir.place(x=330, y=10)

img_atualizar = Image.open('atualizar.png')
img_atualizar = img_atualizar.resize((20,20))
img_atualizar = ImageTk.PhotoImage(img_atualizar)

b_atualizar = Button(frameMeio, command=atualizar, image=img_atualizar, width=95, text='  Atualizar'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_atualizar.place(x=330, y=50)

img_deletar = Image.open('deletar.png')
img_deletar = img_deletar.resize((20,20))
img_deletar = ImageTk.PhotoImage(img_deletar)

b_deletar = Button(frameMeio, command=deletar, image=img_deletar, width=95, text='  Deletar'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_deletar.place(x=330, y=90)

l_total = Label(frameMeio, text='', width=14, height=2, pady=5, anchor=CENTER, font=('Ivy 17 bold'), bg=co7, fg=co1)
l_total.place(x=450, y=17)
l_total_ = Label(frameMeio, text='  Quantidade total de itens  ', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co7, fg=co1)
l_total_.place(x=450, y=17)

def mostrar():
    global tree

    #Tabela Banco de Dados
    tabela_head = ['#Item','Lote', 'Tipo', 'Local', 'Status', 'Data de entrada', 'Data de retirada', 'Peso']
    lista_itens = ver_form()

    tree = ttk.Treeview(frameBaixo, selectmode="extended",columns=tabela_head, show="headings")
    vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameBaixo.grid_rowconfigure(0, weight=12)

    hd=["center","center","center","center","center","center","center", 'center']
    h=[40,150,100,160,130,100,100, 100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1

    for item in lista_itens:
        tree.insert('', 'end', values=item)

    quantidade = []

    for iten in lista_itens:
        quantidade.append(iten[6])

    Total_itens = len(quantidade)
    l_total['text'] = Total_itens

mostrar()

janela.mainloop()