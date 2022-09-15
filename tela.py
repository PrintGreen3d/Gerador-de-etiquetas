import time
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from typing import Type
from bancoSqlLite import *
from relatorio import *


def verificaLista(listaOrigem):
    for i in range(len(listaOrigem)):
        if (len(listaOrigem[i]) == 0):
            return False
    return True


def limpaCampos(self):
    self.t1.delete('0', END)
    self.cb_material.delete(0, END)
    self.cb_cor.delete(0, END)
    self.cb_diametro.delete(0, END)
    self.cb_mesa.delete(0, END)
    self.cb_bico.delete(0, END)
    self.CheckVar1.set(0)
    self.CheckVar2.set(0)
    self.CheckVar3.set(0)
    self.CheckVar4.set(0)
    self.CheckVar5.set(0)
    self.CheckVar6.set(0)


def montaOrigem(listOrigem):
    origem = []
    if (listOrigem[0] == 1):
        origem.append(" I3D ")
    if (listOrigem[1] == 1):
        origem.append(" Coop ")
    if (listOrigem[2] == 1):
        origem.append(" Auto ")
    if (listOrigem[3] == 1):
        origem.append(" Linha Branca ")
    if (listOrigem[4] == 1):
        origem.append(" Eletronicos ")
    if (listOrigem[5] == 1):
        origem.append(" GB ")

    return ''.join(origem)


