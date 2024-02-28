#importando biblioteca
import pyautogui
import time

#criando a variavel lista
lista = 'lista'

#recebendo a lista
for c in range(0, 10):
    pessoas = str(input('qual o seu nome?'))

    #ogranizando a lista
    lista = lista + ('\n {} \n'.format(pessoas))

#acessando o bloco de notas
pyautogui.press("win")
time.sleep(2)
pyautogui.write('bloco de notas')
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)

#escrevendo a lista
pyautogui.write(lista)