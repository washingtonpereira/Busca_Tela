import PySimpleGUI as sg
import requests
import json
import time

__author__ = 'Washington Luis de Assis Pereira'


layout = [
      [sg.Text("Digite o Cep",size=(12,1)),sg.In(size=(20,1),key='cep')],
      [sg.Output(size=(25, 5))],
      [sg.Button("Search"),sg.Exit()]
 ]


janela = sg.Window("Cep", layout, size=(200, 150), element_justification='right')

while True:
    event, values = janela.read(timeout=0)

    if event == 'Search':
        cep = str(values['cep'])
        req = requests.get('https://cep.awesomeapi.com.br/json/' + cep)
        ceq= json.loads(req.text)
        if req.status_code == 200:
            print("Cep:", ceq["cep"])
            print("Estado:", ceq["state"])
            print("Cidade:", ceq["city"])
            print("Rua:", ceq["address_name"])
            print("Bairro:", ceq["district"])
            print(time.ctime())
        if req.status_code >399:
            print("Cep não existe ou foram digitados/"
                  " letras ou numeros com pontos, o cep deve ser digitado com 8 numeros sequencias. ")
            janela['cep'].update("")

    if event == sg.WIN_CLOSED or event == 'Exit':
         break

janela.close()