from fpdf import FPDF

def createPDF(a,local,visitante):
    pdf = FPDF(format='A4',unit='cm')
    pdf.add_page()
    epw=pdf.w-2*pdf.l_margin
    #titulo
    pdf.set_font('Times','B',14.0)
    pdf.cell(epw,0.0,'League Football Results',align='C')
    pdf.ln(1)

    pdf.set_font('Times','',10.0)
    pdf.multi_cell(20,1,'%s'%(a),align='L')
    pdf.ln(1)
    pdf.image('../Outputs/mediaGoles{}{}.png'.format(local,visitante),1,6,9,8)
    pdf.image('../Outputs/maxGoles{}{}.png'.format(local,visitante),10,6,9,8)
    pdf.ln(1)
    pdf.output('../Outputs/PDFResutados.pdf')