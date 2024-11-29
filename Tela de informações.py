from eucalipto import Eucalipto
from pinus import Pinus
from descricoes import*
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk




"""função de criação de objetos"""
lista=[]


   
def cadastraMadeira():
   
    tipo=entryTipo.get()
    peso=entryPeso.get()
    preco=entryPreco.get()
    data=entryData.get()


    
   
    erro=0
    
    if tipo=="Eucalipto": 
        
        if tipo=="":
           
           messagebox.showinfo("Erro", "Preencha o cadastro")
           erro=1

        if erro==0:
            
           e=Eucalipto(tipo, peso, preco, data)
           salvar(e)
           messagebox.showinfo("Cadastro", f"{tipo} Cadastro concluído com sucesso!")

        if peso=="":
          
           messagebox.showinfo("Erro", "Preencha o cadastro")
           erro=1
        if erro==0:
           e=Eucalipto(tipo, peso, preco, data)
           salvar(e)
           messagebox.showinfo("Cadastro", f"{tipo} Cadastro concluído com sucesso!")

        if preco=="":
           messagebox.showinfo("Erro", "Preencha o cadastro")
           erro=1
        if erro==0:
           e=Eucalipto(tipo, peso, preco, data)
           salvar(e)
           messagebox.showinfo("Cadastro", f"{tipo} Cadastro concluído com sucesso!")
           lista.append(e)
           

        






    else:
        if tipo=="":
           
           messagebox.showinfo("Erro", "Preencha o cadastro")
           erro=1

        if erro==0:
           
           p=Pinus(tipo, peso, preco, data)
           salvar(p)
           

        if peso=="":
           
           messagebox.showinfo("Erro", "Preencha o cadastro")
           erro=1
        if erro==0:
            p=Pinus(tipo, peso, preco, data)
            salvar(p)
      

        if preco=="":
           
           messagebox.showinfo("Erro", "Preencha o cadastro")
           erro=1
        if erro==0:
           p=Pinus(tipo, peso, preco, data)
           salvar(p)
           messagebox.showinfo("Cadastro", f"{tipo} Cadastro concluído com sucesso!")
           lista.append(e)
           

def salvar(obj):
    lista.append(obj)

def atualizaListabox():
    listbox.delete(0, tk.END)
    for obj in lista:
        listbox.insert(tk.END, obj.mostrar())



        

    





janela = tk.Tk()
janela.title("Cadastro de Madeira")
janela.geometry("500x300")

janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(0, weight=1)

janelinha = ttk.Notebook(janela)
janelinha.grid(row=0, column=0, sticky="nsew")

tab1 = ttk.Frame(janelinha)
for i in range(6):
    tab1.grid_rowconfigure(i, weight=1)
tab1.grid_columnconfigure(0, weight=1)
tab1.grid_columnconfigure(1, weight=1)

tab2=ttk.Frame(janelinha)
tab2.grid_rowconfigure(0, weight=1)
tab2.grid_columnconfigure(0,weight=1)

janelinha.add(tab1, text="Adicionar")
janelinha.add(tab2, text="Lista")

label1=tk.Label(tab1, text="Data", font=("",15))      #data
label1.grid(row=0, column=0, sticky="w", padx=10)

entryData=tk.Entry(tab1, font=("", 15))                         
entryData.grid(row=0, column=1, sticky="nsew", padx=10, pady=5)

label2=tk.Label(tab1, text="Tipo de Madeira", font=("",15))                   
label2.grid(row=1, column=0, sticky="w", padx=10)

entryTipo=tk.Entry(tab1, font=("", 15))
entryTipo.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)

label3=tk.Label(tab1, text="Peso", font=("",15))                   # Peso
label3.grid(row=2, column=0, sticky="w", padx=10)

entryPeso=tk.Entry(tab1, font=("", 15))
entryPeso.grid(row=2, column=1, sticky="nsew", padx=10, pady=5)

label4=tk.Label(tab1, text="Preço", font=("",15))      #Preço
label4.grid(row=3, column=0, sticky="w", padx=10)

entryPreco=tk.Entry(tab1, font=("", 15))
entryPreco.grid(row=3, column=1, sticky="nsew", padx=10, pady=5)




tk.Label(tab1, text="Espessura", font=("", 15, ))
varTipo = tk.StringVar(value="Eucalipto")

tk.Radiobutton(tab1, text="Grossa", font=("", 15, ), variable=varTipo, value="Grossa").grid(row=4, column=2, sticky="w", padx=10)

tk.Radiobutton(tab1, text="Média", font=("", 15, ), variable=varTipo, value="Média").grid(row=4, column=1, sticky="we", padx=10)

tk.Radiobutton(tab1, text="Fina", font=("", 15, ), variable=varTipo, value="Fina").grid(row=4, column=1, sticky="w", padx=10)



tk.Button(tab1, text="Salvar", font=("", 15), command=cadastraMadeira).grid(row=5, columnspan=2)



######################################################################################


listbox=tk.Listbox(tab2)
listbox.config(font=("", 15))
listbox.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)



tk.Button(tab2, text="Atualizar", font=("", 15), command=atualizaListabox).grid(row=1, column=0)

janela.mainloop()