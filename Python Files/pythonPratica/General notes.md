# General Notes

## Comandos no terminal

Pasta atual: pwd (print work directory)  
Listar componentes da pasta: ls  
Mudar o diretório: cd [*novo endereço*]  
Voltar um diretório acima: cd ..  
Tab - permite auto-complete  

## Criando ambiente virtual para Python

1. Estar no diretório onde se quer criar um venv
2. python -m venv "nome-ambienteVirtual"
3. Entrar na pasta Scipts
4. Ativar o venv: activate  (ou, .\activate)
5. Abrir qualquer arquivo: Ir a pasta com o arquivo > code .
6. python arquivo.py #rodar o arquivo desejado
7. Encerrar o ambiente: deactivate
  
**Caminhos e Diretorios**  
from pathlib import Path, PureWindowsPath  
caminho = Path("../pasta/pasta1", "arquivo.extensao")  
arquivo = pd.read_csv(caminho)  
  
**OU** (apenas para windows)  
caminho-arquivo = PureWindowsPath("../pasta/pasta1", "arquivo.extensao")  

## Organizar arquivos em Python

python -m venv "nome-ambienteVirtual"  
(no terminal - powerShell)  
>> python  
>> import os  
>> os.listdir() - diretório atual  
>> os.mkdir("pasta") - criar nova pasta  
>> os.path.abspath('.') - caminho absoluto do meu diretório atual  
>> os.path.abspath('nova') - caminho absoluto da pasta nova  
>> os.path.join("nome-pasta","nome-arquivo") - cria um endereço com essa junção, de acordo com o sistema operacional (concatena textos)  
>> os.system('dir') - escrevo o comando normal do terminal  # DIR substitui LS no windows  
  
Saindo do Python - exit()  
>> ls  
>> zip teste.zip arquivo.txt - zipar um arquivo definido  
>> os.system('zip teste.zip arquivo.txt') - dentro do python faço a funçõa do sistema  
  
## ORGANIZANDO EM PASTAS

-> organizar.py  
