#
# Escrevendo arquivos com funções do Python
#

def EscreveArquivo():
    arquivo = open("novoArquivo.txt", "w+")

    arquivo.write("Linha gerada com a função 'EscreveArquivo'\r\n ")
    arquivo.close

# EscreveArquivo()


def AlteraArquivo():
    arquivo = open("novoArquivo.txt", "a+")

    arquivo.write("Linha gerada com a função 'AlteraArquivo'\r\n ")
    arquivo.close

AlteraArquivo()