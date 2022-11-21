import sys
import subprocess
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
from reportlab.pdfgen import canvas
from reportlab.graphics.barcode import code128
from dynaconf import settings

img_file = svg2rlg(settings.logoPG3D)
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


def totalDePaginas(listaLote):
    numPaginas = 0
    auxPaginas = int(listaLote)
    while auxPaginas >= 0:
        auxPaginas = auxPaginas - 28
        numPaginas = numPaginas + 1
    print("Total de paginas: " + str(numPaginas))
    return numPaginas


def montaLogo(listaLote):

    #Variavel para contar etiquetas criadas
    numeroLinha = 0
    Coluna = 250
    etiquetaNumero = 0
    etiquetaPorPagina = 0
    totalLote = int(listaLote[1])

    # For para saber quantas paginas precisam ser criadas    
    for i in range(totalDePaginas(totalLote)):

        print("Total do lote dentro do for: " + str(totalLote))
        print("Valor de etiqueta Atual: " + str(etiquetaNumero))

        if (etiquetaNumero > 28):
            etiquetaNumero = totalLote - etiquetaNumero
            print("Valor de etiquetaNumero: " + str(etiquetaNumero))

        teste_x = 30
        teste_y = 750

        while (etiquetaPorPagina < 28 and etiquetaNumero < totalLote):
            renderPDF.draw(img_file, can, teste_x, teste_y)
            etiquetaNumero += 1
            etiquetaPorPagina += 1
            teste_x = teste_x + 160
            resto = etiquetaNumero % 4
            if (resto == 0):
                teste_x = 30
                teste_y = teste_y - 110
                
            #print ("valor de X: " + str(teste_x))
            #print ("valor de Y: " + str(teste_y))
            #print ("valor de resto: " + str(resto))
            
        can.showPage()
    can.save()










###### Teste de posição do Logo
    #renderPDF.draw(img_file, can, 30,  750)
    #renderPDF.draw(img_file, can, 190, 750)
    #renderPDF.draw(img_file, can, 350, 750)
    #renderPDF.draw(img_file, can, 510, 750)
    
    #renderPDF.draw(img_file, can, 30,  640)
    #renderPDF.draw(img_file, can, 190, 640)
    #renderPDF.draw(img_file, can, 350, 640)
    #renderPDF.draw(img_file, can, 510, 640)
    #
    #renderPDF.draw(img_file, can, 30, 530)
    #renderPDF.draw(img_file, can, 190,530)
    #renderPDF.draw(img_file, can, 350,530)
    #renderPDF.draw(img_file, can, 510,530)
    #
    #renderPDF.draw(img_file, can, 30, 420)
    #renderPDF.draw(img_file, can, 190,420)
    #renderPDF.draw(img_file, can, 350,420)
    #renderPDF.draw(img_file, can, 510,420)
    #
    #renderPDF.draw(img_file, can, 30, 310)
    #renderPDF.draw(img_file, can, 190, 310)
    #renderPDF.draw(img_file, can, 350, 310)
    #renderPDF.draw(img_file, can, 510, 310)
    #
    #renderPDF.draw(img_file, can, 30, 200)
    #renderPDF.draw(img_file, can, 190, 200)
    #renderPDF.draw(img_file, can, 350, 200)
    #renderPDF.draw(img_file, can, 510, 200)
    
    #renderPDF.draw(img_file, can, 30, 90)
    #renderPDF.draw(img_file, can, 190, 90)
    #renderPDF.draw(img_file, can, 350, 90)
    #renderPDF.draw(img_file, can, 510, 90)

###### Fim do teste de posição do logo

