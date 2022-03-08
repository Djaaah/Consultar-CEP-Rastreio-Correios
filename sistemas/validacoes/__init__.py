import PySimpleGUI as sg
import requests as r
from sistemas.funcoes import Funcoes as f

class Validar:
    def validar_input_cep(valor, janela):
        validar = len(str(valor['-CEP_DESEJADO-'])) == 8
        if valor['-CEP_DESEJADO-'].strip() != '' and validar and valor['-CEP_DESEJADO-'].isdigit():
            retorno = Validar.validar_dados_cep(valor)
            if retorno == None:
                pass
            else:
                f.exibir_dados_cep(valor, janela)
        else:
            sg.popup("Preencha corretamente o campo do CEP\nDica: 00000000", title='Erro')
    
    def validar_dados_cep(valor):
        CEP = valor['-CEP_DESEJADO-']
        apoio = r.get(f'http://viacep.com.br/ws/{CEP}/json/')

        dados = apoio.json()
        if 'erro' in dados.keys():
            sg.popup('Não foram encontrados dados desse cep, informe um CEP válido!', title='Erro')
        else:
            logradouro = dados['logradouro']
            complemento = dados['complemento']
            bairro = dados['bairro']
            cidade = dados['localidade']
            uf = dados['uf']
            cod_ibge = dados['ibge']
            return [logradouro, complemento, bairro, cidade, uf, cod_ibge]
        
        
            