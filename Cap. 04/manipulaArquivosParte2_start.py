#
# Exemplos de como trabalhar com arquivos
#
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def criaZipModo1():
    shutil.make_archive("ArquivoCompactado", "zip", "//Users//gabrieloriente//Desktop//Python//Cap. 03")

# criaZipModo1()

def criaZipModo2():
    with ZipFile("ArquivoZipModo2.zip", "w") as novoZip:
        novoZip.write("NovoArquivo.bkp")
        novoZip.write("NovoArquivo.txt")
        novoZip.write("zipModo1.zip.zip")

# criaZipModo2()

def DeletaArquivo():
    os.remove("ArquivoZipModo2.zip")

DeletaArquivo()