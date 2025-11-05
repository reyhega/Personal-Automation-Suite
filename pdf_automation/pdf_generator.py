import argparse
from functools import partial

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
PAGE_HEIGHT = defaultPageSize[1]; PAGE_WIDTH = defaultPageSize[0]
styles = getSampleStyleSheet()

author = "Rey HeGa"

def first_page_header(canvas, doc, custom_title):
    canvas.saveState()
    canvas.setFont('Helvetica-Bold', 16)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, custom_title)
    canvas.setFont('Helvetica', 9)
    canvas.drawString(PAGE_WIDTH-90, 0.75 * inch, "Page %d " % doc.page)
    canvas.restoreState()

def later_pages_header(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 9)
    canvas.drawString(PAGE_WIDTH-90, 0.75 * inch, "Page %d " % doc.page)
    canvas.restoreState()

def generate_basic_report(filename, title, body):
    doc = SimpleDocTemplate(filename)
    Story = [Spacer(1, 2*inch)]
    style = styles["Normal"]

    p = Paragraph(body, style)
    Story.append(p)
    Story.append(Spacer(1, 0.2*inch))

    first_page_func = partial(first_page_header, custom_title=title)

    doc.build(Story, onFirstPage=first_page_func, onLaterPages=later_pages_header)


if __name__=="__main__":

    """title = "Hello world"
    body = "This is the body"
    filename = "Generated.pdf"""

    parser = argparse.ArgumentParser(description='Generate PDF file')
    parser.add_argument('--filename', required=True, help='Name with which the file will be created')
    parser.add_argument('--title', default="", help='Title of document')
    parser.add_argument('--body', default="", help='Body text of document')
    args = parser.parse_args()

    generate_basic_report(args.filename, args.title, args.body)