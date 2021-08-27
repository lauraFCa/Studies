import os
from PIL import Image


def eh_imagem(nome_arquivo):
    # filtrar para pegar apenas imagens
    if nome_arquivo.endswith('png') or nome_arquivo.endswith('jpg'):
        return True
    return False


def reduzir(input_dir, output_dir, ext='.jpg'):
    lista_de_arquivos = [nome for nome in os.listdir(
        input_dir) if eh_imagem(nome)]
    # opcao para selecionar a extensao que quero salvar
    for nome in lista_de_arquivos:
        imagem = Image.open(os.path.join(input_dir, nome)).convert('RGB')
        redimensionada = imagem.resize((1280, 720))
        # separar nome do arquivo da extensao [nome, extensao]
        nome_sem_ext = os.path.splitext(nome)[0]
        redimensionada.save(os.path.join(output_dir, nome_sem_ext+ext))


if __name__ == "__main__":
    diretorio = "D:\Documents\pythonPratica\imagens"
    # criar pasta de saida
    if not os.path.isdir('output'):
        os.mkdir('output')

    reduzir(diretorio, 'output')
