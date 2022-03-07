import PySimpleGUI as sg
from sistemas.telas import Telas as t
from sistemas.funcoes import Funcoes as f


tela1 = t.tela1()

while True:
    janela, evento, valor = sg.read_all_windows()

    if evento == sg.WIN_CLOSED:
        break
    
    if evento == '-CEP-':
        f.mostrar_cep(janela)
        
    if evento == '-RASTREIO-':
        f.mostrar_rastreio(janela)
    
    if evento == '-PESQUISAR-':
        f.dados_cep(valor)
        f.exibir_dados_cep(valor, janela)