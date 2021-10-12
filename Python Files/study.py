x = {'nome': 'caio', 'idade': 23, 'telefone': '32222222', 'cpf':'111111111-11'}
print(x)
print(x['nome'])
cadastroPessoas = [{'nome': 'caio', 'idade': 23, 'telefone': '32222222', 'cpf':'111111111-11'}, {'nome': 'lucas', 'idade': 28, 'telefone': '999999999', 'cpf':'222222222-11'}]
print(cadastroPessoas)
print(cadastroPessoas[1]['nome'])

#tupla = dada por um parentesis
def retornaMaior(*list):
    print(max(list))

retornaMaior(1,5,6,89,54,101,7,48)
