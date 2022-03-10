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
        
        
    def validar_input_rastreio(valor, janela):
        validar = len(str(valor['-RASTREIO_DESEJADO-'])) == 13
        if validar:
            p1_correto = str(valor['-RASTREIO_DESEJADO'][:2]).isalpha()
            p2_correto = str(valor['-RASTREIO_DESEJADO'][11::]).isalpha()
            p3_correto = str(valor['-RASTREIO_DESEJADO'][2:11]).isdigit()
        else:
            sg.popup('Formato inválido detectado, preencha o campo de rastreio corretamente\nDica:XX000000000XX')
        if valor['-RASTREIO_DESEJADO-'].strip() != '' and p1_correto and p2_correto and p3_correto:
            pass
            # falta pouco pra terminar a parte de rastreio, testei o ngc e imprimiu certo
        
            