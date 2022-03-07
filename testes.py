import requests as r

cod = 'QI203645677BR'

dados = r.get(f'https://proxyapp.correios.com.br/v1/sro-rastro/{cod}').json()

qtd_registros = len(dados['objetos'][0]['eventos'][0]['dtHrCriado'])
# for i in dados:
#     print(i)
print(qtd_registros)
for i in range(qtd_registros):
    print(dados['objetos'][0]['eventos'][i]['dtHrCriado'])

