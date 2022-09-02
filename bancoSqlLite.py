import sqlite3
import traceback
import re
from dynaconf import settings


con = sqlite3.connect("baseEtiquetas.db")
cursor = con.cursor()


def criaBanco():
    cursor.execute('''CREATE TABLE IF NOT EXISTS "etiquetas1" (
        "Lote"	INTEGER NOT NULL,
        "Quantidade"	INTEGER NOT NULL,
        "Material"	TEXT NOT NULL,
        "Cor"	TEXT NOT NULL,
        "Diametro"	TEXT NOT NULL,
        "Mesa"	TEXT NOT NULL,
        "Bico"	TEXT NOT NULL,
        "Origem"	TEXT NOT NULL,
        "codBarras"	TEXT NOT NULL,
        PRIMARY KEY("Lote" AUTOINCREMENT)
    )''')


def ultimaPosicaoSql():
    cursor.execute(settings.sqlPesquisa)
    for linha in cursor.fetchall():
        ultimoId = list(linha)
    return ultimoId


def adicionaIdCodigoBarras(ultimoId, infoLote):
    listaCodigos = []
    codigoBarras = str(ultimoId[0]) + str(infoLote[7]) + \
        str(infoLote[0]) + str(infoLote[1]) + str(infoLote[2])
    listaCodigos.append(ultimoId[0])
    listaCodigos.append(codigoBarras)
    return listaCodigos


def insertBanco(listaDados):
    print("Fazendo o insert dos dados na tabela")
    try:
        cursor.execute(settings.sqlInsert, (
            int(listaDados[0]),
            str(listaDados[1]),
            str(listaDados[2]),
            str(listaDados[3]),
            str(listaDados[4]),
            str(listaDados[5]),
            str(listaDados[6]),
            str(listaDados[7])))
        con.commit()
        print('Dados inseridos com sucesso.')
    except Exception:
        print("problemas em inserir novos dados")
        traceback.print_exc()
        con.rollback()


def buscaDadosUltimaPosicao(lastID):
    listaLote = []
    cursor.execute(settings.sqlSelect, (lastID[0], ))
    for linha in cursor.fetchall():
        listaLote = list(linha)
    return listaLote


def updateCodigoBarras(dadosBarras):
    print("Fazendo update no campo codigo de barras")
    cursor.execute(settings.sqlUpdate, (dadosBarras[1], dadosBarras[0]))
    con.commit()


def fechaBanco():
    print("Fechando conexão com o banco")
    con.close()


def desfazTudo():
    con.rollback()
    print("Veja o log! Tivemos algum problema no caminho!!!")


def abreBanco():
    con = sqlite3.connect("baseEtiquetas.db")
    cursor = con.cursor()
