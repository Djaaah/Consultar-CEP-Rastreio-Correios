import PySimpleGUI as sg
from sistemas.validacoes import Validar as v
from sistemas.telas import Telas as t
import pandas as pd
from prettytable import PrettyTable as pt

tela1 = t.tela1()

while True:
    janela, evento, valor = sg.read_all_windows()
    
    if evento == sg.WIN_CLOSED:
        break
    
    if evento == '-CEP-':
        t.mostrar_cep(janela)
        
    if evento == '-RASTREIO-':
        t.mostrar_rastreio(janela)
    
    if evento == '-PESQUISAR_CEP-':
        v.validar_input_cep(valor, janela)
        
    if evento == '-PESQUISAR_RASTREIO-':
        janela['-DADOS_RASTREIO-'].update("")
        dados = [['2021-12-11 08:56:45', 'Objeto entregue ao destinatário', 'OLINDA', 'PE', 'Unidade de Distribuição', 1, 'ENCOMENDA PAC', 'ETIQUETA LOGICA PAC QI'], ['2021-12-11 07:08:43', 'Objeto saiu para entrega ao destinatário', 'OLINDA', 'PE', 'Unidade de Distribuição', 1, 'ENCOMENDA PAC', 'ETIQUETA LOGICA PAC QI'], ['2021-12-09 00:47:25', 'Objeto em trânsito - por favor aguarde', 'RECIFE', 'PE', 'Unidade de Tratamento', 1, 'ENCOMENDA PAC', 'ETIQUETA LOGICA PAC QI'], ['2021-12-04 05:50:09', 'Objeto em trânsito - por favor aguarde', 'CAJAMAR', 'SP', 'Unidade de Tratamento', 1, 'ENCOMENDA PAC', 'ETIQUETA LOGICA PAC QI'], ['2021-12-01 10:10:47', 'Objeto em trânsito - por favor aguarde', 'SANTO ANDRE', 'SP', 'Agência dos Correios', 1, 'ENCOMENDA PAC', 'ETIQUETA LOGICA PAC QI'], ['2021-11-30 17:17:09', 'Objeto postado após o horário limite da unidade', 'SANTO ANDRE', 'SP', 'Agência dos Correios', 1, 'ENCOMENDA PAC', 'ETIQUETA LOGICA PAC QI']]
        # dados = pd.DataFrame(dados, columns=["Data do Evento", "Evento", "Local", "Estado", "Unidade", "Qtd. Pacotes", "Tipo de Envio", "Etiqueta"])
        qtd_registros = len(dados)
        dados_finais = pt(["Data do Evento", "Evento", "Local", "Estado", "Unidade", "Qtd. Pacotes", "Tipo de Envio", "Etiqueta"])
        
        
        
        
        for i in range(qtd_registros):
            dados_finais.add_row((dados[i]))
        
        
        print(dados_finais)
        
        

        