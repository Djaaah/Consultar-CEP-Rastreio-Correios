import requests as r

def validar_dados_cep(CEP):
        
        apoio = r.get(f'http://viacep.com.br/ws/{CEP}/json/')
        
        dados = apoio.json()
        if 'erro' in dados.keys():
            print('Não foram encontrados dados desse cep, informe um CEP válido!')
        else:
            logradouro = dados['logradouro']
            complemento = dados['complemento']
            bairro = dados['bairro']
            cidade = dados['localidade']
            uf = dados['uf']
            cod_ibge = dados['ibge']
            return [logradouro, complemento, bairro, cidade, uf, cod_ibge]


print(validar_dados_cep('53370525'))


# cod = 'QI203645677BR'

# dados = r.get(f'https://proxyapp.correios.com.br/v1/sro-rastro/{cod}').json()

# qtd_registros = len(dados['objetos'][0]['eventos'])


# for i in dados['objetos'][0]:
#     print(i)

# registros = []
# apoio = []

# print(qtd_registros)
# for i in range(qtd_registros):
#     try:
#         apoio.append(dados['objetos'][0]['eventos'][i]['dtHrCriado'])
#         apoio.append(dados['objetos'][0]['eventos'][i]['descricao'])
#         apoio.append(dados['objetos'][0]['eventos'][i]['unidade']['endereco']['cidade'])
#         apoio.append(dados['objetos'][0]['eventos'][i]['unidade']['endereco']['uf'])
#         apoio.append(dados['objetos'][0]['eventos'][i]['unidade']['tipo'])
#         apoio.append(dados['quantidade'])
#         apoio.append(dados['objetos'][0]['tipoPostal']['categoria'])
#         apoio.append(dados['objetos'][0]['tipoPostal']['descricao'])
        
#     except:
#         pass
#     finally:
#         registros.append(apoio[:])
#         apoio.clear()

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


    
