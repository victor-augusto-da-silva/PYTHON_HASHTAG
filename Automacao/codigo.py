#1° Abrir o sistema da empresa
import pyautogui
import time 
import pandas as pd 
from dotenv import load_dotenv
import os


# Carregar o arquivo .env.local
load_dotenv(dotenv_path='.env.local')

# Acessar as variáveis
xlogin = os.getenv('X_LOGIN')
ylogin = os.getenv('Y_LOGIN')
xproduto = os.getenv('X_PRODUTO')
yproduto = os.getenv('Y_PRODUTO')
''

    #.click (clicar) .press(pressionar) . wirte(escrever) .hotkey(atalho)
pyautogui.PAUSE = 0.9 #1s
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press("win") #tecla windonws
pyautogui.write("edge")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")

#espera do site para carregar
time.sleep(3)
#2° fazer o login
#login
pyautogui.click(x=xlogin, y=ylogin)
pyautogui.click(clicks=3, interval=0.25)
pyautogui.press("del")
pyautogui.write("victor1231967@hotmail.com")

#senha
pyautogui.press("tab")
pyautogui.press("del")
pyautogui.write("senha123")

#login
pyautogui.press("tab")
pyautogui.press("enter")


#3° Improtar a base de dados
tabela = pd.read_csv("Automacao/produtos.csv")
print(tabela)

time.sleep(2)
#4 cadastrar 1 produto
for linha in tabela.index:       
    #tabela.columns -- coluna --index = linha
    pyautogui.click(x=xproduto, y=yproduto)
    #codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    #marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")
    #tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")
    #categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    #preco_unitario
    preco_unitario  = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    #custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    #obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    #enviar
    pyautogui.press("enter")
    pyautogui.scroll(1000000)
#5° repetir o passo 4 ate cadastrar todos os produtos