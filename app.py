import PySimpleGUI as sg
from sistemas.validacoes import Validar as v
from sistemas.telas import Telas as t


tela1 = t.tela1()

while True:
    janela, evento, valor = sg.read_all_windows()

    if evento == sg.WIN_CLOSED:
        break
    
    if evento == '-CEP-':
        t.mostrar_cep(janela)
        
    if evento == '-RASTREIO-':
        t.mostrar_rastreio(janela)
    
    if evento == '-PESQUISAR-':
        v.validar_input_cep(valor, janela)