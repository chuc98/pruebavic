from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

def drawMyRuler(pdf):
    pdf.drawString(100,810, 'x100')
    pdf.drawString(200,810, 'x200')
    pdf.drawString(300,810, 'x300')
    pdf.drawString(400,810, 'x400')
    pdf.drawString(500,810, 'x500')

    pdf.drawString(10,100, 'y100')
    pdf.drawString(10,200, 'y200')
    pdf.drawString(10,300, 'y300')
    pdf.drawString(10,400, 'y400')
    pdf.drawString(10,500, 'y500')
    pdf.drawString(10,600, 'y600')
    pdf.drawString(10,700, 'y700')
    pdf.drawString(10,800, 'y800')  


def CrearPDF():
    
        
    _Nombre= "Roberto de Jesús García Varela"
    _NombreArchivo="Contrato_Ekkos.pdf" 
    _TituloDocumento="Contrato Ekkos"
    _SubtituloDocumento=_Nombre
    _RFC="RFC290"
    _FechaNacimiento="27/07/1997"
    _EstadoCivil="Soltero"
    _Dirección="Calle siempre viva 123"
    _Email="robertoxd27@gmail.com"

    #_Imagen="./static/ekko.jpg"
    c=canvas.Canvas(_NombreArchivo)
    c.setTitle(_TituloDocumento)
    c.setLineWidth(.3)
    c.setFont('Helvetica',36)

    textLines = [
    'Este es el contrato de: ', _Nombre ,'Quien poseé el RFC: ', _RFC ,
    'Su fecha de nacimiento es: ', _FechaNacimiento ,'Su estado civil es; ', _EstadoCivil ,
    'Su dirección es: ', _Dirección,'Correo electrónico:',_Email,' ' ,
    'textotextotextotextotextotextotextotextotextotexto',
    'textotextotextotextotextotextotextotextotextotexto',
    'textotextotextotextotextotextotextotextotextotexto',
    'textotextotextotextotextotextotextotextotextotexto',
    'textotextotextotextotextotextotextotextotextotexto',
    'textotextotextotextotextotextotextotextotextotexto',
    'textotextotextotextotextotextotextotextotextotexto',
    'textotextotextotextotextotextotextotextotextotexto',
    'textotextotextotextotextotextotextotextotextotexto',
    'textotextotextotextotextotextotextotextotextotexto',
    'textotextotextotextotextotextotextotextotextotexto',
    'textotextotextotextotextotextotextotextotextotexto'
    ]

  

    c.drawCentredString(300,760,_TituloDocumento)
    c.setFont('Helvetica',20)
    c. drawCentredString(290,720,_SubtituloDocumento)

    text = c.beginText(100,680)
    text.setFont("Helvetica", 18)
    for line in textLines:
        text.textLine(line)

    c.drawText(text)
    c.drawCentredString(300,80,_Nombre)
    c.line(200,100,400,100)


    #c.drawInlineImage(_Imagen, 130, 400)

    #drawMyRuler(c)


    c.save()

CrearPDF()





