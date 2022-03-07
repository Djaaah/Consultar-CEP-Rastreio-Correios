import PySimpleGUI as sg
import requests as r

class Funcoes:
    def exibir_dados_cep(valor, janela):
        janela['-LOGRADOURO-'].update(Funcoes.dados_cep(valor)[0]); janela['-ESTADO-'].update(Funcoes.dados_cep(valor)[4])
        janela['-COMPLEMENTO-'].update(Funcoes.dados_cep(valor)[1]); janela['-CIDADE-'].update(Funcoes.dados_cep(valor)[3])
        janela['-BAIRRO-'].update(Funcoes.dados_cep(valor)[2]); janela['-COD.IBGE_CIDADE-'].update(Funcoes.dados_cep(valor)[5])
        
    def dados_cep(valor):
        CEP = valor['-CEP_DESEJADO-']
        dados = r.get(f'http://viacep.com.br/ws/{CEP}/json/').json()
        logradouro = dados['logradouro']
        complemento = dados['complemento']
        bairro = dados['bairro']
        cidade = dados['localidade']
        uf = dados['uf']
        cod_ibge = dados['ibge']
        return [logradouro, complemento, bairro, cidade, uf, cod_ibge]
        
    def mostrar_cep(janela):
        janela['-CONSULTAR_CEP-'].update(visible=True)
        janela['-CONSULTAR_RASTREIO-'].update(visible=False)
    
    
    def dados_rastreio(valor):
        cod_rastreio = valor['-COD_RASTREIO_DESEJADO-']
    
    
    
    def mostrar_rastreio(janela):
        janela['-CONSULTAR_CEP-'].update(visible=False)
        janela['-CONSULTAR_RASTREIO-'].update(visible=True)