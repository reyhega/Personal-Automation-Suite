import argparse
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
PAGE_HEIGHT = defaultPageSize[1]; PAGE_WIDTH = defaultPageSize[0]
styles = getSampleStyleSheet()

title = "Hello world"
body = "This is the body"
author = "Rey HeGa"
filename = "Generated.pdf"

def myFirstPage(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica-Bold', 16)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, title)
    canvas.setFont('Helvetica', 9)
    canvas.drawString(inch, 0.75 * inch, "Page %d %s" % (doc.page, author))
    canvas.restoreState()

def myLaterPages(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 9)
    canvas.drawString(inch, 0.75 * inch, "Page %d %s" % (doc.page, author))
    canvas.restoreState()

def go(filename, body):
    doc = SimpleDocTemplate(filename)
    Story = [Spacer(1, 2*inch)]
    style = styles["Normal"]

    p = Paragraph(body, style)
    Story.append(p)
    Story.append(Spacer(1, 0.2*inch))

    doc.build(Story, onFirstPage=myFirstPage, onLaterPages=myLaterPages)


if __name__=="__main__":

    go(filename, body)