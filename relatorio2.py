from reportlab.graphics import renderPDF
from reportlab.pdfgen import canvas
from svglib.svglib import svg2rlg
from dynaconf import settings
from reportlab.graphics.barcode import code128


pdf_file = "imagens/hello_world.pdf"
my_canvas = canvas.Canvas(pdf_file, pagesize=settings.tipoPagina)
my_canvas.setFont("Helvetica", 6)
y_start = 760


def montaTexto(listaLote):
    string1 = str(listaLote[2]) + " " + str(listaLote[3]) + \
              " - " + str(listaLote[4])
    string2 = "Temperatura do bico: " + str(listaLote[6])
    string3 = "Temperatura do mesa: " + str(listaLote[5])
    Fonte = "Origem: " + str(listaLote[7])

    # linha 1
    my_canvas.drawString(60, (y_start - 10), string1)
    my_canvas.drawString(50, (y_start - 20), string2)
    my_canvas.drawString(60, (y_start - 30), string3)
    my_canvas.drawString(60, (y_start - 40), Fonte)
    my_canvas.drawString(270, (y_start - 10), string1)
    my_canvas.drawString(250, (y_start - 20), string2)
    my_canvas.drawString(260, (y_start - 30), string3)
    my_canvas.drawString(260, (y_start - 40), Fonte)
    my_canvas.drawString(470, (y_start - 10), string1)
    my_canvas.drawString(450, (y_start - 20), string2)
    my_canvas.drawString(460, (y_start - 30), string3)
    my_canvas.drawString(460, (y_start - 40), Fonte)


def montaCodBarra(codBarra, contador):
    codigoBarra = codBarra + str(contador)
    barcode39 = code128.Code128(codigoBarra)
    barcode39Std = code128.Code128(
        codigoBarra, barHeight=35, barWidth=0.9, stop=2)
    return barcode39Std


def add_image(image_path):
    my_canvas = canvas.Canvas(settings.folhaNome)
    drawing = svg2rlg(img_file)
    renderPDF.draw(drawing, my_canvas, 65, 800)
    my_canvas.drawString(45, 785, "ABS Preto - 1.75mm")
    my_canvas.drawString(10, 775, "Temperatura do bico: 180º ~ 220º")
    my_canvas.drawString(25, 765, "Temperatura da mesa: 110º")
    my_canvas.drawString(35, 755, "Origem: I3D - Coop - GB")

    # Monta o codigo de barras
    montaCodBarra("2Akie31ABSPreto", 1).drawOn(my_canvas, -10, 718)

    my_canvas.save()


img_file = "imagens/Logo.svg"
add_image(img_file)