#    #
#    #montaCodBarra(listaLote[8], 1).drawOn(can, -15, 680)
#    #
#    #
#    #montaCodBarra(listaLote[8], 2).drawOn(can, 135, 680)
#    #
#    #
#    #montaCodBarra(listaLote[8], 2).drawOn(can, 290, 680)
#    #
#    #
#    #montaCodBarra(listaLote[8], 2).drawOn(can, 450, 680)
#    #
#    ## Linha 2 
#    #
#    #montaCodBarra(listaLote[8], 1).drawOn(can, -15, 570)
#    #
#    ## Linha 3 
#    #
#    #montaCodBarra(listaLote[8], 1).drawOn(can, -15, 460)
#    #
#    ## Linha 4 
#    #
#    #montaCodBarra(listaLote[8], 1).drawOn(can, -15, 350)
#    #
#    ## Linha 5 
#    #
#    #montaCodBarra(listaLote[8], 1).drawOn(can, -15, 240)
#    #
#    ## Linha 6 
#    #
#    #montaCodBarra(listaLote[8], 1).drawOn(can, -15, 130)
#    #
#    ## Linha 7 
#    #
#    #montaCodBarra(listaLote[8], 1).drawOn(can, -15, 20)
#  
#        
#
#    montaTexto(listaLote)
#    #for x in range(settings.folhaEtiquetas):
#    #    if (x == 0):
#        #    # Monta o Logo
#        #    renderPDF.draw(img_file, can, 50, 5)
#        #    can.drawImage(img_file, 50,
#        #                  y_start, width=120,
#        #                  preserveAspectRatio=True, mask='auto')
#        #    can.drawImage(img_file, 250,
#        #                  y_start, width=120,
#        #                  preserveAspectRatio=True, mask='auto')
#        #    can.drawImage(img_file, 450,
#        #                  y_start, width=120,
#        #                  preserveAspectRatio=True, mask='auto')
#        #    # Monta o codigo de barras
#        #    montaCodBarra(listaLote[8], x).drawOn(can, 30,
#        #                                          (y_start - y_MoveBarra))
#        #    montaCodBarra(listaLote[8], x).drawOn(can, 230,
#        #                                          (y_start - y_MoveBarra))
#        #    montaCodBarra(listaLote[8], x).drawOn(can, 430,
#        #                                          (y_start - y_MoveBarra))
#        #    y_MoveBarra = y_MoveBarra + 110
#
#        #if (x > 0):
#        #    can.drawImage(img_file, 50,  (y_start - locomove), width=120,
#        #                  preserveAspectRatio=True, mask='auto')
#        #    can.drawImage(img_file, 250, (y_start - locomove), width=120,
#        #                  preserveAspectRatio=True, mask='auto')
#        #    can.drawImage(img_file, 450, (y_start - locomove), width=120,
#        #                  preserveAspectRatio=True, mask='auto')
#        #    montaCodBarra(listaLote[8], x).drawOn(can, 30,
#        #                                          (y_start - y_MoveBarra))
#        #    montaCodBarra(listaLote[8], x).drawOn(can, 230,
#        #                                          (y_start - y_MoveBarra))
#        #    montaCodBarra(listaLote[8], x).drawOn(can, 430,
#        #                                          (y_start - y_MoveBarra))
#
#        #    locomove = locomove + 110
#        #    y_MoveBarra = y_MoveBarra + 110
#
#        #x += 1
#    
#
#def montaTexto(listaLote):
#    string1 = str(listaLote[2]) + " " + str(listaLote[3]) + \
#              " - " + str(listaLote[4])
#    string2 = "Temperatura do bico: " + str(listaLote[6])
#    string3 = "Temperatura do mesa: " + str(listaLote[5])
#    Fonte = "Origem: " + str(listaLote[7])
#
#    # linha 1
#    can.drawString(18, 742, string1)
#    can.drawString(5,  733, string2)
#    can.drawString(16, 724, string3)
#    can.drawString(5,  715, Fonte)
#    
#    can.drawString(178, 742, string1)
#    can.drawString(165, 733, string2)
#    can.drawString(176, 724, string3)
#    can.drawString(165, 715, Fonte)
#    
#    can.drawString(338, 742, string1)
#    can.drawString(325, 733, string2)
#    can.drawString(336, 724, string3)
#    can.drawString(325, 715, Fonte)
#    
#    can.drawString(498, 742, string1)
#    can.drawString(485, 733, string2)
#    can.drawString(496, 724, string3)
#    can.drawString(485, 715, Fonte)
#
#    ## linha 2
#    can.drawString(18, 632, string1)
#    can.drawString(5,  623, string2)
#    can.drawString(16, 614, string3)
#    can.drawString(5,  605, Fonte)
#    
#    #can.drawString(60, (y_start - 120), string1)
#    #can.drawString(50, (y_start - 130), string2)
#    #can.drawString(60, (y_start - 140), string3)
#    #can.drawString(60, (y_start - 150), Fonte)
#    #can.drawString(270, (y_start - 120), string1)
#    #can.drawString(250, (y_start - 130), string2)
#    #can.drawString(260, (y_start - 140), string3)
#    #can.drawString(260, (y_start - 150), Fonte)
#    #can.drawString(470, (y_start - 120), string1)
#    #can.drawString(450, (y_start - 130), string2)
#    #can.drawString(460, (y_start - 140), string3)
#    #can.drawString(460, (y_start - 150), Fonte)
#
#    ## linha 3
#    #can.drawString(60, (y_start - 230), string1)
#    #can.drawString(50, (y_start - 240), string2)
#    #can.drawString(60, (y_start - 250), string3)
#    #can.drawString(60, (y_start - 260), Fonte)
#    #can.drawString(270, (y_start - 230), string1)
#    #can.drawString(250, (y_start - 240), string2)
#    #can.drawString(260, (y_start - 250), string3)
#    #can.drawString(260, (y_start - 260), Fonte)
#    #can.drawString(470, (y_start - 230), string1)
#    #can.drawString(450, (y_start - 240), string2)
#    #can.drawString(460, (y_start - 250), string3)
#    #can.drawString(460, (y_start - 260), Fonte)
#
#    ## linha 4
#    #can.drawString(60, (y_start - 340), string1)
#    #can.drawString(50, (y_start - 350), string2)
#    #can.drawString(60, (y_start - 360), string3)
#    #can.drawString(60, (y_start - 370), Fonte)
#    #can.drawString(270, (y_start - 340), string1)
#    #can.drawString(250, (y_start - 350), string2)
#    #can.drawString(260, (y_start - 360), string3)
#    #can.drawString(260, (y_start - 370), Fonte)
#    #can.drawString(470, (y_start - 340), string1)
#    #can.drawString(450, (y_start - 350), string2)
#    #can.drawString(460, (y_start - 360), string3)
#    #can.drawString(460, (y_start - 370), Fonte)
#
#    ## linha 5
#    #can.drawString(60, (y_start - 450), string1)
#    #can.drawString(50, (y_start - 460), string2)
#    #can.drawString(60, (y_start - 470), string3)
#    #can.drawString(60, (y_start - 480), Fonte)
#    #can.drawString(270, (y_start - 450), string1)
#    #can.drawString(250, (y_start - 460), string2)
#    #can.drawString(260, (y_start - 470), string3)
#    #can.drawString(260, (y_start - 480), Fonte)
#    #can.drawString(470, (y_start - 450), string1)
#    #can.drawString(450, (y_start - 460), string2)
#    #can.drawString(460, (y_start - 470), string3)
#    #can.drawString(460, (y_start - 480), Fonte)
#
#    ## linha 6
#    #can.drawString(60, (y_start - 560), string1)
#    #can.drawString(50, (y_start - 570), string2)
#    #can.drawString(60, (y_start - 580), string3)
#    #can.drawString(60, (y_start - 590), Fonte)
#    #can.drawString(270, (y_start - 560), string1)
#    #can.drawString(250, (y_start - 570), string2)
#    #can.drawString(260, (y_start - 580), string3)
#    #can.drawString(260, (y_start - 590), Fonte)
#    #can.drawString(470, (y_start - 560), string1)
#    #can.drawString(450, (y_start - 570), string2)
#    #can.drawString(460, (y_start - 580), string3)
#    #can.drawString(460, (y_start - 590), Fonte)
#
#    ## linha 7
#    #can.drawString(60, (y_start - 670), string1)
#    #can.drawString(50, (y_start - 680), string2)
#    #can.drawString(60, (y_start - 690), string3)
#    #can.drawString(60, (y_start - 700), Fonte)
#    #can.drawString(270, (y_start - 670), string1)
#    #can.drawString(250, (y_start - 680), string2)
#    #can.drawString(260, (y_start - 690), string3)
#    #can.drawString(260, (y_start - 700), Fonte)
#    #can.drawString(470, (y_start - 670), string1)
#    #can.drawString(450, (y_start - 680), string2)
#    #can.drawString(460, (y_start - 690), string3)
#    #can.drawString(460, (y_start - 700), Fonte)
#
#    can.showPage()
#    can.save()

