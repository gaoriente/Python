# 
# Exemplo de acesso a uma base de dados SQLite
#

import sqlite3

def manipulaDados(bancoDados, comando):
    conexao = sqlite3.connect(bancoDados)
    cursor = conexao.cursor()
    cursor.execute(comando)
    conexao.commit()
    conexao.close()

def selecionaDados(bancoDados, comando):
    conexao = sqlite3.connect(bancoDados)
    cursor = conexao.cursor()
    cursor.execute(comando)
    linhas = cursor.fetchall()

    for linha in linhas:
        print(linha)

def ManipulacaoDados():
    comandoInsert = "INSER INTO estados (nome_estado, sigla_estado, nome_capital) VALUES ('Estado teste', 'XX', 'TESTE INCLUSAO')"
    pathBD = "//Users//gabrieloriente//Desktop//Python//Cap. 06//BancoDeDados.db"
    comandoSELECT = "SELECT * FROM estados"

    manipulaDados(pathBD, comandoInsert)
    selecionaDados(pathBD, comandoSELECT)

ManipulacaoDados()

