import sys
import subprocess
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
from reportlab.pdfgen import canvas
from reportlab.graphics.barcode import code128
from dynaconf import settings

img_file = svg2rlg(settings.logoPG3D)
img_amostra = svg2rlg(settings.logoAmostra)
can = canvas.Canvas(settings.folhaNome, pagesize=settings.tipoPagina)
can.setFont("Helvetica", 7)


def abrePDF():
    print("Abrindo o PDF")
    opener = "open" if sys.platform == "darwin" else "xdg-open"
    subprocess.call([opener, settings.folhaNome])
    print("Aguarde ....")


def montaCodBarra(codBarra, contador):
    codigoBarra = codBarra + str(contador)
    barcode39 = code128.Code128(codigoBarra)
    barcode39Std = code128.Code128(codigoBarra, barHeight=33, barWidth=0.46,
                                   stop=2)
    return barcode39Std


def totalDePaginas(listaLote):
    numPaginas = 0
    auxPaginas = int(listaLote)
    while auxPaginas >= 0:
        auxPaginas = auxPaginas - 28
        numPaginas = numPaginas + 1
    print("Total de paginas: " + str(numPaginas))
    return numPaginas


def imprimeCodBarras(listaLote, etiquetaNumero, barras_x, barras_y):
    montaCodBarra(listaLote, etiquetaNumero).drawOn(can, barras_x, barras_y)


def montaTexto(listaLote, escrita_y, escrita_x):

    string1 = str(listaLote[2]) + " " + str(listaLote[3]) + \
        " - " + str(listaLote[4])
    string2 = "Temperatura do bico: " + str(listaLote[6])
    string3 = "Temperatura do mesa: " + str(listaLote[5])
    Fonte = "Origem: " + str(listaLote[7])

    can.drawString(escrita_x, int(escrita_y[0]), string1)
    can.drawString(escrita_x, int(escrita_y[1]), string2)
    can.drawString(escrita_x, int(escrita_y[2]), string3)
    can.drawString(escrita_x, int(escrita_y[3]), Fonte)


def montaLogo(listaLote):

    etiquetaNumero = 0
    etiquetaPorPagina = 0
    totalLote = int(listaLote[1])

    for i in range(totalDePaginas(totalLote)):
        can.setFont("Helvetica", 8)
        if (etiquetaNumero >= 28):
            etiquetaPorPagina = 0

        teste_x = 50
        teste_y = 750
        barras_x = -10
        barras_y = 680
        escrita_x = 8
        escrita_y = [742, 733, 724, 715]

        while (etiquetaPorPagina < 28):

            if (etiquetaNumero == totalLote):
                break

            renderPDF.draw(img_file, can, teste_x, teste_y)
            etiquetaNumero += 1
            etiquetaPorPagina += 1

            if (listaLote[9] == 'Venda'):
                imprimeCodBarras(
                    listaLote[8], etiquetaNumero, barras_x, barras_y)
                montaTexto(listaLote, escrita_y, escrita_x)
                teste_x = teste_x + 150
                barras_x = barras_x + 152
                escrita_x = escrita_x + 152
                resto = etiquetaPorPagina % 4

                if (resto == 0):
                    teste_x = 50
                    barras_x = -10
                    teste_y = teste_y - 110
                    barras_y = barras_y - 110
                    escrita_x = 8
                    escrita_y = [x - 110 for x in escrita_y]
            else:
                montaTexto(listaLote, escrita_y, escrita_x)
                renderPDF.draw(img_amostra, can, teste_x - 35, teste_y - 65)
                teste_x = teste_x + 150
                barras_x = barras_x + 152
                escrita_x = escrita_x + 152
                resto = etiquetaPorPagina % 4

                if (resto == 0):
                    teste_x = 50
                    barras_x = -10
                    teste_y = teste_y - 110
                    barras_y = barras_y - 110
                    escrita_x = 8
                    escrita_y = [x - 110 for x in escrita_y]

        can.showPage()
    can.save()
