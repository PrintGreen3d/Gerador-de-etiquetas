import sys
import subprocess
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
from reportlab.pdfgen import canvas
from reportlab.graphics.barcode import code128
from dynaconf import settings

img_file = svg2rlg(settings.logoPG3D)
y_start = 760

can = canvas.Canvas(settings.folhaNome, pagesize=settings.tipoPagina)
can.setFont("Helvetica", 8)


def abrePDF():
    print("Abrindo o PDF")
    opener = "open" if sys.platform == "darwin" else "xdg-open"
    subprocess.call([opener, settings.folhaNome])
    print("Aguarde ....")


def montaCodBarra(codBarra, contador):
    codigoBarra = codBarra + str(contador)
    barcode39 = code128.Code128(codigoBarra)
    barcode39Std = code128.Code128(codigoBarra, barHeight=33, barWidth=0.7,
                                   stop=2)
    return barcode39Std


def montaLogo(listaLote):
    locomove = 110
    y_MoveBarra = 75
    
    renderPDF.draw(img_file, can, 30, 750)
    montaCodBarra(listaLote[8], 1).drawOn(can, -15, 680)
    

    #renderPDF.draw(img_file, can, 220, 750)
    #renderPDF.draw(img_file, can, 320, 750)
    #renderPDF.draw(img_file, can, 500, 750)
#

    montaTexto(listaLote)
    #for x in range(settings.folhaEtiquetas):
    #    if (x == 0):
        #    # Monta o Logo
        #    renderPDF.draw(img_file, can, 50, 5)
        #    can.drawImage(img_file, 50,
        #                  y_start, width=120,
        #                  preserveAspectRatio=True, mask='auto')
        #    can.drawImage(img_file, 250,
        #                  y_start, width=120,
        #                  preserveAspectRatio=True, mask='auto')
        #    can.drawImage(img_file, 450,
        #                  y_start, width=120,
        #                  preserveAspectRatio=True, mask='auto')
        #    # Monta o codigo de barras
        #    montaCodBarra(listaLote[8], x).drawOn(can, 30,
        #                                          (y_start - y_MoveBarra))
        #    montaCodBarra(listaLote[8], x).drawOn(can, 230,
        #                                          (y_start - y_MoveBarra))
        #    montaCodBarra(listaLote[8], x).drawOn(can, 430,
        #                                          (y_start - y_MoveBarra))
        #    y_MoveBarra = y_MoveBarra + 110

        #if (x > 0):
        #    can.drawImage(img_file, 50,  (y_start - locomove), width=120,
        #                  preserveAspectRatio=True, mask='auto')
        #    can.drawImage(img_file, 250, (y_start - locomove), width=120,
        #                  preserveAspectRatio=True, mask='auto')
        #    can.drawImage(img_file, 450, (y_start - locomove), width=120,
        #                  preserveAspectRatio=True, mask='auto')
        #    montaCodBarra(listaLote[8], x).drawOn(can, 30,
        #                                          (y_start - y_MoveBarra))
        #    montaCodBarra(listaLote[8], x).drawOn(can, 230,
        #                                          (y_start - y_MoveBarra))
        #    montaCodBarra(listaLote[8], x).drawOn(can, 430,
        #                                          (y_start - y_MoveBarra))

        #    locomove = locomove + 110
        #    y_MoveBarra = y_MoveBarra + 110

        #x += 1
    


