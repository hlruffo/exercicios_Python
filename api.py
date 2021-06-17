import requests
import json
import PySimpleGUI as sg

class Tela:
    def __init__(self):
        #layout
        layout = [
            [sg.Text('Selecione a opção desejada')],
            []
            [sg.Button("Receber informação")]
        ]

        #janela
        janela = sg.Window("Cotação de moedas").layout(layout)

        #extrair dados da tela
        self.button, self.values = janela.Read()

    def Iniciar(self):
        print(sef.values)

tela = TelaPython()
tela.Iniciar()

#receber dados
cotas = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotas = cotas.json()

#botão para cota dolar
cota_bitcoin = cotas['USDBRL']['bid']
print(cota_bitcoin)
#botão pra cota euro
cota_bitcoin = cotas['EURBRL']['bid']
print(cota_bitcoin)

#botão para cota bitcoin
cota_bitcoin = cotas['BTCBRL']['bid']
print(cota_bitcoin)