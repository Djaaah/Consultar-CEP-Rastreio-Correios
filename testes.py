import requests as r
import pandas as pd
import jinja2





# for i in dados['objetos'][0]:
#     print(i)



# print(dados)


cod = 'QI203645677BR'

dados = r.get(f'https://proxyapp.correios.com.br/v1/sro-rastro/{cod}').json()
qtd_registros = len(dados['objetos'][0]['eventos'])

registros = []
apoio = []


for i in range(qtd_registros):
    try:
        apoio.append(dados['objetos'][0]['eventos'][i]['dtHrCriado'])
        apoio.append(dados['objetos'][0]['eventos'][i]['descricao'])
        apoio.append(dados['objetos'][0]['eventos'][i]['unidade']['endereco']['cidade'])
        apoio.append(dados['objetos'][0]['eventos'][i]['unidade']['endereco']['uf'])
        apoio.append(dados['objetos'][0]['eventos'][i]['unidade']['tipo'])
        apoio.append(dados['quantidade'])
        apoio.append(dados['objetos'][0]['tipoPostal']['categoria'])
        apoio.append(dados['objetos'][0]['tipoPostal']['descricao'])
        
    except:
        pass
    finally:
        registros.append(apoio[:])
        apoio.clear()
        
        
dados_finais = pd.DataFrame(registros, columns = ["Data do Evento", "Evento", "Local", "Estado", "Unidade", "Qtd. Pacotes", "Tipo de Envio", "Etiqueta"])
pd.options.display.colheader_justify = 'center'
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


    
