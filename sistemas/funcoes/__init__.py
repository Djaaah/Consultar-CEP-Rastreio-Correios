import PySimpleGUI as sg
import requests as r


class Funcoes:
    def exibir_dados_cep(valor, janela):
        from sistemas.validacoes import Validar as v
        janela['-LOGRADOURO-'].update(v.validar_dados_cep(valor)[0]); janela['-ESTADO-'].update(v.validar_dados_cep(valor)[4])
        janela['-COMPLEMENTO-'].update(v.validar_dados_cep(valor)[1]); janela['-CIDADE-'].update(v.validar_dados_cep(valor)[3])
        janela['-BAIRRO-'].update(v.validar_dados_cep(valor)[2]); janela['-COD.IBGE_CIDADE-'].update(v.validar_dados_cep(valor)[5])
        
    def dados_rastreio(valor):
        cod_rastreio = valor['-COD_RASTREIO_DESEJADO-']
    
    
    
    
    