import pyautogui
import time
import pandas

pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(2)

pyautogui.click(x=521, y=414)

pyautogui.write("nedson@gmail.com")
pyautogui.press("tab")
pyautogui.write("password")
pyautogui.press("enter")
time.sleep(2)

table = pandas.read_csv("produtos.csv")
print(table)

for linha in table.index:

    pyautogui.click(x=415, y=294)
    codigo = table.loc[linha, "codigo"]

    pyautogui.write(codigo)
    pyautogui.press("tab")

    pyautogui.write(table.loc[linha, "marca"])
    pyautogui.press("tab")

    pyautogui.write(table.loc[linha, "tipo"])
    pyautogui.press("tab")

    pyautogui.write(str(table.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(table.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(table.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = table.loc[linha, "obs"]
    if not pandas.isna(obs):
         pyautogui.write(obs)
    
    pyautogui.press("tab")
    pyautogui.press("enter")
    
    pyautogui.scroll(5000)


