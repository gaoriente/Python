#
# Arquivo com exemplos de como trabalhar com paths
#

from os  import path
import time

def DadosArquivo():
    ArquivoExiste = path.exists("NovoArquivo.txt")
    ehDiretorio = path.isdir("NovoArquivo.txt")
    pathArquivo = path.realpath("NovoArquivo.txt")
    pathRelativo = path.relpath("NovoArquivo.txt")
    dataCriacao = time.ctime(path.getctime("NovoArquivo.txt")) #c de criacao
    dataModificacao = time.ctime(path.getmtime("NovoArquivo.txt")) #m de modificao

    print(ArquivoExiste)
    print(ehDiretorio)
    print(pathArquivo)
    print(pathRelativo)
    print(dataCriacao)
    print(dataModificacao)

DadosArquivo()
