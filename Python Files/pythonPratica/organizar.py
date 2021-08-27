import os

# Nome dos arquivos
# Extensao do arquivo define o tipo de arquivo
# Pastas: imagens, audios, documentos, videos, outros
# Mover arquivos para pastas

# "nome.merda-de-arquivo.txt".rfind() # retorna indice do elemento, procurando de trás pra frente

audios_ext = ['.mp3', '.wav']
videos_ext = ['.mp4', '.mov', '.avi']
imagens_ext = ['.jpg', '.jpeg', '.png']
documentos_ext = ['.txt', '.log', '.pdf', '.docx']

def pegarExtensao(nome):
    #pegar ultimo ponto do nome do arquivo
    index = nome.rfind('.')
    return nome[index:]

def organiza(diretorio):
    audio_dir = os.path.join(diretorio, "audios")
    img_dir = os.path.join(diretorio, "imagens")
    docs_dir = os.path.join(diretorio, "documentos")
    vid_dir = os.path.join(diretorio, "videos")
    outros_dir = os.path.join(diretorio, "outros")

    # criar pastas (se não existir)
    if not os.path.isdir(audio_dir):
        os.mkdir(audio_dir)
    if not os.path.isdir(img_dir):
        os.mkdir(img_dir)
    if not os.path.isdir(docs_dir):
        os.mkdir(docs_dir)
    if not os.path.isdir(vid_dir):
        os.mkdir(vid_dir)
    if not os.path.isdir(outros_dir):
        os.mkdir(outros_dir)

    nomes_arquivos = os.listdir(diretorio)
    nova_pasta = ''
    for arquivo in nomes_arquivos:
        if os.path.isfile(os.path.join(diretorio, arquivo)): #verificar se é um arquivo e não pasta
            extensao = str.lower(pegarExtensao(arquivo))
            print(arquivo, extensao)
            if extensao in audios_ext:
                nova_pasta = audio_dir
            elif extensao in videos_ext:
                nova_pasta = vid_dir
            elif extensao in imagens_ext:
                nova_pasta = img_dir
            elif extensao in documentos_ext:
                nova_pasta = docs_dir
            else:
                nova_pasta = outros_dir
            
            # mover para a pasta
            antigo = os.path.join(diretorio, arquivo)
            novo = os.path.join(nova_pasta, arquivo)
            os.rename(antigo, novo)  # (endereco_arquivo_original, endereco_para_mover)
            print("Moveu: ", antigo, " para ", novo)


if __name__ == '__main__':
    organiza('arquivos')