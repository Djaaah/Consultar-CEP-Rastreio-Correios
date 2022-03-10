import requests as r
import pandas as pd
from prettytable import PrettyTable as pt

# for i in dados['objetos'][0]:
#     print(i)



# print(dados)


cod = 'QI203645677BR'

dados = r.get(f'https://proxyapp.correios.com.br/v1/sro-rastro/{cod}').json()

qtd_registros = len(dados['objetos'][0]['eventos'])

registros = []
apoio = []
apoio2 = []

for i in range(qtd_registros):
    try:
        apoio2 = dados['objetos'][0]['eventos'][i]['dtHrCriado'].split('T')
        apoio2 = ' '.join(apoio2)
        apoio.append(apoio2)
        apoio.append(dados['objetos'][0]['eventos'][i]['descricao'])
        apoio.append(dados['objetos'][0]['eventos'][i]['unidade']['endereco']['cidade'])
        apoio.append(dados['objetos'][0]['eventos'][i]['unidade']['endereco']['uf'])
        apoio.append(dados['objetos'][0]['eventos'][i]['unidade']['tipo'])
        apoio.append(dados['quantidade'])
        apoio.append(dados['objetos'][0]['tipoPostal']['categoria'])
        
        
    except:
        pass
    finally:
        registros.append(apoio[:])
        apoio.clear()


dados_finais = pt(["Data do Evento", "Evento", "Local", "Estado", "Unidade", "Pacotes", "Tipo de Envio"])

for i in range(qtd_registros):
    dados_finais.add_row(registros[i])

print(dados_finais)


# dados_finais.head().style.set_table_styles([dict(selector='th', props=[('text-align', 'left')]),
#                                     dict(selector='td', props=[('text-align', 'left')])])





# for i in registros:
#     print(i)


# def validar_dados_cep(CEP):
#     apoio = r.get(f'http://viacep.com.br/ws/{CEP}/json/')
        
#     validador = bool()
#     dados = apoio.json()
#     if 'erro' in dados.keys():
#         return validador == True
#     else:
#         return validador == False


# validador = validar_dados_cep('5300000')

# print(validador)


    
