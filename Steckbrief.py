from fpdf import FPDF
#########################################################
A4_HEIGHT = 297
A4_WIDTH = 210
#########################################################
list_gesucht={'Vorname':"",
            'Nachname':"",
            'Wohnort': "",
            'Alter': "",
            'Größe': "",
            'Gestalt': "",
            'Haar':"",
            'Augenfarbe': "",
            'ZuletztgesehenWann':"",
            'ZuletztgesehenWo':"",
            'Zustand':"",
            'Bekleidung':"",
            'Fortbewegung':"",
            'Sonstiges':"",}

list_sonst={'Dateiname':"Steckbrief",
            'Abschnittleiter':"",
            'Funk1':"",
            'Funk2':"",
            'Funk3': "",
            'Ansprechpartner': "",
            'Mobil1': "",
            'Mobil2': "",
             'StandortEL':"",}
####################################################################
# class PDF(FPDF)
# Define Header and Footer of the PDF
#
####################################################################
class PDF(FPDF):
    def header(self):
        #self.cell(0, 15, 'Title', 1, 0, 'C')
        self.set_font('helvetica', size=12) 
        self.image('Header.png', None,10,190)
        self.ln(40)


    def footer(self):
        self.set_y(-15)
        self.set_line_width(0.5)
        self.set_font('helvetica', size=12) 
        self.line(x1=10, y1=280, x2=200, y2=280)
        self.cell(0,10, f'Seite {self.page_no()}',align='R')
        


pdf = PDF(format="A4")
pdf.add_page()
pdf.set_font('helvetica', size=12)            
pdf.cell(0,20,"hello world",border=True)

pdf.add_page()
pdf.output(list_sonst["Dateiname"] + ".pdf")