class MyWindow:
    def __init__(self, win):
        self.lbl1 = Label(win, text='Quantidade')
        self.lbl1.place(x=15, y=10)

        self.lbl4 = Label(win, text='Material')
        self.lbl4.place(x=170, y=10)

        self.lbl2 = Label(win, text='Cor')
        self.lbl2.place(x=15, y=60)

        self.lbl3 = Label(win, text='Diametro')
        self.lbl3.place(x=170, y=60)

        self.lbl5 = Label(win, text='Temp. Mesa')
        self.lbl5.place(x=15, y=110)

        self.lbl6 = Label(win, text='Temp. Bico')
        self.lbl6.place(x=170, y=110)

        self.lbl7 = Label(win, text='Origem do Material:')
        self.lbl7.place(x=15, y=160)

        self.t1 = Entry(width="10", bd=3)
        self.btn1 = Button(win, text='Salva')
        self.btn2 = Button(win, text='Gerar')
        self.btn3 = Button(win, text='Cancelar')
        self.t1.place(x=15, y=30)

        # self.t2.place(x=200, y=100)
        self.b1 = Button(win, text='Salvar', width="8", command=self.add)
        self.b2 = Button(win, text='Gerar', width="8")
        self.b3 = Button(win, text='Cancelar', width="8")

        self.b2.bind('<Button-1>', self.sub)
        self.b3.bind('<Button-1>', self.close_win)

        self.b1.place(x=20, y=300)
        self.b2.place(x=120, y=300)
        self.b3.place(x=220, y=300)

        var = StringVar()
        var.set("ABS")
        data = ("ABS", "PLA", "PETg")
        self.cb_material = Combobox(win, width="15", values=data)
        self.cb_material.place(x=170, y=30)

        cor_var = StringVar()
        cor_var.set(" ")
        cor_data = ("Preto", "Branco", "Azul", "Verde",
                    "Roxo", "Vermelho", "Cinza")
        self.cb_cor = Combobox(win, width="15", values=cor_data)
        self.cb_cor.place(x=15, y=80)

        cor_var = StringVar()
        cor_var.set(" ")
        cor_data = ("1.75 mm", "2.85 mm")
        self.cb_diametro = Combobox(win, width="15", values=cor_data)
        self.cb_diametro.place(x=170, y=80)

        cor_var = StringVar()
        cor_var.set(" ")
        cor_data = ("110º", "70º", "80º")
        self.cb_mesa = Combobox(win, width="15", values=cor_data)
        self.cb_mesa.place(x=15, y=130)

        cor_var = StringVar()
        cor_var.set(" ")
        cor_data = ("220º - 240º", "180º ~ 220º", "235º - 260º")
        self.cb_bico = Combobox(win, width="15", values=cor_data)
        self.cb_bico.place(x=170, y=130)

        self.CheckVar1 = IntVar()
        self.CheckVar2 = IntVar()
        self.CheckVar3 = IntVar()
        self.CheckVar4 = IntVar()
        self.CheckVar5 = IntVar()
        self.CheckVar6 = IntVar()

        self.Button1 = Checkbutton(window, text="I3D",
                                   variable=self.CheckVar1,
                                   onvalue=1,
                                   offvalue=0,
                                   height=2,
                                   width=10)

        self.Button2 = Checkbutton(win, text="Coop",
                                   variable=self.CheckVar2,
                                   onvalue=1,
                                   offvalue=0,
                                   height=2,
                                   width=10)

        self.Button3 = Checkbutton(win, text="Auto",
                                   variable=self.CheckVar3,
                                   onvalue=1,
                                   offvalue=0,
                                   height=2,
                                   width=10)

        self.Button4 = Checkbutton(win, text="Linha Branca",
                                   variable=self.CheckVar4,
                                   onvalue=1,
                                   offvalue=0,
                                   height=2,
                                   width=10)

        self.Button5 = Checkbutton(win, text="Eletronicos",
                                   variable=self.CheckVar5,
                                   onvalue=1,
                                   offvalue=0,
                                   height=2,
                                   width=10)

        self.Button6 = Checkbutton(win, text="GB",
                                   variable=self.CheckVar6,
                                   onvalue=1,
                                   offvalue=0,
                                   height=2,
                                   width=10)

        self.Button1.place(x=0, y=180)  # i#D
        self.Button3.place(x=3, y=210)  # AUTO
        self.Button5.place(x=23, y=240)  # Eletronicos
        self.Button2.place(x=135, y=180)
        self.Button4.place(x=160, y=210)
        self.Button6.place(x=125, y=240)

    def add(self):
        listDadosLote = []
        listOrigem = []
        try:
            listDadosLote.append(self.t1.get())
            listDadosLote.append(self.cb_material.get())
            listDadosLote.append(self.cb_cor.get())
            listDadosLote.append(self.cb_diametro.get())
            listDadosLote.append(self.cb_mesa.get())
            listDadosLote.append(self.cb_bico.get())
            listOrigem.append(self.CheckVar1.get())
            listOrigem.append(self.CheckVar2.get())
            listOrigem.append(self.CheckVar3.get())
            listOrigem.append(self.CheckVar4.get())
            listOrigem.append(self.CheckVar5.get())
            listOrigem.append(self.CheckVar6.get())
            listDadosLote.append(montaOrigem(listOrigem))

            if (listDadosLote[1] == 'ABS'):
                listDadosLote.append(str('Akie'))
            elif (listDadosLote[1] == 'PLA'):
                listDadosLote.append(str('Emi'))
            else:
                listDadosLote.append(str('Hitomi'))

            if verificaLista(listDadosLote) is False:
                messagebox.showerror("Erro", "Nem todos os campos foram \
                                   preenchidos")
            else:
                insertBanco(listDadosLote)
                time.sleep(2)
                finalId = ultimaPosicaoSql()
                listaCodigos = adicionaIdCodigoBarras(finalId, listDadosLote)
                updateCodigoBarras(listaCodigos)
                time.sleep(2)
                messagebox.showinfo("INCLUSÂO", "Dados Inseridos com \
                    sucesso!!")
        except Exception:
            print("problemas em inserir novos dados")
            traceback.print_exc()
            desfazTudo()
            messagebox.showerror("INCLUSÂO", "Os dados não foram inseridos!")

        # Limpeza dos campos
        limpaCampos(self)

    def sub(self, event):
        try:
            abreBanco()
            finalId = ultimaPosicaoSql()
            listaLote = buscaDadosUltimaPosicao(finalId)
            montaLogo(listaLote)
            time.sleep(2)
            abrePDF()
        except Exception:
            messagebox.showerror("Listagem", "Não foram listado corretamente!")
            traceback.print_exc()
            con.rollback()

    def close_win(self, event):
        window.destroy()
        fechaBanco()


window = Tk()
mywin = MyWindow(window)
window.title('Gerador de Etiquetas')
window.geometry("350x350+10+20")
window.mainloop()
