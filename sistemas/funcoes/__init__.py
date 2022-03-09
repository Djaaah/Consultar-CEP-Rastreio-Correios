import PySimpleGUI as sg
import requests as r
import sistemas.validacoes as v

class Funcoes:
    def exibir_dados_cep(valor, janela):
        janela['-LOGRADOURO-'].update(v.Validar.validar_dados_cep(valor)[0]); janela['-ESTADO-'].update(v.Validar.validar_dados_cep(valor)[4])
        janela['-COMPLEMENTO-'].update(v.Validar.validar_dados_cep(valor)[1]); janela['-CIDADE-'].update(v.Validar.validar_dados_cep(valor)[3])
        janela['-BAIRRO-'].update(v.Validar.validar_dados_cep(valor)[2]); janela['-COD.IBGE_CIDADE-'].update(v.Validar.validar_dados_cep(valor)[5])
        
    def dados_rastreio(valor):
        cod_rastreio = valor['-COD_RASTREIO_DESEJADO-']
    
    
    
    
    