from tkinter import Tk, Button, Entry, Label, messagebox
from tkinter.ttk import Combobox
import listas


LEFT = 70
fonte = ("Arial", 14, "bold")
class Window:

    def __init__(self, window):
        self.cadastrados = ['Jose da Silva', 'Joao da Silva']

        self.lbl_pessoas=Label(window, text="Pessoas: ", font=fonte)
        self.lbl_pessoas.place(x=LEFT, y=50)
        self.combo = Combobox(window, values=self.cadastrados, font=fonte)
        self.combo.place(x=LEFT+90, y=50)

        self.lbl_nome=Label(window, text="Nome: ", font=fonte)
        self.lbl_nome.place(x=LEFT, y=100)
        self.txtfld=Entry(window, text="Nome", bd=1, font=fonte)
        self.txtfld.place(x=LEFT+90, y=100)

        self.adicionar_botoes(window)

    def adicionar_botoes(self, window):
        self.btn_add = Button(window, text="Adicionar", command=self.inserir, font=fonte)
        self.btn_add.place(x=LEFT, y=150)

        self.btn_remover = Button(window, text="Remover", command=self.remover, font=fonte)
        self.btn_remover.place(x=LEFT+130, y=150)

        self.btn_buscar = Button(window, text="Buscar", command=self.buscar, font=fonte)
        self.btn_buscar.place(x=LEFT+250, y=150)

        self.btn_limpar = Button(window, text="Limpar", command=self.limpar, font=fonte)
        self.btn_limpar.place(x=LEFT, y=200)

        self.btn_ordenar = Button(window, text="Ordenar", command=self.ordenar, font=fonte)
        self.btn_ordenar.place(x=LEFT+100, y=200)

        self.btn_tamanho = Button(window, text="Quantidade", command=self.mostrar_quantidade, font=fonte)
        self.btn_tamanho.place(x=LEFT+220, y=200)

        self.btn_maiusculo = Button(window, text="Converter Maiúsculo", command=self.deixar_maiusculo, font=fonte)
        self.btn_maiusculo.place(x=LEFT, y=250)

        self.btn_repetidos = Button(window, text="Remover Repetidos", command=self.remover_repetidos, font=fonte)
        self.btn_repetidos.place(x=LEFT+220, y=250)

    def mostrar_quantidade(self):
        quantidade = listas.pegar_quantidade(self.cadastrados)
        messagebox.showinfo(title="Sucesso", message=f"Há {quantidade} elementos na lista")

    def inserir(self):
        if not self.txtfld.get():
            messagebox.showwarning(title="Falha", message="Campo nome vazio")
            return
        sucesso = listas.adicionar_elemento(self.cadastrados, self.txtfld.get())
        if sucesso:
            self.combo.delete(0, "end")
            self.combo['values'] = self.cadastrados
            messagebox.showinfo(title="Sucesso", message="Nome inserido com sucesso")
        else:
            messagebox.showwarning(title="Falha", message="Nome inválido")

    def remover(self):
        sucesso = listas.remover_elemento(self.cadastrados, self.txtfld.get())
        if sucesso:
            self.combo.delete(0, "end")
            self.combo['values'] = self.cadastrados
            messagebox.showinfo(title="Sucesso", message="Nome removido com sucesso")
        else:
            messagebox.showwarning(title="Falha", message="Nome não encontrado")

    def limpar(self):
        listas.limpar_lista(self.cadastrados)
        self.combo.delete(0, "end")
        self.combo['values'] = self.cadastrados
        messagebox.showinfo(title="Sucesso", message="Todos os nomes apagados")

    def buscar(self):
        sucesso = listas.buscar_elemento(self.cadastrados, self.txtfld.get())
        if sucesso:
            # mudar combobox
            messagebox.showinfo(title="Sucesso", message="Nome encontrado")
        else:
            messagebox.showwarning(title="Falha", message="Nome não encontrado")

    def deixar_maiusculo(self):
        if self.cadastrados:
            self.cadastrados = listas.converter_maiusculo(self.cadastrados)
            messagebox.showinfo(title="Sucesso", message="Nomes convertidos para maiúsculo")
            self.combo['values'] = self.cadastrados
        else:
            messagebox.showwarning(title="Falha", message="Lista vazia")

    def ordenar(self):
        if self.cadastrados:
            listas.ordenar_lista(self.cadastrados)
            self.combo['values'] = self.cadastrados
            messagebox.showinfo(title="Sucesso", message="Itens ordenados")
        else:
            messagebox.showwarning(title="Falha", message="Lista vazia")

    def remover_repetidos(self):
        if self.cadastrados:
            self.cadastrados = listas.eliminar_repetidos(self.cadastrados)
            self.combo['values'] = self.cadastrados
            messagebox.showinfo(title="Sucesso", message="Repetições removidas")
        else:
            messagebox.showwarning(title="Falha", message="Lista vazia")


window=Tk()
objWindow = Window(window)

window.title('Hello Python')
window.geometry("500x500+10+20")
window.mainloop()