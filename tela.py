from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk



## cores ---------------------

co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#3fbfb9"   # verde
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde
co10 ="#6e8faf"  # 
co11 = "#f2f4f2"

## criando janela

janela = Tk()
janela.title("Dicionario")
janela.geometry("350x415")
janela.configure(background = co1)
janela.resizable(width = False , height = False)


##Frames

frameTop = Frame(janela, width = 350.,height = 50, bg = co1, relief = "flat")
frameTop.grid(row = 0, column = 0)

frameMid = Frame(janela, width = 350, height = 90, bg = co1, relief = "solid")
frameMid.grid(row = 1, column = 0)

frameBot = Frame(janela, width = 350, height = 290, bg = co1, relief = "raised")
frameBot.grid(row = 2, column = 0)

## abrindo a imagem logo

app_img = Image.open("logo.png")
app_img = app_img.resize((40,40))
app_img = ImageTk.PhotoImage(app_img)

## logo

app_logo = Label(frameTop, image = app_img, width = 900, compound = LEFT, padx = 5, relief = FLAT, anchor = NW, bg = co1, fg= co4)
app_logo.place(x = 5, y = 0)

## texto do cabecalho

app_cabecalho = Label(frameTop, text = "Dicionario", compound = LEFT, padx = 5, relief = FLAT, anchor = NW, font = ("Verdana 20"), bg = co1, fg = co4)
app_cabecalho.place(x = 50, y = 0)

## linha de separacao do cabecalho 

l_linha = Label(frameTop, width = 395, height = 1, anchor = NW, font = ("Verdana 1"), bg = co3, fg = co1)
l_linha.place(x = 0, y = 47)


## frame mid 
## campo de busca

l_palavra = Label(frameMid, text = "Digite a palavra", height = 1, anchor = NW, font = ("Ivy 10"), bg = co1, fg = co4)
l_palavra.place(x = 7, y = 15)
e_palavra = Entry(frameMid, width = 18, font = ("Ivy 14"), justify = "left", relief = "solid")
e_palavra.place(x = 10, y = 41)


## botao de busca

img_procurar = Image.open("find.png")
img_procurar = img_procurar.resize((20,20))
img_procurar = ImageTk.PhotoImage(img_procurar)
b_procurar = Button(frameMid, image = img_procurar, compound = LEFT, width = 100, text = "  Procurar", bg = co1, fg = co0, font= ("Ivy 11"), overrelief = RIDGE)
b_procurar.place( x = 230, y = 40)

janela.mainloop()