def montaTexto(listaLote):
    string1 = str(listaLote[2]) + " " + str(listaLote[3]) + \
              " - " + str(listaLote[4])
    string2 = "Temperatura do bico: " + str(listaLote[6])
    string3 = "Temperatura do mesa: " + str(listaLote[5])
    Fonte = "Origem: " + str(listaLote[7])

    # linha 1
    can.drawString(18, (y_start - 18), string1)
    can.drawString(5, (y_start - 25), string2)
    can.drawString(16, (y_start - 35), string3)
    can.drawString(5, (y_start - 45), Fonte)
    
    can.drawString(270, (y_start - 10), string1)
    can.drawString(250, (y_start - 20), string2)
    can.drawString(260, (y_start - 30), string3)
    can.drawString(260, (y_start - 40), Fonte)
    can.drawString(470, (y_start - 10), string1)
    can.drawString(450, (y_start - 20), string2)
    can.drawString(460, (y_start - 30), string3)
    can.drawString(460, (y_start - 40), Fonte)

    # linha 2
    can.drawString(60, (y_start - 120), string1)
    can.drawString(50, (y_start - 130), string2)
    can.drawString(60, (y_start - 140), string3)
    can.drawString(60, (y_start - 150), Fonte)
    can.drawString(270, (y_start - 120), string1)
    can.drawString(250, (y_start - 130), string2)
    can.drawString(260, (y_start - 140), string3)
    can.drawString(260, (y_start - 150), Fonte)
    can.drawString(470, (y_start - 120), string1)
    can.drawString(450, (y_start - 130), string2)
    can.drawString(460, (y_start - 140), string3)
    can.drawString(460, (y_start - 150), Fonte)

    # linha 3
    can.drawString(60, (y_start - 230), string1)
    can.drawString(50, (y_start - 240), string2)
    can.drawString(60, (y_start - 250), string3)
    can.drawString(60, (y_start - 260), Fonte)
    can.drawString(270, (y_start - 230), string1)
    can.drawString(250, (y_start - 240), string2)
    can.drawString(260, (y_start - 250), string3)
    can.drawString(260, (y_start - 260), Fonte)
    can.drawString(470, (y_start - 230), string1)
    can.drawString(450, (y_start - 240), string2)
    can.drawString(460, (y_start - 250), string3)
    can.drawString(460, (y_start - 260), Fonte)

    # linha 4
    can.drawString(60, (y_start - 340), string1)
    can.drawString(50, (y_start - 350), string2)
    can.drawString(60, (y_start - 360), string3)
    can.drawString(60, (y_start - 370), Fonte)
    can.drawString(270, (y_start - 340), string1)
    can.drawString(250, (y_start - 350), string2)
    can.drawString(260, (y_start - 360), string3)
    can.drawString(260, (y_start - 370), Fonte)
    can.drawString(470, (y_start - 340), string1)
    can.drawString(450, (y_start - 350), string2)
    can.drawString(460, (y_start - 360), string3)
    can.drawString(460, (y_start - 370), Fonte)

    # linha 5
    can.drawString(60, (y_start - 450), string1)
    can.drawString(50, (y_start - 460), string2)
    can.drawString(60, (y_start - 470), string3)
    can.drawString(60, (y_start - 480), Fonte)
    can.drawString(270, (y_start - 450), string1)
    can.drawString(250, (y_start - 460), string2)
    can.drawString(260, (y_start - 470), string3)
    can.drawString(260, (y_start - 480), Fonte)
    can.drawString(470, (y_start - 450), string1)
    can.drawString(450, (y_start - 460), string2)
    can.drawString(460, (y_start - 470), string3)
    can.drawString(460, (y_start - 480), Fonte)

    # linha 6
    can.drawString(60, (y_start - 560), string1)
    can.drawString(50, (y_start - 570), string2)
    can.drawString(60, (y_start - 580), string3)
    can.drawString(60, (y_start - 590), Fonte)
    can.drawString(270, (y_start - 560), string1)
    can.drawString(250, (y_start - 570), string2)
    can.drawString(260, (y_start - 580), string3)
    can.drawString(260, (y_start - 590), Fonte)
    can.drawString(470, (y_start - 560), string1)
    can.drawString(450, (y_start - 570), string2)
    can.drawString(460, (y_start - 580), string3)
    can.drawString(460, (y_start - 590), Fonte)

    # linha 7
    can.drawString(60, (y_start - 670), string1)
    can.drawString(50, (y_start - 680), string2)
    can.drawString(60, (y_start - 690), string3)
    can.drawString(60, (y_start - 700), Fonte)
    can.drawString(270, (y_start - 670), string1)
    can.drawString(250, (y_start - 680), string2)
    can.drawString(260, (y_start - 690), string3)
    can.drawString(260, (y_start - 700), Fonte)
    can.drawString(470, (y_start - 670), string1)
    can.drawString(450, (y_start - 680), string2)
    can.drawString(460, (y_start - 690), string3)
    can.drawString(460, (y_start - 700), Fonte)

    can.showPage()
    can.save()

