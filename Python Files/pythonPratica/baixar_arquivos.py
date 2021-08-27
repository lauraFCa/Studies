import os
import requests

def baixar_arquivo(url, endereco):
    resposta_servidor = requests.get(url)  # requisita ao servidor
    # se passar uma url normal, conteudo eh o HTML normal. Devo passar o endereco do arquivo
    if resposta_servidor.status_code == requests.codes.OK:
        with open(endereco, 'wb') as novo_arquivo:  #crio arquivo para escrever, apenas dentro do with - nao preciso fechar
            novo_arquivo.write(resposta_servidor.content)
    else:
        resposta_servidor.raise_for_status()


if __name__ == '__main__':
    base_url = 'https://math.mit.edu/classes/18.745/Notes/Lecture_{}_Notes.pdf'
    output_dir = 'output'
    for i in range(1, 26):
        nome_arquivo = os.path.jion(output_dir, 'nota_de_aula_{}.pdf'.format(i))
        baixar_arquivo(base_url.format(i), nome_arquivo)